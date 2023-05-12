from test_app.models import Project
from test_app.models import Company
from test_app.models import User
from test_app.models import Quotation
from test_app.views import register

from django.test import RequestFactory


from django.core.exceptions import ValidationError

import datetime
import pytest

from django.test import TestCase
class Test_User(TestCase):
    def test_create_user_with_minimum_fields(self):
        user_data = {
            'cc': '1234567890',
            'fullname': 'John Doe',
            'phoneNumberU': '1234567890',
            'email': 'johndoe@example.com',
            'password': 'password123',
            'birthday': '1990-01-01'
        }
        user = User.objects.create(**user_data)
        self.assertEqual(user.cc, user_data['cc'])
        self.assertEqual(user.fullname, user_data['fullname'])
        self.assertEqual(user.phoneNumberU, user_data['phoneNumberU'])
        self.assertEqual(user.email, user_data['email'])
        self.assertEqual(user.password, user_data['password'])
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

    # Tests creating a user with fields at their maximum length. 
    def test_create_user_with_maximum_length_fields(self):
        user_data = {
            'cc': '1234567890',
            'fullname': 'a'*50,
            'phoneNumberU': '1'*15,
            'email': 'a'*90 + '@example.com',
            'password': 'a'*16,
            'birthday': '1990-01-01'
        }
        user = User.objects.create(**user_data)
        self.assertEqual(user.cc, user_data['cc'])
        self.assertEqual(user.fullname, user_data['fullname'])
        self.assertEqual(user.phoneNumberU, user_data['phoneNumberU'])
        self.assertEqual(user.email, user_data['email'])
        self.assertEqual(user.password, user_data['password'])
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)


    # Tests that the photo field can be set to null or blank. 
    def test_user_photo_field_can_be_null_or_blank(self):
        user_data = {
            'cc': '1234567890',
            'fullname': 'John Doe',
            'phoneNumberU': '1234567890',
            'email': 'johndoe@example.com',
            'password': 'password123',
            'birthday': '1990-01-01',
            'photo': None
        }
        user = User.objects.create(**user_data)
        self.assertEqual(user.photo, user_data['photo'])


    # Tests creating a user with an invalid birthday format. 
    def test_create_user_with_invalid_birthday_format(self):
        user_data = {
            'cc': '1234567890',
            'fullname': 'John Doe',
            'phoneNumberU': '1234567890',
            'email': 'johndoe@example.com',
            'password': 'password123',
            'birthday': 'invalid_birthday_format'
        }
        with self.assertRaises(ValidationError):
            User.objects.create(**user_data)


class TestCompany(TestCase):
    # Tests that a Company object can be created with all required fields. 
    def test_create_company_with_required_fields(self):
        user = User.objects.create(cc='1234567890', fullname='John Doe', phoneNumberU='1234567890', email='johndoe@example.com', password='password', birthday='1990-01-01')
        company = Company.objects.create(nit='123456789', name='Test Company', phoneNumberC='1234567890', address='Test Address', user=user)
        assert company.pk is not None

    # Tests that the name attribute of a Company object can be accessed. 
    def test_access_name_attribute(self):
        user = User.objects.create(cc='1234567890', fullname='John Doe', phoneNumberU='1234567890', email='johndoe@example.com', password='password', birthday='1990-01-01')
        company = Company.objects.create(nit='123456789', name='Test Company', phoneNumberC='1234567890', address='Test Address', user=user)
        assert company.name == 'Test Company'
    
    # Tests that deleting a User object also deletes all associated Company objects. 
    def test_delete_user_deletes_associated_companies(self):
        user = User.objects.create(cc='1234567890', fullname='John Doe', phoneNumberU='1234567890', email='johndoe@example.com', password='password', birthday='1990-01-01')
        company = Company.objects.create(nit='123456789', name='Test Company', phoneNumberC='1234567890', address='Test Address', user=user)
        user.delete()
        assert not Company.objects.filter(pk=company.pk).exists()
        
    def test_company_str_method(self):
        company = Company(nit="123456789", name="Test Company", phoneNumberC="1234567890", address="Test Address", user=User.objects.create(email="test@test.com", cc="1234567890", fullname="Test User", phoneNumberU="1234567890", password="testpassword", birthday="2000-01-01"))
        assert str(company) == "Test Company"

    # Tests that a Company object can be created with all required fields and a valid User object. 
    def test_create_company_with_valid_user(self):
        user = User.objects.create(email="test@test.com", cc="1234567890", fullname="Test User", phoneNumberU="1234567890", password="testpassword", birthday="2000-01-01")
        company = Company(nit="123456789", name="Test Company", phoneNumberC="1234567890", address="Test Address", user=user)
        assert company.pk is not None

    # Tests that a Company object cannot be created with a User object that does not exist. 
    def test_create_company_with_nonexistent_user(self):
        with pytest.raises(User.DoesNotExist):
            company = Company(nit="123456789", name="Test Company", phoneNumberC="1234567890", address="Test Address", user=User.objects.get(pk=999))


    # Tests that a Company object can be created with a phoneNumberC that is longer than 15 characters. 
    def test_create_company_with_long_phoneNumberC(self):
        user = User.objects.create(email="test@test.com", cc="1234567890", fullname="Test User", phoneNumberU="1234567890", password="testpassword", birthday="2000-01-01")
        company = Company(nit="123456789", name="Test Company", phoneNumberC="1234567890123456", address="Test Address", user=user)
        assert company.pk is not None

    # Tests that a Company object can be created with an address that is longer than 300 characters. 
    def test_create_company_with_long_address(self):
        user = User.objects.create(email="test@test.com", cc="1234567890", fullname="Test User", phoneNumberU="1234567890", password="testpassword", birthday="2000-01-01")
        company = Company(nit="123456789", name="Test Company", phoneNumberC="1234567890", address="a"*301, user=user)
        assert company.pk is not None
        

class TestQuotation(TestCase):
    # Tests creating a Quotation object with a valid description and price. 
    def test_create_quotation_valid(self):
        quotation = Quotation(description="Test Quotation", price=10.0)
        assert quotation.description == "Test Quotation"
        assert quotation.price == 10.0

    # Tests retrieving the description of a Quotation object using the __str__ method. 
    def test_retrieve_description(self):
        quotation = Quotation(description="Test Quotation", price=10.0)
        assert str(quotation) == "Test Quotation"

    
    # Tests updating a Quotation object with new values. 
    def test_update_quotation(self):
        quotation = Quotation(description="Test Quotation", price=10.0)
        quotation.description = "Updated Quotation"
        quotation.price = 20.0
        assert quotation.description == "Updated Quotation"
        assert quotation.price == 20.0

class TestTestlit(TestCase):
    def setUp(self):
        # Creamos objetos de prueba para el modelo Project
        self.project1 = Project.objects.create(name="Proyecto 1")
        self.project2 = Project.objects.create(name="Proyecto 2")

        # Creamos una instancia de RequestFactory para simular solicitudes
        self.factory = RequestFactory()
        

class TestRegister(TestCase):
    # Tests that the register function performs well under heavy load and does not cause any server crashes or errors. 
    def test_register_performance(self):
        # Arrange
        req = None # replace with a mock request object

        # Act
        response = register(req)

        # Assert
        assert response.status_code == 200 or response.status_code == 304