from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView 
from django.urls import reverse_lazy, reverse 

# Create your views here.
from .models import Post
from .forms import CommentForm

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post_list.html"

class CommentGet(DetailView): 
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    
class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "post_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        post = self.object
        return reverse("post_detail", kwargs={"pk": post.pk})

class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
    model = Post
    fields = (
        "title",
        "company",
        "location",
        "job_type",
        "internship_status",
        "body",
    )
    template_name = "post_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class PostCreateView(LoginRequiredMixin, CreateView): # new
    model = Post
    template_name = "post_new.html"
    fields = (
        "title",
        "company",
        "location",
        "job_type",
        "internship_status",
        "body",
        ) 
    
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)
    