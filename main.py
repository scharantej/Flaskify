 
# Import necessary libraries
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# Define the list of items
items = [
    {"name": "Item 1", "description": "Description of Item 1", "price": 10},
    {"name": "Item 2", "description": "Description of Item 2", "price": 20},
    {"name": "Item 3", "description": "Description of Item 3", "price": 30},
]

# Define the routes
@app.route("/")
def index():
    """Render the index page."""
    return render_template("index.html", items=items)

@app.route("/item/<item_id>")
def item_details(item_id):
    """Render the item details page."""
    item = items[int(item_id) - 1]
    return render_template("item_details.html", item=item)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
