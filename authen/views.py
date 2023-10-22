from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def authen(request):
    return render(request,"authen/authen.py")


def register(request):
    response_data = {
        'status': False,
        'error' : 'Sorry, something went wrong.'
    }
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_confirm = request.POST["password_confirm"]
        gender = request.POST["gender"]
        pin = request.POST["pin"]
        profession = request.POST["profession"]
        if password != password_confirm:
            response_data = {
                'status': False,
                'error' : 'Password not matching'
            }
        else:
            try:
                user = User.objects.get(username = email)
                response_data = {
                    'status': False,
                    'error' : 'Sorry, user already exists!'
                }
            except User.DoesNotExist:
                try:
                    user = User.objects.create_user(email,email,password)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.is_active=False
                    user.save()
                    response_data = {
                        'status': True,
                        'error' : 'Welcome, you are registered success.'
                    }
                except Exception as e:
                    response_data = {
                        'status': False,
                        'error' : f'Error: {str(e)}'
                    }
    return JsonResponse(response_data)
    
