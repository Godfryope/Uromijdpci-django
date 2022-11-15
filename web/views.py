from re import TEMPLATE
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Blog, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, ContactForm
from django.db.models import Q

# Create your views here.
class HomeView(ListView):
    model: Blog
    template_name = 'web/index.html'
    paginate_by = 3
    context_object_name = 'blog_data'

    def get_queryset(self):
        return Blog.objects.all()
    
    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     if self.request.method == "GET":
    #         context['form'] = ContactForm()
    #     else:
    #         context['form'] = ContactForm(request.POST)
    #         if form.is_valid():
    #             subject = form.cleaned_data["subject"]
    #             from_email = form.cleaned_data["from_email"]
    #             message = form.cleaned_data['message']
    #             try:
    #                 send_mail(subject, message, from_email, ["elolengodfrey@gmail.com"])
    #             except BadHeaderError:
    #                 return HttpResponse("Invalid header found.")
    #             return redirect("success")
    #     # context['blog_data'] = Blog.objects.all()
    #     context['form'] = ContactForm()

    #     return context



# def contactView(request):
#     if request.method == 'GET':
#         Blog_data = Blog.objects.filter(newsfeed=False)
#         newsfeed = Blog.objects.filter(newsfeed=True)
#         # page = request.GET.get('page', 1)
#         # paginator = Paginator(Blog_data, 4)
#         form = ContactForm()
#         # try:
#         #     Blog_data = paginator.page(page)
#         # except PageNotAnInteger:
#         #     Blog_data = paginator.page(1)
#         # except EmptyPage:
#         #     Blog_data = paginator.page(paginator.num_pages)
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['elolengodfrey@gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     context = {
#         "Blog": Blog_data,
#         'form': form,
#         'feed': newsfeed,
#     }
#     return render(request, "web/index.html", context)
class successView(TemplateView):
    template_name = 'web/email_success.html'


# class BlogListView(ListView):
#     model = Blog
#     template_name = 'web/index.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'web/details.html'
    context_object_name = 'blog'

    # def get_context_data(self, **kwargs):
    #     context = super(PostDetail, self).get_context_data(**kwargs)
    #     if request.method == "POST":
    #         comment_form = CommentForm(request.POST or None)
    #         if comment_form.is_valid():
    #             comment=comment_form.save(commit=False)
    #             comment.post=post
    #             comment.save()
    #     else:
    #         comment_form = CommentForm()
    #     context['post']=post.objects.all()
    #     context['comments']=comments.objects.all()
    #     context['comment_form']=comment_form()        
    #     template_name='Post_detail.html'
    #     return render(request, template_name, context)

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['latest'] = Blog.objects.order_by('-timestamp')[:4]
        context['comment'] = Comment.objects.filter(aprroved=True)
        context['form'] = CommentForm()
        return context
    
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_URL(self):
        return reverse ('request: detail', kwargs = {'slug':self.object.blog.slug})

    def form_valid(self, form):
        blog = get_object_or_404(Request, slug = self.kwargs ['slug'])
        Form.instance.blog = Request
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):

#rendering create view
class BlogCreateView(CreateView):
    model = Blog
    template_name = 'web/proj_new.html'
    fields = '__all__'

#rendering update view
class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'web/proj_edit.html'
    fields = '__all__'


#rendering delete view
class BlogDeleteView(DeleteView): # new
    model = Blog
    template_name = 'web/proj_delete.html'
    success_url = "/"

class SearchResultsView(ListView):
    model = Blog
    template_name = "web/search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Blog.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


