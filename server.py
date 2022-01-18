"""Server for app."""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify, send_from_directory)
from model import db, connect_to_db
import crud
# import requests
# import json
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'xcvnzmv,nz,dfhaksd32239q48sdjfka'
app.jinja_env.undefined = StrictUndefined

@app.route('/items', methods = ['GET'])
def get_items():
    """Display a table with the items in inventory."""

    return render_template('items.html', items = crud.get_items())

@app.route('/items', methods = ['DELETE'])
def delete_item():
    """Display a table with the items in inventory."""

    item_to_delete = request.form.get('item-to-delete')
    print(f"item to delete is {item_to_delete}")

    return render_template('items.html', items = crud.get_items())





if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True, port=5001)