from django.shortcuts import render

def home(request):


	context={}
	return render(request,'blogPages/index.html',context)




def contactUs(request):

	context={}
	return render(request,'blogPages/contactUs.html',context)



def aboutUs(request):

	context={}
	return render(request,'blogPages/aboutUs.html',context)



