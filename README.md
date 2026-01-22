# Adirasite - Django REST API with JWT Authentication

A complete Django REST Framework application with JWT authentication, email verification, and product management API.

## Features

✨ **JWT Authentication**
- Secure token-based authentication
- Access and refresh token system
- Email verification before login
- Logout with token blacklisting

📦 **Product Management**
- List all products with pagination
- Search and filter functionality
- Create/Update/Delete products (Admin only)
- Product details with pricing and stock info

👤 **User Management**
- User registration with email verification
- User profile management
- Admin panel for user management
- Custom user model with email-based authentication

🔒 **Security Features**
- CORS enabled for cross-origin requests
- CSRF protection
- Password hashing
- Environment-based configuration
- Production-ready settings

🚀 **Production Ready**
- Ready for PythonAnywhere deployment
- Static files configuration
- Media files support
- Comprehensive error handling

## Technology Stack

- **Django 6.0+** - Web framework
- **Django REST Framework** - REST API
- **SimpleJWT** - JWT authentication
- **django-cors-headers** - CORS handling
- **python-dotenv** - Environment variables
- **SQLite** - Database (can use PostgreSQL in production)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/adirasite.git
cd adirasite
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to `.env` and update values:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```dotenv
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
BACKEND_URL=http://localhost:8000
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 8. Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## API Endpoints

### Authentication Endpoints

#### Register User
```
POST /api/auth/register/
Content-Type: application/json

{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "password2": "securepassword123",
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1990-01-15",
    "phone_number": "+1234567890"
}

Response (201):
{
    "user": {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "date_joined": "2024-01-22T10:00:00Z",
        "email_verified": false
    },
    "message": "User registered successfully. Please check your email to verify your account.",
    "email_sent": true
}
```

#### Verify Email
```
GET /api/auth/verify-email/?token=VERIFICATION_TOKEN

Response (200):
{
    "message": "Email verified successfully. You can now login."
}
```

#### Login
```
POST /api/auth/login/
Content-Type: application/json

{
    "username": "john_doe",
    "password": "securepassword123"
}

Response (200):
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "username": "john_doe",
    "email": "john@example.com",
    "email_verified": true
}
```

#### Refresh Token
```
POST /api/auth/token/refresh/
Content-Type: application/json

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}

Response (200):
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### Logout
```
POST /api/auth/logout/
Authorization: Bearer ACCESS_TOKEN
Content-Type: application/json

{
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}

Response (200):
{
    "message": "Successfully logged out."
}
```

#### Get User Profile
```
GET /api/auth/profile/
Authorization: Bearer ACCESS_TOKEN

Response (200):
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "date_joined": "2024-01-22T10:00:00Z",
    "email_verified": true
}
```

#### Update User Profile
```
PATCH /api/auth/profile/
Authorization: Bearer ACCESS_TOKEN
Content-Type: application/json

{
    "first_name": "Jonathan",
    "last_name": "Doe"
}

Response (200):
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "Jonathan",
    "last_name": "Doe",
    "date_joined": "2024-01-22T10:00:00Z",
    "email_verified": true
}
```

### Product Endpoints

#### List All Products
```
GET /api/products/?page=1&search=laptop&ordering=-price
Authorization: Bearer ACCESS_TOKEN

Response (200):
{
    "count": 25,
    "next": "http://localhost:8000/api/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Laptop",
            "description": "High-performance laptop",
            "price": "999.99",
            "stock": 10,
            "is_active": true,
            "on_sale": false,
            "created_at": "2024-01-20T10:00:00Z",
            "updated_at": "2024-01-22T10:00:00Z"
        }
    ]
}
```

#### Get Product Details
```
GET /api/products/1/
Authorization: Bearer ACCESS_TOKEN

Response (200):
{
    "id": 1,
    "name": "Laptop",
    "description": "High-performance laptop",
    "price": "999.99",
    "stock": 10,
    "is_active": true,
    "on_sale": false,
    "created_at": "2024-01-20T10:00:00Z",
    "updated_at": "2024-01-22T10:00:00Z"
}
```

