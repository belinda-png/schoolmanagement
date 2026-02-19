from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def addteacher(request):
    if request.method == "POST":
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher Added Successfully!')
            return redirect('teacher_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddTeacherForm()
    return render(request, 'add_teacher.html', {'form': form})

def viewteacher(request, id):
    teacher_list = get_object_or_404(Teacher, pk=id)
    return render(request, 'view_teacher.html', {'teacher_list': teacher_list})

def updateteacher(request, id):
    teacher_list = get_object_or_404(Teacher, pk=id)
    if request.method == "POST":
        form = AddTeacherForm(request.POST, instance=teacher_list)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher Updated Successfully!')
            return redirect('teacher_list')
        else:
            form = AddTeacherForm(instance=teacher_list)
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddTeacherForm(instance=teacher_list)
    return render(request, 'update_teacher.html', {'form': form, 'teacher_list': teacher_list})

def deleteteacher(request, id):
    teacher_list = get_object_or_404(Teacher, pk=id)
    if request.method == "POST":
        teacher_list.delete()
        messages.success(request, 'Teacher Deleted Successfully!')
        return redirect('teacher_list')
    else:
        return render(request, 'delete_teacher.html', {'teacher_list': teacher_list})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def addstudent(request):
    if request.method == "POST":
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Added Successfully!')
            return redirect('student_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddStudentForm()
    return render(request, 'add_student.html', {'form': form})

def viewstudent(request, id):
    student_list = get_object_or_404(Student, pk=id)
    return render(request, 'view_student.html', {'student_list': student_list})

def updatestudent(request, id):
    student_list = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        form = AddStudentForm(request.POST, instance=student_list)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Updated Successfully!')
            return redirect('student_list')
        else:
            form = AddStudentForm(instance=student_list)
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddStudentForm(instance=student_list)
    return render(request, 'update_student.html', {'form': form, 'student_list': student_list})

def deletestudent(request, id):
    student_list = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        student_list.delete()
        messages.success(request, 'Student Deleted Successfully!')
        return redirect('student_list')
    else:
        return render(request, 'delete_student.html', {'student_list': student_list})

def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam_list.html', {'exams': exams})

def addexam(request):
    if request.method == "POST":
        form = AddExamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exam Created Successfully!')
            return redirect('exam_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddExamForm()
    return render(request, 'add_exam.html', {'form': form})

def viewexam(request, id):
    exam_list = get_object_or_404(Exam, pk=id)
    return render(request, 'view_exam.html', {'exam_list': exam_list})

def updateexam(request, id):
    exam_list = get_object_or_404(Exam, pk=id)
    if request.method == "POST":
        form = AddExamForm(request.POST, instance=exam_list)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exam Updated Successfully!')
            return redirect('exam_list')
        else:
            form = AddExamForm(instance=exam_list)
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddExamForm(instance=exam_list)
    return render(request, 'update_exam.html', {'form': form, 'exam_list': exam_list})

def deleteexam(request, id):
    exam_list = get_object_or_404(Exam, pk=id)
    if request.method == "POST":
        exam_list.delete()
        messages.success(request, 'Exam Deleted Successfully!')
        return redirect('exam_list')
    else:
        return render(request, 'delete_exam.html', {'exam_list': exam_list})

# Additional views for missing models
def classname_list(request):
    return render(request, 'classname_list.html', {'classnames': ClassName.objects.all()})

def addclassname(request):
    if request.method == "POST":
        form = AddClassNameForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class Added Successfully!')
            return redirect('classname_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddClassNameForm()
    return render(request, 'add_classname.html', {'form': form})

def viewclassname(request, id):
    classname = get_object_or_404(ClassName, pk=id)
    return render(request, 'view_classname.html', {'classname': classname})

def updateclassname(request, id):
    classname = get_object_or_404(ClassName, pk=id)
    if request.method == "POST":
        form = AddClassNameForm(request.POST, instance=classname)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class Updated Successfully!')
            return redirect('classname_list')
        else:
            form = AddClassNameForm(instance=classname)
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddClassNameForm(instance=classname)
    return render(request, 'update_classname.html', {'form': form, 'classname': classname})

def deleteclassname(request, id):
    classname = get_object_or_404(ClassName, pk=id)
    if request.method == "POST":
        classname.delete()
        messages.success(request, 'Class Deleted Successfully!')
        return redirect('classname_list')
    else:
        return render(request, 'delete_classname.html', {'classname': classname})

def subject_list(request):
    return render(request, 'subject_list.html', {'subjects': Subject.objects.all()})

def addsubject(request):
    if request.method == "POST":
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject Added Successfully!')
            return redirect('subject_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddSubjectForm()
    return render(request, 'add_subject.html', {'form': form})

def viewsubject(request, id):
    subject = get_object_or_404(Subject, pk=id)
    return render(request, 'view_subject.html', {'subject': subject})

def updatesubject(request, id):
    subject = get_object_or_404(Subject, pk=id)
    if request.method == "POST":
        form = AddSubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject Updated Successfully!')
            return redirect('subject_list')
        else:
            form = AddSubjectForm(instance=subject)
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddSubjectForm(instance=subject)
    return render(request, 'update_subject.html', {'form': form, 'subject': subject})

def deletesubject(request, id):
    subject = get_object_or_404(Subject, pk=id)
    if request.method == "POST":
        subject.delete()
        messages.success(request, 'Subject Deleted Successfully!')
        return redirect('subject_list')
    else:
        return render(request, 'delete_subject.html', {'subject': subject})

def attendance_list(request):
    return render(request, 'attendance_list.html', {'attendances': Attendance.objects.all()})

def addattendance(request):
    if request.method == "POST":
        form = AddAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance Marked Successfully!')
            return redirect('attendance_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddAttendanceForm()
    return render(request, 'add_attendance.html', {'form': form})

def viewattendance(request, id):
    attendance = get_object_or_404(Attendance, pk=id)
    return render(request, 'view_attendance.html', {'attendance': attendance})

def updateattendance(request, id):
    attendance = get_object_or_404(Attendance, pk=id)
    if request.method == "POST":
        form = AddAttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance Updated Successfully!')
            return redirect('attendance_list')
        else:
            form = AddAttendanceForm(instance=attendance)
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddAttendanceForm(instance=attendance)
    return render(request, 'update_attendance.html', {'form': form, 'attendance': attendance})

def deleteattendance(request, id):
    attendance = get_object_or_404(Attendance, pk=id)
    if request.method == "POST":
        attendance.delete()
        messages.success(request, 'Attendance Deleted Successfully!')
        return redirect('attendance_list')
    else:
        return render(request, 'delete_attendance.html', {'attendance': attendance})

def reportcard_list(request):
    return render(request, 'reportcard_list.html', {'reportcards': Reportcard.objects.all()})

def addreportcard(request):
    if request.method == "POST":
        form = AddReportcardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reportcard Added Successfully!')
            return redirect('reportcard_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddReportcardForm()
    return render(request, 'add_reportcard.html', {'form': form})

def viewreportcard(request, id):
    reportcard = get_object_or_404(Reportcard, pk=id)
    return render(request, 'view_reportcard.html', {'reportcard': reportcard})

def updatereportcard(request, id):
    reportcard = get_object_or_404(Reportcard, pk=id)
    if request.method == "POST":
        form = AddReportcardForm(request.POST, instance=reportcard)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reportcard Updated Successfully!')
            return redirect('reportcard_list')
        else:
            form = AddReportcardForm(instance=reportcard)
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddReportcardForm(instance=reportcard)
    return render(request, 'update_reportcard.html', {'form': form, 'reportcard': reportcard})

def deletereportcard(request, id):
    reportcard = get_object_or_404(Reportcard, pk=id)
    if request.method == "POST":
        reportcard.delete()
        messages.success(request, 'Reportcard Deleted Successfully!')
        return redirect('reportcard_list')
    else:
        return render(request, 'delete_reportcard.html', {'reportcard': reportcard})

# RecentActivity Views
def recent_activity_list(request):
    activities = RecentActivity.objects.all()
    return render(request, 'recent_activity_list.html', {'activities': activities})

def addrecentactivity(request):
    if request.method == "POST":
        form = AddRecentActivityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Activity Added Successfully!')
            return redirect('recent_activity_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddRecentActivityForm()
    return render(request, 'add_recent_activity.html', {'form': form})

def viewrecentactivity(request, id):
    activity = get_object_or_404(RecentActivity, pk=id)
    return render(request, 'view_recent_activity.html', {'activity': activity})

def updaterecentactivity(request, id):
    activity = get_object_or_404(RecentActivity, pk=id)
    if request.method == "POST":
        form = AddRecentActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Activity Updated Successfully!')
            return redirect('recent_activity_list')
        else:
            form = AddRecentActivityForm(instance=activity)
            messages.error(request, 'Please correct the error below.')
    else:
        form = AddRecentActivityForm(instance=activity)
    return render(request, 'update_recent_activity.html', {'form': form, 'activity': activity})

def deleterecentactivity(request, id):
    activity = get_object_or_404(RecentActivity, pk=id)
    if request.method == "POST":
        activity.delete()
        messages.success(request, 'Activity Deleted Successfully!')
        return redirect('recent_activity_list')
    else:
        return render(request, 'delete_recent_activity.html', {'activity': activity})

# Dashboard view to show recent activities
def dashboard(request):
    recent_activities = RecentActivity.objects.all()[:10]  # Show last 10 activities
    context = {
        'recent_activities': recent_activities,
        'total_students': Student.objects.count(),
        'total_teachers': Teacher.objects.count(),
        'total_classes': ClassName.objects.count(),
        'total_exams': Exam.objects.count(),
    }
    return render(request, 'dashboard.html', context)