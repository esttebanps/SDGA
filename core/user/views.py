from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    return render(request, 'users/login.html')
    
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user:
    #         login(request, user)
    #         return redirect('sdga/home.html')
    #     else:
    #         return render(request, 'user/login.html', {'error': 'Invalid username and password'})
    # return render(request, 'user/login.html')
        