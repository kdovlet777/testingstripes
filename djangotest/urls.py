from django.urls import path
from items.views import buy_item, item_detail
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:id>/', buy_item, name='buy_item'),
    path('item/<int:id>/', item_detail, name='item_detail'),
] 