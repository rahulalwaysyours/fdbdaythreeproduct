#!/usr/bin/env python
"""
Development utilities script for Adirasite project
"""

import os
import sys
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adirasite.settings')
sys.path.insert(0, str(Path(__file__).resolve().parent))
django.setup()

from django.core.management import call_command
from accounts.models import User
from products.models import Product

def create_test_data():
    """Create test data for development"""
    print("\n📝 Creating test data...")
    
    # Create test user if not exists
    if not User.objects.filter(username='testuser').exists():
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            email_verified=True
        )
        print(f"✅ Created test user: {user.username}")
    
    # Create test admin if not exists
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        print(f"✅ Created admin user: {admin.username}")
    
    # Create sample products
    sample_products = [
        {
            'name': 'Laptop Pro',
            'description': 'High-performance laptop with 16GB RAM',
            'price': 1299.99,
            'stock': 10,
            'is_active': True,
            'on_sale': False
        },
        {
            'name': 'Wireless Mouse',
            'description': 'Ergonomic wireless mouse',
            'price': 29.99,
            'stock': 50,
            'is_active': True,
            'on_sale': True
        },
        {
            'name': 'USB-C Cable',
            'description': '2m USB-C charging cable',
            'price': 14.99,
            'stock': 100,
            'is_active': True,
            'on_sale': False
        },
        {
            'name': 'Monitor 27"',
            'description': '4K Ultra HD monitor',
            'price': 399.99,
            'stock': 5,
            'is_active': True,
            'on_sale': True
        },
    ]
    
    for product_data in sample_products:
        if not Product.objects.filter(name=product_data['name']).exists():
            Product.objects.create(**product_data)
            print(f"✅ Created product: {product_data['name']}")
    
    print("✅ Test data created successfully!\n")

def reset_database():
    """Reset database to clean state"""
    print("\n🔄 Resetting database...")
    call_command('flush', '--noinput')
    call_command('migrate')
    create_test_data()
    print("✅ Database reset successfully!\n")

def show_urls():
    """Show available API URLs"""
    print("\n📋 Available API Endpoints:\n")
    print("Authentication:")
    print("  POST   /api/auth/register/          - Register new user")
    print("  POST   /api/auth/login/             - Login and get JWT tokens")
    print("  POST   /api/auth/token/refresh/     - Refresh access token")
    print("  POST   /api/auth/logout/            - Logout user")
    print("  GET    /api/auth/profile/           - Get user profile")
    print("  PATCH  /api/auth/profile/           - Update user profile")
    print("  GET    /api/auth/verify-email/      - Verify email address")
    print("\nProducts:")
    print("  GET    /api/products/               - List all products")
    print("  POST   /api/products/               - Create product (admin only)")
    print("  GET    /api/products/{id}/          - Get product details")
    print("  PATCH  /api/products/{id}/          - Update product (admin only)")
    print("  DELETE /api/products/{id}/          - Delete product (admin only)")
    print("\nAdmin:")
    print("  GET    /admin/                      - Django admin panel")
    print()

def main():
    """Main menu"""
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'test-data':
            create_test_data()
        elif command == 'reset':
            reset_database()
        elif command == 'urls':
            show_urls()
        elif command == 'help':
            print("\nUsage: python develop.py [command]\n")
            print("Commands:")
            print("  test-data    - Create sample test data")
            print("  reset        - Reset database to clean state")
            print("  urls         - Show available API endpoints")
            print("  help         - Show this help message\n")
        else:
            print(f"Unknown command: {command}")
            print("Run 'python develop.py help' for available commands")
    else:
        show_urls()

if __name__ == '__main__':
    main()
