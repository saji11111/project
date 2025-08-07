from django import forms
from .models import Bill  # ✅ Add this line to fix the error

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['patient_name', 'service_description', 'amount', 'gst_percent', 'paid']

class BillFilterForm(forms.Form):
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    paid_status = forms.ChoiceField(
        required=False,
        choices=[('', 'All'), ('paid', 'Paid'), ('unpaid', 'Unpaid')]
    )
