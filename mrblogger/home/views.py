from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from mrblog.models import Post
from django.contrib.auth.models import User


#html pages
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']
        contact=Contact(name=name, email=email, phone=phone,content=content)
        contact.save()
        messages.success(request, "Your message has been successfully sent")

    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle=Post.objects.filter(title__icontains=query)
        allPostsContent=Post.objects.filter(content__icontains=query)
        allPostsAuthor=Post.objects.filter(author__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent,allPostsAuthor)

    if allPosts.count()==0:
        messages.warning(request,'No search results found, please refine your query')
    params={'allPosts': allPosts, 'query':query }
    return render(request,'home/search.html',params)


#authentication api's
def about(request):
    return render(request,'home/about.html')

def handleSignup(request):
    if request.method=="POST":
        # get the post parameters
        username=request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email= request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

       #checks for errorneous inputs
        if len(username)>10:
            messages.error(request,"username must be in 10 char")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "username must contain letters and numbers")
            return redirect('home')
        if password!=password2:
            messages.error(request,"password do not match")
            return redirect('home')

        #create user

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your account has been succesfully created")
        return redirect('home')
    else:
        return HttpResponse('404 - not allowed')

def handleLogin(request):
    if request.method=='POST':
        #get post parameters
        usernamelogin=request.POST['usernamelogin']
        passwordlogin=request.POST['passwordlogin']
        user=authenticate(username=usernamelogin,password=passwordlogin)

        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"invalid credentials, try again")
            return redirect('home')

    return HttpResponse('404- not found')

def handleLogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect('home')

