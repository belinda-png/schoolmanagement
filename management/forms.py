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

class UserCreationForm(forms.ModelForm):
    USER_CHOICE = [
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
        ('Principal', 'Principal'),
    ]
    role = forms.ChoiceField(choices=USER_CHOICE, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password')
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserEditForm(forms.ModelForm):
    password = None
    class Meta:
        model = User
        fields = ('username', 'email', 'role')

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