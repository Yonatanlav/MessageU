from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from messageU.router import router



urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/auth/login/$', obtain_jwt_token, name='api-login'),
    url(r'^api/', include(router.urls))
    
]

urlpatterns += [
    url(r'', include(router.urls)),
    
]