from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'categories'
urlpatterns = [
    path('add/', views.add_category, name='add_category'),
    path('list/', views.categories_list, name='list_categories'),

]
urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)