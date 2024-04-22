from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .forms import createUserForm, CreateLoginForm
from UserPage import views
# Create your views here.



def signUp(request):
    if request.session.has_key('admin'):
        return HttpResponse("Admin home page")
    elif request.session.has_key('user'):
        return redirect(views.home)
    
    form = createUserForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            num = "+91" + request.POST['phonenum']
            form.save()
            return redirect('signin')
        else:
            return render(request, 'sign-up.html', {'form':form}) 
    return render(request, 'sign-up.html',{'form':form})



def signIn(request):
    if request.session.has_key('admin'):
        return HttpResponse("Admin home page")
    elif request.session.has_key('user'):
        return redirect(views.home)
    
    form = CreateLoginForm(request.POST or None)

    if request.method =='POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user:
                if user.is_superuser:
                    request.session['admin'] = username
                    return HttpResponse("Admin home page")
                else:
                    request.session['user'] = username
                    return redirect(views.home)
            return render(request,'sign-in.html',{'form':form,"err":"Invalid Credential"})
    return render(request,'sign-in.html',{'form':form})
