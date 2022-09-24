from django.shortcuts import render, redirect
from . models import Student, Gender, StudentClass, ScoreSheet, Term, Session
from . forms import ScoreForm, StudentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

@login_required(login_url='login')
def registeration(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form':form,
    }
    return render(request, 'registeration.html', context)

@login_required(login_url='login')
def update_student(request, pk):
    student = Student.objects.get(id = pk)
    form = StudentForm(instance = student)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form':form,
    }
    return render(request, 'update_student.html', context)

@login_required(login_url='login')
def update_score(request, pk):
    c_session= Session.objects.filter(is_current = True).first()
    c_term = Term.objects.filter(is_current = True).first()
    student = Student.objects.get(id = pk)
    student_class = student.student_class
    score = ScoreSheet.objects.filter(student__id = pk).first()
    form = ScoreForm(initial={
        'session':c_session,
        'term':c_term,
        'student':student,
        'student_class':student_class,
    }, instance=score)

    form = ScoreForm(instance=score)
    if request.method == 'POST':
        form = ScoreForm(request.POST,instance=score)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form':form,
        'score':score
    }

    return render(request, 'update_score.html', context)

@login_required(login_url='login')
def dashboard(request):
    my_students = Student.objects.all()
    student_class = StudentClass.objects.all()
    total = my_students.count()
    males = Student.objects.filter(sex__name = 'Male').count()
    females = Student.objects.filter(sex__name = 'Female').count()

    context = {
        'my_students':my_students,
        'total':total,
        'males':males,
        'females':females,
        'student_class':student_class,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def student(request, pk):
    student = Student.objects.get(id = pk)
    context = {
        'student':student,
    }
    return render(request, 'student.html', context)

@login_required(login_url='login')
def single_class(request,pk):
    my_class = StudentClass.objects.get(id=pk)
    class_members = my_class.student_set.all()
    context = {
        'my_class':my_class,
        'class_members':class_members,
    }
    return render(request, 'single_class.html', context)

@login_required(login_url='login')
def single_student(request,pk):
    my_student = Student.objects.get(id=pk)
    context = {
        'my_student':my_student,
    }
    return render(request, 'single_student.html', context)

@login_required(login_url='login')
def add_score(request,pk):
    c_session= Session.objects.filter(is_current = True).first()
    c_term = Term.objects.filter(is_current = True).first()
    student = Student.objects.get(id = pk)
    student_class = student.student_class
    form = ScoreForm(initial={
        'session':c_session,
        'term':c_term,
        'student':student,
        'student_class':student_class,
    })
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form .is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form':form,
    }
    return render(request, 'add_score.html', context)

@login_required(login_url='login')
def report(request, pk):
    my_student = Student.objects.get(id=pk)
    report_card = ScoreSheet.objects.filter(student__id = pk).first()
    subjects = my_student.scoresheet_set.all()

    context = {
        'report_card':report_card,
        'subjects':subjects,
    }
    return render(request, 'report.html', context)

def Logout(request):
    logout(request)
    return redirect('login')