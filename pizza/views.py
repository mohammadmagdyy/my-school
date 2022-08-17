from django.utils.html import format_html
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth 


from django.utils import timezone

#from .serializers import customersserializer, postserializer 
from .models import  students

from datetime import datetime
import re
from django.contrib.auth import authenticate , login
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from rest_framework import status
#from rest_framework.views import APIView
#from rest_framework import mixins , generics,viewsets
#from rest_framework.authentication import BasicAuthentication,TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
#from .permissions import IsAuthorizedOrReadonly


# Create your views here.
def index(request):
    st=None
    if request.user.is_authenticated and not request.user.is_anonymous:
         
          try:
            st= students.objects.get(user=request.user)
          except students.DoesNotExist:
            st=None
      
          context={
                'student':st
                        }
           
    else:
         context={}
    return render(request,'pages/index.html',context)
    

def indexarab(request):
    st=None
    if request.user.is_authenticated and not request.user.is_anonymous:
         
          try:
            st= students.objects.get(user=request.user)
          except students.DoesNotExist:
            st=None
      
          context={
                'student':st
                        }
           
    else:
         context={}
    return render(request,'pages/indexarab.html',context)

def signup(request):
    fname=''
    lname=None
    phone=''
    city=''
    password=''
   
    confirm =''
   
    matt=None
    matt2=None
    terms=None
    username=None
    if request.method == 'POST' and 'btnsubmitup' in request.POST:
        if 'fname' in request.POST and 'user' in request.POST and 'phone' in request.POST and 'city' in request.POST and 'confirmpass' in request.POST  and 'terms' in request.POST and 'pass' in request.POST:
            fname=request.POST['fname']
            username=request.POST['user']
            phone=request.POST['phone']
            city=request.POST['city']
            password=request.POST['pass']
          
            confirm=request.POST['confirmpass']
            
            matt=re.match("[0-9]",password)
            matt2=re.match("[a-zA-z]",password)
            ismatched=bool(matt)
            ismatched2=bool(matt2)
            terms=request.POST['terms']
            if fname and username and phone and city and password  and confirm :
                if password != confirm:
                     messages.warning(request,'passwords must be equal')
                     fname=request.POST['fname']
                     username=request.POST['user']
                     phone=request.POST['phone']
                     city=request.POST['city']
                     password=request.POST['pass']
                   
                     confirm=request.POST['confirmpass']
                    
                     return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
          
           'confirmpass':confirm,
          
        })
                elif len(password)<8:
                      messages.warning(request,'passwords must contain at 8 characters including an upper case letter , a lower case letter and anumber')
                      fname=request.POST['fname']
                      username=request.POST['user']
                      phone=request.POST['phone']
                      city=request.POST['city']
                      password=request.POST['pass']
                     
                      confirm=request.POST['confirmpass']
                     
                      return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
          
           'confirmpass':confirm,
           
        })
                elif students.objects.filter(phone=phone).exists():
                    messages.warning(request,'phone number already exists')
                    fname=request.POST['fname']
                    username=request.POST['user']
                    phone=request.POST['phone']
                    city=request.POST['city']
                    password=request.POST['pass']
                   
                    confirm=request.POST['confirmpass']
                  
                    return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
          
           'confirmpass':confirm,
          
        })
                elif  ismatched:
                     messages.warning(request,'passwords must contain at 8 characters including an upper case letter , a lower case letter and anumber ')
                     fname=request.POST['fname']
                     username=request.POST['user']
                     phone=request.POST['phone']
                     city=request.POST['city']
                     password=request.POST['pass']
                   
                     confirm=request.POST['confirmpass']
                    
                     return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
          
           'confirmpass':confirm,
           
        })
                elif User.objects.filter(username=username).exists():
                    messages.warning(request,'username already exists')
                    fname=request.POST['fname']
                    username=request.POST['user']
                    phone=request.POST['phone']
                    city=request.POST['city']
                    password=request.POST['pass']
                   
                    confirm=request.POST['confirmpass']
                  
                    return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
          
           'confirmpass':confirm,
          
        })
                elif  ismatched:
                     messages.warning(request,'passwords must contain at 8 characters including an upper case letter , a lower case letter and anumber ')
                     fname=request.POST['fname']
                     username=request.POST['user']
                     phone=request.POST['phone']
                     city=request.POST['city']
                     password=request.POST['pass']
                   
                     confirm=request.POST['confirmpass']
                    
                     return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
          
           'confirmpass':confirm,
           
        })
                elif not re.findall("[a-z]",password) or not re.findall("[A-Z]",password)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   :
                     messages.warning(request,'passwords must contain at 8 characters including an upper case letter , a lower case letter and anumber. ')
                     fname=request.POST['fname']
                     username=request.POST['user']
                     phone=request.POST['phone']
                     city=request.POST['city']
                     password=request.POST['pass']
                  
                     confirm=request.POST['confirmpass']
                     
                     return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
          
           'confirmpass':confirm,
           
        })
               
                else:
                    user=User.objects.create_user(username=username,password=password)
                    
                    
                    user.save()
                    customerprofile=students(
                        user=user,name=fname,phone=phone,city=city,
                    )
                    customerprofile.save()
                    fname=''
                    username=''
                    phone=''
                    city=''
                    password=''
                   
                    confirm=''
                   



                    messages.success(request,format_html("you registered sucess ,<a href='/signin' style='color:green;'>sign in</a> to attend your lectures "))
                    return redirect('signup')
                   
        else:
            messages.warning(request,'something went wrong!')
            return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
          
           'confirmpass':confirm,
          
        })
        


    else:    
        return render(request,'pages/profile/signup.html')


   
     



