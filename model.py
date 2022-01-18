"""Data models for app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    """A product."""

    __tablename__ = "products"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_name = db.Column(db.String, nullable=False)
    SKU = db.Column(db.String, nullable=False, unique=True)
    items = db.relationship("Item", back_populates="product")

    def __repr__(self):
        return f"<Product id={self.id}, product_name={self.product_name}, SKU={self.SKU}"


class Item(db.Model):
    """An item. This is an individual instance of a product."""

    __tablename__ = "items"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    serial_number = db.Column(db.String)
    product = db.relationship("Product", back_populates="items")

    def __repr__(self):
        return f"Item id={self.id}, product_id={self.product_id}, serial_number={self.serial_number}"


class Customer(db.Model):
    """A customer (to whom a shipment is sent)."""

    __tablename__ = "customers"

    id = db.Column(db.Integer,
                   autoincrement=True,
                   primary_key=True)
    full_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Customer id={self.id} full_name={self.full_name} email={self.email}>"


class Shipment(db.Model):
    """A shipment (order)."""

    __tablename__ = "shipments"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    is_shipped = db.Column(db.Boolean)
    order_date = db.Column(db.DateTime)
    street_address = db.Column(db.String)
    city = db.Column(db.String)
    state_or_province = db.Column(db.String(2))
    country = db.Column(db.String)

    def __repr__(self):
        return f"<Shipment id={self.id} customer_id ={self.id} is_shipped={self.is_shipped}"


class Shipment_item(db.Model):
    """Manage the relationship between Items and Shipments."""

    __tablename__ = "shipment_items"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    shipment_id = db.Column(db.Integer, db.ForeignKey('shipments.id'))

    def __repr__(self):
        return f"<Shipment_item id={self.id} item_id={self.item_id} shipment_id ={self.shipment_id}"


def connect_to_db(flask_app, db_uri="postgresql:///inventory_track_app", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app, echo=False)
