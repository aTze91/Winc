
import csv
import os
import shutil
from classes import Inventory


# testing if new_csv create a new file .csv to use as inventory

inventory = Inventory('inventory_test')
# inventory_path = os.path.join(os.getcwd(), 'inventory_test.csv')
assert os.path.exists(inventory.path) is True

# testing if buy_product add the product on the last line of the inventory
inventory.buy('eggs', '2022-05-04', 2.80, 5.6, 10)
inventory.buy('eggs', '2022-05-04', 2.80, 5.6, 4)
inventory.buy('broccoli', '2022-05-23', 2.30, 4.5, 20)

with open(inventory.path, 'r', newline='') as csvfile:
    test_reader = reader = csv.reader(csvfile,  delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
    rows = []
    for row in test_reader:
        rows += [row]
    csvfile.close()
assert [1, 'broccoli', '2022-05-23', 2.3, 4.5, 20.0] == rows[1]
assert [0.0, 'eggs', '2022-05-04', 2.8, 5.6, 14.0] == rows[0]

# testing set_date

inventory.set_date('2022-05-22')
test_product_0 = inventory.get_product(0)
test_product_1 = inventory.get_product(1)

assert inventory.today == '2022-05-22'
assert test_product_1.today == '2022-05-22'

# testing if is_expired recognise an expired product


assert test_product_0.is_expired() is True
assert test_product_1.is_expired() is False

# testing sell_product

inventory.sell(1, 8)
test_product = inventory.get_product(1)
assert test_product.quantity == 12
inventory.set_date()

# testing revenue
assert inventory.revenue('2021-04-20', inventory.today)["description"] == '8.0 sold products for a total value of 36.0'

# testing if clean_inventory leaves the inventory with no products

inventory.clean()
with open(inventory.path, newline='') as csvfile:
    test_reader = csv.reader(csvfile, delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
    for row in test_reader:
        assert test_reader.line_num == 0
    csvfile.close()
shutil.rmtree(inventory.dirpath)
