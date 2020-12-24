from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from Admin import models


def index(request):
    """
    后台管理首页
    :param request:
    :return:
    """
    # TODO: 判断是否登录了，如果没有登录，返回到登录页面
    # TODO: 如果登录了，则进入后台管理页面
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
        # TODO: 判断用户名是否存在 且 用户密码正确
        if len(models.Users.objects.filter(username=username)) != 0 and models.Users.objects.filter(
                username=username).first.password == password:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("账号或密码错误")


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
        # TODO: 判断用户名是否重复
        # TODO: 判断密码强度是否足够
        # TODO: 判断密码与确认密码是否一致
        # TODO: 密码加密存入数据库 或者在 前端加密
        username = request.POST.get("UserName")  # 用户名
        password = request.POST.get("PassWord")  # 密码
        screenname = request.POST.get("ScreenName")  # 昵称
        email = request.POST.get("Email")  # 电子邮箱
        models.Users.objects.create(username=username, password=password, screenName=screenname, email=email)
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
        # TODO: 判断用户名是否重复
        # TODO: 判断密码强度是否足够
        # TODO: 判断密码与确认密码是否一致
        return HttpResponse("暂未开放")


def test_ajax(request):
    print(request.POST)
    if request.method == "POST":
        data = {
            "code": 200,
            "msg": "OK",
            "data": {
                "message": "注册成功"
            }
        }
        return JsonResponse(data)
    else:
        data = {
            "code": 404,
            "msg": "NOT FOUND",
            "data": {
            }
        }
        return JsonResponse(data)
