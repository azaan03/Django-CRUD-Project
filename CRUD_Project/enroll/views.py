from django.shortcuts import render,HttpResponseRedirect
from .models import User
from .forms import UserForm

def home(request):
    return render(request, 'enroll/home.html')

def about(request):
    return render(request, 'enroll/about.html')

def contact(request):
    return render(request, 'enroll/contact.html')

def crud_operations(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = UserForm()
    else:
        fm = UserForm()
    stud = User.objects.all()
    return render(request, 'enroll/operations.html', {'form': fm, 'stu': stud})


def delete(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/crud_operations/')
    
def update(request,id):
    if request.method=="POST":
        ui=User.objects.get(pk=id)
        fm=UserForm(request.POST,instance=ui)
        if fm.is_valid():
            fm.save()
            fm=UserForm()
    else:
        ui=User.objects.get(pk=id)
        fm=UserForm(instance=ui)
    return render(request, 'enroll/update.html',{'form':fm})
   
        
        