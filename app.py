from flask import Flask
from dbcreds import production_mode
import endpoints.client, endpoints.client_login, endpoints.restaurant, endpoints.restaurant_login, endpoints.restaurant_images, endpoints.menu_item, endpoints.menu_item_images, endpoints.client_order
from flask_cors import CORS

# calling the Flask function which will return a value that will be used in my API
app = Flask(__name__)
CORS(app)

############### CLIENT ###############
@app.post('/api/client')
def post_client():
    return endpoints.client.post()

@app.get('/api/client')
def get_client():
    return endpoints.client.get()

@app.patch('/api/client')
def patch_client():
    return endpoints.client.patch()

@app.delete('/api/client')
def delete_client():
    return endpoints.client.delete()


############### CLIENT LOGIN ###############
@app.post('/api/client-login')
def post_client_login():
    return endpoints.client_login.post()

@app.delete('/api/client-login')
def delete_client_token():
    return endpoints.client_login.delete()


############### RESTAURANT ###############
@app.post('/api/restaurant')
def post_restaurant():
    return endpoints.restaurant.post()

@app.get('/api/restaurant')
def get_restaurant():
    return endpoints.restaurant.get()

@app.patch('/api/restaurant')
def patch_restaurant():
    return endpoints.restaurant.patch()

@app.delete('/api/restaurant')
def delete_restaurant():
    return endpoints.restaurant.delete()


############### RESTAURANT LOGIN ###############
@app.post('/api/restaurant-login')
def post_restaurant_login():
    return endpoints.restaurant_login.post()

@app.delete('/api/restaurant-login')
def delete_restaurant_login():
    return endpoints.restaurant_login.delete()


############### RESTAURANT IMAGES ###############
@app.post('/api/restaurant-images')
def post_restaurant_images():
    return endpoints.restaurant_images.post()

@app.get('/api/restaurant-images')
def get_restaurant_images():
    return endpoints.restaurant_images.get()

@app.patch('/api/restaurant-images')
def patch_restaurant_images():
    return endpoints.restaurant_images.pacth()


############### MENU ITEM ###############
@app.post('/api/menu-item')
def post_menu_item():
    return endpoints.menu_item.post()

@app.get('/api/menu-item')
def get_all_menu_items():
    return endpoints.menu_item.get()

@app.patch('/api/menu-item')
def patch_menu_item():
    return endpoints.menu_item.patch()

@app.delete('/api/menu-item')
def delete_menu_item():
    return endpoints.menu_item.delete()


############### MENU ITEM IMAGES ###############
@app.post('/api/menu-item-images')
def post_menu_item_image():
    return endpoints.menu_item_images.post()

@app.patch('/api/menu-item-images')
def patch_menu_item_image():
    return endpoints.menu_item_images.pacth()


############### CLIENT_ORDER ###############
@app.post('/api/client-order')
def post_order():
    return endpoints.client_order.post()

@app.get('/api/client-order')
def get_order():
    return endpoints.client_order.get()


# if statement to check if the production_mode variable is true, if yes, run in production mode, if not, run in testing mode
if (production_mode):
    print("Running in Production Mode")
    import bjoern  # type: ignore
    bjoern.run(app, "0.0.0.0", 5010)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode")

    app.run(debug=True)