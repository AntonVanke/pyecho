from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    后台管理首页
    :param request:
    :return:
    """
    # 判断是否登录了，如果没有登录，返回到登录页面
    # 如果登录了，则进入后台管理页面
    return HttpResponse("OK")


def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    # 如果是 Get 请求，返回用户登录界面
    # 如果是 POST 请求则判断用户密码是否正确
    if request.method == 'GET':
        page = {
            "title": "用户登录",
        }
        return render(request, "Admin/login.html", locals())
    else:
        # username 用户名， password 用户密码
        username = request.POST.get("UserName")
        password = request.POST.get("PassWord")
        return HttpResponse("OK")


def register(request):
    """
    用户注册
    :param request:
    :return:
    """
    # 如果是 Get 请求，返回用户注册
    # 如果是 POST 请求则判断注册内容是否符合要求
    if request.method == 'GET':
        page = {
            "title": "用户注册",
        }
        return render(request, "Admin/register.html", locals())
    else:
        # 判断用户名是否重复
        # 判断密码强度是否足够
        # 判断密码与确认密码是否一致
        username = request.POST.get("UserName")
        password = request.POST.get("PassWord")
        email = request.POST.get("Email")
        telnumber = request.POST.get("TelNumber")
        return HttpResponse("ok")


def forget(request):
    """
    忘记密码
    :param request:
    :return:
    """
    if request.method == 'GET':
        page = {
            "title": "忘记密码",
        }
        return render(request, "Admin/forget.html", locals())
    else:
        # 判断用户名是否重复
        # 判断密码强度是否足够
        # 判断密码与确认密码是否一致
        return HttpResponse("暂未开放")
