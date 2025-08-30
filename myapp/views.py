from django.shortcuts import render
from myDjangoCelery.celery import add
from myapp.tasks import sub
from celery.result import AsyncResult
# Create your views here.

#  using delay
# def home(request):
#     result1 = add.delay(10,20)
#     result2  =sub.delay(80 ,70)
#     return render(request , 'app/home.html' ,{'result':result1})

# using apply_sync()
def home(request):
    result = add.apply_async(args=[10,20])
    # result2  =sub.apply_async(args=[80 ,70])
    return render(request , 'app/home.html' ,{'result':result})


def result(request , id):
    result = AsyncResult(id)
    return render(request , 'app/result.html' , {'result':result} )


def about(request):
    return render(request , 'app/about.html')

def contact(request):
    return render(request , 'app/contact.html')