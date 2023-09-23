from django.shortcuts import render,redirect
from .forms import UserLogForm,UserRegForm,Post
from .models import UserTable,PostTable
from django.contrib import messages
from django.db.models import Q

def home(request):
	posts = PostTable.objects.select_related('user_id').values('user_id__name', 'topic', 'link', 'content','created_at')
	context={'data':posts}
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
	print("name",name)
	print("email",email)
	dataset=model.objects.values('topic','content','link')

	form=Post()
	if request.method=='POST':
		form=Post(request.POST)
		if form.is_valid():
			# user_id=UserTable.objects.values('id').filter(Q(name=name)and Q(email=email))
			user = UserTable.objects.filter(name=name, email=email).first()
			print(user)
			if user:
				new_post=form.save(commit=False)
				new_post.user_id=user
				new_post.save()
				messages.success(request,'Post Uploaded !')
				return redirect('userHome')

			# form.save()
			# messages.success(request,'Post Uploaded !')
			# return redirect('userHome')


	context={'form':form,'dataset':dataset}
	return render(request,'blogPages/userHome.html',context)
