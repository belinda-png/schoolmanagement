from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class AddUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class AddTeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class AddStudentForm(ModelForm):
    class Meta:
        model = Student 
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class AddClassNameForm(ModelForm):
    class Meta:
        model = ClassName
        fields = '__all__'

class ClassNameForm(forms.ModelForm):
    class Meta:
        model = ClassName
        fields = '__all__'

class AddSubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class UserCreationForm(UserCreationForm):
    USER_CHOICE = [
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
        ('Principal', 'Principal'),
    ]
    role = forms.ChoiceField(choices=USER_CHOICE, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']
        if user.role == 'Teacher':
            user.is_teacher = True
        if user.role == 'Student':
            user.is_student = True
        if user.role == 'Principal':
            user.is_principal = True
        if commit:
            user.save()
            return user

class UserEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('username', 'email', 'is_active', 'is_teacher', 'is_student', 'is_principal')

class ReportcardForm(ModelForm):
    class Meta:
        model = Reportcard
        fields = '__all__'

class AddReportcardForm(ModelForm):
    class Meta:
        model = Reportcard
        fields = '__all__'

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

class AddAttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

class AddExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

class RecentActivityForm(forms.ModelForm):
    class Meta:
        model = RecentActivity
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AddRecentActivityForm(ModelForm):
    class Meta:
        model = RecentActivity
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }