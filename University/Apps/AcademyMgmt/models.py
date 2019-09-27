from django.db import models


# Create your models here.


class Student(models.Model):
    LastName = models.CharField(max_length=35)
    SecLastName = models.CharField(max_length=35)
    Name = models.CharField(max_length=35)
    PIN = models.CharField(max_length=8)
    DOB = models.DateField()
    GENDERS = (('F', 'FEMALE'), ('M','MALE'))
    Gender = models.CharField(max_length=1, choices=GENDERS, default='M')

    def FullName(self):
        String = "{0} {1} {2}"
        return String.format(self.LastName, self.SecLastName, self.Name)

    def __str__(self):
        return self.FullName()

class Course(models.Model):
    Name = models.CharField(max_length=50)
    Credits = models.PositiveSmallIntegerField()
    Status = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.Name, self.Credits)

class Enrollment(models.Model):
    Student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    DOE = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        String = "{0} => {1}"
        return String.format(self.Student, self.Course.Name)

