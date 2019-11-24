from django.shortcuts import render
from django.views import generic
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task

class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task

class CreateTaskView(LoginRequiredMixin, generic.CreateView):
    redirect_field_name = 'to_do_list/task_detail.html'
    form_class = TaskForm
    model = Task

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateTaskView(LoginRequiredMixin, generic.UpdateView):
    redirect_field_name = 'to_do_list/task_detail.html'
    form_class = TaskForm
    model = Task

class DeleteTaskView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy('to_do_list:all')