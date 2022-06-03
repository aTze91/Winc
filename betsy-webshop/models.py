import peewee

db = peewee.SqliteDatabase(':memory:')


class Tag(peewee.Model):
    name = peewee.CharField()
    description = peewee.CharField()

    class Meta:
        database = db


class Product(peewee.Model):
    name = peewee.CharField()
    description = peewee.CharField()
    price_in_cents = peewee.IntegerField()
    tags = peewee.ManyToManyField(Tag)
    in_stock = peewee.IntegerField()

    class Meta:
        database = db


class User(peewee.Model):
    name = peewee.CharField()
    address = peewee.CharField()
    iban = peewee.CharField()
    products = peewee.ManyToManyField(Product)

    class Meta:
        database = db


class Transaction(peewee.Model):
    buyer = peewee.ForeignKeyField(User, backref='user_id')
    product = peewee.ForeignKeyField(Product, backref='product_id')
    quantity = peewee.IntegerField()
    date = peewee.DateTimeField()

    class Meta:
        database = db

ProductTag = Product.tags.get_through_model()
UserProduct = User.products.get_through_model()