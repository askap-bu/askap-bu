from django.urls import path
from .views import * 
urlpatterns = [
    path('', ShowHomeView.as_view(), name='home'),
    path('students', ShowAllStudentsView.as_view(), name='show_all_students'),
    path('teachers', ShowAllTeachersView.as_view(), name='show_all_teachers'),
    path('classes', AllClassView, name='show_all_classes'),
    path('create', CreateClassView.as_view(), name ='create_class'),
    path('class/<int:pk>/delete', DeleteClassView.as_view(), name ='delete_class'),
    path('student/<int:pk>', StudentPageView.as_view(), name='student'),
    path('student/<int:pk>/update', UpdateStudentView.as_view(), name ='update_student'),
    path('teacher/<int:pk>', TeacherPageView.as_view(), name='teacher'),
    path('student/<int:pk>/show_possible_classes', ShowPossibleClassesView.as_view(), name='show_possible_classes'),
    path('student/<int:student_pk>/add_class/<int:class_pk>', add_class, name='add_class'),


]