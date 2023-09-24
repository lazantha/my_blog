from django.shortcuts import render,redirect
from .forms import UserLogForm,UserRegForm,Post
from .models import UserTable,PostTable
from django.contrib import messages
from django.db.models import Q

def testing(request):

	url="https://www.youtube.com/embed/ly36kn0ug4k?si=PJxpJTsH2D311M2M"
	
	return render(request,'blogPages/test.html',{'url':url})

def home(request):
	posts_edu = PostTable.objects.select_related('user_id').values('user_id__name', 'topic', 'link', 'content','created_at').filter(category='education').order_by('created_at')
	posts_know = PostTable.objects.select_related('user_id').values('user_id__name', 'topic', 'link', 'content','created_at').filter(category='knowledge').order_by('created_at')
	posts_enter = PostTable.objects.select_related('user_id').values('user_id__name', 'topic', 'link', 'content','created_at').filter(category='entertainment').order_by('created_at')
	posts_other = PostTable.objects.select_related('user_id').values('user_id__name', 'topic', 'link', 'content','created_at').filter(category='other').order_by('created_at')
	def linkFilter(dataset):
		for items in dataset:
			tokens=items['link'].split()
			path=(tokens[3])
			url_src=path.split('"')
			items['link']=url_src[1]
			return dataset
	post_edu=linkFilter(posts_edu)
	post_know=linkFilter(posts_know)
	post_enter=linkFilter(posts_enter)
	post_other=linkFilter(posts_other)
	context={'data_edu':post_edu,'data_know':post_know,'data_enter':post_enter,'data_other':post_other}
	return render(request,'blogPages/index.html',context)



def contactUs(request):

	context={}
	return render(request,'blogPages/contactUs.html',context)



def aboutUs(request):

	context={}
	return render(request,'blogPages/aboutUs.html',context)



def userLogin(request):
	form=UserLogForm()
	if request.method=='POST':
		form=UserLogForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			email=form.cleaned_data['email']
			request.session['name']=name
			request.session['email']=email
			print("session has been set")
			#database
			model=UserTable
			data=model.objects.values('name','email').filter(Q(name=name)and Q(email=email))
			if data:
				messages.success(request,'Login Success')
				return redirect('userHome')
			else:
				messages.success(request,'Check User Name Or Email ')
				return redirect('userLogin')
				print("Not exist")
			
	context={'form':form}
	return render(request,'blogPages/userLogin.html',context)



def userSignUp(request):
	form=UserRegForm()
	if request.method=='POST':
		form=UserRegForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Success')
			return redirect('userLogin')
			
	context={'form':form}
	return render(request,'blogPages/userReg.html',context)


def userHome(request):
	model=PostTable
	name=request.session.get('name')
	email=request.session.get('email')
	dataset=model.objects.values('topic','content','link')
	for items in dataset:
		tokens=items['link'].split()
		path=(tokens[3])
		url_src=path.split('"')
		items['link']=url_src[1]
	form=Post()
	if request.method=='POST':
		form=Post(request.POST)
		if form.is_valid():
			# user_id=UserTable.objects.values('id').filter(Q(name=name)and Q(email=email))
			user = UserTable.objects.filter(name=name, email=email).first()
			if user:
				new_post=form.save(commit=False)
				new_post.user_id=user
				new_post.save()
				messages.success(request,'Post Uploaded !')
				return redirect('userHome')
	context={'form':form,'dataset':dataset}
	return render(request,'blogPages/userHome.html',context)
