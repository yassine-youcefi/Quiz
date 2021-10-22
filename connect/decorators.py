from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect


# def unauthenticated_user(view_func):
#     def wrapper_func(request,*args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('main:index')
#         else:
#             return view_func(request *args, **kwargs)    

#     return wrapper_func   


         