from django.conf.urls import include, url
from django.contrib import admin
#from django.conf.urls import handler404
#from webBomberos.views import mi_error_404

#handler404 = mi_error_404

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('webBomberos.urls')),
]
