from django.shortcuts import render,redirect
from .forms import UserLogForm,UserRegForm
from .models import UserTable
from django.contrib import messages
from django.db.models import Q
def home(request):


	context={}
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

	context={}
	return render(request,'blogPages/userHome.html',context)
