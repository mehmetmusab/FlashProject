# Project: Flask Product Listing App

## Overview
This is a simple Flask web application that displays a list of products, provides search functionality, and allows users to view product details. The app uses SQLite as its database and includes basic HTML and CSS for styling.

## Features
- **Home Page**: Displays a list of products with images, descriptions, and prices.
- **Search**: Allows users to search for products by name, description, or category.
- **Product Details**: Shows detailed information about a selected product, including breadcrumbs for navigation.

## Technologies Used
- Python (Flask framework)
- SQLite (for database)
- HTML, CSS (for frontend)

## Setup Instructions
### 1. Clone the Repository
```bash
https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install flask flask-sqlalchemy
```

### 4. Initialize the Database
Run the app once to create the database and populate it with sample data:
```bash
python app.py
```

### 5. Run the Application
```bash
python app.py
```
The app will be accessible at `http://127.0.0.1:5000/`.

## File Structure
```
project-folder/
|-- app.py             # Main Flask application
|-- models.py          # Database models
|-- static/
|   |-- css/
|   |   |-- style.css  # Styling for the app
|   |-- images/        # Product images
|-- templates/
|   |-- home.html      # Home page template
|   |-- product_detail.html # Product details template
```

## License
This project is open-source and available under the MIT License.

