from django.shortcuts import render, redirect
from django.http import HttpResponse
from Myapp.models import Student
from Myapp.Forms import StudentForm, Employeeform


# Create your views here.
def assign(request):
    return render(request, 'assignment.html')


def enlist(request):
    return render(request, 'Assignment2.html')


def cat(request):
    return render(request, 'Assignment3.html')


def form(request):
    return render(request, 'Assignment4.html')


def members(request):
    all = Student.objects.all().values()
    details = {
        "members": all
    }
    return render(request, 'Members.html', details)


def student(request):
    stu = StudentForm()
    return render(request, 'Student.html', {'form': stu})


def employee(request):
    if request.method == 'post':
        form = Employeeform(request.post)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = Employeeform()
        return render(request, 'Employee.html', {'form': form})


def setsession(request):
    request.session['firstname'] = 'Manuel'
    request.session['lastname'] = 'eMobilis'
    request.session['email'] = 'relmvrelm@gmail.com'
    return HttpResponse('Session has been successfully created')


def getsession(request):
    fname = request.session['firstname']
    lname = request.session['lastname']
    emailaddress = request.session['email']
    return HttpResponse(fname + ' ' + lname + ' ' + emailaddress)


def forms(request):
    return render(request, 'Form.html')


def newassign(request):
    return render(request, 'FormAssign.html')
