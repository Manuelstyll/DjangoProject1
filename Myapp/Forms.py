from django import forms
from Myapp.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'age', 'phone_number']

class Employeeform(forms.Form):
    firstname= forms.CharField(label="Enter firstname", max_length=50)
    lastname= forms.CharField(label="Enter lastname", max_length=50)
    age= forms.IntegerField(label="Enter age")
    phone= forms.IntegerField(label="Enter phone number")
