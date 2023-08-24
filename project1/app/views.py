from django.shortcuts import render, redirect
from .models import Employee, Concern

def employee_concerns(request):
    employees = Employee.objects.all()
    return render(request, 'mentalhealth/employee_concerns.html', {'employees': employees})

from django.shortcuts import render, redirect

def login(request):
    # Handle login logic here
    if request.method == 'POST':
        # Get the employee ID from the login form
        employee_id = request.POST['employee_id']
        # Perform authentication or other necessary operations
        # Redirect to the dashboard page on successful login
        return redirect('dashboard')
    return render(request, 'login.html')

def dashboard(request):
    # Handle dashboard logic here
    return render(request, 'dashboard.html')

def concern(request):
    # Handle concern submission logic here
    if request.method == 'POST':
        # Get the form data from the concern submission form
        employee_name = request.POST['employee_name']
        employee_id = request.POST['employee_id']
        concern_title = request.POST['concern_title']
        concern_description = request.POST['concern_description']
        # Save the data to the database or perform other operations
        # Redirect to the thank you page on successful submission
        return redirect('thankyou')
    return render(request, 'concern.html')

def thankyou(request):
    # Handle thank you page logic here
    return render(request, 'thankyou.html')
