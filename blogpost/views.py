# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from blogpost.models import Blogpost

def index(request):
	post=Blogpost.objects.all()[:5]
	return render_to_response('index.html',{'posts':post})
	#return HttpResponse(u"huangse wangzhan")
def view_post(request,slug):
	return render_to_response('blogpost_detail.html',{'posts': get_object_or_404(Blogpost,slug=slug)})
# Create your views here.
