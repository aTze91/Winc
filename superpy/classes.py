import os
from datetime import datetime as dt
from datetime import timedelta
import csv


class Inventory():

    field_names = ['id', 'name', 'expiring_date', 'buy_price', 'sell_price', 'quantity']
    products = []

    def __init__(self, name):
        self.name = name
        self.dirpath = os.path.join(os.getcwd(), name)
        self.path = os.path.join(self.dirpath, f'{name}.csv')
        self.record_path = os.path.join(self.dirpath, f'record_{name}.csv')
        self.today_path = os.path.join(self.dirpath, f'today_{name}.txt')
        self.report_dirpath = os.path.join(self.dirpath, 'reports')
        print(f'Searching for {self.name}....')
        if os.path.exists(self.path):  # if the inventary files already exist we recover the contained data
            print(f'{self.name} found!')
            # here we the recover the today date and the creation date stored in the file today.txt
            with open(self.today_path, 'r', newline='') as today_file:                                                         
                dates = today_file.readline().split(sep='|')
                self.today = dates[0]
                self.creation_date = dates[1]
            # then we create a list of Product instances to store into self.products
            for i in range(1, self.len() +1):
                product = self.get_product(i)
                self.products.append(product)
        else: # if the inventary files don't exists we create a new inventory
            print(f'{self.name} not found...')
            os.mkdir(self.dirpath)
            os.mkdir(self.report_dirpath)
            self.today = dt.strftime(dt.today(), '%Y-%m-%d')
            self.creation_date = self.today
            lines = [self.today, '|', self.today]
            with open(self.today_path, 'a',) as today:
                today.writelines(lines)
            with open(self.path, 'w') as inventory:
                inventory.close()
            with open(self.record_path, 'w') as record:
                record.close()
            print(f'A new directory for {self.name} is been created at : {self.dirpath}')

    def len(self): # returns the number of products in the inventary
        counter = 0
        with open(self.path, 'r',  newline='') as inventory:
            reader = csv.reader(inventory)
            for row in reader:
                counter += 1
        return counter

    def clean(self): # removes all the products and movements recorded
        os.remove(self.path)
        with open(self.path, 'a') as inventory:
            inventory.close()

    def set_date(self, date=dt.strftime(dt.today(), '%Y-%m-%d')): # changes the date considered today by superpy
        if date is None:
            date = dt.strftime(dt.today(), '%Y-%m-%d')
        lines = [date, '|', self.creation_date]
        with open(self.today_path, 'w') as today:
            today.writelines(lines)
            today.close()
        self.today = date
        print(f'Today is : {self.today}')

    def advance_date(self, step): # advances the date considered today by the number of days given as argument
        new_date = dt.strptime(self.today, '%Y-%m-%d')
        new_date += timedelta(days=step)
        self.today = dt.strftime(new_date, '%Y-%m-%d')
        self.set_date(self.today)

    def write_on_csv(self, path, row): # writes a new row on cvs files 
        with open(path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(row)
        csvfile.close()

    def replace_product(self, new_product): # replaces the row that correspond to the id of the new product
        new_products = []
        # here we create a list of Products that contains the replaced product  
        for product in self.products:
            if product.id == new_product.id:
                new_products.append(new_product)
            else:
                new_products.append(product)
        self.clean() # we delete all the data from the .csv file where the products data is stored
        for product in new_products:# we write the updated data into the .csv file 
            row = [product.id, product.name, product.expiring_date, product.buy_price, product.sell_price, product.quantity]
            self.write_on_csv(self.path, row)

    def buy(self, name, expiring_date, buy_price, sell_price, quantity):  # adds one product to the file inventory.csv,
        in_stock = False                                                  # if the product already exists, his quanity will be increased,                                           
        for product in self.products: 
            if product.name == name and product.expiring_date == expiring_date:
                print('in stock')
                in_stock = True
                id = product.id
                new_quantity = product.quantity + quantity
                self.replace_product(Product(id, name, expiring_date, buy_price, sell_price, new_quantity, self.today))
        if in_stock is False:
            id = self.len() + 1
            product = Product(id, name, expiring_date, buy_price, sell_price, quantity, self.today)
            self.products.append(product)
            row = [product.id, product.name, product.expiring_date, product.buy_price, product.sell_price, product.quantity]
            self.write_on_csv(self.path, row)
        row = ['buy', name, buy_price, quantity, self.today, id]
        self.write_on_csv(self.record_path, row) # add a new row to the file record

    def sell(self, id, quantity=1):  # reduces the quantity of the corresponding product
        product = self.get_product(id)
        if product.quantity - quantity < 0:
            print(f'ERROR: Only {str(product.quantity)} in stock!')
        else:
            product.quantity -= quantity
            self.replace_product(product)
            row = ['sell', product.name, product.sell_price, quantity, self.today, product.id]
            self.write_on_csv(self.record_path, row) # add a new row to the file record

    def report(self, key, from_date, to_date, export): # returns a dict that can contain diffent data based on the given key and save the same data on a csv file
        if from_date is None:
            from_date = self.creation_date
        if to_date is None:
            to_date = self.today
        rows =[]
        report_path = os.path.join(self.report_dirpath, f'{key}-{from_date}_{to_date}.csv')
        report_data = {}
        if key == 'expired':
            report_data = self.expired_products()
            if export:
                rows = [['ID', 'NAME', 'EXPIRING DATE', 'BUY PRICE', 'SELL PRICE', 'IN STOCK']]
                for product in report_data['products']:
                    rows.append([product.id, product.name, product.expiring_date, product.buy_price, product.sell_price, product.quantity])
        elif key == 'movements':
            rows = None
            report_data = self.movements(from_date, to_date)
        elif key == 'revenue':
            report_data = self.revenue(from_date, to_date)    
        elif key == 'profits':
            report_data = self.profits(from_date, to_date)
            if export:
                rows = [['NAME', 'PROFIT']]
                for product in report_data['products']:
                    rows.append([report_data['products'][product]['name'], report_data['products'][product]['profit']])
        elif key == 'expenses':
            report_data = self.expenses(from_date, to_date)
        if (key == 'revenue' or key == 'expenses') and export:
            rows = [['NAME', 'QUANTITY', 'VALUE']]
            for product in report_data['products']:
                rows.append([report_data['products'][product]['name'], report_data['products'][product]['quantity'], report_data['products'][product]['value']])
        if rows:
            for row in rows:
                self.write_on_csv(report_path, row)
        return report_data

    def expired_products(self): # returns a dict that contain all the expired products in the inventory
        expired_data = {}
        products = []
        value_couter = 0
        for i in range(1, (self.len())):
            product = self.get_product(i)
            if product.is_expired():
                products.append(product)
                value_couter += product.buy_price
        expired_data['products'] = products
        expired_data['total_value'] = value_couter
        expired_data['description'] = f'{len(products)} expired products for a total value of {value_couter}'
        return expired_data

    def movements(self, from_date, to_date): # returns a dict that contain all the recorded movements
        if to_date is None:
            to_date = self.today
        movements_data = {
            'sold': {
                'movements': [],
                'tot_quantity': 0,
                'tot_value': 0
                },
            'bought': {
                'movements': [],
                'tot_quantity': 0,
                'tot_value': 0
                },
            'description': ['sold/bougth', 'name', 'price', 'quantity', 'date', 'id']
            }

        with open(self.record_path, 'r') as record:
            reader = csv.reader(record, delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                # row indexing: [sold\bougth,name,price,quantity,date,id]
                if row[0] == 'sell' and from_date <= row[4] and to_date >= row[4]:
                    movements_data['sold']['tot_quantity'] += (row[3])
                    movements_data['sold']['tot_value'] += (row[2] * row[3])
                    movements_data['sold']['movements'].append([row[1], row[2], row[3], row[4], int(row[5])])
                elif row[0] == 'buy' and from_date <= row[4] and to_date >= row[4]:
                    movements_data['bought']['tot_quantity'] += (row[3])
                    movements_data['bought']['tot_value'] += (row[2] * row[3])
                    movements_data['bought']['movements'].append([row[1], row[2], row[3], row[4], int(row[5])])
        record.close
        return movements_data

    def revenue(self, from_date, to_date): # returns a dict that contain the revenue data for each product
        revenue_data = {
            'products': {},
            'tot_value': 0,
            'tot_quantity': 0,
            'description': ''
        }
        sold_data = self.movements(from_date, to_date)['sold']
        for movement in sold_data['movements']:
            # movement is a list with indexing: [name,price,quantity,date,id]
            if movement[0] in revenue_data:
                revenue_data['products'][movement[0]]['quantity'] += movement[2]
                revenue_data['products'][movement[0]]['value'] += movement[1] * movement[2]
            else:
                revenue_data['products'][movement[0]] = {
                    'name': movement[0],
                    'quantity': movement[2],
                    'value': movement[1] * movement[2]}
        revenue_data['tot_value'] = sold_data['tot_value']
        revenue_data['tot_quantity'] = sold_data['tot_quantity']
        q = sold_data['tot_quantity']
        v = sold_data['tot_value']
        revenue_data['description'] = f'{q} sold products for a total value of {v}'
        return revenue_data

    def expenses(self, from_date, to_date):# returns a dict that contain the expenses data for each product
        expenses_data = {
            'products': {},
            'tot_value': 0,
            'tot_quantity': 0,
            'description': ''
        }
        bought_data = self.movements(from_date, to_date)['bought']
        for movement in bought_data['movements']:
            # movement is a list with indexing: [name,price,quantity,date,id]
            if movement[1] in expenses_data:
                expenses_data['products'][movement[0]]['quantity'] += movement[3]
                expenses_data['products'][movement[0]]['value'] += movement[2] * movement[3]
            else:
                expenses_data['products'][movement[0]] = {
                    'name': movement[0],
                    'quantity': movement[2],
                    'value': movement[1] * movement[2]}
        expenses_data['tot_value'] = bought_data['tot_value']
        expenses_data['tot_quantity'] = bought_data['tot_quantity']
        q = bought_data['tot_quantity']
        v = bought_data['tot_value']
        expenses_data['description'] = f'{q} bought products for a total value of {v}'
        return expenses_data

    def profits(self, from_date, to_date): # returns a dict that contain the profits data for each product
        expenses_data = self.expenses(from_date, to_date)
        revenue_data = self.revenue(from_date, to_date)
        profits_data = {
            'products': {},
            'tot_value': 0,
            'tot_quantity': 0,
            'description': ''
        }
        for product in revenue_data['products']:
            profits_data['products'][product] = {
                    'name': product,
                    'profit':  revenue_data['products'][product]['value'] - expenses_data['products'][product]['value']
                     }
        profits_data['tot_profit'] = revenue_data['tot_value'] - expenses_data['tot_value']
        v = profits_data['tot_profit']
        profits_data['description'] = f'total profits: {v}'
        return profits_data

    def get_product(self, id): # returns the product corresponding to the gien id
        in_stock = False
        with open(self.path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile,  delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                if row[0] == id:
                    in_stock = True
                    my_product = Product(int(row[0]), row[1], row[2], row[3], row[4], row[5], self.path)
                    csvfile.close()
                    my_product.today = self.today
                    return my_product
        if in_stock is False:
            print('ERROR: Product not in stock!!!')
        return in_stock
    pass

# we use Product instances to manage the data of single products 
class Product():

    def __init__(self, id, name, expiring_date, buy_price, sell_price, quantity, today):
        self.id = id
        self.name = name
        self.expiring_date = expiring_date
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.quantity = quantity
        self.today = today

    def is_expired(self): # returns True if the product i expired, False if it doesn't
        if self.today > self.expiring_date:
            return True
        else:
            return False
    pass
