from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('base.urls')),
    path('miembros/', include('django.contrib.auth.urls')),
    path('miembros/', include('miembros.urls')),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls)),
    )
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]