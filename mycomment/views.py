from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from mycomment.models import head_comment, comment
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import loader, RequestContext
from mycomment.common_response import LoginDataView
from mycomment.decorator import login_decorator


is_login = False
# 首页
# Param:
# Todo
# return head_comment_list,login_data
#@Test3
class home(LoginDataView):
    def get(self, request):
        data = self.login_data
        data["head_comment_list"] = head_comment.objects.all()
        return render(request, "home.html", data)
    

# 登录
def login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = auth.authenticate(username = u,password = p)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("login failed")
    elif request.method == 'GET':
        return render(request, 'login.html')
    else:
        return HttpResponse("error")

# 退出
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

# 发布
def post(request):
    if request.method == 'POST':
        tags = request.POST['tags']
        t = request.POST['title']
        content = request.POST['content']
        if request.user.is_authenticated:
            head_comment.objects.create(tags = tags, title = t, content = content, user = request.user)
            return HttpResponse("title:"+t+" tags:"+tags+" content:"+content+" 发帖成功！")
        else:
            return HttpResponse("先登录下")
    elif request.method == 'GET':
        return render(request, 'post.html')
    else:
        return HttpResponse("method error")

# 注册
def register(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        email = request.POST['email']
        r_p = request.POST['rpassword']
        try:
            user = User.objects.create_user(username = u, password = p, email = email)
        except:
            return HttpResponse("user existed!")
        if user is not None:
            return HttpResponse("register success")
        else:
            return HttpResponse("register failed")
    elif request.method == 'GET':
        return render(request, 'register.html')
    else:
        return HttpResponse("method error")

# posts展示页面
def posts(request, id):
    try:
        h = head_comment.objects.get(id=id)
        comments = comment.objects.filter(father = h.id)
        comment_data = \
            [[comment.user, comment.content, comment.thumb_up.count(), comment.thumb_down.count()] \
            for comment in comments]
        return render(request, "comment.html", 
            {"h": h,
            "thumb_data": [h.thumb_up.count(), h.thumb_down.count()], 
            "comment_data": comment_data
            })
    except Exception as e:
        return HttpResponse(str(e))

#提交评论
def comments(request):
    if request.method == "POST":
        content = request.POST['content']
        father_id = request.POST['father_id']
        father = head_comment.objects.get(id = father_id)
        comment.objects.create(content = content, user = request.user, father = father)
        return HttpResponseRedirect("/posts-"+father_id)
    else:
        return HttpResponse("404")

def ajax_test(request):
    return HttpResponse("3")

@login_decorator
def test(request, data):
    return HttpResponse("test",data)