def signuparab(request):
    fname=''
    lname=None
    phone=''
    city=''
    password=''
    email=''
    confirm =''
    gender=''
    matt=None
    matt2=None
    terms=None
    username=None
    if request.method == 'POST' and 'btnsubmitup' in request.POST:
        if 'fnamear' in request.POST  and 'phonear' in request.POST and 'userar'in request.POST and 'cityar' in request.POST  and 'confirmpassar' in request.POST and 'terms' in request.POST and 'passar' in request.POST:
            fname=request.POST['fnamear']
            username=request.POST['userar']
            phone=request.POST['phonear']
            city=request.POST['cityar']
            password=request.POST['passar']
            
            confirm=request.POST['confirmpassar']
            
            matt=re.match("[0-9]",password)
            matt2=re.match("[a-zA-z]",password)
            ismatched=bool(matt)
            ismatched2=bool(matt2)
            terms=request.POST['terms']
            if fname  and phone and city and password  and confirm and username:
                if password != confirm:
                     messages.warning(request,'يجب ان تتساوى كلمتى السر')
                     fname=request.POST['fnamear']
                     username=request.POST['userar']
                     phone=request.POST['phonear']
                     city=request.POST['cityar']
                     password=request.POST['passar']
                   
                     confirm=request.POST['confirmpassar']
                    
                     return render(request,'pages/profile/signuparab.html',{
           'fnamear':fname,
           'userar':username,
           'phonear':phone,
           'cityar':city,
           'passar':password,
           'confirmpassar':confirm,
           
        })
                elif len(password)<8:
                      messages.warning(request,'يجب ان تتكون كلمة السر من ثمان عناصر تتضمن حرف انجليزى كبير و حرف انجليزى صغير و رقم')
                      fname=request.POST['fnamear']
                      username=request.POST['userar']
                      phone=request.POST['phonear']
                      city=request.POST['cityar']
                      password=request.POST['passar']
                      
                      confirm=request.POST['confirmpassar']
                      
                      return render(request,'pages/profile/signuparab.html',{
           'fnamearab':fname,
            'userar':username,
           'phonear':phone,
           'cityar':city,
           'passar':password,
           
           'confirmpassar':confirm,
           
        })
                elif students.objects.filter(phone=phone).exists():
                    messages.warning(request,'رقم الهاتف موجود بالفعل')
                    fname=request.POST['fnamear']
                    username=request.POST['userar']
                    phone=request.POST['phonear']
                    city=request.POST['cityar']
                    password=request.POST['passar']
                   
                    confirm=request.POST['confirmpassar']
                  
                    return render(request,'pages/profile/signuparab.html',{
           'fnamear':fname,
           'userar':username,
           'phonear':phone,
           'cityar':city,
           'passar':password,
          
           'confirmpassar':confirm,
          
        })
                elif User.objects.filter(username=username).exists():
                    messages.warning(request,'اسم المستخدم موجود بالفعل')
                    fname=request.POST['fnamear']
                    username=request.POST['userar']
                    phone=request.POST['phonear']
                    city=request.POST['cityar']
                    password=request.POST['passar']
                   
                    confirm=request.POST['confirmpassar']
                  
                    return render(request,'pages/profile/signuparab.html',{
           'fnamear':fname,
           'userar':username,
           'phonear':phone,
           'cityar':city,
           'passar':password,
          
           'confirmpassar':confirm,
          
        })
                elif  ismatched:
                     messages.warning(request,'يجب ان تتكون كلمة السر من ثمان عناصر تتضمن حرف انجليزى كبير و حرف انجليزى صغير و رقم')
                     fname=request.POST['fnamear']
                     username=request.POST['userar']
                     phone=request.POST['phonear']
                     city=request.POST['cityar']
                     password=request.POST['passar']
                     
                     confirm=request.POST['confirmpassar']
                     
                     return render(request,'pages/profile/signuparab.html',{
           'fnamear':fname,
           'userar':username,
           'phonear':phone,
           'cityar':city,
           'passar':password,
           
           'confirmpassar':confirm,
          
        })
                elif not re.findall("[a-z]",password) or not re.findall("[A-Z]",password)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   :
                     messages.warning(request,' يجب ان تتكون كلمة السر من ثمان عناصر تتضمن حرف انجليزى كبير و حرف انجليزى صغير و رقم')
                     fname=request.POST['fnamear']
                     username=request.POST['userar']
                     phone=request.POST['phonear']
                     city=request.POST['cityar']
                     password=request.POST['passar']
                     
                     confirm=request.POST['confirmpassar']
                     
                     return render(request,'pages/profile/signuparab.html',{
           'fnamear':fname,
           'userar':username,
           'phonear':phone,
           'cityar':city,
           'passar':password,
         
           'confirmpassar':confirm,
           
        })
                
                else:
                    user=User.objects.create_user(username=username,password=password)
                    
                    
                    user.save()
                    customerprofile=students(
                        user=user,name=fname,phone=phone,city=city,
                    )
                    customerprofile.save()
                    fname=''
                    username=''
                    phone=''
                    city=''
                    password=''
                    username = ''
                    confirm=''
                   



                    messages.success(request,format_html("كى تتمكن من حضور محاضراتك<a href='/signinarab' style='color:green;'> سجل دخول</a> لقد قمت بالاشتراك بنجاح"))
                    return redirect('signuparab')
                   
        else:
            messages.warning(request,'لقد حدث شئ ما خطأ!')
            return render(request,'pages/profile/signuparab.html',{
           'fnamear':fname,
           'userar':username,
           'phonear':phone,
           'cityar':city,
           'passar':password,
          
           'confirmpass':confirm,
          
        })
        


    else:    
        return render(request,'pages/profile/signuparab.html')

