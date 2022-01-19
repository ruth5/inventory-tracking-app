"""Server for app."""

from flask import (Flask, render_template, request, flash, redirect, jsonify)
from model import db, connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'xcvnzmv,nz,dfhaksd32239q48sdjfka'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def redirect_from_homepage():
    """Redirects users to the item inventory page, the main page of the site."""

    return redirect('/items')


@app.route('/items', methods=['GET'])
def get_items():
    """Display a table with the items in inventory."""

    return render_template('items.html', items=crud.get_items())


@app.route('/items', methods=['POST'])
def create_item():
    """Add a new item to inventory based on the output of the new item form."""

    product_id = request.form.get('product-id')
    warehouse_id = request.form.get('warehouse-id')
    serial_number = request.form.get('serial-number')
    product = crud.get_product_by_id(product_id)
    warehouse = crud.get_warehouse_by_id(warehouse_id)

    crud.create_item(product_id, warehouse_id, serial_number)
    if serial_number:
        flash(f"{product.product_name} with serial number {serial_number} added to {warehouse.warehouse_name} warehouse inventory")
    else:
        flash(
            f"A new {product.product_name} item was added to {warehouse.warehouse_name} warehouse inventory")
    return render_template('items.html', items=crud.get_items())


@app.route('/items/<item_id>', methods=['PUT'])
def edit_item(item_id):
    """Edit an item's data."""

    serial_number = request.json.get("serialNumber")
    warehouse_id = request.json.get("warehouseID")
    item = crud.get_item_by_id(item_id)
    item.serial_number = serial_number
    item.warehouse_id = int(warehouse_id)
    db.session.commit()
    return {"success": True, "status": f"Item data for this {item.product.product_name} item has been updated"}


@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete an item from inventory."""

    item_to_delete = crud.get_item_by_id(item_id)
    crud.delete_item(item_to_delete)

    return jsonify(f"Item {item_id} deleted")

@app.route('/warehouses', methods=['POST'])
def create_warehouse():
    """Add a new warehouse to database based on the output of the new warehouse form."""

    warehouse_name = request.json.get("warehouseName")
    street_address = request.json.get("streetAddress")
    city = request.json.get("city")
    state_or_province = request.json.get("state")
    postal_code = request.json.get("postal-code")
    country = request.json.get("country")
    crud.create_warehouse(warehouse_name, street_address,
                          city, state_or_province, postal_code, country)

    return {"success": True, "status": f"New warehouse {warehouse_name} has been created."}

@app.route('/new-item-form', methods=['GET'])
def show_new_item_form():
    """Display a form where users can generate new items."""

    return render_template('new-item-form.html', products=crud.get_products(), warehouses=crud.get_warehouses())


@app.route('/edit-item-form', methods=['GET'])
def show_edit_item_form():
    """Display a form where users can edit existing items."""

    item_id = request.args.get('item-id')
    return render_template('edit-item-form.html', item=crud.get_item_by_id(item_id), warehouses=crud.get_warehouses())


@app.route('/new-warehouse-form', methods=['GET'])
def show_new_warehouse_form():
    """Display a form where users can generate new warehouses."""

    return render_template('new-warehouse-form.html')





if __name__ == "__main__":
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True, port=5001)
