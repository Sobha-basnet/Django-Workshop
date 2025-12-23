from django.urls import path
from . import views

urlpatterns = [
    # Main page showing the table
    path('', views.home, name='home'),
    
    # URL for the "Submit" form action
    path('create/', views.student_create_view, name='student_create_view'),
    
    # URL for editing a specific student (needs ID)
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    
    # URL for deleting a specific student (needs ID)
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]