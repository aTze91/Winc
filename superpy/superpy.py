from numpy import append
import parser_help as h
from classes import Inventory
import argparse as ap
from rich import table as tb
import rich
import matplotlib.pyplot as plt
import numpy as np


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.


def main():
    # with this function we display a table
    def print_table(columns, rows, title):
        table = tb.Table(title=title)
        for column in columns:
            table.add_column(column, justify="center")
        for row in rows:
            str_row = []
            for value in row:
                str_row.append(str(value))
            table.add_row(*str_row)
        rich.print(table)
    
    def show_plot(x,y):
        #plt.style.use('_mpl-gallery')
        # plot
        
        pass

    # this function wrap the data tha we get from inventory.report() into columns and rows,
    # then calls print_table() 
    def show_expired():
        data = inventory.report('expired', None, None, args.exp)
        rows = []
        for product in data['products']:
            rows.append([product.id, product.name, product.expiring_date, product.buy_price, product.sell_price, product.quantity])
        columns = ['ID', 'NAME', 'EXPIRATION DATE', 'BUY PRICE', 'SELL PRICE', 'IN STOCK']
        print_table(columns, rows, data['description'].upper())

    # this function wrap the data tha we get from inventory.report() into columns and rows,
    # then calls print_table()
    def show_movements():
        data = inventory.report('movements', args.from_date, args.to_date, args.exp)
        columns = ['NAME', 'BUY PRICE', 'QUANTITY', 'DATE', 'ID']
        rows = data['bought']['movements']
        title = 'BUY MOVEMENTS:'
        print_table(columns, rows, title)
        columns = ['NAME', 'SELL PRICE', 'QUANTITY', 'DATE', 'ID']
        rows = data['sold']['movements']
        title = 'SELL MOVEMENTS:'
        print_table(columns, rows, title)

    # this function wrap the data tha we get from inventory.report() into columns and rows,
    # then calls print_table()
    def show_revenue():
        rows = []
        x = []
        y = []
        data = inventory.report('revenue', args.from_date, args.to_date, args.exp)
        columns = ['NAME', 'QUANTITY', 'VALUE']
        for product in data['products']:
            rows.append([data['products'][product]['name'], data['products'][product]['quantity'], data['products'][product]['value']])
        print_table(columns, rows, data['description'].upper())

    # this function wrap the data tha we get from inventory.report() into columns and rows,
    # then calls print_table() 
    def show_expenses():
        rows = []
        data = inventory.report('expenses', args.from_date, args.to_date, args.exp)
        columns = ['NAME', 'QUANTITY', 'VALUE']
        for product in data['products']:
            rows.append([data['products'][product]['name'], data['products'][product]['quantity'], data['products'][product]['value']])
        print_table(columns, rows, data['description'].upper())

    # this function wrap the data tha we get from inventory.report() into columns and rows,
    # then calls print_table() 
    def show_profits():
        x = []
        y = []
        rows = []
        data = inventory.report('profits', args.from_date, args.to_date, args.exp)
        columns = ['NAME', 'PROFIT']
        for product in data['products']:
            rows.append([data['products'][product]['name'], data['products'][product]['value']])
        print_table(columns, rows, data['description'].upper())


    # here we define parser and the positonal argument 'name'    
    parser = ap.ArgumentParser(description='Manage inventories', formatter_class=ap.RawTextHelpFormatter)
    parser.add_argument('name', type=str, help=h.name)
    
    # here we define the subparsers that we will use as commands in the CLI
    subparsers = parser.add_subparsers(dest='command')
    inv_parser = subparsers.add_parser('inv', help=h.i, formatter_class=ap.RawTextHelpFormatter)
    buy_parser = subparsers.add_parser('buy', help=h.b, formatter_class=ap.RawTextHelpFormatter)
    sell_parser = subparsers.add_parser('sell', help=h.s, formatter_class=ap.RawTextHelpFormatter)
    report_parser = subparsers.add_parser('report',help=h.rep, formatter_class=ap.RawTextHelpFormatter)
    set_date_parser = subparsers.add_parser('set-date', help=h.sd, formatter_class=ap.RawTextHelpFormatter)
    advance_parser = subparsers.add_parser('advance', help=h.a, formatter_class=ap.RawTextHelpFormatter)
    clean_parser = subparsers.add_parser('clean', help=h.c, formatter_class=ap.RawTextHelpFormatter)
    
    # here we add some arguments to the subparsers
    report_parser.add_argument('--r', type=str, dest='r', choices=['expired', 'movements', 'revenue', 'expenses', 'profits', 'all'], default='all', help=h.r)
    report_parser.add_argument('--exp', dest='exp', choices=['csv', 'png'], help= h.export)
    buy_parser.add_argument('--product-name', type=str, dest='p_name', help=h.pname)
    buy_parser.add_argument('--expiration-date', type=str, dest='exp_date', help=h.exp)
    buy_parser.add_argument('--buy-price', type=float, dest='buy_price', help=h.bprice)
    buy_parser.add_argument('--sell-price', type=float, dest='sell_price', help=h.sprice)
    buy_parser.add_argument('--quantity', type=int, dest='quantity', help=h.quant)
    sell_parser.add_argument('--quantity', type=int, dest='quantity', help=h.quant)
    sell_parser.add_argument('--product-id', type=int, dest='p_id', help=h.id)
    report_parser.add_argument('--from', type=str, dest='from_date', help=h.to)
    report_parser.add_argument('--to', type=str, dest='to_date', help=h.to)
    set_date_parser.add_argument('--to', type=str, dest='to_date', help=h.to)
    advance_parser.add_argument('--step', type=int, dest='step', default=1, help=h.id)

    # here we check what the use want to do and we execute it
    args = parser.parse_args()
    inventory = Inventory(args.name)
    if args.command == 'buy':
        name = args.p_name
        if name and args.exp_date and args.buy_price and args.sell_price and args.quantity:
            inventory.buy(name.lower(), args.exp_date, args.buy_price, args.sell_price, args.quantity)
        else:
            print('ERROR: missing arguments!!!')
            print('Correct sintax: superpy.py <inventory-name> --buy --product-name <product-name> --expiration-date <date> --buy-price <buy-price> --sell-price <sell-price> --quantity <quantity>')
    elif args.command == 'sell':
        if args.p_id and args.quantity:
            inventory.sell(args.p_id, args.quantity)
        else:
            print('ERROR: missing arguments!!!')
            print('Correct sintax: superpy.py <inventory-name> --sell --product-id <product-id> --quantity <quantity>')
    elif args.command == 'set-date':
        inventory.set_date(args.to_date)
    elif args.command == 'report':
        if args.r == 'expired':
            show_expired()
        elif args.r == 'movements':
            show_movements()
        elif args.r == 'revenue':
            show_revenue()
        elif args.r == 'expenses':
            show_expenses()
        elif args.r == 'profits':
            show_profits()
        elif args.r == 'all':
            show_expired()
            show_movements()
            show_revenue()
            show_expenses()
            show_profits()
        else:
            print('ERROR: comand not found')
    elif args.command == 'inv':
        rows = []
        for product in inventory.products:
            rows.append([product.id, product.name, product.expiring_date, product.buy_price, product.sell_price, product.quantity])
        columns = ['ID', 'NAME', 'EXPIRING DATE', 'BUY PRICE', 'SELL PRICE', 'IN STOCK']
        print_table(columns, rows, f'{inventory.name.upper()}    DATE: {inventory.today.upper()}')
    elif args.command == 'clean':
        inventory.clean()
    elif args.command == 'advance':
        inventory.advance_date(args.step)
    pass


if __name__ == "__main__":
    main()