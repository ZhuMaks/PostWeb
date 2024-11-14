from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.
def posts_home(request):
    posts = Articles.objects.order_by('-date')
    return render(request, 'posts/posts_home.html', {'posts': posts})

class PostDetailView(DetailView):
    model = Articles
    template_name = 'posts/details_view.html'
    context_object_name = 'Article'

class PostUpdateView(UpdateView):
    model = Articles
    template_name = 'posts/create.html'

    form_class = ArticlesForm

class PostDeleteView(DeleteView):
    model = Articles
    success_url = '/posts/'
    template_name = 'posts/post-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form was wrong'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'posts/create.html', data)
