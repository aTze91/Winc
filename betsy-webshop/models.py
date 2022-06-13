import peewee

db = peewee.SqliteDatabase(':memory:')


class Tag(peewee.Model):
    name = peewee.CharField(primary_key=True, unique=True)
    description = peewee.CharField(unique=True)

    class Meta:
        database = db


class Product(peewee.Model):
    name = peewee.CharField(unique=True)
    description = peewee.CharField(unique=True)
    price = peewee.DoubleField(constraints = [peewee.Check('price > 0')])
    tags = peewee.ManyToManyField(Tag)
    in_stock = peewee.IntegerField(constraints = [peewee.Check('in_stock >= 0')])

    class Meta:
        database = db


class User(peewee.Model):
    name = peewee.CharField() # I am leaving the possibility to duplicate names to handle homonymous cases
    address = peewee.CharField()
    iban = peewee.CharField(unique=True)
    products = peewee.ManyToManyField(Product)

    class Meta:
        database = db


class Transaction(peewee.Model):
    buyer = peewee.ForeignKeyField(User, backref='user_id')
    product = peewee.ForeignKeyField(Product, backref='product_id')
    quantity = peewee.IntegerField(constraints = [peewee.Check('quantity > 0')])
    date = peewee.DateTimeField()

    class Meta:
        database = db


ProductTag = Product.tags.get_through_model()
UserProduct = User.products.get_through_model()