from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email address'}))
    first_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'})) 
    last_name = forms.CharField(label="",max_length=100 , widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'})) 
    
    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name', 'email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = '' 
        self.fields['username'].help_text = '<span class="form-text-text-muted"<small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text-text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password cant\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li><li>'  

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text-text-muted"<small>Enter the same password as before, for verification.</small></span>'   


#    Create Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    Phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    student_id = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Student_id", "class":"form-control"}), label="")
    Email = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    University = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"University", "class":"form-control"}), label="")
    School = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"School", "class":"form-control"}), label="")
    Department = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Department", "class":"form-control"}), label="")
    Block_Dorm = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Block/Dorm", "class":"form-control"}), label="")
    Acadamics = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Acadamics", "class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)

    class RecordForm(forms.Form):
        class meta:
            model = Record
            fields = '__all__'
            


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    