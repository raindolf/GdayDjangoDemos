from django.conf.urls import patterns, include, url
from demo1.views import hello
from demo1.views import welcome

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',

url(r'^hello/', hello),
url(r'^welcome/', welcome),
    # Examples:
    # url(r'^$', 'demo1.views.home', name='home'),
    # url(r'^demo1/', include('demo1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url(r'^admin/', include(admin.site.urls)),
)
