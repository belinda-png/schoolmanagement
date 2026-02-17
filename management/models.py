from django.db import models

# Create your models here
USER_CHOICE = [
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
        ('Principal', 'Principal'),
        ('Student', 'Student'),
        ('Parent', 'Parent'),
    ]

class User(models.Model):
    role = models.CharField(max_length=20, choices=USER_CHOICE)
    email = models.EmailField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Teacher(models.Model):
    Name = models.CharField(max_length=20)
    Subject = models.CharField(max_length=30)
    Email = models.EmailField()
    number = models.IntegerField()
    subject = models.CharField(max_length=30)
    class_name = models.CharField(max_length=50)
    def __str__(self):
        return self.Name
    
GENDER_CHOICE = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]

STATUS_CHOICE = [ 
        ('Active', 'Active'),
        ('On Leave', 'On Leave'),
        ('Transferred', 'Transferred')
    ]

class Student(models.Model):
    name = models.CharField(max_length=20)
    Date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    admission_number = models.IntegerField()
    address = models.TextField()
    Enrollment_date = models.DateField()
    classname = models.ForeignKey('ClassName', on_delete=models.CASCADE,)
    grade = models.CharField(max_length=5)
    section = models.CharField(max_length=1)
    GPA = models.FloatField()   
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,)
    def __str__(self):
        return self.name    

class ClassName(models.Model):
    name = models.CharField(max_length=5)
    capacity = models.IntegerField()
    students = models.ManyToManyField(Student, blank=True)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE,)
    Gradename = models.CharField(max_length=50)
    students_list = models.ManyToManyField(Student, blank=True, related_name='grade')
    section = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,)
    classname = models.ForeignKey(ClassName, on_delete=models.CASCADE)

class Exam(models.Model):
    EXAM_TYPES = (
            ('Midterm', 'Midterm'),
            ('Final', 'Final'),
            ('Quiz', 'Quiz'),
        )

    name = models.CharField(max_length=100)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_date = models.DateField()
    total_marks = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')])   
    teacher_marking = models.ForeignKey(Teacher, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.student.name} - {self.date}"

class Reportcard(models.Model): 
    totalmarks = models.IntegerField(default=0, blank=False, null=False)   
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    position = models.CharField(max_length=20)
    teacher_comment = models.TextField()
    term = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.student.name} - {self.exam}"