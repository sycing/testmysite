from django.shortcuts import render
from django.http import HttpResponseRedirect
from fxtweb.models import VqTestcase as vt
from fxtweb.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import forms
import os
# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()


def home(request):
    #string =vt.objects.all()
    string=vt.objects.order_by('-tcno')
    aaa=[]
    ccc=vt.objects.values('interfaceid').distinct()
    for i in ccc:
        aaa.append(i['interfaceid'])

    if request.method == "POST":
        upload_file(request)
        # uf = UserForm(request.POST, request.FILES)
        # if uf.is_valid():
        #     if uf.is_valid():
        #         # 获取表单信息
        #         username = uf.cleaned_data['username']
        #         headImg = uf.cleaned_data['headImg']
        #         # 写入数据库
        #         user = User()
        #         user.username = username
        #         user.headImg = headImg
        #         user.save()
        #         return HttpResponse('upload ok!')
        # else:
        #      uf = UserForm()
    # return render(request, 'home.html', {'string':string, 'bbb':aaa,'uf':uf})
    return render(request, 'home.html', {'string': string, 'bbb': aaa})
def interfaceId(request):

    dOptions=vt.objects.filter(interfaceid='Login')
    return render(request, 'home.html', {'dOptions':dOptions})
def search(request):
    # infaceids=request.GET.copy()
    # infaceid=infaceids['id']
    infaceid = request.GET['id']


    if request.method == "POST":
        # uf = UserForm(request.POST, request.FILES)
        # if uf.is_valid():
        #     if uf.is_valid():
        #         # 获取表单信息
        #         username = uf.cleaned_data['username']
        #         headImg = uf.cleaned_data['headImg']
        #         # 写入数据库
        #         user = User()
        #         user.username = username
        #         user.headImg = headImg
        #         user.save()
        #         return HttpResponse('upload ok!')
        # else:
        #     uf = UserForm()
        upload_file(request)

    if infaceid=="" or infaceid=="all":
        return HttpResponseRedirect("/")
    else:
        testcase = vt.objects.filter(interfaceid=infaceid)
        aaa = []
        ccc = vt.objects.values('interfaceid').distinct()
        for i in ccc:
            aaa.append(i['interfaceid'])
        # return render_to_response('home.html', {'string':testcase, 'bbb':aaa, 'ccc':infaceid,'uf':uf})
        return render_to_response('home.html', {'string': testcase, 'bbb': aaa, 'ccc': infaceid})

def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        # print(myFile)
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("upload",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        # print(destination.read())
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        uploadfilepath=os.path.join("upload",myFile.name)
        user=User()
        user.username=myFile.name
        user.headImg=uploadfilepath
        # user.save()
    # return HttpResponse("upload over!")