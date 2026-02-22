from django.db import models

# Create your models here
# USER_CHOICE = [
#         ('Teacher', 'Teacher'),
#         ('Student', 'Student'),
#         ('Principal', 'Principal'),
#         ('Student', 'Student'),
#         ('Parent', 'Parent'),
#     ]

# class User(models.Model):
#     role = models.CharField(max_length=20, choices=USER_CHOICE)
#     email = models.EmailField(max_length=30)
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)

SUBJECT_CHOICES = [
    ('Mathematics', 'Mathematics'),
    ('English', 'English'),
    ('Science', 'Science'),
    ('Social Studies', 'Social Studies'),
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('History', 'History'),
    ('Geography', 'Geography'),
    ('Computer Science', 'Computer Science'),
    ('Physical Education', 'Physical Education'),
    ('Art', 'Art'),
    ('Music', 'Music'),
    ('Economics', 'Economics'),
    ('Business Studies', 'Business Studies'),
    ('Literature', 'Literature'),
    ('Religious Education', 'Religious Education'),
    ('Foreign Language', 'Foreign Language'),
]

class Teacher(models.Model):
    Name = models.CharField(max_length=20)
    Subject = models.CharField(max_length=30, choices=SUBJECT_CHOICES)
    Email = models.EmailField(max_length=225, blank=False, null=False, default=0)
    number = models.CharField(max_length=13, blank=False, null=False)
    class_name = models.CharField(max_length=50, blank=False, null=False)
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

GRADE_CHOICES = [
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ]

class Student(models.Model):
    Fullname = models.CharField(max_length=20, blank=False, null=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    classname = models.ForeignKey('ClassName', on_delete=models.CASCADE, related_name='student_class')
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    section = models.CharField(max_length=225, blank=False, null=False, default='A')
    GPA = models.FloatField(max_length=4, blank=False, null=False)
    email = models.EmailField(max_length=225, blank=False, null=False, default=0)
    subjects = models.CharField(max_length=50, choices=SUBJECT_CHOICES, blank=True, null=True)
    
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='class_teacher_students')
    
    def __str__(self):
        return self.Fullname    

class ClassName(models.Model):
    name = models.CharField(max_length=225)
    capacity = models.IntegerField()
    students = models.ManyToManyField(Student, blank=True, related_name='class_students')
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='class_teacher')
    Gradename = models.CharField(max_length=50)
    students_list = models.ManyToManyField(Student, blank=True, related_name='class_students_list')
    section = models.CharField(max_length=10)
    def __str__(self):
        return self.name

# class Subject(models.Model):
#     name = models.CharField(max_length=30)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subject_teacher')
#     classname = models.ForeignKey(ClassName, on_delete=models.CASCADE, related_name='subject_class')

# class Exam(models.Model):
#     EXAM_TYPES = (
#             ('Midterm', 'Midterm'),
#             ('Final', 'Final'),
#             ('Quiz', 'Quiz'),
#         )

#     name = models.CharField(max_length=100)
#     exam_type = models.CharField(max_length=20, choices=EXAM_TYPES)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     exam_date = models.DateField()
#     total_marks = models.IntegerField()

#     def __str__(self):
#         return f"{self.name} - {self.subject}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Leave', 'On Leave')])   
    teacher_marking = models.ForeignKey(Teacher, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.student.name} - {self.date}"

ACTIVITY_TYPE_CHOICES = [
    ('Attendance', 'Attendance'),
    ('Teacher Assignment', 'Teacher Assignment'),
    ('Class Activity', 'Class Activity'),
    ('Meeting', 'Meeting'),
    ('Event', 'Event'),
    ('Other', 'Other'),
]

class RecentActivity(models.Model):
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPE_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    classname = models.ForeignKey(ClassName, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Recent Activities"
    
    def __str__(self):
        return f"{self.title} - {self.date.strftime('%Y-%m-%d %H:%M')}"