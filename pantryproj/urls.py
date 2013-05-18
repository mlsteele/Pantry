from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# RESTframework
from pantry.models import Grocery
from rest_framework import viewsets, routers

# admin
admin.autodiscover()

# REST
class GroceryViewSet(viewsets.ModelViewSet):
    model = Grocery

rest_router = routers.DefaultRouter()
rest_router.register(r'grocerys',  GroceryViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pantryproj.views.home', name='home'),
    # url(r'^pantryproj/', include('pantryproj.foo.urls')),

    # rest api
    url(r'^API-REST-1/', include(rest_router.urls)),

    # pantry
    url(r'^test1$', 'pantry.views.test1'),
    url(r'^$', 'pantry.views.grocerys'),

    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += staticfiles_urlpatterns()
