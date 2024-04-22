from django.shortcuts import render, redirect
from django.http import HttpResponse
from signInUp import views
# Create your views here.




def home(request):
    if request.session.has_key('admin'):
        return HttpResponse("Admin home page")
    elif request.session.has_key('user'):
        return render(request,'home.html')
    else:
        return redirect(views.signIn)
    

