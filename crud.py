"""CRUD operations."""

from model import db, Product, Item, connect_to_db


def create_product(product_name, SKU):
    """Create and return a new product."""

    product = Product(product_name=product_name, SKU=SKU)

    db.session.add(product)
    db.session.commit()

    return product

def create_item(product_id, serial_number=None):
    """Create and return a new item."""

    item = Item(product_id=product_id, serial_number=serial_number)
    db.session.add(item)
    db.session.commit()

    return item

if __name__ == '__main__':
    from server import app
    connect_to_db(app, echo=False)