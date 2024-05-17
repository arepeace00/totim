from django.shortcuts import render
from subproject_totim.models import Student,SHobby, Mentor
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
    displaydata = Mentor.objects.all().values()
    context = {
        'lastname' : 'Aryan FIrazz',
         'displaydata' : displaydata
    }
    return render (request,'index.html',context)

def newmentor(request):
    displaydata = Mentor.objects.all().values()
    if request.method == 'POST' :
        menid1=request.POST['mentorid']
        menname1 =request.POST['mentorname']
        menroomno1=request.POST['mentorroomno']
        data =Mentor(menid=menid1,menname=menname1,menroomno=menroomno1)
        data.save()

        context = {
         'displaydata' : displaydata,
         'message' : 'NEW MENTOR HAS BEEN SAVE'
        }

        return render (request,'newmentor.html',context)
    else :
       dict = {
         'displaydata' : displaydata,
         'message' : ''
        }
        
    return render (request,'newmentor.html',dict)

def newstudent(request):
    stumentor1 = Student.objects.all().values()
    mymentor = Mentor.objects.all().values()

    if request.method == 'POST' :
        stuid=request.POST['stuid']
        stuname =request.POST['stuname']
        stuemail=request.POST['stuemail']
        stuage=request.POST['stuage']
        menid1= request.POST['selectmenid']
        mentornew = Mentor.objects.get(menid=menid1)
        data =Student(studid=stuid,stuname=stuname,stuemail=stuemail,stuage=stuage,stumentor=mentornew)
        data.save()

        context = {
         'stumentor' : stumentor1,
         'mymentor' : mymentor,
         'message' : 'NEW STUDENT HAS BEEN SAVE'
        }

        return render (request,'newstudent.html',context)

    else:
         dict = {
         'stumentor' : stumentor1,
         'mymentor' : mymentor,
         'message' : ''
        }
         
         return render (request,'newstudent.html',dict)
    
def update(request,menid):
    updateid = Mentor.objects.get(menid=menid)
    dict = {
        'updateid' : updateid
    }
    return render (request,'update.html',dict)

def updatedata(request,menid):
    data=Mentor.objects.get(menid=menid)
    menname=request.POST['mentorname']
    menroomno =request.POST['mentorroomno']
    data.menname=menname
    data.menroomno = menroomno
    data.save

    return HttpResponseRedirect(reverse("newmentor"))

def viewdelete(request,menid):
    datanakdelete = Mentor.objects.get(menid=menid)
    dict = {
        'datatobedeleted' : datanakdelete
    }
    return render (request,'delete.html',dict)

def delete(request,menid):
    deletementor=Mentor.objects.get(menid=menid)
    deletementor.delete()
 
    return HttpResponseRedirect(reverse("newmentor"))