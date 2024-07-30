from django.urls import path

from. import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('user_dashboard/', views.userDashboard, name='user_dashboard'),
    path('quotation_request/', views.userquotation_request, name='quotation_request'),
    path('user_bids/', views.user_bids, name='user_bids'),
    path('report/', views.report, name='report'),
    path('download/specification/<int:quotation_id>/', views.download_specification, name='download_specification'),
    path('download/boq/<int:quotation_id>/', views.download_boq, name='download_boq'),
    path('download/attachement/<int:supplier_bid>/', views.download_attachement, name='download_attachement'),
    path('download/supplier/boq/<int:supplier_bid>/', views.download_supplier_boq, name='download_supplier_boq'),
    path('request_detail/<int:quotation_id>/', views.request_detail, name='request_detail'),
    path('send/', views.send_quotation, name='send'),
    path('signup/',views.signup, name='signup' ),
    path('supplier_dashboard/',views.supplier_dashboard, name='supplier_dashboard' ),
    path('bid_history/',views.bid_history, name='bid_history' ),
    path('bid/',views.bid, name='bid' ),
    path('suppliers_bids/<int:quotation_request_id>/',views.view_suppliers_bids, name='suppliers_bids' ),
    path('bids_line/<int:quotation_request_id>/<int:supplier_bid_id>', views.view_bids_on_line, name='bids_line'),
    path('edit_request/id=<int:quotation_request_id>', views.edit_request, name='edit_request'),
    path('logout/', views.logout_view, name='logout'),
    path('user_profile/',views.user_profile, name='user_profile'),
    path('supplier_profile/',views.supplier_profile, name='supplier_profile'),
    path('view_bid_history/<int:quotation_line_id>', views.view_bid_history, name='view_bid_history'),
     path('download_bids_excel/<int:quotation_request_id>/<int:user_id>/', views.download_bids_excel, name='download_bids_excel'),
   path('generate-excel/<int:quotation_request_id>/', views.generate_price_comparison_excel, name='generate_price_comparison_excel'),

 
 
 
]