from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # API
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/v1/", include("snippets.urls")),
    # Auth for browsable API
    path("auth/", include("rest_framework.urls")),
    # Django admin
    path("admin/", admin.site.urls),
]
