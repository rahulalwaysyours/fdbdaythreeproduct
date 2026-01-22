# 📋 Adirasite Project - Documentation Index

Welcome to the **Adirasite** Django REST API project! This is a complete, production-ready application with JWT authentication.

## 🎯 Start Here

### For First-Time Setup
1. **[QUICKSTART.md](./QUICKSTART.md)** - Get running in 5 minutes
2. **[README.md](./README.md)** - Complete project documentation

### For Running the Project
- **Windows**: Double-click `startup.bat`
- **macOS/Linux**: Run `chmod +x startup.sh && ./startup.sh`
- **Manual**: Follow [QUICKSTART.md](./QUICKSTART.md)

## 📚 Documentation Files

### Essential Reading

| File | Purpose | Read When |
|------|---------|-----------|
| [QUICKSTART.md](./QUICKSTART.md) | Quick setup & common commands | Starting development |
| [README.md](./README.md) | Full API documentation & examples | Learning the API |
| [PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md) | What's been implemented | Understanding features |

### For Deployment

| File | Purpose | Read When |
|------|---------|-----------|
| [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) | PythonAnywhere deployment steps | Ready to deploy |
| [PRODUCTION_CHECKLIST.md](./PRODUCTION_CHECKLIST.md) | Pre-deployment checklist | Before going live |
| wsgi_pythonanywhere.py | WSGI configuration template | Configuring PythonAnywhere |

### Configuration

| File | Purpose | Read When |
|------|---------|-----------|
| .env.example | Environment variables template | First setup |
| .env | Your local configuration | Running locally |
| requirements.txt | All Python dependencies | Installing packages |

## 🚀 Quick Commands

```bash
# First time setup
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python develop.py test-data

# Daily usage
python manage.py runserver              # Start server
python develop.py urls                  # See API endpoints
python develop.py test-data            # Create test data
python test_api.py                     # Test all endpoints

# Database
python develop.py reset                 # Reset database
python manage.py shell                  # Django shell
python manage.py createsuperuser        # Create admin

# Deployment
python manage.py collectstatic --noinput # Collect static files
```

## 📖 API Testing

### Option 1: Postman (Recommended)
1. Import `Adirasite_API.postman_collection.json`
2. Set `base_url` variable to `http://localhost:8000`
3. Use provided requests to test API

### Option 2: Command Line
```bash
# Get token
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'

# Use token
curl -X GET http://localhost:8000/api/products/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Option 3: Automated Tests
```bash
python test_api.py
```

## 🔐 Default Test Credentials

| User | Username | Password |
|------|----------|----------|
| Regular User | testuser | testpass123 |
| Admin User | admin | admin123 |

## 🌐 Access Points

| Page | URL | Notes |
|------|-----|-------|
| Home | http://localhost:8000 | Landing page |
| Admin Panel | http://localhost:8000/admin | Login with admin credentials |
| API Docs | See README.md | Endpoint documentation |
| Postman | Import .json file | Complete API collection |

## 📁 Project Structure

```
adirasite/
├── 📄 Core Files
│   ├── manage.py              # Django CLI
│   ├── requirements.txt        # Dependencies
│   ├── .env                   # Configuration (local)
│   ├── .env.example           # Configuration template
│   ├── .gitignore             # Git ignore patterns
│   └── db.sqlite3             # Database
│
├── ⚙️ Django Project
│   └── adirasite/
│       ├── settings.py        # JWT, CORS, Email config
│       ├── urls.py            # URL routing
│       ├── wsgi.py            # WSGI for production
│       └── asgi.py            # ASGI configuration
│
├── 👤 Accounts App
│   └── accounts/
│       ├── models.py          # User model
│       ├── views.py           # Auth endpoints
│       ├── serializers.py     # API serializers
│       ├── urls.py            # Auth URLs
│       └── utils.py           # Email utilities
│
├── 📦 Products App
│   └── products/
│       ├── models.py          # Product model
│       ├── views.py           # Product endpoints
│       ├── serializers.py     # API serializers
│       └── urls.py            # Product URLs
│
├── 🔧 Tools & Scripts
│   ├── develop.py             # Development utilities
│   ├── test_api.py            # API testing script
│   ├── startup.bat            # Windows startup
│   ├── startup.sh             # Linux/macOS startup
│   └── wsgi_pythonanywhere.py # PythonAnywhere config
│
├── 🧪 API Testing
│   ├── Adirasite_API.postman_collection.json
│   └── test_api.py
│
└── 📚 Documentation
    ├── README.md              # Complete documentation
    ├── QUICKSTART.md          # Quick setup guide
    ├── PROJECT_SUMMARY.md     # What's implemented
    ├── DEPLOYMENT_GUIDE.md    # PythonAnywhere guide
    ├── PRODUCTION_CHECKLIST.md # Pre-deployment
    ├── .env.example           # Config template
    └── INDEX.md               # This file
