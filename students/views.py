from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Student
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import StudentForm

def index(request):
    sort_by = request.GET.get('sort_by', 'student_number')  # Default sort is by 'student_number'
    student_list = Student.objects.all().order_by(sort_by)
    paginator = Paginator(student_list, 6)  # Show 6 students per page.
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    return render(request, 'students/index.html', {'students': students})

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def search(request):
    if request.method == "GET":
        search_text = request.GET.get('search_text', None)
        page_number = request.GET.get('page')
        if search_text:
            student_list = Student.objects.filter(Q(first_name__icontains=search_text) | Q(last_name__icontains=search_text))
        else:
            student_list = Student.objects.all()
        paginator = Paginator(student_list, 5)  # Show 10 students per page.
        students = paginator.get_page(page_number)
        return render(request, 'students/search_results.html', {'students': students})
    
def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student_number = form.cleaned_data['student_number']

            # Check if the student number already exists in the database.
            try:
                Student.objects.get(student_number=student_number)
            except Student.DoesNotExist:
                new_student = Student(
                    student_number=student_number,
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    address=form.cleaned_data['address'],
                    form=form.cleaned_data['form'],
                    paidFees=form.cleaned_data['paidFees']
                )
                new_student.save()

                return render(request, 'students/add.html', {
                    'form': StudentForm(),
                    'success': True
                })

            # If the student number already exists, show an error message.
        else:
            return render(request, 'students/add.html', {
                'form': form
        })
    else:
        form = StudentForm()
        return render(request, 'students/add.html', {
            'form': form
    })

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html',{
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html',{
        'form':form,
    })

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))