#### Create Product (Admin Only)
```
POST /api/products/
Authorization: Bearer ADMIN_ACCESS_TOKEN
Content-Type: application/json

{
    "name": "Desktop",
    "description": "High-end desktop computer",
    "price": "1299.99",
    "stock": 5,
    "is_active": true,
    "on_sale": true
}

Response (201):
{
    "id": 2,
    "name": "Desktop",
    "description": "High-end desktop computer",
    "price": "1299.99",
    "stock": 5,
    "is_active": true,
    "on_sale": true,
    "created_at": "2024-01-22T10:00:00Z",
    "updated_at": "2024-01-22T10:00:00Z"
}
```

#### Update Product (Admin Only)
```
PATCH /api/products/1/
Authorization: Bearer ADMIN_ACCESS_TOKEN
Content-Type: application/json

{
    "price": "899.99",
    "stock": 15,
    "on_sale": true
}

Response (200):
{
    "id": 1,
    "name": "Laptop",
    "description": "High-performance laptop",
    "price": "899.99",
    "stock": 15,
    "is_active": true,
    "on_sale": true,
    "created_at": "2024-01-20T10:00:00Z",
    "updated_at": "2024-01-22T10:00:00Z"
}
```

#### Delete Product (Admin Only)
```
DELETE /api/products/1/
Authorization: Bearer ADMIN_ACCESS_TOKEN

Response (204): No Content
```

## Frontend Integration Example

### React Example

```javascript
const API_URL = 'http://localhost:8000/api';

// Register
async function register(userData) {
  const response = await fetch(`${API_URL}/auth/register/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(userData)
  });
  return response.json();
}

// Login
async function login(username, password) {
  const response = await fetch(`${API_URL}/auth/login/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  const data = await response.json();
  localStorage.setItem('access_token', data.access);
  localStorage.setItem('refresh_token', data.refresh);
  return data;
}

// Get Products
async function getProducts(page = 1) {
  const token = localStorage.getItem('access_token');
  const response = await fetch(`${API_URL}/products/?page=${page}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
}

// Refresh Token
async function refreshToken() {
  const refresh = localStorage.getItem('refresh_token');
  const response = await fetch(`${API_URL}/auth/token/refresh/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ refresh })
  });
  const data = await response.json();
  localStorage.setItem('access_token', data.access);
  return data;
}
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```dotenv
# Django
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
CSRF_TRUSTED_ORIGINS=http://localhost:3000,http://localhost:8000

# Email
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@example.com

# Backend
BACKEND_URL=http://localhost:8000

# Security
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
```

## Deployment

For detailed deployment instructions to PythonAnywhere, see [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md).

Quick summary:
1. Create virtual environment
2. Install dependencies
3. Configure `.env` for production
4. Run migrations
5. Collect static files
6. Configure WSGI
7. Set up static file serving
8. Reload web app

## Admin Panel

Access Django admin at `/admin/` using superuser credentials.

## File Structure

```
adirasite/
├── adirasite/          # Project settings
│   ├── settings.py     # Django configuration
│   ├── urls.py         # URL routing
│   ├── wsgi.py         # WSGI application
│   └── asgi.py         # ASGI application
├── accounts/           # User management app
│   ├── models.py       # User model
│   ├── views.py        # Authentication views
│   ├── serializers.py  # Authentication serializers
│   ├── urls.py         # Authentication URLs
│   └── utils.py        # Email utilities
├── products/           # Product management app
│   ├── models.py       # Product model
│   ├── views.py        # Product views
│   ├── serializers.py  # Product serializers
│   └── urls.py         # Product URLs
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
├── media/              # User uploaded files
├── requirements.txt    # Python dependencies
├── manage.py           # Django CLI
├── .env                # Environment variables (local)
├── .env.example        # Environment variables template
└── DEPLOYMENT_GUIDE.md # Deployment instructions
```

## Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test accounts
python manage.py test products

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## Troubleshooting

### Issue: "Token is invalid or expired"
**Solution**: Use the refresh token endpoint to get a new access token.

### Issue: "CORS error" when accessing from frontend
**Solution**: Add your frontend URL to `CORS_ALLOWED_ORIGINS` in `.env`.

### Issue: Email not sending
**Solution**: 
- For Gmail, use an App Password (not your account password)
- Enable "Less secure app access" if using regular password
- Check `EMAIL_BACKEND` is set correctly

### Issue: Database locked
**Solution**: Remove old `.db` file and run migrations again.

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For questions or issues:
- Check the [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)
- Review Django REST Framework documentation
- Check Django documentation

## Contact

Email: support@adirasite.com
