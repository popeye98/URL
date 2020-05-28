
from django.urls import path,include
from shortner.views import kirr_redirect_view,KirrCBView,HomeView
from . import views
urlpatterns = [
    path('', HomeView.as_view()),
    #path('a/<str:sc>',views.kirr_redirect_view,name="Home"),
    path('<str:sc>',views.KirrCBView.as_view(),name='scode'),

]