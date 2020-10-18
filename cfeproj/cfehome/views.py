from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost

#Dont Repeat Yourself = DRY
def home_page(request):
	my_title ="Hello there...."
	qs=BlogPost.objects.all()[:5]
	context={"title":"Welcome to Try Django","blog_list":qs}
	return render(request,"home.html",context)

def about_page(request):
	return render(request,"about.html",{"title":"About"})

def contact_page(request):
	
	form = ContactForm(request.POST or None)
	
	if form.is_valid():
		 print(form.cleaned_data)
		 form = ContactForm()
	context={"title":"Contact Us","form":form }
	return render(request,"form.html",context)
	#else :
	#	return render(request, "form1.html",{"title":"Contact Us"} )

def example_page(request):
	context={"title":"Example"}
	template_name = "Hello_world.html"
	template_obj=get_template(template_name)
	return HttpResponse(template_obj.render(context))
	#render(request,"Hello_world.html",{"title":"Contact Us"})
