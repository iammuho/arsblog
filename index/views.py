from django.shortcuts import render,render_to_response,RequestContext
from django.db import models
from posts.models import Posts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):

	#page retrieves
	page = request.GET.get('page')


	post_list = Posts.objects.all().order_by("-id");
	#paginate post_list as per page 25 items
	paginator = Paginator(post_list, 10)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)



	return render_to_response('index/index.html',locals(),context_instance=RequestContext(request))