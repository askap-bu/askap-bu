# File name: models.py 
# Author: Andriana Skaperdas (askap@bu.edu)
# Description: Holds all the views for /dance_site


from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from .models import Student, Class, Teacher
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse
from .forms import CreateClassForm, UpdateStudentForm
from django.db.models import Q

# Create your views here.

class ShowHomeView(ListView):
    """view for the homepage"""
    model = Student
    template_name = 'dance_site/home.html'
    context_object_name = 'home'

# all views related to Class

class ShowAllClassesView(ListView):
    """view for a list of all classes"""
    model = Class
    template_name = 'dance_site/show_all_classes.html'
    context_object_name = 'show_all_classes'
    
    
def AllClassView(request):
    """view for a list of all classes"""
    context={}
    query=""
    if request.GET:
        query=request.GET['q']
        context['query']=str(query)
    show_all_classes = get_search_queryset(query)   
    context['show_all_classes'] = show_all_classes
    return render(request, 'dance_site/show_all_classes.html', context)


def get_search_queryset(query=None):
    """ function to get a queryset for a class"""
    queryset=[]
    queries = query.split(" ")
    for q in queries:
        classes= Class.objects.filter((Q(class_name__icontains=q) | Q(day__icontains=q))).distinct()
        for c in classes:
            queryset.append(c)
    return list(set(queryset))


class DeleteClassView(DeleteView):
    """ a view to delete a class """
    template_name = 'dance_site/delete_class.html'
    queryset = Class.objects.all()

    def get_success_url(self):
        """return to the urls which we should be directed to on delete"""
        pk = self.kwargs.get('pk')
        classd= Class.objects.filter(pk=pk)
        return reverse('show_all_classes') 

class CreateClassView(CreateView):
    ''' subclass of createview to display form to make a class'''
    form_class= CreateClassForm
    template_name='dance_site/create_class_form.html' 

    def get_success_url(self):
        """return to the urls which we shoudl be directed to on delete"""
        pk = self.kwargs.get('pk')
        classd= Class.objects.filter(pk=pk)
        return reverse('show_all_classes') 



#views related to Student

class StudentPageView(DetailView):
    """show all information for one person"""
    model= Student
    template_name = 'dance_site/student_page.html'
    
    def get_context_data(self, **kwargs):
        ''' Return a dictionary with context data for this template to use'''
        context = super(StudentPageView,self).get_context_data(**kwargs)
        return context #could be meaningless

class ShowPossibleClassesView(DetailView):
    """ show all the classes a student can add to thier enrollment list"""
    model=Student
    template_name='dance_site/show_possible_classes.html'
    context_object_name='student'
    query = ""

def add_class(request, student_pk, class_pk):
    '''process add_class request to add a class for a given student'''
    student= Student.objects.get(pk=student_pk)
    addclass= Class.objects.get(pk=class_pk)
    student.classes_taken.add(addclass)
    student.save()
    return redirect(reverse('student', kwargs={'pk':student_pk}))

class UpdateStudentView(UpdateView):
    """ show the page and form to update a student's information"""
    form_class= UpdateStudentForm
    template_name = 'dance_site/update_student.html'
    queryset = Student.objects.all()

class ShowAllStudentsView(ListView):
    """ create a subclass of listview to display all students"""
    model= Student 
    template_name= 'dance_site/show_all_students.html'
    context_object_name = 'show_all_students'



# def AllStudentViewGrid(request):
#     """view for a list of all classes"""
#     context={}
#     # query=""
#     # if request.GET:
#     #     query=request.GET['q']
#     #     context['query']=str(query)
#     people=Student.objects.all()
#     show_all_students= lol(people,3)
#     context['show_all_students'] = show_all_students
#     return render(request, 'dance_site/show_all_student_grid.html', context)

   

# def lol(people, num_col):
#     list_tot = []
#     list_int = []
#     count = 0
#     for p in people:
#         if len(list_int) < num_col:
#             list_int.append(p)
#             if len(list_int) == num_col:
#                 list_tot.append(list_int)
#                 list_int = []
#             if people[count] == people[(len(people) - 1)]:# there are no more people, append
#                 list_tot.append(list_int)
#             count += 1
#     return list_tot


#Views related to Teacher
class ShowAllTeachersView(ListView):
    """ create a subclass of listview to display all teachers"""
    model= Teacher
    template_name= 'dance_site/show_all_teachers.html'
    context_object_name = 'show_all_teachers'

class TeacherPageView(DetailView):
    """show all informtation for one teacher """
    model= Teacher
    template_name = 'dance_site/teacher_page.html'
    
    def get_context_data(self, **kwargs):
        ''' Return a dictionary with context data for this template to use'''
        context = super(TeacherPageView,self).get_context_data(**kwargs)
        return context 


