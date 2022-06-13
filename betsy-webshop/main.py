__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"
from datetime import datetime
from models import Tag, Transaction, User, Product, ProductTag, UserProduct, db

db.connect()
db.create_tables([Tag, Transaction, User, Product, ProductTag, UserProduct])


def search(term):
    result = (ProductTag
                .select(ProductTag, Product, Tag)
                .join(Product)
                .switch(ProductTag)
                .join(Tag)
                .where((Tag.name ** ('%' + term + '%'))        # I use ILIKE and wildcards to handle litle spelling mistakes
                | (Tag.description ** ('%' + term + '%')) 
                | (Product.name ** ('%' + term + '%')) 
                | (Product.description ** ('%' + term + '%')))
                .group_by(Product.name)
                .objects())
    return result


def list_user_products(user_id):
    userproducts = (UserProduct.
                 select(UserProduct,User,Product)
                 .join(Product)
                 .switch(UserProduct)
                 .join(User)
                 .where(User.id==user_id)
                 .dicts())
    return userproducts


def list_products_per_tag(tag_name):
    products_per_stag = (ProductTag
                .select(ProductTag,Product,Tag)
                .join(Tag)
                .switch(ProductTag)
                .join(Product)
                .where(Tag.name==tag_name)
                .dicts())
    return products_per_stag

# product must be a dict {'name': str, 'description': str, 'price': float, 'in_stock': int}
def add_product_to_catalog(user_id, product):
    new_product, created = Product.get_or_create(name=product['name'], defaults=product)
    new_product.save()
    if created is False:
        print('One product with this name already exists')
    else:
        tags = Tag.select().objects()
        possible_tags = str.split(new_product.description.lower())
        # if a new product is been created I check if I can connect it to any Tag in the database
        for tag in tags:
            if tag.name.lower() in possible_tags:
                new_product.tags.add(tag)
        new_product.save()
        user = User.get(User.id==user_id)
        user.products.add(new_product)



def update_stock(product_id, new_quantity):
    product = Product.get(Product.id==product_id)
    product.in_stock = new_quantity
    product.save()


def purchase_product(product_id, buyer_id, quantity):
    product = Product.get(Product.id==product_id)
    if product.in_stock >= quantity: 
        update_stock(product_id, (product.in_stock - quantity))
        buyer = User.get(User.id==buyer_id)
        transaction = Transaction.create(product=product, buyer=buyer, quantity=quantity, date=datetime.now())
        transaction.save()
        return transaction
    else:
        print('ERROR: not enough in stock')
        return None


def remove_product(product_id):
    product = Product.get(Product.id==product_id)
    product.delete_instance()
    product.save()


def add_user(user_name, address, iban):
    new_user, created =(User.get_or_create(name=user_name, address=address ,
                                           defaults={'name': user_name, 'address': address, 'iban': iban}))
    if created is False:
        print('User already exists')
    new_user.save()
    return new_user


def add_tag(tag_name, description): # I use get_or_create to check if the tag already exist 
    new_tag, created = Tag.get_or_create(name=tag_name, defaults={'name': tag_name, 'description': description})
    if created is False:  
        print('Tag already exists')
    else: # if a new tag is been created I check if I can connect it to any Product in the database 
        for product in Product.select().objects():
            if new_tag.name.lower() in str.split(product.description.lower()):
                product.tags.add(new_tag)
                product.save()
    new_tag.save()
    return new_tag
