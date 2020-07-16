from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View ,TemplateView,ListView, DetailView , CreateView, DeleteView, UpdateView
from . import models
from django.urls import reverse_lazy
# Create your views here.
# def index(request) :
#     return  render(request,'index.html')


class CBView(TemplateView):

    template_name = 'index.html'

# class CBView(view) :
    # def get(self,request):
        # return HttpResponse("content")

class indexView(TemplateView):
    template_name = 'template.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'THIS IS THE VALUE'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbvapp/school_detail.html'
    
class SchoolCreateView(CreateView):
    fields = ('name','principal','location') 
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('principal','name')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("cbvapp:list")
