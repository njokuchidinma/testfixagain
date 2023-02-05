from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views import View


# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/about.html')

class Blog(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/blog.html')

class Blog_grid(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/blog-grid.html')

class Blog_single(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/blog-single.html')

class Service(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/service.html')

class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/contact.html')

class Signup(View):
    def get(self, request, *args, **kwargs):
         return render(request, 'clone/signup.html')    
    
    def post(self, request, *args, **kwargs):
            fname=request.POST.get('firstname')
            lname=request.POST.get('lastname')
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            cpword=request.POST.get('confirm_password')

            if password==cpword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'username already exists')
                # return redirect('signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'email address already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=fname, last_name=lname)
                user.set_password(password)
                user.save()
                return redirect('signin')
            

class Signin(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/signin.html')    

class Portfolio(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/portfolio.html')

class Team(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/team.html')

class Faq(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/faq.html')

class Error(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/team.html')

class Pricing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clone/pricing.html')