from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from home.models import Contact
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# password for test user is Harry$$$***000
# Create your views here.
# def index(request):
#     print(request.user)
#     if request.user.is_anonymous:
#         return redirect("/login") 
#     return render(request, 'index.html')

# def loginUser(request):
#     if request.method=="POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)

#         # check if user has entered correct credentials
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             # A backend authenticated the credentials
#             login(request, user)
#             return redirect("/")

#         else:
#             # No backend authenticated the credentials
#             return render(request, 'login.html')

#     return render(request, 'login.html')

# def logoutUser(request):
#     logout(request)
#     return redirect("/login")


def contact(request):
          
          if request.method == "POST":
                  name = request.POST.get('name')
                  email= request.POST.get('email')
                  phone = request.POST.get('phone')
                  location = request.POST.get('location')
                  message = request.POST.get('message')
                  contact1 = Contact(name=name , email=email , phone=phone , location=location , message=message , date= datetime.today()) 
                  contact1.save()
          return render(request ,'contact.html')
    # return HttpResponse("this is contact page ")

def about(request):
       return render(request , 'aboutus.html')
    # return HttpResponse("this is about page ")
def services(request):
         return render(request , 'services.html')
    # return HttpResponse("this is services page ")

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super(CustomUserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user



@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login/')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login/')
