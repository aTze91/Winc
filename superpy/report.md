# **SUPERPY REPORT**

## *Here are three implementations that I liked:*
1. **The method write_on_csv() as easy as it is, it made my code much more clean and readable. At one point I noticed that everytime I needed to write on a csv file I was doing it in a different way leaving code and outputs very chaotic, so I decided to implement a method that standardizes the way I write a new row on csv file. I found it very usefull while coding the rest of superpy, because I didn't need to think about how to write on csv files anymore. With write_on_csv() it is enough to give the row you want to write wrapped into a list and the path of the file you want to write on, as arguments, next is the snippet of the code:**

```
    def write_on_csv(self, path, row): 
        with open(path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(row)
        csvfile.close()
```

2. **While write_on_csv solved the writing on csv files problem, get_product() solved a big part of reading it, even though this method is limited to read only through the lines of the csv file containing the inventory itself, this is still a big part of the reading from csv files. It gives the possibility to wrap the data of each product in the inventary into a class object Product(), next is the snippet of the code:**

```
def get_product(self, id): # returns the product corresponding to the gien id
        in_stock = False
        with open(self.path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile,  delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                if row[0] == id:
                    in_stock = True
                    my_product = Product(row[0], row[1], row[2], row[3], row[4], row[5], self.path)
                    csvfile.close()
                    my_product.today = self.today
                    return my_product
        if in_stock is False:
            print('ERROR: Product not in stock!!!')
        return in_stock
```

3. **I think organizing the data that comes from the class Inventory methods expired(), movements(), revenue(), expenses() and profit() into a well structured dict is a proper thing I did, it gives the possibility to use that data into different ways, even though I use it only to save the data on csv files or showing it as a easy to read table in the command line. In case we want to add functionality to superpy we can always acces and use that data in an easy way, for example expenses() return this:**
```

expenses_data = {
            'products': {
                'product': {
                    'name': ....
                    'quantity': ... 
                    'value': ...
                }
            },
            'tot_value': 0,
            'tot_quantity': 0,
            'description': ''
        }
```
