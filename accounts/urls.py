from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router  = DefaultRouter()

router.register(r'purchase-order', PurchaseOrderView, basename='purchase-order')
router.register(r'purchase-memo', PurchaseMemoView, basename='purchase-memo')
router.register(r'item', ItemView, basename='item')


urlpatterns = [
    path('', RegisterUserView.as_view(), name='register'),
    path('send_invite_mail', InviteUserViaEmailView.as_view(), name='send_invite_mail'),
    path('register-via-invite', RegisterInviteUserView.as_view(), name='regsiter_via_invite'),
    path('login', LoginView.as_view(), name='login'),
    path('employee-login', LoginView.as_view(), name='login'),
    # path('purchase-order', PurchaseOrderView.as_view(), name='purchase-order'),
]


urlpatterns += router.urls