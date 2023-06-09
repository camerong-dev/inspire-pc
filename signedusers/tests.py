from django.test import TestCase
from django.contrib.auth.models import User
from .forms import RegisterForm


class RegisterFormTests(TestCase):
    def test_register_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_form_invalid(self):
        form_data = {
            'username': 'testuser',
            'email': 'invalid_email',
            'password1': 'testpassword',
            'password2': 'different_password',
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_form_save(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))


class RegisterFormViewTests(TestCase):
    def test_register_view_get(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_register_view_post_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post('/register/', data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/signedusers/login/')
        # Redirects to login page if user registered

        # Verify user is created
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_view_post_invalid(self):
        form_data = {
            'username': 'testuser',
            'email': 'invalid_email',
            'password1': 'testpassword',
            'password2': 'different_password',
        }
        response = self.client.post('/register/', data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        # Stays on register.html if form contains invalid data

        # Verify user is not created
        self.assertFalse(User.objects.filter(username='testuser').exists())
