#!/bin/bash
# Adirasite Development Startup Script for macOS/Linux

echo ""
echo "========================================"
echo "    Adirasite - Django REST API"
echo "    Development Startup Script"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment"
        echo "Make sure Python 3 is installed"
        exit 1
    fi
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate virtual environment"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
pip list | grep -i django > /dev/null
if [ $? -ne 0 ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies"
        exit 1
    fi
else
    echo "Dependencies already installed."
fi

# Check if database needs migrations
echo "Checking database..."
if [ ! -f "db.sqlite3" ]; then
    echo "Running migrations..."
    python manage.py migrate
    if [ $? -ne 0 ]; then
        echo "Error: Failed to run migrations"
        exit 1
    fi
    
    echo "Creating test data..."
    python develop.py test-data
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --quiet

echo ""
echo "========================================"
echo "    ✅ Setup Complete!"
echo "========================================"
echo ""
echo "Available commands:"
echo "   - Start server:   python manage.py runserver"
echo "   - Show URLs:      python develop.py urls"
echo "   - Create test data: python develop.py test-data"
echo "   - Reset database: python develop.py reset"
echo "   - Run tests:      python test_api.py"
echo "   - Django shell:   python manage.py shell"
echo ""
echo "Test Users:"
echo "   - testuser / testpass123"
echo "   - admin / admin123"
echo ""
echo "Access points:"
echo "   - Homepage:     http://localhost:8000"
echo "   - Admin panel:  http://localhost:8000/admin"
echo "   - API docs:     See README.md"
echo ""
echo "Starting development server..."
echo "Press Ctrl+C to stop the server"
echo ""

python manage.py runserver
