from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from product.models import Item
# Create your views here.
    ###################################
    ##        register User        ##
    ###################################
def register(request):
 	template="register.html"
 	context={}
 	return render(request,template,context)
 ##########################################

def  register_backend(request):
  # try:
     user=User.objects.create_user(request.POST['username'],
          request.POST['email'],
        	request.POST['password']
        	)
     user.first_name=request.POST['first_name']
     user.last_name=request.POST['last_name']
     user.save()
     return HttpResponseRedirect('/')
  # except:
    # return HttpResponse("user is exist")

    ###################################
    ##        register User        ##
    ###################################
    ###################################
    ##        logout User        ##
    ###################################
def logout_backend(request):
  logout(request)
  items =Item.objects.all()
  context={
  'items':items,
     }

  return render(request,'home.html',context)
   ###################################
    ##        logout User        ##
   ###################################
   ###################################
    ##        login User        ##
   ###################################

def log(request):
     return render(request,'login.html',{})
 #############    #################################
def logBackend(request):
  u=request.POST['username']
  p=request.POST['password']
  result=authenticate(request,username=u,password=p)
  if result is not None:
    print(result.username)
    items =Item.objects.all()
    context={
      'items':items,
      'user':result,
    }
    login(request,result)
    return render(request,'home.html',context)
  else:
     return HttpResponse("user is not exist")


