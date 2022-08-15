from django.urls import path , include
from .import views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
#from rest_framework.routers import DefaultRouter
#from rest_framework.authtoken import views as tokenview

#router=DefaultRouter()
#router.register('klo',views.view_set),

urlpatterns = [
    path('',views.index, name="index"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logout,name="logout"),
    path('signin',views.signin,name="signin"),
    path('profile',views.profile,name="profile"),
    path('pizza',views.pizza,name="pizza"),
    path('flavor/<int:pro_id>',views.product,name="flavor"),
    path('about',views.about,name="about"),
    path('products',views.productss,name="products"),
    path('search',views.search,name="search"),
    path('addtocard',views.addtocard,name="addtocard"),
    path('mycard',views.mycard,name="mycard"),
    path(' <int:orderdetail_id>',views.remove_from_cart,name='remove_from_cart'),
     path('  <int:orderdetail_id>',views.add_to_quantity,name='add_to_quantity'),
          path('   <int:orderdetail_id>',views.sub_from_quantity,name='sub_from_quantity'),
          path('payment',views.paymentt,name="payment"),
          path('rest',views.rest,name="rest"),
          path('admin', admin.site.urls),
          path('generalsearch',views.generalsearch,name="generalsearch"),
         # path('datalist',views.getdata),
         # path('datalistpk/<int:pk>',views.getdatapk),
          #path('cbv',views.cbv.as_view()),
          # path('cbvpk/<int:pk>',views.cbv_pk.as_view()),
          # path('mixin1',views.mixinapi.as_view()),
           #path('mixins/<int:pk>',views.mixiapipk.as_view()),
           #path('ge1',views.genericlist.as_view()),
          # path('get2/<int:pk>',views.genericlistapi.as_view()),
            #path('klo',include(router.urls)),
            #path('tok',tokenview.obtain_auth_token),
             #path('post/<int:pk>',views.post_pk.as_view()),
             # path('post',views.post.as_view()),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)