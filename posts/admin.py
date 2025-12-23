from django.contrib import admin
# Add "Student" to the import line below
from .models import Post, Student 

admin.site.register(Post)
admin.site.register(Student)