from re import TEMPLATE
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Project
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def contactView(request):
    if request.method == 'GET':
        project_data = Project.objects.filter(newsfeed=False)
        newsfeed = Project.objects.filter(newsfeed=True)
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['elolengodfrey@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    context = { 
        "project": project_data, 
        'form': form,
        'feed': newsfeed,
    }
    return render(request, "web/index.html", context)
def successView(request):
    return render(request, 'web/email_success.html' )


# class ProjectListView(ListView):
#     model = Project
#     template_name = 'web/index.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'web/details.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['posts'] = Project.objects.order_by('-timestamp')[:3]
        return context

#rendering create view
class ProjectCreateView(CreateView):
    model = Project
    template_name = 'web/proj_new.html'
    fields = '__all__'

#rendering update view
class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'web/proj_edit.html'
    fields = '__all__'


#rendering delete view
class ProjectDeleteView(DeleteView): # new
    model = Project
    template_name = 'web/proj_delete.html'
    success_url = "/"


