from django.urls import path, include
from django_web import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index_view, name='index_view'),  # index
    path('django_web/', include('django_web.urls')),  # hello

]
