from django.shortcuts import render,render_to_response,RequestContext
from django.db import models
from posts.models import Posts
from django.core.paginator import Paginator

# Create your views here.

def index(request):


	posts_ = Posts.objects.all().order_by("-id");

	posts = Paginator(posts_, 0)


	return render_to_response('index/index.html',locals(),context_instance=RequestContext(request))