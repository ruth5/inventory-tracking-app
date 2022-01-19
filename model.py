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
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouses.id'))
    serial_number = db.Column(db.String)
    product = db.relationship("Product", back_populates="items")
    warehouse = db.relationship("Warehouse", back_populates="items")

    def __repr__(self):
        return f"Item id={self.id}, product_id={self.product_id}, serial_number={self.serial_number}"


class Warehouse(db.Model):
    """A warehouse."""

    __tablename__ = "warehouses"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    warehouse_name = db.Column(db.String)
    street_address = db.Column(db.String)
    city = db.Column(db.String)
    state_or_province = db.Column(db.String(2))
    postal_code = db.Column(db.String)
    country = db.Column(db.String)

    items = db.relationship("Item", back_populates="warehouse")


    def __repr__(self):
        return f"<Warehouse id={self.id} warehouse_name={self.warehouse_name}"



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
