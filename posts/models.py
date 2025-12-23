from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.title

class Student(models.Model):
    # 'id' is created automatically, no need to add it manually
    studentName = models.CharField(max_length=100)
    studentEmail = models.EmailField(unique=True) # unique=True prevents duplicate emails
    age = models.IntegerField()
    address = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.studentName