# Adirasite - Quick Start Guide

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip (Python package manager)
- Git

### 1. Clone/Navigate to Project

```bash
cd "path/to/adirasite"
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Already configured in `.env` file for development.

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7. Create Test Data (Optional)

```bash
python develop.py test-data
```

This creates:
- Test user: `testuser` / password: `testpass123`
- Admin user: `admin` / password: `admin123`
- Sample products

### 8. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 9. Run Development Server

```bash
python manage.py runserver
```

Server will be available at `http://localhost:8000`

## 📝 Useful Commands

### View All API Endpoints
```bash
python develop.py urls
```

### Reset Database
```bash
python develop.py reset
```

### Run Django Shell
```bash
python manage.py shell
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Make Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🌐 Accessing the Application

### Admin Panel
- URL: `http://localhost:8000/admin/`
- Username: `admin`
- Password: `admin123`

### Home Page
- URL: `http://localhost:8000/`

### API Endpoints

#### Authentication
- **Register**: `POST /api/auth/register/`
- **Login**: `POST /api/auth/login/`
- **Token Refresh**: `POST /api/auth/token/refresh/`
- **Logout**: `POST /api/auth/logout/`
- **Profile**: `GET /api/auth/profile/`
- **Verify Email**: `GET /api/auth/verify-email/?token=TOKEN`

#### Products
- **List Products**: `GET /api/products/`
- **Get Product**: `GET /api/products/{id}/`
- **Create Product** (Admin): `POST /api/products/`
- **Update Product** (Admin): `PATCH /api/products/{id}/`
- **Delete Product** (Admin): `DELETE /api/products/{id}/`

## 🔐 Authentication

### Get JWT Token

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

Response:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Use Token to Access API

```bash
curl -X GET http://localhost:8000/api/products/ \
  -H "Authorization: Bearer ACCESS_TOKEN_HERE"
```

## 📦 Project Structure

```
adirasite/
├── adirasite/              # Django project settings
│   ├── settings.py         # Configuration
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI app
├── accounts/              # User management
│   ├── models.py          # User model
│   ├── views.py           # Auth views
│   ├── serializers.py     # API serializers
│   └── urls.py            # Auth URLs
├── products/              # Product management
│   ├── models.py          # Product model
│   ├── views.py           # Product views
│   ├── serializers.py     # API serializers
│   └── urls.py            # Product URLs
├── templates/             # HTML templates
├── static/                # Static files
├── media/                 # User uploads
├── db.sqlite3            # Database
├── manage.py             # Django CLI
├── requirements.txt      # Dependencies
├── .env                  # Environment variables
├── .env.example          # Environment template
├── README.md             # Full documentation
├── DEPLOYMENT_GUIDE.md   # Deployment instructions
└── develop.py            # Development utilities
```

## 🧪 Testing API with Postman

1. Import `Adirasite_API.postman_collection.json` into Postman
2. Create an environment with:
   - `base_url`: `http://localhost:8000`
   - `access_token`: (will be auto-filled after login)
   - `refresh_token`: (will be auto-filled after login)

## 📄 API Documentation

For complete API documentation, see [README.md](./README.md)

## 🚀 Deployment

For PythonAnywhere deployment, see [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)

### Quick deployment checklist:
1. Generate new SECRET_KEY
2. Create `.env` with production settings
3. Set `DEBUG=False`
4. Configure email settings
5. Run `python manage.py collectstatic --noinput`
6. Set up WSGI configuration on PythonAnywhere
7. Reload web app

## 🆘 Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution**: Ensure virtual environment is activated and all packages are installed:
```bash
pip install -r requirements.txt
```

### Issue: "Static files not found"
**Solution**: Collect static files:
```bash
python manage.py collectstatic --noinput
```

### Issue: "Database is locked"
**Solution**: Delete `db.sqlite3` and run migrations again:
```bash
rm db.sqlite3
python manage.py migrate
```

### Issue: "Port 8000 already in use"
**Solution**: Run on different port:
```bash
python manage.py runserver 8001
```

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com)
- [Django REST Framework](https://www.django-rest-framework.org)
- [JWT Authentication](https://django-rest-framework-simplejwt.readthedocs.io)
- [PythonAnywhere Help](https://help.pythonanywhere.com)

## 🤝 Contributing

Feel free to fork and contribute!

## 📞 Support

For issues or questions:
1. Check the [README.md](./README.md)
2. Review [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)
3. Check Django/DRF documentation

Happy coding! 🎉
