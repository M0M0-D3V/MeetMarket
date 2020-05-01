from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register_page),
    path('register_submit', views.register),
    path('login_submit', views.log_in),
    path('dashboard', views.successful_log_in),
    path('admin_controls', views.admin_controls),
    path('user/edit_user/<int:user_id>', views.edit_user),
    path('admin_controls/post_edit_user/<int:user_id>', views.post_edit_user),
    path('user/delete_user/<int:user_id>', views.delete_user),
    path('admin_controls/post_new_cat', views.post_new_cat),
    path('admin_controls/edit_category/<int:category_id>', views.edit_category),
    path('admin_controls/post_edit_cat/<int:category_id>',
         views.post_edit_category),
    path('admin_controls/delete_category/<int:category_id>',
         views.delete_category),
    path('category/delete_category/<int:category_id>', views.delete_category),
    path('direct_message', views.direct_message),
    path('logout', views.log_out),

]
