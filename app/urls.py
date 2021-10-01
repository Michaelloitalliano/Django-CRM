from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

router = routers.SimpleRouter()
router.register(r'company', CompanyView, basename='company')
router.register(r'employee', EmployeeView)
router.register(r'partnership', PartnershipView)
urlpatterns = [
    # path('api/company/create/', CompanyView.as_view({'post': 'create'}), name='company_create'),
    # path('api/company/list/', CompanyView.as_view({'get': 'list'}), name='company'),
    
    # path('api/employee/list/', EmployeeView.as_view({'get': 'list'}), name='employee'),

    # path('api/partnership/create/', PartnershipView.as_view({'post': 'create'}), name='partnership_create'),
    # path('api/partnership/list/', PartnershipView.as_view({'get': 'list'}), name='partnership'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('auth/', include('rest_framework.urls'))
]
urlpatterns += router.urls