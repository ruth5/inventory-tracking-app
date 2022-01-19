"""CRUD operations."""

from model import db, Product, Item, Warehouse, connect_to_db


def create_product(product_name, SKU):
    """Create and return a new product."""

    product = Product(product_name=product_name, SKU=SKU)

    db.session.add(product)
    db.session.commit()

    return product


def create_item(product_id, warehouse_id=None, serial_number=None):
    """Create and return a new item."""

    item = Item(product_id=product_id, warehouse_id=warehouse_id,
                serial_number=serial_number)
    db.session.add(item)
    db.session.commit()

    return item


def create_warehouse(warehouse_name, street_address=None, city=None, state_or_province=None, postal_code=None, country=None):
    """Create and return a new warehouse."""

    warehouse = Warehouse(warehouse_name=warehouse_name, street_address=street_address, city=city,
                          state_or_province=state_or_province, postal_code=postal_code, country=country)
    db.session.add(warehouse)
    db.session.commit()

    return warehouse


def get_items():
    """Get a list of all items in the database, ordered by product_id."""

    items = Item.query.order_by(Item.product_id, Item.id)

    return items


def get_products():
    """Get a list of all products in the database."""

    products = Product.query.all()

    return products


def get_warehouses():
    """Get a list of all warehouses in the database."""

    warehouses = Warehouse.query.all()

    return warehouses


def get_product_by_id(product_id):
    """Returns a product with the given product id if it exists, otherwise return None"""

    return Product.query.filter_by(id=product_id).first()


def get_item_by_id(item_id):
    """Returns a item with the given item id if it exists, otherwise return None"""

    return Item.query.filter_by(id=item_id).first()


def get_warehouse_by_id(warehouse_id):
    """Returns a warehouse with the given warehouse id if it exists, otherwise return None"""

    return Warehouse.query.filter_by(id=warehouse_id).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app, echo=False)
