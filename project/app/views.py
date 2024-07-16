from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from django.views import View
from .models import *
from .forms import *

class TeacherListView(ListView):
    model = Teacher
    template_name = "app/teacher_list.html"
    context_object_name = "teachers"
    

# add TeacherCreateView which add the page with form which help us to add the new teacher

# class TeacherCreateView(View):

#     def get(self, request):
#         form = TeacherForm()
#         return render(request, "app/teacher_add.html", {"form": form})


#     def post(self, request):
#         form = TeacherForm(request.POST)
#         if form.is_valid():
#             form.save()
#             empty_form = TeacherForm()
#             return render(request, "app/teacher_add.html", {"form": empty_form})
#         return render(request, "app/teacher_add.html", {"form": form})



class TeacherCreateView(CreateView):
    model = Teacher 
    form_class = TeacherForm
    template_name = "app/teacher_add.html"
    success_url = reverse_lazy("teachers_list")