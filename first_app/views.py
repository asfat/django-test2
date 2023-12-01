from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d ={ 'author':'Rahim','age':10,'lst':['python','is','best'],'birthday':datetime.datetime.now(), 'courses':[
        {
            'id':1,
            'name':"django",
            'fee':1000
        },
        {
            'id':2,
            'name':"python",
            'fee':1200
        },
        {
            'id':3,
            'name':"html",
            'fee':1500
        }
    ],
        
    }
    return render(request,'home.html',context=d)