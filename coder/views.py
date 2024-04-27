from django.shortcuts import HttpResponse, render, redirect
from .models import Contact, myPost, blogComment
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
	allPost = list(myPost.objects.all())
	top3Post = []
	for i in range(3):
		mostview = 0
		blogPost=""
		for post in allPost:
			if post.postViews > mostview:
				mostview = post.postViews
				blogPost=post

		top3Post.append(blogPost)
		allPost.remove(blogPost)

	params = {'user':request.user,"posts":top3Post}
	return render(request,'index.html', params)

def getBlog(request, slug):
	getPost = myPost.objects.filter(slug=slug)
	allComments = blogComment.objects.filter(post=getPost[0])
	views = getPost[0].postViews+1
	comments = [comment for comment in allComments if comment.parent == None]
	replys = [comment for comment in allComments if comment.parent != None]
	print(comments)
	params = {'user':request.user, 'post':getPost, 'comments':comments, 'replys':replys}
	return render(request, 'blogContent.html',params)

def getBlogsList(request):
	allPost = myPost.objects.all()
	params = {'user':request.user, 'posts':allPost}
	return render(request, 'blogsList.html',params)

def about(request):
	params = {'user':request.user}
	return render(request, 'about.html', params)

def contact(request):
	if request.method == "POST":
		name1 = request.POST.get('name')
		phone1 = request.POST.get('phone')
		email1 = request.POST.get('email')
		decs1 = request.POST.get('txtarea')
		contact = Contact(name=name1, email=email1, desc=decs1, phone=phone1, contact_date=date.today())
		contact.save()
		messages.success(request,"Your Query sended <b>Successfully</b>")
		return render(request,'contact.html')

	if request.method == "GET":
		return render(request, 'contact.html')

def handleSignUp(request):
	if request.method == "POST":
		username1 = request.POST.get('username')
		phone1 = request.POST.get('phone')
		email1 = request.POST.get('email')
		pass1 = request.POST.get('pass1')
		pass2 = request.POST.get('pass2')

		# Checking crediantial	
		if pass1 != pass2:
			messages.error(request, 'Please Enter <b>Correct Password!!!</b>')
			return redirect(index)
		if authenticate(username=username1, password=pass1) != None:
			messages.error(request, 'That username is already taken. <b>Try another</b>')
			return redirect('/')
		if not username1.isalnum():
			messages.error(request, 'Enter Proper <b>Username!!!</b>')
			return redirect(index)

		myuser = User.objects.create_user(username1, email1, pass1)
		print(myuser)
		myuser.first_name = username1
		myuser.save()
		messages.success(request, "Signed Up <b>Successfully</b>")
		return redirect('/')
	else:
		return HttpResponse("404 - Not Found")

def handleLogin(request):
	if request.method == "POST":
		loginUsername = request.POST.get('usernameLogin')
		loginPass = request.POST.get('passLogin')
		user = authenticate(username=loginUsername, password=loginPass)

		if user is not None:
			login(request, user)
			messages.success(request, "Successfully <b>Logged in</b>")
			return redirect(index)
		else:
			messages.error(request,"Please Check your <b>Username and Password</b>")
			return redirect(index)
	else:
		return HttpResponse("<h1>404 - Not Found</h1>")

def handleLogout(request):
	logout(request)
	messages.success(request, "You Logged Out <b>Successfully</b>")
	return redirect(index)

def postComment(request):
	if request.method == "POST":
		commentTxt = request.POST.get('txtComment')
		postSno = request.POST.get('postSno')
		user = request.user
		parentSno = request.POST.get('parentSno')
		print(parentSno)
		post = myPost.objects.get(sno=postSno)
		if len(commentTxt) == 0:
			return redirect("/blog/"+post.slug)
		if parentSno == "":	
			blogcomment = blogComment(comment=commentTxt, user=user, post=post)
			blogcomment.save()
			messages.success(request, "Your comment sended successfully")
		elif parentSno != "":
			parent = blogComment.objects.get(sno=parentSno)
			blogcomment = blogComment(comment=commentTxt, user=user, post=post, parent=parent)
			blogcomment.save()
			messages.success(request, "Your reply sended successfully")
		return redirect("/blog/"+post.slug)

def searchBlog(request):
	if request.method == "POST":
		allPost = myPost.objects.all()
		searchtxt = request.POST.get('searchText').lower()
		searchedBlog = []
		for post in allPost:
			title = post.title.lower()
			print("post title",title)
			if title.find(searchtxt) != -1:
				searchedBlog.append(post)
				print("founded")
		if 	len(searchedBlog) != 0:
			print(searchedBlog)
			params = {'user':request.user, 'posts':searchedBlog}
			return render(request, 'blogsList.html',params)
		else:
			messages.error(request,"Your Search is <b>NOT FOUND!!!</b>")
			return redirect('/')

	else:
		return HttpResponse("<h1>404 - NOT Found</h1>")