```

## ✨ Features Implemented

### ✅ Authentication & Security
- JWT token-based authentication
- Email verification before login
- Secure password hashing
- Token refresh mechanism
- Logout with token blacklisting
- CORS protection
- CSRF protection

### ✅ API Endpoints
- User registration
- User login
- Token refresh
- User profile management
- Email verification
- Product listing with pagination
- Product search & filtering
- Product CRUD (admin only)

### ✅ Production Ready
- Environment variables management
- Static files configuration
- Media files support
- Database migrations
- Error handling
- Debug mode switching
- HTTPS ready
- Gunicorn WSGI server

### ✅ Development Tools
- Management commands utility
- API testing script
- Postman collection
- Test data generator
- Database reset utility
- URL listing utility

### ✅ Documentation
- Complete API documentation
- Quick start guide
- Deployment instructions
- Production checklist
- Project summary
- Configuration examples

## 🎯 Development Workflow

### Day 1: Understanding
1. Read [QUICKSTART.md](./QUICKSTART.md)
2. Run `startup.bat` (or startup.sh)
3. Test API with Postman
4. Read [README.md](./README.md)

### Day 2: Customization
1. Modify models in accounts/models.py or products/models.py
2. Create migrations: `python manage.py makemigrations`
3. Run migrations: `python manage.py migrate`
4. Update views and serializers as needed
5. Test with `python test_api.py`

### Day 3: Deployment
1. Review [PRODUCTION_CHECKLIST.md](./PRODUCTION_CHECKLIST.md)
2. Follow [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)
3. Deploy to PythonAnywhere
4. Test all endpoints on live server

## ❓ Troubleshooting

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "Static files not found"
```bash
python manage.py collectstatic --noinput
```

### "Database is locked"
```bash
rm db.sqlite3
python manage.py migrate
python develop.py test-data
```

### "Port 8000 already in use"
```bash
python manage.py runserver 8001
```

### "Email not sending"
- Check credentials in .env
- Use Gmail App Password (not regular password)
- Check EMAIL_BACKEND setting

## 📚 Learning Resources

### Official Documentation
- [Django Documentation](https://docs.djangoproject.com)
- [Django REST Framework](https://www.django-rest-framework.org)
- [SimpleJWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io)

### PythonAnywhere
- [PythonAnywhere Help](https://help.pythonanywhere.com)
- [PythonAnywhere Django Guide](https://help.pythonanywhere.com/pages/Django/)

### API Best Practices
- [RESTful API Design](https://restfulapi.net)
- [JWT Best Practices](https://tools.ietf.org/html/rfc8725)
- [CORS Specification](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

## 🔐 Security Reminders

✅ **Always:**
- Keep SECRET_KEY secret
- Use environment variables for sensitive data
- Never commit .env to version control
- Use HTTPS in production
- Validate all user input
- Keep dependencies updated

❌ **Never:**
- Hardcode credentials
- Use DEBUG=True in production
- Expose error details to users
- Use weak passwords
- Deploy without HTTPS

## 📞 Support & Help

### Quick Help
1. Check [QUICKSTART.md](./QUICKSTART.md) for common commands
2. See [README.md](./README.md) for API examples
3. Review [PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md) for features

### Getting Help
1. Check the error message carefully
2. Search Django/DRF documentation
3. Review troubleshooting section above
4. Check stack traces in terminal

### Before Deploying
1. Read [PRODUCTION_CHECKLIST.md](./PRODUCTION_CHECKLIST.md)
2. Follow [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) step-by-step
3. Test all endpoints thoroughly
4. Backup your database

## 🎉 You're All Set!

This project is **complete and production-ready**. You have:

✅ Full JWT authentication system
✅ Complete REST API
✅ Production configuration
✅ Comprehensive documentation
✅ Development tools
✅ Deployment guide
✅ Testing utilities

### Next Steps:
1. Try the project locally (startup.bat or startup.sh)
2. Test API endpoints with Postman
3. Customize for your needs
4. Deploy to PythonAnywhere

**Happy coding! 🚀**

---

**Last Updated**: January 22, 2026
**Version**: 1.0 - Complete & Production Ready
