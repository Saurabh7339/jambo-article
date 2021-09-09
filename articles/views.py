from django.shortcuts import render,redirect
from .models import Articles
from django.http import HttpResponse,HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .import forms

@login_required(login_url="/accounts/login/")
def articles_list(request):
	articles  = Articles.objects.all().order_by('date')
	return render(request ,'articles/articles_list.html',{'articles':articles})


def update_article(request,slug):
	article = Articles.objects.get(slug=slug)
	if request.method =='POST':
		article.title  = request.POST.get('title')
		article.body = request.POST.get('body')
		article.slug = request.POST.get('slug')
		article.save()
		return redirect('articles:articles')
			
	return render(request,'articles/update.html',{'article':article})

def delete_article(request,slug):
		user = request.user
		article=Articles.objects.get(slug=slug)
		if article.author==request.user:
			obj = Articles.objects.get(slug=slug)
			idd = obj.id
			instance = Articles.objects.get(id=idd)
			instance.delete()
			return redirect('articles:articles')
			#article.delete()
		else:
			return HttpResponseForbidden()

@login_required(login_url="/accounts/login/")
def article_detail(request,slug):
	article = Articles.objects.get(slug=slug)
	return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
	if request.method=='POST':
		form = forms.CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('articles:articles')
	form = forms.CreateArticle()
	return render(request,'articles/article_create.html',{'form':form})
