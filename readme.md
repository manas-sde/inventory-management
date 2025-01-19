# Inventory Management System

### Written by: Manas Mishra
(GitHub: [manas-sde](https://github.com/manas-sde))

---

## Overview

This is a Django-based Inventory Management System that provides functionality to manage products, suppliers, stock movements, sale orders, and stock levels. It includes the following features:

- Add, list, and manage products and suppliers.
- Record stock movements (incoming and outgoing).
- Create, complete, and cancel sale orders.
- Check current stock levels.
- Filtering and basic user interface for navigation.

---

## Features

1. **Add Product**: Add new products with validation for stock quantity, price, and details.
2. **List Products**: Retrieve a list of all products, including their details and supplier information.
3. **Add Supplier**: Add suppliers with validation for email and phone number format.
4. **List Suppliers**: View all suppliers with detailed information.
5. **Add Stock Movement**: Record stock additions or removals and update stock levels.
6. **Create Sale Order**: Create new sale orders and update stock.
7. **Cancel Sale Order**: Cancel sale orders and adjust stock accordingly.
8. **Complete Sale Order**: Mark sale orders as complete and update stock.
9. **List Sale Orders**: Retrieve all sale orders with their details.
10. **Stock Level Check**: View current stock levels for all products.

---

## Installation

Follow these steps to set up and run the Inventory Management System:

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/manas-sde/inventory-management-system.git
   cd inventory-management-system
   ```

2. **Create a Virtual Environment**  
   Create and activate a virtual environment for the project:
   ```bash
   virtualenv venv
   ```
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**  
   Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**  
   Run the following command to apply database migrations:
   ```bash
   py manage.py migrate
   ```

5. **Run the Development Server**  
   Start the Django development server:
   ```bash
   py manage.py runserver
   ```

6. **Access the Application**  
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

---

## Project Structure

The project contains the following key files and directories:

```
├── inventory_management/          # Main Django app folder
├── templates/                     # HTML templates for the UI
├── static/                        # Static files (CSS, JS)
├── requirements.txt               # Project dependencies
├── manage.py                      # Django's main management script
└── README.md                      # This README file
```

---

## How to Contribute

1. Fork the repository on GitHub.
2. Create a new feature branch.
3. Commit your changes and push the branch.
4. Open a pull request for review.

---

## License

This project is licensed under the MIT License.

---

### Contact

For queries or support, please reach out via GitHub: [manas-sde](https://github.com/manas-sde).

