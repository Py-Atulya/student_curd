from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def __init__(self,*args,**kwargs):
        super(StudentForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter the First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter the Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter the Email Address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter the Phone Number'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter the Address'
        