def signin(request):
    username=None
    password=None
    if request.method=='POST' and 'btnsubmit' in request.POST and 'user' in request.POST and 'psw' in request.POST and 'agree' in request.POST:
       
           username=request.POST['user']
           password=request.POST['psw']
           if username and password:
                user=auth.authenticate(username=username,password=password)
                if user is not None:
                   auth.login(request,user)
                   messages.success(request,'you have loggined successfully')
                   username=''
                   password=''
                else:
                    messages.warning(request,'wrong username or password!')
                    return render(request,'pages/profile/signin.html',
                    {
                        'username':username,
                        'password':password
                    }
                    )
           else:
                messages.warning(request,'wrong username or password!') 
                return redirect('signin') 
                  
           return redirect('signin')
    else:  
       
        return render(request,'pages/profile/signin.html')
def signinarab(request):
    username=None
    password=None
    if request.method=='POST' and 'btnsubmit' in request.POST and 'userar' in request.POST and 'pswar' in request.POST and 'agree' in request.POST:
       
           usernamee=request.POST['userar']
           passworde=request.POST['pswar']
           if usernamee and passworde:
                user=auth.authenticate(username=usernamee,password=passworde)
                if user is not None:
                   auth.login(request,user)
                   messages.success(request,'لقد تم تسجيل دخولك بنجاح')
                   username=''
                   password=''
                else:
                    messages.warning(request,'خطأ فى اسم المستخدم او كلمة السر')
                    return render(request,'pages/profile/signinarab.html',
                    {
                        'username':usernamee,
                        'password':passworde
                    }
                    )
           else:
                messages.warning(request,'خطأ فى اسم المستخدم او كلمة السر') 
                return redirect('signinarab') 
                  
           return redirect('signinarab')
    else:  
       
        return render(request,'pages/profile/signinarab.html')        

def profile(request):
    fname=None
    username=None
    phone=None
    password=None
    confirmpsw=None
    city=None
    gender=None
    email=None
    context=None
    if request.user.is_authenticated:
        customer=students.objects.get(user=request.user)
        context= {
        'city':customer.city,
        'user':request.user.username,
        'pass':request.user.password,
        'email':request.user.email,
        'fname':customer.name,
        'phone':customer.phone,
    }
        if request.method=='POST' and 'btnsave' in request.POST and 'agree' in request.POST:
            fname=request.POST['fname']
            username=request.POST['user']
            phone=request.POST['phon']
           
            password=request.POST['password']
            confirmpsw=request.POST['conpsw']
            city=request.POST['city']
            email=request.POST['mail']
          
           
            if fname and username and phone and city and password and email and confirmpsw :
                customer.name=fname
                customer.phone=phone
                customer.city=city
                if password != confirmpsw:
                    messages.info(request,'passwords are not equal')
                elif not password.startswith('pbkdf2_sha256$'):
                     request.user.set_password(password)
                    

                
                
                request.user.save()
                customer.save()
                messages.success(request,'your data has been saved')
    else:
         messages.success(request,'you must loggin to edit your profile')
        
         return render(request,'pages/profile/profile.html',context)

    return render(request,'pages/profile/profile.html',context)
    if request.method=='POST' and 'btnsave' in request.POST:
            fname=request.POST['fname']
            username=request.POST['user']
            phone=request.POST['phone']
            city=request.POST['city']
            password=request.POST['pass']
            email=request.POST['email']
            confirm=request.POST['confirmpass']
            gender=request.POST['gender']
            if fname and username and phone and city and password and email and confirmpassword and gender:
                if request.user.is_authenticated and 'agree' in request.POST:
                    pass
    
