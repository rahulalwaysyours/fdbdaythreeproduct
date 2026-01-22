# PythonAnywhere Deployment Guide for Adirasite

## Prerequisites
- PythonAnywhere account (create at https://www.pythonanywhere.com)
- Git installed on your local machine
- GitHub or similar repository with your code

## Step-by-Step Deployment

### 1. Generate a Strong Secret Key
Before deploying, generate a new SECRET_KEY for production:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 2. On PythonAnywhere - Initial Setup

1. Log in to PythonAnywhere
2. Go to **Files** tab and navigate to home directory
3. Open **Bash console**

### 3. Clone Your Repository

```bash
cd ~
git clone https://github.com/YOUR_USERNAME/adirasite.git
cd adirasite
```

### 4. Create Python Virtual Environment

```bash
# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.10 adirasite

# Activate it (should auto-activate in bash console)
workon adirasite
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create `.env` file in your project root:

```bash
cat > ~/.env << 'EOF'
DEBUG=False
SECRET_KEY=your-generated-secret-key-here
ALLOWED_HOSTS=yourusername.pythonanywhere.com
BACKEND_URL=https://yourusername.pythonanywhere.com

CORS_ALLOWED_ORIGINS=https://yourusername.pythonanywhere.com
CSRF_TRUSTED_ORIGINS=https://yourusername.pythonanywhere.com

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
DEFAULT_FROM_EMAIL=your-email@gmail.com

SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
EOF
```

**Important**: Replace placeholder values with your actual configuration!

### 7. Setup Database

```bash
cd ~/adirasite
python manage.py migrate
```

### 8. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 9. Create Superuser (Admin)

```bash
python manage.py createsuperuser
# Follow the prompts to create admin user
```

### 10. Setup Web App in PythonAnywhere

1. Go to **Web** tab
2. Click **Add a new web app**
3. Select **Manual configuration** → **Python 3.10**
4. Once created, click on the web app configuration
5. Under **Virtualenv**, set to: `/home/yourusername/.virtualenvs/adirasite`
6. Under **Code** section:
   - Source code: `/home/yourusername/adirasite`
   - Working directory: `/home/yourusername/adirasite`

### 11. Configure WSGI File

Go back to Web app configuration, find **WSGI configuration file** and click it. Replace the entire content with:

```python
import os
import sys
from pathlib import Path

path = '/home/yourusername/adirasite'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'adirasite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 12. Configure Static Files

Still in Web app configuration, scroll to **Static files** section and add:

- URL: `/static/`
- Directory: `/home/yourusername/adirasite/staticfiles`

And:

- URL: `/media/`
- Directory: `/home/yourusername/adirasite/media`

### 13. Reload Web App

Go to **Web** tab and click **Reload** button.

### 14. Test Your Application

Visit `https://yourusername.pythonanywhere.com` in browser

### 15. Verify API Endpoints

Test these endpoints:
- `https://yourusername.pythonanywhere.com/api/auth/register/` - User registration
- `https://yourusername.pythonanywhere.com/api/auth/login/` - User login (get JWT tokens)
- `https://yourusername.pythonanywhere.com/api/products/` - Product list (requires authentication)
- `https://yourusername.pythonanywhere.com/admin/` - Django admin panel

## Common Issues and Solutions

### Issue: "ModuleNotFoundError" or Import Errors
**Solution**: Ensure virtual environment is set correctly in Web app configuration.

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic --noinput` and reload web app.

### Issue: Database errors
**Solution**: Run `python manage.py migrate` in bash console.

### Issue: Email not sending
**Solution**: 
1. Enable "Less secure app access" if using Gmail
2. Or use an "App Password" if 2FA is enabled
3. Test with `EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend` first

### Issue: "CSRF verification failed"
**Solution**: Ensure `CSRF_TRUSTED_ORIGINS` includes your domain in `.env`.

## Updating Code After Deployment

1. Make changes locally and commit to GitHub:
```bash
git add .
git commit -m "Your message"
git push origin master
```

2. On PythonAnywhere bash console:
```bash
cd ~/adirasite
git pull origin master
python manage.py migrate  # if database changes
python manage.py collectstatic --noinput
```

3. Reload web app from **Web** tab

## Running Scheduled Tasks (Optional)

To run periodic tasks (like cleanup), use PythonAnywhere's **Scheduled tasks** tab.

## Monitoring and Logs

Check error logs in PythonAnywhere:
- Go to **Web** tab
- Scroll to **Log files**
- Check **Error log** for issues

## Important Security Reminders

✓ Keep SECRET_KEY secret and unique
✓ Use strong database password
✓ Use app-specific email password (not main password)
✓ Enable HTTPS (PythonAnywhere handles this automatically)
✓ Regularly update dependencies: `pip install --upgrade -r requirements.txt`
✓ Monitor and clean up old logs

## API Authentication

All API endpoints except `/api/auth/register/` and `/api/auth/login/` require JWT token.

### Getting JWT Token

```bash
curl -X POST https://yourusername.pythonanywhere.com/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"your_username","password":"your_password"}'
```

Response includes `access` and `refresh` tokens.

### Using JWT Token

Include in request header:
```
Authorization: Bearer your_access_token_here
```

### Refreshing Token

```bash
curl -X POST https://yourusername.pythonanywhere.com/api/auth/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh":"your_refresh_token"}'
```

## Deployment Checklist

- [ ] Generated new SECRET_KEY
- [ ] Created `.env` with production values
- [ ] Set DEBUG=False
- [ ] Configured ALLOWED_HOSTS correctly
- [ ] Set up CORS_ALLOWED_ORIGINS
- [ ] Configured email settings
- [ ] Ran migrations
- [ ] Collected static files
- [ ] Created superuser
- [ ] Configured WSGI file
- [ ] Set static files paths
- [ ] Tested all API endpoints
- [ ] Checked error logs
- [ ] Tested email verification
- [ ] Tested JWT authentication

## Support

For more help, visit:
- PythonAnywhere Help: https://help.pythonanywhere.com
- Django Documentation: https://docs.djangoproject.com
- Django REST Framework: https://www.django-rest-framework.org
