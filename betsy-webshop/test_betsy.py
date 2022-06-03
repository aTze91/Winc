from main import add_tag,add_user,add_product_to_catalog,remove_product,purchase_product,list_products_per_tag,list_user_products,search
from models import ProductTag, Tag, Transaction, User, Product, UserProduct
# --------------------ADD_TAG------------------------------------------------------#
add_tag('organic', '...')
add_tag('art', '...')
add_tag('furniture', '...')
add_tag('gift', '...')
add_tag('organic', '...')
tags = Tag.select().dicts()
assert tags == [{'id': 1, 'name': 'organic', 'description': '...'},
                {'id': 2, 'name': 'art', 'description': '...'},
                {'id': 3, 'name': 'furniture', 'description': '...'},
                {'id': 4, 'name': 'gift', 'description': '...'}]
# --------------------------------------------------------------------------#

# ---------------ADD_USER--------------------------------------#
add_user('Nik', 'Prins Hendrikkade 106', 'xxxx10002000')
add_user('Julia', 'Weteringschaans 41', 'tttt90006000')
add_user('Anna', 'Overtoom 31', 'ffff30004000')
add_user('Bob', 'Weteringschaans 41', 'cccc20007000')
add_user('Bob', 'Prins Hendrikkade 106', 'vvvv40007000')
add_user('Nik', 'Prins Hendrikkade 106', 'xxxx10002000')

assert  User.select().dicts() == [{'id': 1, 'name': 'Nik', 'address': 'Prins Hendrikkade 106', 'iban': 'xxxx10002000'},
                    {'id': 2, 'name': 'Julia', 'address': 'Weteringschaans 41', 'iban': 'tttt90006000'},
                    {'id': 3, 'name': 'Anna', 'address': 'Overtoom 31', 'iban': 'ffff30004000'},
                    {'id': 4, 'name': 'Bob', 'address': 'Weteringschaans 41', 'iban': 'cccc20007000'},
                    {'id': 5, 'name': 'Bob', 'address': 'Prins Hendrikkade 106', 'iban': 'vvvv40007000'}]
# ----------------------------------------------------------------------------#

# ----------------------------------add_product_to_catalog---------------------#
test_products = [
    {'product': {'name': 'sun glasses', 'description': 'wood frame , good for gift', 'price_in_cents': 7000, 'in_stock': 10}, 'id_user': 1},
    {'product': {'name': 'robot t-shirt', 'description': 'Hand printed t_shirt made of organic cotton', 'price_in_cents': 3490, 'in_stock': 7}, 'id_user': 2},
    {'product': {'name': 'gift card', 'description': 'nice art gift to say Happy birthday!', 'price_in_cents': 240, 'in_stock': 60}, 'id_user': 3},
    {'product': {'name': 'happy coffee', 'description': 'art gift coffee cup', 'price_in_cents': 400, 'in_stock': 20}, 'id_user': 4},
    {'product': {'name': 'scary mask', 'description': 'art furniture hand made wood mask', 'price_in_cents': 12000,'in_stock': 4}, 'id_user': 5},
    {'product': {'name': 'wallet', 'description': 'nice gift ledder wallet', 'price_in_cents': 4000, 'in_stock': 12}, 'id_user': 1},
    {'product': {'name': 'dino sweater', 'description': 'Hand printed sweater this is art', 'price_in_cents': 4700, 'in_stock': 8}, 'id_user': 2},
    {'product': {'name': 'sorry card', 'description': 'apologize with this art card', 'price_in_cents': 240, 'in_stock': 50}, 'id_user': 3}]

for product in test_products:
    add_product_to_catalog(product['id_user'], product['product'])
add_tag('cotton', '...')
assert Product.select().dicts() == [{'id': 1, 'name': 'sun glasses', 'description': 'wood frame , good for gift', 'price_in_cents': 7000, 'in_stock': 10},
                                   {'id': 2, 'name': 'robot t-shirt', 'description': 'Hand printed t_shirt made of organic cotton', 'price_in_cents': 3490, 'in_stock': 7},
                                   {'id': 3, 'name': 'gift card', 'description': 'nice art gift to say Happy birthday!','price_in_cents': 240, 'in_stock': 60},
                                   {'id': 4, 'name': 'happy coffee', 'description': 'art gift coffee cup','price_in_cents': 400,'in_stock': 20},
                                   {'id': 5, 'name': 'scary mask', 'description': 'art furniture hand made wood mask', 'price_in_cents': 12000,'in_stock': 4},
                                   {'id': 6, 'name': 'wallet', 'description': 'nice gift ledder wallet', 'price_in_cents': 4000,'in_stock': 12},
                                   {'id': 7, 'name': 'dino sweater', 'description': 'Hand printed sweater this is art', 'price_in_cents': 4700, 'in_stock': 8},
                                   {'id': 8, 'name': 'sorry card', 'description': 'apologize with this art card', 'price_in_cents': 240,'in_stock': 50}]
# --------------------------------------------------------------------------------------------------#

# ----------------------------------REMOVE_PRODUCT----------------------------------------------#
remove_product(5)
assert Product.get_or_none(Product.id==5) is None
# ---------------------------------------------------------------------------------------------#

# ------------------------PURCHASE_PRODUCT-----------------------------------------------------#
assert purchase_product(2, 4, 100) == None
purchase_product(2, 4, 1)
product = Product.get(Product.id==2)
assert product.in_stock == 6
bobtransactions = User.select(User,Transaction).join(Transaction).where(User.id==4).dicts()
assert bobtransactions[0]['product']==2
# ---------------------------------------------------------------------------------------------#

# --------------------------------LIST_PRODUCT_PER_TAG-----------------------------------------#
assert len(list_products_per_tag(5)) == 1
# --------------------------------------------------------------------------------------#

# ---------------------------------LIST_USER_PRODUCTS-------------------------------#
assert len(list_user_products(2)) == 2
# ----------------------------------------------------------------------------------------#

# -----------------------------------SEARCH------------------------------------------------#
assert search('Cofe')[0] == Product.get(Product.name=='happy coffee')
#--------------------------------------------------------------------------------------------#




print('-------------------------USERS------------------------------')
for user in User.select().dicts():
    print(user)
print('---------------------PRODUCTS-------------------------------')
for product in Product.select().dicts():
    print(product)
print('----------------TAGS-----------------------------')
for tag in Tag.select().dicts():
    print(tag)
print('-----------------------USERS_PRODUCTS--------------------------------------')
userproducts = (UserProduct.
                 select(UserProduct,User,Product)
                 .join(Product)
                 .switch(UserProduct)
                 .join(User)
                 .dicts())
for userproduct in userproducts:
    print(userproduct)
print('---------------------PRODUCTS_TAGS--------------------------')
productstags = (ProductTag
                .select(ProductTag,Product,Tag)
                .join(Tag)
                .switch(ProductTag)
                .join(Product)
                .dicts())
for producttag in productstags:
    print(producttag)
print('-----------------TRANSACTIONS---------------------------')
for transaction in Transaction.select().dicts():
    print(transaction)