from django.conf.urls import include, url
from django.contrib import admin
from monitor import views as Monitor

urlpatterns = [
    # Examples:
    # url(r'^$', 'temp_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^monitor/senddata', Monitor.senddata),
]
