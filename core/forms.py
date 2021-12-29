from django import forms
from django.forms import fields, ModelForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from core.models import BillingAddress,Item

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

''' The Buyers Profile Section Form '''
class BuyersDetailsForm(ModelForm):
#    class Meta:
#         model = BillingAddress
#         fields = '__all__'
    class Meta:
        model = BillingAddress
        fields = ['first_name','last_name','street_address','towm_city','zip','mobile_number']
   
    #first_name = forms.CharField(max_length=100)

class AddtoCartForm(forms.Form):
    class Meta:
        slug = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Promo code'
        }))  

    qty = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder': 'qty',
        'class': 'form-control'
    }))


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St',
        'class': 'form-control'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment, studio, or floor',
        'class': 'form-control'
    }))
    # country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={
    #     'class': 'custom-select d-block w-100'

    # }))
    country = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'South Africa',
        'class': 'form-control ',
        'readonly':'readonly',

    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    # payment_option = forms.ChoiceField(
    #     widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()
