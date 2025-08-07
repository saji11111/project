from django import forms
from .models import Room, RoomAllocation

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'available']

class RoomAllocationForm(forms.ModelForm):
    class Meta:
        model = RoomAllocation
        fields = ['patient_id', 'patient_name', 'room']
