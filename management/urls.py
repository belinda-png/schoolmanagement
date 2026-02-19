from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    
    # Teacher URLs
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.addteacher, name='addteacher'),
    path('teachers/<int:id>/', views.viewteacher, name='viewteacher'),
    path('teachers/<int:id>/update/', views.updateteacher, name='updateteacher'),
    path('teachers/<int:id>/delete/', views.deleteteacher, name='deleteteacher'),
    
    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.addstudent, name='addstudent'),
    path('students/<int:id>/', views.viewstudent, name='viewstudent'),
    path('students/<int:id>/update/', views.updatestudent, name='updatestudent'),
    path('students/<int:id>/delete/', views.deletestudent, name='deletestudent'),
    
    # Exam URLs
    path('exams/', views.exam_list, name='exam_list'),
    path('exams/add/', views.addexam, name='addexam'),
    path('exams/<int:id>/', views.viewexam, name='viewexam'),
    path('exams/<int:id>/update/', views.updateexam, name='updateexam'),
    path('exams/<int:id>/delete/', views.deleteexam, name='deleteexam'),
    
    # ClassName URLs
    path('classes/', views.classname_list, name='classname_list'),
    path('classes/add/', views.addclassname, name='addclassname'),
    path('classes/<int:id>/', views.viewclassname, name='viewclassname'),
    path('classes/<int:id>/update/', views.updateclassname, name='updateclassname'),
    path('classes/<int:id>/delete/', views.deleteclassname, name='deleteclassname'),
    
    # Subject URLs
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/add/', views.addsubject, name='addsubject'),
    path('subjects/<int:id>/', views.viewsubject, name='viewsubject'),
    path('subjects/<int:id>/update/', views.updatesubject, name='updatesubject'),
    path('subjects/<int:id>/delete/', views.deletesubject, name='deletesubject'),
    
    # Attendance URLs
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.addattendance, name='addattendance'),
    path('attendance/<int:id>/', views.viewattendance, name='viewattendance'),
    path('attendance/<int:id>/update/', views.updateattendance, name='updateattendance'),
    path('attendance/<int:id>/delete/', views.deleteattendance, name='deleteattendance'),
    
    # Reportcard URLs
    path('reportcards/', views.reportcard_list, name='reportcard_list'),
    path('reportcards/add/', views.addreportcard, name='addreportcard'),
    path('reportcards/<int:id>/', views.viewreportcard, name='viewreportcard'),
    path('reportcards/<int:id>/update/', views.updatereportcard, name='updatereportcard'),
    path('reportcards/<int:id>/delete/', views.deletereportcard, name='deletereportcard'),
    
    # RecentActivity URLs
    path('activities/', views.recent_activity_list, name='recent_activity_list'),
    path('activities/add/', views.addrecentactivity, name='addrecentactivity'),
    path('activities/<int:id>/', views.viewrecentactivity, name='viewrecentactivity'),
    path('activities/<int:id>/update/', views.updaterecentactivity, name='updaterecentactivity'),
    path('activities/<int:id>/delete/', views.deleterecentactivity, name='deleterecentactivity'),
]
