from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login,logout
from django.contrib import messages
from .forms import AddStudent
from .models import student

def home(request):
	if request.user.is_authenticated:
		return render(request, 'home.html', {})
	else:
		return redirect('login')


def new_student(request):
	form = AddStudent(request.POST , request.FILES)
	if request.user.is_authenticated:
		if request.method== "POST":
			if form.is_valid():
				form.save()
				messages.success(request, "student add ..")
				return redirect('home')
		return render(request, 'add_student.html', {'form':form})
	else:
		messages.success(request, "You Must Be Login ")
		return redirect('home')

def student_table(request):
	students = student.objects.all()
	if request.user.is_authenticated:
		return render(request , 'student_table.html' , {'students':students})
	else:
		messages.success(request, "You Must Be Login ")
		return redirect('login')
