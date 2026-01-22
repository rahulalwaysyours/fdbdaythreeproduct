# Production Deployment Checklist

## Before Deployment

### Security
- [ ] Generate a new SECRET_KEY using: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
- [ ] Set `DEBUG = False` in settings
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Set strong password for database (if not using SQLite)
- [ ] Review and secure email credentials
- [ ] Enable SSL/HTTPS (PythonAnywhere provides this)
- [ ] Set `SECURE_SSL_REDIRECT = True`
- [ ] Set `SESSION_COOKIE_SECURE = True`
- [ ] Set `CSRF_COOKIE_SECURE = True`

### Environment Configuration
- [ ] Create `.env` file with production settings
- [ ] Copy from `.env.example` and update values
- [ ] Set `BACKEND_URL` to your production domain
- [ ] Configure `CORS_ALLOWED_ORIGINS` with your frontend domain
- [ ] Configure `CSRF_TRUSTED_ORIGINS` with your frontend domain
- [ ] Set up email credentials (Gmail App Password recommended)

### Database
- [ ] Run `python manage.py migrate`
- [ ] Verify all migrations applied
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] Test database connection
- [ ] Back up database before deployment

### Static & Media Files
- [ ] Run `python manage.py collectstatic --noinput`
- [ ] Verify static files collected to `staticfiles/` directory
- [ ] Configure static file serving on web server
- [ ] Configure media file directory
- [ ] Set appropriate permissions on directories

### Code Quality
- [ ] Run tests: `python manage.py test`
- [ ] Check for errors: `python manage.py check`
- [ ] Review and commit all code changes
- [ ] Tag release version in git
- [ ] Push to remote repository

### Dependencies
- [ ] Update `requirements.txt`: `pip freeze > requirements.txt`
- [ ] Verify all dependencies in production match local
- [ ] Remove development-only packages if any
- [ ] Document any new dependencies

## PythonAnywhere Deployment

### Account Setup
- [ ] Create PythonAnywhere account
- [ ] Have SSH key generated (optional but recommended)
- [ ] Have repository access credentials ready

### Server Setup
- [ ] Clone repository in PythonAnywhere
- [ ] Create virtual environment
- [ ] Install dependencies from `requirements.txt`
- [ ] Create `.env` file with production values
- [ ] Run migrations
- [ ] Collect static files
- [ ] Create superuser

### Web App Configuration
- [ ] Set Python version (3.10+)
- [ ] Set virtual environment path
- [ ] Configure WSGI file
- [ ] Add static files mapping:
  - URL: `/static/` → Directory: `/home/username/adirasite/staticfiles`
- [ ] Add media files mapping:
  - URL: `/media/` → Directory: `/home/username/adirasite/media`
- [ ] Verify domain is added
- [ ] Enable HTTPS (PythonAnywhere handles automatically)

### Testing After Deployment
- [ ] [ ] Access homepage
- [ ] [ ] Test user registration
- [ ] [ ] Verify email sending (check email logs)
- [ ] [ ] Test email verification link
- [ ] [ ] Test user login
- [ ] [ ] Verify JWT tokens work
- [ ] [ ] Test product list endpoint
- [ ] [ ] Test product creation (admin only)
- [ ] [ ] Test product update (admin only)
- [ ] [ ] Test product delete (admin only)
- [ ] [ ] Check admin panel at `/admin/`
- [ ] [ ] Verify static files load (CSS, JS)
- [ ] [ ] Test API from frontend

### Performance
- [ ] Check error logs for warnings
- [ ] Monitor database queries
- [ ] Test pagination works correctly
- [ ] Verify search/filter functionality
- [ ] Test with multiple concurrent users (load testing)

### Monitoring
- [ ] Set up error logging
- [ ] Monitor error logs regularly
- [ ] Set up uptime monitoring
- [ ] Set up performance monitoring
- [ ] Create backup schedule
- [ ] Test backup and restore process

## Post-Deployment

### Documentation
- [ ] Update README with production domain
- [ ] Document any configuration changes
- [ ] Document deployment process for future reference
- [ ] Update API documentation with production URL

### Maintenance
- [ ] Establish regular backup schedule
- [ ] Plan security updates schedule
- [ ] Set up dependency update monitoring
- [ ] Create incident response plan
- [ ] Document rollback procedure

### Security
- [ ] Regularly update dependencies
- [ ] Monitor security advisories
- [ ] Review access logs regularly
- [ ] Rotate credentials periodically
- [ ] Monitor for suspicious activity

### Performance
- [ ] Monitor response times
- [ ] Monitor database performance
- [ ] Monitor disk usage
- [ ] Monitor CPU usage
- [ ] Optimize slow queries

## Rollback Plan

If something goes wrong:

1. **Immediate Actions**
   - Check error logs: `tail -f /var/log/adirasite/error.log`
   - Stop web app from PythonAnywhere dashboard
   - Verify database backup exists

2. **Code Rollback**
   - SSH into PythonAnywhere
   - `cd ~/adirasite`
   - `git log --oneline` (view commits)
   - `git checkout <previous-commit-hash>`
   - `python manage.py collectstatic --noinput`
   - Reload web app

3. **Database Rollback**
   - Contact PythonAnywhere support for database backup restoration
   - Or use your local database backup

4. **Communication**
   - Notify users of the issue
   - Provide status updates
   - Confirm when service is restored

## Useful PythonAnywhere Commands

### SSH Into PythonAnywhere
```bash
ssh yourusername@ssh.pythonanywhere.com
```

### View Web App Logs
```bash
# Error log
tail -f /var/log/yourusername.pythonanywhere.com.error.log

# Access log
tail -f /var/log/yourusername.pythonanywhere.com.access.log
```

### Reload Web App
```bash
touch /var/www/yourusername_pythonanywhere_com_wsgi.py
```

### Run Management Commands
```bash
cd ~/adirasite
workon adirasite  # Activate virtual environment
python manage.py <command>
```

## Monitoring Services

### Recommended Monitoring Tools
- [Sentry](https://sentry.io) - Error tracking
- [New Relic](https://newrelic.com) - Performance monitoring
- [DataDog](https://www.datadoghq.com) - Infrastructure monitoring
- [UptimeRobot](https://uptimerobot.com) - Uptime monitoring

## Scaling Considerations

As traffic grows:
- [ ] Consider upgrading PythonAnywhere plan
- [ ] Implement caching (Redis)
- [ ] Use CDN for static files
- [ ] Optimize database queries
- [ ] Consider moving to dedicated server
- [ ] Implement load balancing

## Security Hardening

- [ ] Implement rate limiting on API
- [ ] Add CAPTCHA to registration
- [ ] Implement 2FA for admin
- [ ] Audit user permissions regularly
- [ ] Review and update CORS settings regularly
- [ ] Implement security headers
- [ ] Use API versioning for stability

## Compliance & Legal

- [ ] Set up privacy policy
- [ ] Set up terms of service
- [ ] Implement GDPR compliance (if EU users)
- [ ] Implement data retention policies
- [ ] Document data handling procedures
- [ ] Set up data deletion mechanism

---

**Last Updated**: January 22, 2026
**Deployment Checklist Version**: 1.0
