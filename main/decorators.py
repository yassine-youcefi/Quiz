
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func():

            groupe = None
            if request.user.groups.exist():
                groupe = request.user.groups.all()[0].name
            if groupe in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized')
        return wrapper_func
    return decorator  