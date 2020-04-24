from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from .models import Student, Class, Teacher
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse
from .forms import CreateClassForm, UpdateStudentForm

# Create your views here.

class ShowHomeView(ListView):
    """view for a list of all classes"""
    model = Student
    template_name = 'dance_site/home.html'
    context_object_name = 'home'

# all views related to Class

class ShowAllClassesView(ListView):
    """view for a list of all classes"""
    model = Class
    template_name = 'dance_site/show_all_classes.html'
    context_object_name = 'show_all_classes'

class DeleteClassView(DeleteView):
    """ a view to delete a class """
    template_name = 'dance_site/delete_class.html'
    queryset = Class.objects.all()

    def get_success_url(self):
        """return to the urls which we shoudl be directed to on delete"""
        pk = self.kwargs.get('pk')
        classd= Class.objects.filter(pk=pk)
        return reverse('show_all_classes') 

class CreateClassView(CreateView):
    ''' subclass of createview to display form to make a class'''
    form_class= CreateClassForm
    template_name='dance_site/create_class_form.html'




#views related to Student
class StudentPageView(DetailView):
    """show all quotes and all images for one person"""
    model= Student
    template_name = 'dance_site/student_page.html'
    
    def get_context_data(self, **kwargs):
        ''' Return a dictionary with context data for this template to use'''
        context = super(StudentPageView,self).get_context_data(**kwargs)
        return context #could be meaningless

class ShowPossibleClassesView(DetailView):
    model=Student
    template_name='dance_site/show_possible_classes.html'
    context_object_name='student'

def add_class(request, student_pk, class_pk):
    '''process add_class request to add a class for a given student'''
    student= Student.objects.get(pk=student_pk)
    addclass= Class.objects.get(pk=class_pk)
    student.classes_taken.add(addclass)
    student.save()
    return redirect(reverse('student', kwargs={'pk':student_pk}))

    
class UpdateStudentView(UpdateView):
    form_class= UpdateStudentForm
    template_name = 'dance_site/update_student.html'
    queryset = Student.objects.all()


class ShowAllStudentsView(ListView):
    """ create a subclass of listview to display all students"""

    model= Student 
    template_name= 'dance_site/show_all_students.html'
    context_object_name = 'show_all_students'


#Views related to Teacher
class ShowAllTeachersView(ListView):
    """ create a subclass of listview to display all teachers"""

    model= Teacher
    template_name= 'dance_site/show_all_teachers.html'
    context_object_name = 'show_all_teachers'

class TeacherPageView(DetailView):
    """show all quotes and all images for one person"""
    model= Teacher
    template_name = 'dance_site/teacher_page.html'
    
    def get_context_data(self, **kwargs):
        ''' Return a dictionary with context data for this template to use'''
        context = super(TeacherPageView,self).get_context_data(**kwargs)
        return context 