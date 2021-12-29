from django.urls import path
from .views import (
    ItemDetailView,
    HomeView,
    Profile,
    add_to_cart,
    remove_from_cart,
    ShopView,
    OrderSummaryView,
    remove_single_item_from_cart,
    CheckoutView,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    CategoryView,
    PaymentSuccess,
    PaymentCancelled,
    PaymentError,
    ProductDetailView,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('', home, name='home'),
    path('profile/', Profile, name='profile'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment_success/',PaymentSuccess, name='pay_OK'),
    path('payment_cancelled/',PaymentCancelled, name='pay_Cancel'),
    path('payment_error/',PaymentError, name='pay_Error'),

    path('category/<slug>/', CategoryView.as_view(), name='category'),
    
    #path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('product/<int:id>/', ProductDetailView, name='product'),
    #Changing to a function view to add the form
    #path('product/<slug>', ProductDetailView, name='product'),
    #/<int:id>/
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
