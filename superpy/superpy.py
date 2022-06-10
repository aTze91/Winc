# Imports
import parser_help as h
from classes import Inventory
import argparse as ap
from rich import table as tb
import rich
import matplotlib.pyplot as plt

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.


def main():

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

    def show_expired():
        data = inventory.report('expired', None, None)
        rows = []
        for product in data['products']:
            rows.append([product.id, product.name, product.expiring_date, product.buy_price, product.sell_price, product.quantity])
        columns = ['ID', 'NAME', 'EXPIRATION DATE', 'BUY PRICE', 'SELL PRICE', 'IN STOCK']
        print_table(columns, rows, data['description'].upper())

    def show_movements():
        data = inventory.report('movements', args.from_date, args.to_date)
        columns = ['NAME', 'BUY PRICE', 'QUANTITY', 'DATE', 'ID']
        rows = data['bought']['movements']
        title = 'BUY MOVEMENTS:'
        print_table(columns, rows, title)
        columns = ['NAME', 'SELL PRICE', 'QUANTITY', 'DATE', 'ID']
        rows = data['sold']['movements']
        title = 'SELL MOVEMENTS:'
        print_table(columns, rows, title)

    def show_revenue():
        rows = []
        data = inventory.report('revenue', args.from_date, args.to_date)
        columns = ['NAME', 'QUANTITY', 'VALUE']
        for product in data['products']:
            rows.append([data['products'][product]['name'], data['products'][product]['quantity'], data['products'][product]['value']])
        print_table(columns, rows, data['description'].upper())

    def show_expenses():
        rows = []
        data = inventory.report('expenses', args.from_date, args.to_date)
        columns = ['NAME', 'QUANTITY', 'VALUE']
        for product in data['products']:
            rows.append([data['products'][product]['name'], data['products'][product]['quantity'], data['products'][product]['value']])
        print_table(columns, rows, data['description'].upper())

    def show_profits():
        rows = []
        data = inventory.report('profits', args.from_date, args.to_date)
        columns = ['NAME', 'PROFIT']
        for product in data['products']:
            rows.append([data['products'][product]['name'], data['products'][product]['profit']])
        print_table(columns, rows, data['description'].upper())
        

    parser = ap.ArgumentParser(description='Manage inventories', formatter_class=ap.RawTextHelpFormatter)
    command_group = parser.add_mutually_exclusive_group()
    parser.add_argument('name', type=str, help=h.name)
    command_group.add_argument('-b', '--buy', action='store_true', help=h.b)
    command_group.add_argument('-s', '--sell', action='store_true', help=h.s)
    command_group.add_argument('-r', '--report', action='store_true', help=h.rep)
    command_group.add_argument('-sd', '--set-date', action='store_true', help=h.sd)
    command_group.add_argument('-a', '--advance', action='store_true', help=h.a)
    command_group.add_argument('-c', '--clean', action='store_true', help=h.c)
    command_group.add_argument('-i', '--inventory', action='store_true', help=h.i)
    parser.add_argument('--r', type=str, dest='r', choices=['expired', 'movements', 'revenue', 'expenses', 'profits', 'all'], default='all', help=h.r)
    parser.add_argument('--product-name', type=str, dest='p_name', help=h.pname)
    parser.add_argument('--expiration-date', type=str, dest='exp_date', help=h.exp)
    parser.add_argument('--buy-price', type=float, dest='buy_price', help=h.bprice)
    parser.add_argument('--sell-price', type=float, dest='sell_price', help=h.sprice)
    parser.add_argument('--quantity', type=int, dest='quantity', help=h.quant)
    parser.add_argument('--product-id', type=int, dest='p_id', help=h.id)
    parser.add_argument('--from', type=str, dest='from_date', help=h.to)
    parser.add_argument('--to', type=str, dest='to_date', help=h.to)
    parser.add_argument('--step', type=int, dest='step', default=1, help=h.id)
    args = parser.parse_args()
    inventory = Inventory(args.name)
    if args.buy:
        if args.p_name.lower() and args.exp_date and args.buy_price and args.sell_price and args.quantity:
            inventory.buy(args.p_name.lower(), args.exp_date, args.buy_price, args.sell_price, args.quantity)
        else:
            print('ERROR: missing arguments!!!')
            print('Correct sintax: superpy.py <inventory-name> --buy --product-name <product-name> --expiration-date <date> --buy-price <buy-price> --sell-price <sell-price> --quantity <quantity>')
    elif args.sell:
        if args.p_id and args.quantity:
            inventory.sell(args.p_id, args.quantity)
        else:
            print('ERROR: missing arguments!!!')
            print('Correct sintax: superpy.py <inventory-name> --sell --product-id <product-id> --quantity <quantity>')
    elif args.set_date:
        inventory.set_date(args.to_date)
    elif args.report:
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
            plt.show()
        else:
            print('ERROR: comand not found')
    elif args.inventory:
        rows = []
        for product in inventory.products:
            rows.append([product.id, product.name, product.expiring_date, product.buy_price, product.sell_price, product.quantity])
        columns = ['ID', 'NAME', 'EXPIRING DATE', 'BUY PRICE', 'SELL PRICE', 'IN STOCK']
        print_table(columns, rows, f'{inventory.name.upper()}    DATE: {inventory.today.upper()}')
    elif args.clean:
        inventory.clean()
    elif args.advance:
        inventory.advance_date(args.step)
    pass


if __name__ == "__main__":
    main()
