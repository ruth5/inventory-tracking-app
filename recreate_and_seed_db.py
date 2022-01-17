"""Seeds the database with 10 test users."""

import os
import requests

from faker import Faker

import random


import crud, model, server

os.system('dropdb inventory_track_app')
os.system('createdb inventory_track_app')

model.connect_to_db(server.app, echo=False)
model.db.create_all()

fake = Faker()
Faker.seed(438234)
random.seed(3482394)

def get_fake_product_names():
    """Gets a list of fake product names from the Fake Store API."""

    url = "https://fakestoreapi.com/products"
    req = requests.get(url)
    req_json = req.json()
    fake_product_names = [product['title'] for product in req_json]

    return fake_product_names



def make_fake_products(fake_product_names):
    """Seed the database with fake products. Return a list of the fake products"""
    
    fake_products = []
    for fake_product_name in fake_product_names:
        # Note, in a real inventory tracking system there would often be letters in the SKU, 
        # and the SKU would often have letters or numerical codes that correlated with product attributes.
        # For simplicity, I will use a random number of a specific length as this is easily generated
        # by the faker library in python.
        fake_SKU = fake.ean(length=8)
        fake_products.append(crud.create_product(fake_product_name, fake_SKU))

    return fake_products
    
def make_fake_items(fake_products):
    """Seed the database with fake items based on fake products."""
    electronics = {'WD 2TB Elements Portable External Hard Drive - USB 3.0 ', 'SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s', 'Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5', 'WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive', 'Acer SB220Q bi 21.5 inches Full HD (1920 x 1080) IPS Ultra-Thin', 'Samsung 49-Inch CHG90 144Hz Curved Gaming Monitor (LC49HG90DMNXZA) – Super Ultrawide Screen QLED '}
    for fake_product in fake_products:
        # randomly generate between 1 and 15 items of each product
        for i in range(random.randint(1, 15)):
            if fake_product.product_name in electronics:
                # Only electronics get serial numbers in this example database.
                # Again, use the faker library barcode generator function for simplicity
                fake_serial_number = fake.ean(length=13)
                crud.create_item(fake_product.id, fake_serial_number)
            else:
                crud.create_item(fake_product.id)


fake_product_names = get_fake_product_names()
fake_products = make_fake_products(fake_product_names)
make_fake_items(fake_products)

