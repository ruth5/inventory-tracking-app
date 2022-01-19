"""Tests for Inventory Tracking app"""

"""Important: the first time this script is run, run "createdb inventory_test_db" on the command line to create the test database."""


import server
import unittest
import crud
from model import db, connect_to_db, Warehouse, Product, Item


def test_data():
    """Data for test db for tests"""

    # in case the function is called again, get rid of any old data and start again.
    Item.query.delete()
    Warehouse.query.delete()
    Product.query.delete()

    test_warehouse = crud.create_warehouse('Mountain View')
    test_product = crud.create_product('Salted Caramel Ice Cream', 'ICE32489104')
    crud.create_item(test_product.id, warehouse_id = test_warehouse.id)


class FlaskTests(unittest.TestCase):
    """Integration tests: testing Flask server and database."""


    def setUp(self):
        """Perform before every tests"""
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

        # Connect to test database

        connect_to_db(server.app, "postgresql:///inventory_test_db")

        # Create tables and add sample data
        db.create_all()
        test_data()
    
    def test_get_warehouses(self):
        """Test that test warehouse can be queried with crud.get_warehouses() function."""


        warehouses = crud.get_warehouses()
        # there should only be one warehouse in the database
        warehouse = warehouses[0]
        self.assertEqual(warehouse.warehouse_name, 'Mountain View')
    

    def test_items_page(self):
        """Test that the items page loads."""

        result = self.client.get('/items')
        self.assertIn(b'<h1>Item Inventory</h1>', result.data)

    def test_new_warehouse_form_page(self):
        """Test that the new warehouse item form page loads."""

        result = self.client.get('/new-warehouse-form')
        self.assertIn(b'<h1>Add a New Warehouse</h1>', result.data)

    def test_new_item_form_page(self):
        """Test that the new item form page loads."""

        result = self.client.get('/new-item-form')
        self.assertIn(b'<h1>Add Item to Inventory</h1>', result.data)

    def test_create_item_and_display(self):
        """Test that newly created item shows up on items page."""

        warehouse = crud.create_warehouse('Sunnyvale')
        product = crud.create_product('Honey Lavender Ice Cream', 'ICE324989234')
        crud.create_item(product.id, warehouse.id)

        result = self.client.get('/items')
        self.assertIn(b'Honey Lavender Ice Cream', result.data)




if __name__ == '__main__':
    unittest.main()