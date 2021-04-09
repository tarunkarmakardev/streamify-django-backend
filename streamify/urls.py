from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('streamify/api/', include('accounts.urls')),
    path('streamify/api/streams/', include('streams.urls'))
    # path('admin/', include('core.urls')),
]
