"""
URL configuration for Shop product.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Shop import settings
from product import views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('products/', views.products_view),
    path('products/<int:id>/', views.products_detail_view),
    path('products/create/', views.product_create_view),

    path('categories/', views.categories_view),
    path('users/register/', users_views.register_view),
    path('users/login/', users_views.login_view),
    path('users/logout/', users_views.logout_view)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
