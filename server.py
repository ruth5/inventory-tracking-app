"""Server for app."""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify, send_from_directory)
from model import db, connect_to_db
import crud
# import json
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'xcvnzmv,nz,dfhaksd32239q48sdjfka'
app.jinja_env.undefined = StrictUndefined

@app.route('/items', methods = ['GET'])
def get_items():
    """Display a table with the items in inventory."""

    return render_template('items.html', items = crud.get_items())

@app.route('/items', methods = ['POST'])
def create_item():
    """Add a new item to inventory based on the output of the new item form."""

    product_id = request.form.get('product-id')
    warehouse_id = request.form.get('warehouse-id')
    serial_number = request.form.get('serial-number')
    product = crud.get_product_by_id(int(product_id))
    warehouse = crud.get_warehouse_by_id(int(warehouse_id))

    crud.create_item(product_id, warehouse_id, serial_number)
    if serial_number:
        flash(f"{product.product_name} with serial number {serial_number} added to inventory")
    else:
        flash(f"A new {product.product_name} item was added to inventory")
    return render_template('items.html', items = crud.get_items())

@app.route('/items/<item_id>', methods = ['PUT'])
def edit_item(item_id):
    """Edit an item's data."""

    serial_number = request.json.get("serialNumber")
    item = crud.get_item_by_id(item_id)
    item.serial_number = serial_number
    db.session.commit()
    return { "success": True, "status": "Item data has been updated"}




@app.route('/items/<item_id>', methods = ['DELETE'])
def delete_item(item_id):
    """Delete an item from inventory."""
    item_to_delete = crud.get_item_by_id(item_id)
    db.session.delete(item_to_delete)
    db.session.commit()
    return jsonify(f"Item {item_id} deleted")

@app.route('/new-item-form', methods = ['GET'])
def show_new_item_form():
    """Display a form where users can generate new items."""

    return render_template('new-item-form.html', products = crud.get_products(), warehouses = crud.get_warehouses())

@app.route('/edit-item-form', methods = ['GET'])
def show_edit_item_form():
    """Display a form where users can edit existing items."""

    item_id = request.args.get('item-id')
    return render_template('edit-item-form.html', item=crud.get_item_by_id(item_id))






if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True, port=5001)