def logindata_response(request):
    if request.user.is_authenticated:
        return {"login_data":[request.user.username, "logout"],}
    else:
        return {"login_data":["login", "register"],}

from django.views.generic import View

class LoginDataView(View):
    
    def __init__(self):
        View.__init__(self)

    def dispatch(self, request):
        if request.user.is_authenticated:
            self.login_data = {"login_data": [request.user.username,'logout']}
        else:
            self.login_data = {"login_data":["login", "register"],}
        return self.get(request)