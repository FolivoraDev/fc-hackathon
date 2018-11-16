# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 10

    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    model = Post
    paginate_by = 10

    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all()
