# NShop E-commerce Platform Documentation

## Project Overview
NShop is a Django-based e-commerce platform that allows users to browse products, add them to their cart, manage quantities, and place orders. The application follows the MVT (Model-View-Template) architecture pattern and consists of several interconnected Django apps.

## System Requirements
- Python 3.x
- Django 5.1.x
- Web browser with JavaScript enabled

## Project Structure

### Django Apps
The project consists of the following Django apps:

1. **mainapp**: Core product functionality
2. **authentication**: User login and registration
3. **cart**: Shopping cart management

### Directory Structure
```
Nshop/
├── Nshop/                  # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── mainapp/                # Main product functionality
├── authentication/         # User authentication 
├── cart/                   # Shopping cart management
├── static/                 # Static assets
│   ├── css/
│   └── js/
├── media/                  # User-uploaded content
└── manage.py               # Django management script
```

## Features

### User Management
- User registration with custom form validation
- Authentication with custom login forms
- Session management

### Product Management
- Browse product listings
- View detailed product information
- Admin interface for adding, editing, and deleting products

### Shopping Cart
- Add products to cart
- Adjust item quantities (increase/decrease)
- Remove items from cart
- Real-time price calculation with AJAX

## Models

### Product (mainapp.models)
```python
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    desc = models.TextField(max_length=500)
    img = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField()
```

### CartItem (cart.models)
```python
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
```

## Views

### Main App Views
- `homeView`: Displays all products
- `ProductDetails`: Shows detailed information about a product
- `AddProduct`: Form for adding new products (staff only)
- `EditProduct`: Form for updating product details (staff only)
- `DelProduct`: Form for removing products (staff only)

### Authentication Views
- `UserRegister`: Handles new user registration
- `UserLogin`: Processes user login

### Cart Views
- `viewCart`: Displays the user's cart contents
- `addToCart`: Adds a product to the cart
- `remFromCart`: Removes an item from the cart
- `addQuantity`: AJAX endpoint to increase item quantity
- `remQuantity`: AJAX endpoint to decrease item quantity

## Templates

### Base Template
- `base.html`: The master template containing the navigation bar, footer, and common styling

### Product Templates
- `home.html`: Product grid display
- `product_details.html`: Detailed product view
- `add_products.html`: Form for adding products
- `edit_product.html`: Form for editing products
- `del_product.html`: Confirmation for product deletion

### Authentication Templates
- `signin.html`: Login form
- `signup.html`: Registration form

### Cart Templates
- `cart.html`: Shopping cart display with quantity controls

## JavaScript Functionality

The `script.js` file contains functionality for updating cart quantities asynchronously:

```javascript
function updateCart(actionUrl, cartItemId, isAdd, csrf_token) {
    fetch(actionUrl, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Update UI elements with new data
        // ...
    })
    .catch(error => console.error('Error:', error));
}
```

This function:
1. Sends AJAX requests to the server
2. Updates quantity, subtotal, and overall total in real-time
3. Removes items from the DOM when quantity reaches zero

## URL Patterns

### Main URLs
- `/`: Homepage with product listings
- `/about`: About page
- `/contact`: Contact page
- `/products/<id>`: Product details
- `/products/add`: Add product (staff only)
- `/products/edit/<id>`: Edit product (staff only)
- `/products/del/<id>`: Delete product (staff only)

### Authentication URLs
- `/accounts/login`: User login
- `/accounts/register`: User registration
- `/accounts/logout`: User logout

### Cart URLs
- `/cart/`: View cart contents
- `/cart/addCart/<product_id>`: Add item to cart
- `/cart/remCart/<cart_item_id>`: Remove item from cart
- `/cart/add/<cart_item_id>`: AJAX endpoint to increase quantity
- `/cart/remove/<cart_item_id>`: AJAX endpoint to decrease quantity

## Security Features
- CSRF protection for all forms and AJAX requests
- Login required for cart operations
- Staff-only access for product management
- Authentication via Django's built-in system

## Setup and Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv virt`
3. Activate the virtual environment:
   - Windows: `virt\Scripts\activate`
   - Unix/MacOS: `source virt/bin/activate`
4. Install dependencies: `pip install django Pillow`
5. Apply migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Run the development server: `python manage.py runserver`

## Future Enhancements
- Checkout and payment processing
- User profiles and order history
- Product categories and filtering
- Search functionality
- Product reviews and ratings
