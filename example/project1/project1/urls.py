from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'app1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^payment/', 'app1.views.payment', name='payment'),
    url(r'^response/', 'app1.views.response', name='response'),
    url(r'^admin/', include(admin.site.urls)),
]
