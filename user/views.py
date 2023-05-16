from django.shortcuts import render

# Create your views here.
def user_login(request):
    print('let the user login')
    return render(request, 'login.html')