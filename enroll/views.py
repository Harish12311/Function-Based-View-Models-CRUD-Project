from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User


# Create your views here.
# this frunction will add new item and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
        # fm.save()
        reg = User(
            name=nm,
            email=em,
            password=pw,
        )
        reg.save()
        fm = StudentRegistration()
    else:
        fm = StudentRegistration()

    stud = User.objects.all()
    return render(request, 'enroll/addAndShow.html', {'forms': fm, 'stud': stud})


#this function will updeta/edit

def update_date(request ,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
     pi=User.objects.get(pk=id)
    fm = StudentRegistration(request.POST, instance=pi)
    return render(request,'enroll/updateStudent.html',{'form':fm})


#this  function is used to delete tha data

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('add_show')

