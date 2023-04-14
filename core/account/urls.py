# registration
# login
# logout
# reset pass
# forgot pass
from django.urls import path, include

app_name = 'account'

urlpatterns = [

    path('api/', include('account.api.urls')),

]
