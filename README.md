# Drift – Car Rental Management System

![Drift Landing Page](screenshots/landing.png)

A modern car rental management system built using **Python, Django, SQLite, Bootstrap, and Object-Oriented Programming (OOP)** principles. Drift provides a seamless vehicle rental experience for customers while offering administrators powerful tools to manage vehicles, rentals, and user activities.

## Overview:

Drift streamlines the car rental process by allowing users to browse available vehicles, rent cars, manage payments, select pickup locations, and track rental history. Administrators can efficiently manage the vehicle inventory and monitor rental activities through a dedicated dashboard.

## Features:

### Customer Features:

* User registration and secure login
* Browse available vehicles
* Rent cars with a simple booking process
* Add and manage account balance
* Multiple payment options:

  * Wallet Balance
  * Card Payment
  * PayPal
* Update profile information
* Upload profile picture
* Interactive pickup location selection using map and API integration
* View personal rental history
* Export rental history as PDF

### Administrator Features:

* Add new vehicles
* Delete vehicles
* Manage vehicle inventory
* View rental records of all users
* Monitor rental activities and system usage

## Technology Stack:

| Category     | Technologies                                    |
| ------------ | ----------------------------------------------- |
| Frontend     | HTML, CSS, Bootstrap, JavaScript                |
| Backend      | Python, Django                                  |
| Database     | SQLite                                          |
| Architecture | Object-Oriented Programming (OOP)               |
| Features     | CRUD Operations, Authentication & Authorization |
| Integrations | PayPal, Map APIs                                |
| Utilities    | PDF Generation, File Upload Handling            |

## Application Screenshots:

<details>
  <summary><b>Click to View Screenshots</b></summary>

  <br>

### Landing Page

![Landing Page](screenshots/landing.png)

### Location Picker & Map Integration

![Location Selection](screenshots/location_map.png)

### Vehicle Catalog

![Car Listings](screenshots/car_listings.png)

### Admin Dashboard

![Admin Dashboard](screenshots/admin_dashboard.png)

### Checkout & Payment System

![Payment Page](screenshots/payment.png)

### Rental History

![Rental History](screenshots/rental_history.png)

</details>

## Installation & Setup:

### 1. Clone the Repository

```bash
git clone https://github.com/zerwailyas/drift.git
cd drift
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

### 6. Open in Browser

```text
http://127.0.0.1:8000
```

## Project Structure:

```text
Drift/
│
├── static/
├── templates/
├── screenshots/
├── database/
├── models/
├── utils/
├── app/
├── manage.py
├── requirements.txt
└── README.md
```

## Key Highlights:

* Developed using Object-Oriented Programming principles for scalability and maintainability.
* Implemented secure authentication and role-based access control.
* Integrated multiple payment methods including PayPal.
* Added map-based location selection using API integration.
* Generated downloadable PDF rental reports.
* Designed separate functionalities for customers and administrators.
* Built a complete CRUD-based vehicle management system.

## Future Enhancements:

* Email notifications and booking receipts
* Advanced vehicle search and filtering
* Personalized vehicle recommendations
* Reservation scheduling system
* Analytics dashboard for administrators
* Enhanced mobile responsiveness

## Contributors:

* **Zerwa Ilyas**
* **Javeria Iftikhar**

## Author:

**Zerwa Ilyas**

Computer Science Student • Python Developer • Backend & Database Enthusiast
