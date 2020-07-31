from django.urls import path
from reg.views import log,logBackend,register,register_backend,logout_backend
app_name="reg"
urlpatterns = [
    path('log/', log,name='log'),
    path('logBackend/',logBackend,name='logBackend'),
    path('register/', register,name='register'),
    path('register_backend/', register_backend,name='register_backend'),
    path('logout_backend/',logout_backend,name='logout_backend'),
    
]
