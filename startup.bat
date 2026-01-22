@echo off
REM Adirasite Development Startup Script for Windows

echo.
echo ========================================
echo    Adirasite - Django REST API
echo    Development Startup Script
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error: Failed to create virtual environment
        echo Make sure Python is installed and added to PATH
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
pip list | findstr /i "django djangorestframework" >nul
if errorlevel 1 (
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
) else (
    echo Dependencies already installed.
)

REM Check if database needs migrations
echo Checking database...
if not exist "db.sqlite3" (
    echo Running migrations...
    python manage.py migrate
    if errorlevel 1 (
        echo Error: Failed to run migrations
        pause
        exit /b 1
    )
    
    echo Creating test data...
    python develop.py test-data
)

REM Collect static files
echo Collecting static files...
python manage.py collectstatic --noinput --quiet

echo.
echo ========================================
echo    ✅ Setup Complete!
echo ========================================
echo.
echo Available commands:
echo   - Start server:   python manage.py runserver
echo   - Show URLs:      python develop.py urls
echo   - Create test data: python develop.py test-data
echo   - Reset database: python develop.py reset
echo   - Run tests:      python test_api.py
echo   - Django shell:   python manage.py shell
echo.
echo Test Users:
echo   - testuser / testpass123
echo   - admin / admin123
echo.
echo Access points:
echo   - Homepage:     http://localhost:8000
echo   - Admin panel:  http://localhost:8000/admin
echo   - API docs:     See README.md
echo.
echo Starting development server...
echo Press Ctrl+C to stop the server
echo.
python manage.py runserver
