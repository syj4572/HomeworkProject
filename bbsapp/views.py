from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import  JsonResponse
from .models import MessageBoard

def cc(request) :
    writer = request.POST['writer']
    title = request.POST['title']
    content = request.POST['content']
    mdata = MessageBoard(writer=writer, title=title,content=content)
    mdata.save()
    return redirect("rrname")

def rr(request) :
    page = request.GET.get('page',1)
    mlist = MessageBoard.objects.all()
    paginator = Paginator(mlist[::-1],5)
    mlistpage = paginator.get_page(page)
    context = {"mlist":mlistpage}
    return render(request, 'news_crud.html', context)

def uu(request):
    if request.method == "POST" :
        pk = request.GET.get("pk")
        message = MessageBoard.objects.get(pk=pk)
        message.writer = request.POST['writer']
        message.title = request.POST['title']
        message.content = request.POST['content']
        message.save()
        return redirect("rrname")
    else :
        pk = request.GET.get("pk")
        message = MessageBoard.objects.get(pk=pk)
        message.cnt += 1
        message.save()

        jsonContent = {"writer" : message.writer, "title": message.title, "content": message.content, "cnt": message.cnt }
        return JsonResponse( jsonContent, json_dumps_params={'ensure_ascii':False})

def dd(request) :
    pk = request.GET['pk']
    message = MessageBoard.objects.get(pk=pk)
    message.delete()
    return redirect("rrname")
