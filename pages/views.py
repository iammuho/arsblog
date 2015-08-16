# -*- coding: utf-8 -*-
import json
from django.shortcuts import render,render_to_response,RequestContext
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Contact


# Create your views here.

def contact(request):

	if request.method == 'POST':
		response_data = {}

		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message'];

		contact = Contact(name=name,email=email,message=message)
		contact.save()

		response_data['result'] = 'success'
		response_data['message'] = 'İletişim formunuz başarılı bir şekilde kaydedildi'

		return HttpResponse(json.dumps(response_data), content_type="application/json")





	return render_to_response('pages/contact.html',locals(),context_instance=RequestContext(request))


