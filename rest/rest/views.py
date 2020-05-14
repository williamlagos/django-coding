from django.contrib.auth.models import User

from .mixins import HybridDetailView, HybridListView

class UsersDetailView(HybridDetailView):
    
    model = User

class UsersListView(HybridListView):

    model = User
