from django.urls import path
from demo import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views 

urlpatterns = [
    # ///////////////////////////////
    path('myhome/', views.index, name='index'),
    path('post/<int:x>/', views.post, name='post'),
    path('posts/', views.posts, name='posts'),
    path('add/', views.add, name='add'),
    path('products/' ,views.products,name="products"),
    path('product/<p_id>/', views.product, name='product_details'),
    path('add_product/',views.add_product,name="add_product"),
    path('product_del/<p_id>/',views.del_product,name="product_del"),
    path('del_comment/<c_id>/',views.del_comment,name="del_comment"),
    path('product_edit/<p_id>/',views.product_edit,name="product_edit"),
    path('signup/',views.register,name="signup"),
    path('logout/',views.logout_user,name='logout'),
    path('login/',views.login_user,name='login'),
    path("fav/",views.fav,name="fav"),
    path("counter/" ,views.counter ,name="counter")
    # path('posts/',TemplateView.as_view(template_name="products.html"), name='posts')
    # ///////////////////////////////

]