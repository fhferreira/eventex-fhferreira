from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class FormSubscriptionTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = self.make_validated_form()
        expected = ('name', 'cpf', 'email', 'phone')
        self.assertSequenceEqual(expected, tuple(form.fields))

    def test_cpf_is_digits(self):
        """CPF must only accept digits."""
        form = self.make_validated_form(cpf='ABC45678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must only accept digits."""
        form = self.make_validated_form(cpf='45678901')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def make_validated_form(self, **kwargs):
        valid = dict(
            name='Flavio Henrique Ferreira',
            cpf='12345678901',
            email='flaviometalvale@gmail.com',
            phone='16992084635'
        )
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
