from django import forms 
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    address1=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}),required=False)

    shipping_full_name=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}),required=False)
    shipping_email=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),required=False)
    shipping_address1=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}),required=True)
    shipping_address2=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address2'}),required=False)
    shipping_city=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),required=False)
    shipping_state=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),required=False)
    shipping_zip=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip'}),required=False)
    shipping_country=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Coutnry'}),required=False)
    class Meta:
        model=ShippingAddress()
        fields=['shipping_full_name', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_zip', 'shipping_country']
        exclude=['User']