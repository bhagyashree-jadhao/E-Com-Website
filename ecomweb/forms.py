from django import forms

from ecomweb.models import Custemer


class CustomerForm(forms.ModelForm):
    class Meta:
        model=Custemer
        fields="__all__"


        