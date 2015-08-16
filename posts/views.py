from django.shortcuts import render,render_to_response,RequestContext

from .models import Posts

# Create your views here.

def detail(request,slug):


	post = Posts.objects.get(slug=slug)




	return render_to_response('posts/detail.html',locals(),context_instance=RequestContext(request))