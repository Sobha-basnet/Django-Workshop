from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# 1. VIEW ALL ACTIVE STUDENTS
def home(request):
    # Changed .all() to .filter(is_deleted=False)
    students = Student.objects.filter(is_deleted=False)
    form = StudentForm()
    return render(request, 'posts/index.html', {'students': students, 'form': form})

# 2. CREATE A NEW STUDENT (WITH EMAIL)
def student_create_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            
            # Prepare email details
            subject = 'Welcome to the Student Portal'
            message = f'Hi {student.studentName}, your registration was successful!'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [student.studentEmail]
            
            try:
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, "Student added and Welcome Email sent!")
            except Exception as e:
                messages.warning(request, f"Student added, but email failed: {e}")
                
            return redirect('home')
    return redirect('home')

# 3. UPDATE AN EXISTING STUDENT
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'posts/edit_student.html', {'form': form, 'student': student})

# 4. SOFT DELETE A STUDENT
def delete_student(request, id):
    # Fetch the student
    student = get_object_or_404(Student, id=id)
    
    if request.method == "POST":
        student.is_deleted = True  # Soft delete
        student.save()
        messages.success(request, f"{student.studentName} moved to trash.")
        return redirect('home')
    
    #  THIS LINE: This shows the "Are you sure?" page
    return render(request, 'posts/delete_confirm.html', {'student': student})