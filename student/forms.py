from django import forms
from .models import student 

class AddStudent(forms.ModelForm):
	pic = forms.ImageField()
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
	father_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"father Name", "class":"form-control"}), label="")
	mother_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Mother name", "class":"form-control"}), label="")
	grandfather = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"grandfather name", "class":"form-control"}), label="")
	data_of_birth = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date","placeholder":"date of birth", "class":"form-control"}), label="")
	born_city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"city", "class":"form-control"}), label="")
	class Meta:
		model = student
		exclude = ("user",) 