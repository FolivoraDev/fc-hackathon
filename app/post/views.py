# Create your views here.
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Comment


class PostListView(ListView):
    model = Post
    paginate_by = 10

    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all()


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'posts/create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


def comment_create_view(request, pk):
    if request.method == 'POST':
        Comment.objects.create(
            post=Post.objects.get(pk=pk),
            content=request.POST['content'],
            author=request.user,
            password=111,
        )
        return redirect('post-list')


class PostDetailView(DetailView):
    model = Post
    paginate_by = 10

    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all()
