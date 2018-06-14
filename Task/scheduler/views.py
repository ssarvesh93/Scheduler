from django.views import generic
from .models import TaskManager
from .forms import UserForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View, ListView
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    template_name = 'scheduler/index.html'
    model = TaskManager

    def IndexView(request):
        args={'user',request.user}
        return render(request,'scheduler/index.html',args)

class AddTask(CreateView):
    model=TaskManager
  #  template_name = 'scheduler/taskmanager_form.html'
    fields=['task','t_Creator','t_Assigned','t_Done']
    success_url = reverse_lazy('sdlrs:index')

class UserFormView(View):
    form_class=UserForm
    template_name='scheduler/registration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            #Clean Data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('sdlrs:index')

        return render(request, self.template_name, {'form': form})

class DetailView(generic.DetailView):
    model = TaskManager
    template_name = 'scheduler/detail.html'

class TaskDelete(DeleteView):
    model=TaskManager
    success_url = reverse_lazy('sdlrs:index')

class TaskUpdate(UpdateView):
    model=TaskManager
    fields=['task','t_Creator','t_Assigned','t_Done']
    success_url = reverse_lazy('sdlrs:index')

def post_list(request):
    posts = TaskManager.objects.all()
    query = request.GET.get('q')
    query = TaskManager.objects.filter(title__icontains=query)
    context={
        'post' : posts,
    }
    return render(request,'scheduler/index.html',context)