from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .form import Student
from .models import user
from django.shortcuts import redirect
# Create your views here.
def Add(request):
    if request.method =='POST':
        fm = Student(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'New Data Added')
            fm = Student()
        return redirect('/')
    else:
        fm = Student()
    stud = user.objects.all()
    return render(request,'start/addandshow.html',{'form':fm,'data':stud})
 

def delete(request,id):
     if request.method =='POST':
         dl = user.objects.get(pk=id)
         dl.delete()
         return HttpResponseRedirect('/')
     
def update(request,id): 
    if request.method =='POST':
        pi = user.objects.get(pk=id)
        fm = Student(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = user.objects.get(pk=id)
        fm = Student(instance = pi)
        
    return render(request, 'start/update.html',{'form':fm})
    
    
