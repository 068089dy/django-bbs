from django.shortcuts import HttpResponse

def login_decorator(func):
    def wrapper(*args, **kw):
        if args[0].user.is_authenticated:
            args[1] = 1
        else:
            args[1] = 2
        return func(*args, **kw)
    return wrapper