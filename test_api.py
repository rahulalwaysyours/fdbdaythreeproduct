#!/usr/bin/env python
"""
Test runner for Adirasite project
Run: python test_api.py
"""

import os
import sys
import django
import json
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adirasite.settings')
sys.path.insert(0, str(Path(__file__).resolve().parent))
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model
from accounts.models import User
from products.models import Product

User = get_user_model()

class APITester:
    def __init__(self):
        self.client = Client()
        self.base_url = 'http://localhost:8000'
        self.access_token = None
        self.refresh_token = None
        self.test_results = []
        
    def log(self, test_name, status, message=""):
        """Log test result"""
        result = f"{'✅' if status else '❌'} {test_name}"
        if message:
            result += f" - {message}"
        print(result)
        self.test_results.append({
            'test': test_name,
            'status': status,
            'message': message
        })
    
    def test_registration(self):
        """Test user registration"""
        print("\n🔐 Testing Registration...\n")
        
        response = self.client.post('/api/auth/register/', {
            'username': 'apitest',
            'email': 'apitest@example.com',
            'password': 'testpass123',
            'password2': 'testpass123',
            'first_name': 'API',
            'last_name': 'Test'
        }, content_type='application/json')
        
        self.log('Registration', response.status_code == 201, f"Status: {response.status_code}")
    
    def test_login(self):
        """Test user login"""
        print("\n🔑 Testing Login...\n")
        
        # Ensure test user exists and email is verified
        user, _ = User.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'testuser@example.com',
                'email_verified': True,
                'first_name': 'Test',
            }
        )
        user.set_password('testpass123')
        user.save()
        
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        }, content_type='application/json')
        
        success = response.status_code == 200
        if success:
            data = json.loads(response.content)
            self.access_token = data.get('access')
            self.refresh_token = data.get('refresh')
        
        self.log('Login', success, f"Status: {response.status_code}")
    
    def test_get_profile(self):
        """Test getting user profile"""
        print("\n👤 Testing Profile...\n")
        
        if not self.access_token:
            self.test_login()
        
        response = self.client.get(
            '/api/auth/profile/',
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )
        
        self.log('Get Profile', response.status_code == 200, f"Status: {response.status_code}")
    
    def test_products(self):
        """Test product endpoints"""
        print("\n📦 Testing Products...\n")
        
        if not self.access_token:
            self.test_login()
        
        # Test list products
        response = self.client.get(
            '/api/products/',
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )
        self.log('List Products', response.status_code == 200, f"Status: {response.status_code}")
        
        # Get first product if exists
        if Product.objects.exists():
            product = Product.objects.first()
            response = self.client.get(
                f'/api/products/{product.id}/',
                HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
            )
            self.log('Get Product', response.status_code == 200, f"Status: {response.status_code}")
    
    def test_token_refresh(self):
        """Test token refresh"""
        print("\n🔄 Testing Token Refresh...\n")
        
        if not self.refresh_token:
            self.test_login()
        
        response = self.client.post(
            '/api/auth/token/refresh/',
            {'refresh': self.refresh_token},
            content_type='application/json'
        )
        
        self.log('Token Refresh', response.status_code == 200, f"Status: {response.status_code}")
    
    def test_without_token(self):
        """Test that endpoints require authentication"""
        print("\n🔒 Testing Authentication Requirement...\n")
        
        response = self.client.get('/api/products/')
        
        self.log('Auth Required', response.status_code == 401, 
                 f"Status: {response.status_code} (should be 401)")
    
    def run_all_tests(self):
        """Run all tests"""
        print("🚀 Starting API Tests...\n")
        
        self.test_without_token()
        self.test_registration()
        self.test_login()
        self.test_get_profile()
        self.test_products()
        self.test_token_refresh()
        
        # Summary
        print("\n" + "="*50)
        print("📊 Test Summary")
        print("="*50)
        
        total = len(self.test_results)
        passed = sum(1 for r in self.test_results if r['status'])
        failed = total - passed
        
        print(f"Total Tests: {total}")
        print(f"Passed: ✅ {passed}")
        print(f"Failed: ❌ {failed}")
        print(f"Success Rate: {(passed/total)*100:.1f}%\n")
        
        if failed == 0:
            print("🎉 All tests passed!\n")
        else:
            print("⚠️ Some tests failed. Check the output above.\n")

if __name__ == '__main__':
    tester = APITester()
    tester.run_all_tests()
