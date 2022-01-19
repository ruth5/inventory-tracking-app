# Inventory Tracking App Overview
This is an inventory tracking web application. The application has the following features:
- Basic CRUD functionality. Using the web app, the following actions can be completed:
    * Create inventory items
    * Edit them
    * Delete them
    * View a list of them
- Ability to create warehouses/locations and assign inventory to specific locations

# Tech Stack
Backend: Python, Flask, PostgreSQL, SQLAlchemy, Jinja2

Frontend: JavaScript, HTML/CSS, Bootstrap

# Structure
- `server.py` contains Flask server setup and all routes
- `model.py` set up of PostgreSQL database that stores items, products, and warehouses
- `crud.py` contain functions for interacting with the PostgreSQL database
- `/static/templates/` contains all HTML Jinja templates
- `/static/js/` contains all JavaScript files, mainly used to send fetch requests to backend.
- `tests.py` contains tests for the application

# Running the app

- Set up and activate a python virtual environment. In the command line, run:
    * `virtualenv env`
    * `source env/bin/activate`
- Install all dependencies:
    * `pip3 install -r requirements.txt`
- Set up and seed the database (NOTE: this will drop the database and create a new one. Do not run this script if you do not want to drop the database)
    * run `python3 recreate_and_seed_db.py`
- Start up the server and run the app!
    * run `python3 server.py`
    * Navigate `localhost:5001` to see the app in your browser

# Running tests

- Set up a testing database:
    * `createdb inventory_test_db`
- Run the test file
    * `python3 tests.py`



# Next steps

In the future, I would prioritize the following as I worked to improve the app:
- Add additional tests, including unit tests and integration tests, to improve test coverage
- Create different inventory views, such as a view that shows item counts by product or by warehouse
- Improve the UI for adding or editing new items. Currently adding/editing items involves redirection to a different page and then back to the item inventory. It would be nice if users could edit/add items with a modal or other tool on the same page.
- Deploy the site
