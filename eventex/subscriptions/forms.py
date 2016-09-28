from django import forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import title


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError("CPF deve conter apenas números", 'digits')

    if len(value) != 11:
        raise ValidationError("CPF deve conter 11 digitos", 'length')


class SubscriptionForm(forms.Form):
    name = forms.CharField(label="Nome")
    cpf = forms.CharField(label="Cpf", validators=[validate_cpf])
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Telefone")

    def clean_name(self):
        return title(self.cleaned_data['name'])