from django.contrib import admin
from django.urls import path

from . import views
from .views.home import Index, store, store1
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView, some_view
from .views.contactus import contactus
from .views.aboutus import aboutus
from .views.webuild import webuild
from .views.team import team
from .views.product import product
from .views.lenses import lenses
from .views.product import product
from .views.userprofile import userprofile
from .views.feedback import feedback
from .views.forgetpassword import forgetpassword
from .middlewares.auth import auth_middleware
from .views.employeesignup import EmpSignup
from .views.empdash import empdash

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store, name='store'),
    path('store1', store1, name='store1'),

    path('contactus', contactus.as_view(), name='contactus'),
    path('userprofile', userprofile.as_view(), name='userprofile'),
    path('feedback', feedback.as_view(), name='feedback'),
    path('lenses', lenses, name='lenses'),
    path('aboutus', aboutus, name='aboutus'),
    path('webuild', webuild, name='webuild'),
    path('some_view', some_view, name='some_view'),
    path('product', product, name='product'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('forgetpassword', forgetpassword.as_view(), name='forgetpassword'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('empsignup', EmpSignup.as_view(), name='empsignup'),
    path('empdash', empdash, name='empdash'),
    path('team',team, name='team'),
]
