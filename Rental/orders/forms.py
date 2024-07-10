from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'days', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

