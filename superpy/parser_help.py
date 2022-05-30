name = "select wich inventary to manage,\n\
in case the inventary doesn't exist a new one will be created."
i = "display the products in stock"
b = " require arguments : --product-name --expiration-date --buy-price --sell-price -quantity'\n\
add a product to the inventatry,if the product already exists his quantity will be increased"
s = "require arguments : --product-id --quantity' , decrease the quantity of one product"
sd = "change the date that superpy perceives as today\nadditional arguments: --from,--to"
a = "advance the date that superpy perceives as today\nadditional arguments: --step"
rep = " display report data and create a csv file containing the that data\nadditional arguments: --r, --from, --to"
c = "remove all the products by the inventary"
pname = 'product name'
exp = 'expiration date the format must be Y-m-d'
bprice = 'price of the product when you buy it'
sprice = 'price of the product when you sell it'
quant = 'quantity must be an int'
id = 'product id must be an int'
to = 'last day of a range of dates, format must be Y-m-d'
frm = 'first day of a range of dates, format must be Y-m-d'
r = "choices : 'expired': to get a report of all expired products\n\
          'movements': to get a report of all the buy/sell movements\n\
          'revenue': to get a report of the revenue\n\
          'expenses': to get a report of the expenses\n\
          'profits': to get a report of the profits\n\
          'all': to get expired, movements, revenue, expenses, profit report"
