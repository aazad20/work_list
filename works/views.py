from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from .models import Work
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class worklogin(LoginView):
    template_name = "works/login.html"
    fields = '__all__'
    redirect_authenticated_url = True
    def get_success_url(self):
        return reverse_lazy('works')

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect("works")
        return super(worklogin,self).get(*args,**kwargs)

class workregister(FormView):
    template_name = 'works/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('works')

    
    def form_valid(self, form): 
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(workregister,self).form_valid(form)

      
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect("works")
        return super(workregister,self).get(*args,**kwargs)


class worklist(LoginRequiredMixin,ListView):
    model = Work
    #print([post.pk for post in Work.objects.all()])
    context_object_name='Works'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['Works'] = context['Works'].filter(user=self.request.user)
        context["count"] =  context['Works'].filter(done=False).count()
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['Works']=context['Works'].filter(title__icontains=search_input)
        

        context['search_input']=search_input
        return context

class workdetail(LoginRequiredMixin,DetailView):
    model = Work

class workcreate(LoginRequiredMixin,CreateView):
    model = Work
    fields = ['title','desc','done']
    success_url = reverse_lazy('works')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(workcreate,self).form_valid(form)






    
class workupdate(LoginRequiredMixin,UpdateView):
    model = Work
    fields = ['title','desc','done']
    success_url = reverse_lazy('works')

class workdelete(LoginRequiredMixin,DeleteView):
    model = Work
    fields = '__all__'
    success_url = reverse_lazy('works')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(workcreate,self).form_valid(form)