from django.shortcuts import render
from django.http import HttpResponse
# from django_comments.models import Comment


# def home(request):
#     com = Comment()
#     com.comment = "hello"
#     com.user_name = 'dy'
#     return render(request, 'home.html', {"com":com})


# def get_cookie(request):
#     if "favorite_color" in request.COOKIES:
#         return HttpResponse("cookie:"+request.COOKIES['favorite_color'])


# def set_cookie(request):
#     if "favorite_color" in request.GET:
#         response = HttpResponse("cookie:"+request.COOKIES['favorite_color'])
#         response.set_cookie("favorite_color",request.GET["favorite_color"])
#         return response
#     else:
#         response = HttpResponse()
#         response.set_cookie("favorite_color","blue")
#         return response


# def set_session(request):
#     if 'fav_color' in request.session:
#         return HttpResponse(request.session['fav_color'])
#     else:
#         request.session["fav_color"] = "blue"
#         return HttpResponse("no session")


# def get_session(request):
#     if 'fav_color' in request.session:
#         request.session["fav_color"] = "blue"
#         return HttpResponse(request.session['fav_color'])
#     else:
#         return HttpResponse("no session")