# DRIFT

# Project Setup Instructions

## Environment Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate    # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Development Server

```bash
python manage.py runserver
```

- Access the application at: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin/
- User management: http://127.0.0.1:8000/users/


## Important Notes

- Always activate your virtual environment before working on the project
- Use `deactivate` to exit the virtual environment
- For Django admin access, create a superuser first:
  ```bash
  python manage.py createsuperuser
  ```
```
