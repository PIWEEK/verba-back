from django.conf.urls import url, include
from quotes import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tags', views.TagViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'quotes', views.QuoteViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]
