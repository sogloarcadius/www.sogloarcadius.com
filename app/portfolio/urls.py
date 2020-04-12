
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns



urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'^', include('apps.core.urls', namespace="core")),
    url(r'^admin/', admin.site.urls),
    prefix_default_language=True
)

urlpatterns += [
    url(r'^api/', include('apps.core.urls', namespace="core")),
    url(r'^api/', include('apps.users.urls', namespace="users")),
    url(r'^api/', include('apps.projects.urls', namespace="projects")),
    url(r'^api/', include('apps.resume.urls', namespace="resume")),
    url(r'^api/', include('django_prometheus.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