#def rest(request):
    #data = customers.objects.all()
    #response={
    #'customer':list(data.values())
    #}
    return JsonResponse(response)
def logout(request):
    auth.logout(request)
    return redirect('index')
#@api_view(['GET','POST'])
# def getdata(request):
   
    #if request.method=='GET':
        #customer=customers.objects.all()
        #serializer=customersserializer(customer,many=True)
        #return Response(serializer.data)
    #elif request.method=='POST':
        #serializer=customersserializer(data= request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data,status=status.HTTP_201_CREATED)
        #return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

#@api_view(['GET','PUT','DELETE'])
#def getdatapk(request,pk):
    #try:
      #  customer=customers.objects.get(pk=pk)
  #  except customer.DOSENOTEXISTS:
            #return Response(status=status.HTTP_404_NOT_FOUND)

   # if request.method=='GET':
       # serializer=customersserializer(customer)
        #return  Response(serializer.data)

    #elif request.method=='PUT':
        #serializer=customersserializer(customer,data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data,status.HTTP_202_ACCEPTED)
        #return Response(serializer.data,status.HTTP_400_BAD_REQUEST)
    #elif request.method=='DELETE':
        #serializer=customersserializer(data=request.data)
        #if serializer.is_valid():
            #serializer.delete()
            #return Response(status=status.HTTP_204_NO_CONTENT)
#class cbv(APIView):
   # def get(self,request):
       # customer=customers.objects.all()
       # serializer=customersserializer(customer,many=True)
        #return Response(serializer.data,status=status.HTTP_200_OK)

    #def post(self,request):
        #customer=customers.objects.all()
        #serializer=customersserializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data ,status=status.HTTP_201_CREATED)
        #return Response(serializer,status=status.HTTP_400_BAD_REQUEST)
#class cbv_pk(APIView):
        #def get(self,request,pk):
           # customer=customers.objects.get(pk=pk)
            #serializer=customersserializer(customer)
            #return Response(serializer.data,status=status.HTTP_200_OK)
       # def put(self,request,pk):
           # customer=customers.objects.get(pk=pk)
           # serializer=customersserializer(customer,data=request.data)
            #if serializer.is_valid():
               # serializer.save()
                #return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            #return Response(status=status.HTTP_400_BAD_REQUEST)
       #def delete(self,request,pk):
            #customer=customers.objects.get(pk=pk)
            
            #customer.delete()
            #return Response(status=status.HTTP_204_NO_CONTENT) 
#class mixinapi(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
        #queryset=customers.objects.all()
        #serializer_class=customersserializer

        #def get(self,request):
            #return self.list(request)
        #def post(self,request):
            #return self.create(request)
#class mixiapipk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    #queryset=customers.objects.all()
    #serializer_class=customersserializer
    #def get(self,request,pk):
        #eturn self.retrieve(request)
    #def put(self,request,pk):
       # return self.update(request)
    #def delete(self,request,pk):
        #return self.destroy(request)

#class genericlist(generics.ListCreateAPIView):
     #queryset=customers.objects.all()
     #serializer_class=customersserializer
     #authentication_classes=[TokenAuthentication]
     #permission_classes=[IsAuthorizedOrReadonly]

#class genericlistapi(generics.RetrieveUpdateDestroyAPIView):
     #queryset=customers.objects.all()
     #serializer_class=customersserializer
     #authentication_classes=[TokenAuthentication]
     #permission_classes=[IsAuthorizedOrReadonly]

#class view_set(viewsets.ModelViewSet):
     #queryset=customers.objects.all()
     #serializer_class=customersserializer
#class post(generics.ListCreateAPIView):
   # permission_classes=[IsAuthorizedOrReadonly]
    #queryset=Post.objects.all()
   # serializer_class=postserializer

#class post_pk(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes=[IsAuthorizedOrReadonly]
    #queryset=Post.objects.all()
    #serializer_class=postserializer




    

def pizza(request):
    return render(request,'pages/product/pizza.html')


   
   



def about(request):
    return render(request,'pages/product/about.html')







