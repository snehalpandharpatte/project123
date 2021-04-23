from django.db import models

# Create your models here.


class CommonFields(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class College(CommonFields): 
    address = models.CharField(max_length=100)
    fees = models.IntegerField()

    class Meta:
        db_table = 'colg'

class Principle(CommonFields):
    exp = models.FloatField()
    college = models.OneToOneField(College, on_delete=models.CASCADE)

    class Meta:
        db_table = 'principle'


class Department(CommonFields):
    strength = models.IntegerField(default=60)
    college = models.ForeignKey(College, on_delete=models.CASCADE,related_name='dept')

    class Meta:
        db_table = 'dept'


print("Hello")
class Teacher(CommonFields):
    exp = models.FloatField()
    salary = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE,related_name='teacher')

    class Meta:
        db_table = 'teacher'


class Subject(CommonFields):
    practical= models.BooleanField(default=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name='subj')

    class Meta:
        db_table = 'sub'


class Student(CommonFields):
    age = models.IntegerField()
    marks = models.IntegerField()
    subject = models.ManyToManyField(Subject,related_name='stud')

    class Meta:
        db_table = 'stud'


# from up to down use related name and from bottom to up use main name
# when one to many relation use .all() and for one to one relation use get
