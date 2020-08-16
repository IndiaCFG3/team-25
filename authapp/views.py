from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from authapp.models import UserProfile
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'authapp/registersignup.html')
    first_name = request.POST['user_name']
    email = request.POST['email-id']
    password = request.POST['pwd']
    phone = request.POST['mobile_number']
    user = User.objects.create_user(first_name, email, password)
    user.save()
    login(request, user)
    teacher = UserProfile(user = user, isTeacher=True, phone=phone, isFeaturePhone=False)
    teacher.save()
    return render(request, "authapp/registersignup.html")

def login_view(request):
    if request.method == "GET":
        return render(request, "authapp/loginpage.html")
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(username=username, password=password)
    if user is None:
        return render(request, "authapp/loginpage.html", {"error": "Invalid Credentials"})
    login(request, user)
    return HttpResponseRedirect("/")
