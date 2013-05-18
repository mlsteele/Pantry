from django.shortcuts import render, get_object_or_404
from pantry.models import Grocery

def test1(request):
    grocerys = Grocery.objects.filter(count=1)
    return render(request, 'pantry/test1.html', {'grocerys': grocerys})

def grocerys(request):
  return render(request, 'pantry/grocerys.html')

def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'pantry/post.html', {'post': post})
