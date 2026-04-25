from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Candidate, Item, SupportCase, Order, PayrollEntry

def home(request):
    return render(request, 'home.html')

def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidates})

def candidate_detail(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    return render(request, 'candidate_detail.html', {'candidate': candidate})

@login_required
def inventory_list(request):
    items = Item.objects.all()
    return render(request, 'inventory_list.html', {'items': items})

def support_cases(request):
    cases = SupportCase.objects.all()
    return render(request, 'support_cases.html', {'cases': cases})

def sales_order(request):
    orders = Order.objects.all()
    return render(request, 'sales_order.html', {'order': orders})

def payroll(request):
    payroll_entries = PayrollEntry.objects.all()
    return render(request, 'payroll.html', {'payroll_entries': payroll_entries})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')