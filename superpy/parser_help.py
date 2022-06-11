# Here you can find the stings to display in the help message 

name = ": is the name of the inventory tha you want to manage,\n\
  in case superpy doesn't find an inventory with that name,\n\
  a new inventory will be created automatically.\n\n"
i = ": display all the products in stock.\n\n"
b = ": you can use 'buy' to add a product to the inventory.\n\n"
       
s = ": use 'sell' to remove a product from the inventory or decrease his quantity.\n\n"
sd = ": change the date that superpy perceives as today.\n\n"
a = ": advance the date that superpy perceives as today.\n\n"
rep = ": create and display report data, optionally you can export the report into .csv files.\n\n"
c = ": remove all the products by the inventory."
pname = ': is the name of the product, note that superpy is not case sensitive about product names\n\n'
exp = ': is expiration date of the product,\n\
    note that products with the same name\n\
    but different expiration date\n\
    are considered different products\n\
    the date format must be <Y-m-d>\n\n'
bprice = ': is the price of the product when you buy it.\n\n'
sprice = ':  is the price of the product when you sell it.\n\n'
quant = ': is the quantity of the product tha you want buy or sell.\n\n'
id = ': is the id of the product that you want sell.\n\n'
to = ': whit this flag you can specify the last day of a range of dates that you want work on,\n\
        by defaulf is value correspond to the attribute self.today of the inventory,\n\
        his format must be <Y-m-d>.\n\n'
frm = ': whit this flag you can specify the firt day of a range of dates that you want work on,\n\
        by defaulf is value correspond to the creation date of the inventory,\n\
        his format must be <Y-m-d>.\n\n'
r = ": with this flag you can specify what kind of report you want to create, his default value is 'all',\n\
  choices : 'expired': to get a report of all expired products\n\
            'movements': to get a report of all the buy/sell movements\n\
            'revenue': to get a report of the revenue\n\
            'expenses': to get a report of the expenses\n\
            'profits': to get a report of the profits\n\
            'all': to get expired, movements, revenue, expenses, profit report.\n\n"
export = ' add this flag if you want to export the report data into .csv files\n\n'
