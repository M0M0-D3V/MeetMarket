from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_item', views.new_item),
    path('item/<int:item_id>', views.item_info),
    path('category/<int:category_id>', views.category_page),
    path('user/<int:user_id>', views.user_page),
    path('create_item', views.create_item),
    path('item/<int:item_id>/edit', views.edit),
    path('post_edit/<int:item_id>', views.post_edit),
    path('item/<int:item_id>/delete', views.delete),
    path('new_review', views.new_review),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
    path('all_listings', views.all_listings),
    path('flag_item/<int:item_id>', views.flag_item),
    path('admin_flag_control/<int:item_id>', views.admin_flag_control),
    path('all_categories', views.all_categories),
]
