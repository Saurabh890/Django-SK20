from django.shortcuts import render, get_object_or_404 , redirect
from django.http import Http404
# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required




def blog_post_detail_page(request,slug):

	# querySet = BlogPost.objects.filter(slug=slug)
	# if querySet.count() == 0 :
	# 	raise Http404
	# else:
	# 	obj = querySet.first()
	#obj = querySet.first()
	print("Django Says", request.method, request.path, request.user)
	obj = get_object_or_404(BlogPost,slug=slug)
	template_name = 'blog/detail.html'
	context= {"object":obj}
	return render(request, template_name, context)


def blog_post_list_view(request):
	#qs=BlogPost.objects.filter(title__icontains='hello')
	qs=BlogPost.objects.all().published()
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		qs=(qs| my_qs).distinct()
	template_name ='blog/list.html'
	context={"object_list":qs}
	return render(request,template_name,context)



def blog_post_detail_view(request,slug):
	obj = get_object_or_404(BlogPost,slug=slug)
	template_name ='blog/detail.html'
	context={"object":obj}
	return render(request,template_name,context)

@staff_member_required
#@login_required
def blog_post_create_view(request):
	# if not request.user.is_authenticated:
	# 	return render(request,"not-a-user.html",{})
	form = BlogPostModelForm(request.POST or None, request.FILES or None )
	if form.is_valid():
		obj=form.save(commit=False)
		obj.user=request.user
		obj.save()
		 # print(form.cleaned_data)
		 # title = form.cleaned_data['title']
		 #obj=BlogPost.objects.create(**form.cleaned_data)
		form = BlogPostModelForm()
	template_name ='form.html'
	context={'form':form}
	return render(request,template_name,context)


def blog_post_update_view(request, slug):
	obj = get_object_or_404(BlogPost,slug=slug)
	form = BlogPostModelForm(request.POST or None, instance = obj)
	if form.is_valid():
		form.save()
	template_name ='form.html'
	context={'form':form,"title":f"Update {obj.title}"}
	return render(request,template_name,context)


def blog_post_delete_view(request, slug):
	obj = get_object_or_404(BlogPost,slug=slug)
	template_name ='blog/delete.html'
	if request.method == 'POST':
		obj.delete()
		return redirect("/blog")
	context={"object":obj}
	return render(request,template_name,context)