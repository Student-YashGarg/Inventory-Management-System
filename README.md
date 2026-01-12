# Inventory Management System (IMS)

A **GUI-based Inventory Management System** built using **Python, CustomTkinter, and MySQL**.  
The application follows a **clean architecture (GUI + Model + DAO)** and provides **role-based dashboards** for administration and shopping/billing operations.

---
#-----------------------------------------------------------------------------------------------
## 🚀 Features
- Secure login system
- Role-based access (Admin / Shopping)
- Admin dashboard for inventory management
- Shopping dashboard for billing and sales
- Automatic product stock updates after purchase
- Modular, scalable, and maintainable code structure

---
#----------------------------------------------------------------------------------------------
## 🧭 Application Entry Points
The system can be launched in **three different ways** depending on the use case:

### 
1️⃣ Login-Based Entry (Recommended):
  python LOGIN_MAIN_FORM.py
  
  User logs in using username and password
  Based on credentials:
  Admin Dashboard opens
  Shopping Dashboard opens
  
2️⃣ Direct Admin Dashboard
  python IMS.py
  
  Opens the Admin Dashboard directly
  Useful for development and testing

3️⃣ Direct Shopping Dashboard
  python SHOPPING.py
  
  Opens the Shopping / Billing Dashboard directly
  Useful for POS and billing testing
###
#--------------------------------------------------------------------------------------------
🖥️ Dashboards Overview

  🔐 Login Form:
  User authentication
  Role-based dashboard redirection
  
  🛠️ Admin Dashboard:
  Manage products, categories, and suppliers
  View and control inventory
  Monitor product availability and stock levels
  
  🛒 Shopping Dashboard:
  Product selection and quantity management
  Bill generation
  Automatic stock deduction after purchase

#------------------------------------------------------------------------------------------------
🛠️ Technologies Used

  Python
  CustomTkinter (CTk)
  MySQL
  SQL
  DAO Design Pattern
  MVC-like Architecture

#-------------------------------------------------------------------------------------------------
📂 Project Structure

  Inventory_Management_System/
  ├── LOGIN_MAIN_FORM.py
  ├── IMS.py
  ├── SHOPPING.py
  ├── models/
  ├── dao/
  ├── database/
  ├── assets/
  └── README.md

#------------------------------------------------------------------------------------------------------
🗄️ Database

  MySQL database is used to store:
    User credentials
    Product details
    Categories
    Suppliers
    Sales and billing records
    All database operations are handled using a DAO layer

#------------------------------------------------------------------------------------------------------
🎯 Purpose of the Project
  
  This project was developed to:
    Apply Python and SQL concepts in a real-world application
    Practice GUI development using CustomTkinter
    Implement clean and maintainable architecture
    Build a strong portfolio project for internships and entry-level roles
    
#################################################################################################################
👤 Author
  
  Yash Garg
  B.Tech Graduate
  Python | SQL | CustomTkinter | Machine Learning
