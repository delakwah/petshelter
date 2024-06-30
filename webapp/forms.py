from django import forms
from django.forms import ModelForm
from .models import Adopt, Volunteer, Pets

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adopt
        fields = ['pet', 'fname', 'lname', 'age', 'gender', 'phonenum', 'email', 'address', 'occup']
        widgets = {
            'pet': forms.HiddenInput(),
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phonenum': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'occup': forms.TextInput(attrs={'class': 'form-control'}),
        }

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['firstname', 'lastname', 'age', 'gender', 'phonenum', 'email' ]
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phonenum': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class PetForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ['name', 'desc', 'breed', 'age', 'health', 'pet_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'health': forms.TextInput(attrs={'class': 'form-control'}),
            'pet_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta: 
        model = Pets
        fields = ['name', 'desc', 'breed', 'age', 'health', 'pet_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'health': forms.TextInput(attrs={'class': 'form-control'}),
            'pet_image': forms.FileInput(attrs={'class': 'form-control'}),
        }