from .models import Post
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from posts.forms import PostForm
from urllib import quote_plus


@login_required(login_url='/accounts/login/')
def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Successfully created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Something went wronge")

	context = {
		"form" : form,
	}
	return render(request, "post_form.html", context )

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	print instance
	# share_string = quote_plus(instance.content)
	print instance
	context = {
		"instance" : instance,
	}

	return render(request, "post_detail.html", context )

def post_list(request):
	queryset_list = Post.objects.all()
	
	query = request.GET.get("q")
	if query:
		queryset_list =queryset_list.filter(title__icontains=query)
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request_var = "page"

	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	
	context = {
		"object_list" : queryset,
		"page_request_var" : page_request_var

	}

	return render(request, "posts.html", context )


@login_required(login_url='/accounts/login/')
def post_update(request, id=None):

	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	print (request.user, instance.user )
	if not ( request.user == instance.user ):
		return redirect("posts:list")
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully updated")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Something went wronge")

	context = {
		"instance" : instance,
		"form" : form,
	}

	return render(request, "post_form.html", context )
@login_required(login_url='/accounts/login/')
def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	return redirect("posts:list")

	