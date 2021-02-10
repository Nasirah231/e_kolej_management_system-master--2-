from django import forms
from django.forms import ChoiceField

from e_kolej_management_app.models import Students

class ChoiceNoValidation(ChoiceField):
    def validate(self, value):
        pass

class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control","autocomplete":"off"}))
    password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )

    gender = forms.ChoiceField(label="gender", choices=gender_choice, widget=forms.Select(
        attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", max_length=50, widget=forms.FileInput(
        attrs={"class": "form-control"}))

class EditStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )

    gender = forms.ChoiceField(label="gender", choices=gender_choice, widget=forms.Select(
        attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", max_length=50, widget=forms.FileInput(
        attrs={"class": "form-control"}), required=False)


class ApplyForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    gender = forms.ChoiceField(label="gender", choices=gender_choice, widget=forms.Select(
        attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    
    level_choice = (
        ("Diploma", "Diploma"),
        ("Degree", "Degree"),
        ("Master", "Master")
    )

    level = forms.ChoiceField(label="level", choices=level_choice, widget=forms.Select(
        attrs={"class": "form-control"}))
    
    scholarship_choice = (
        ("Yes", "Yes"),
        ("No", "No")
    )

    scholarship = forms.ChoiceField(label="scholarship", choices=scholarship_choice, widget=forms.Select(
        attrs={"class": "form-control"}))
    family_income = forms.CharField(label="family income", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    family_dependent = forms.CharField(label="family dependent", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))

    family_problem_choice = (
        ("Yes", "Yes"),
        ("No", "No")
    )

    family_problem = forms.ChoiceField(label="family problem", choices=family_problem_choice, widget=forms.Select(
        attrs={"class": "form-control"}))

    health_problem_choice = (
        ("Yes", "Yes"),
        ("No", "No")
    )

    health_problem = forms.ChoiceField(label="health problem", choices=health_problem_choice, widget=forms.Select(
        attrs={"class": "form-control"}))


    

    


    


