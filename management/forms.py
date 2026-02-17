from django.forms import ModelForm
from models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

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
    class meta:
        model = Student 
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class AddClassForm(ModelForm):
    class Meta:
        model = ClassName
        fields = '__all__'

class AddSubjectForm(ModelForm):
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
        if user== 'teacher':
            user.is_teacher = True
        if user == 'student':
            user.is_student = True
        if user == 'principal':
            user.is_principal = True
        if commit:
            user.save()
            return user
class UserEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('username', 'email', 'is_active', 'is_teacher', 'is_student', 'is_principal')

