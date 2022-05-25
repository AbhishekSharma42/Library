from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import json 

# Create your views here.

def Index(request):
        return render(request,"Index.html");


def saveBook(request):
        try:
                bookname = request.GET['name']
                bookPrize = request.GET['prize']
                book_page = request.GET['page']
                if bookname=="" or bookPrize == "" or book_page =="":
                        return HttpResponse("All fill required...")
                else:
                        data = Uploade(BookName = bookname, prize = bookPrize , pages = book_page)
                try:
                        data.save()
                        return HttpResponse("true")
                except:
                        return HttpResponse("false")
        except:
                pass
   
def jsondata(request):
        ls = list()
        d = Uploade.objects.all()
        for i in d :
                seri = BookSerializer(i)
                ls.append(seri.data);
        #         print(seri.data)
        # print(ls)
        return HttpResponse(json.dumps(ls))