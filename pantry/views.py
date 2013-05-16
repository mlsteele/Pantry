from django.shortcuts import render, get_object_or_404
from pantry.models import Grocery

def index(request):
    grocerys = Grocery.objects.filter(count=1)
    return render(request, 'pantry/index.html', {'grocerys': grocerys})

def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'pantry/post.html', {'post': post})
