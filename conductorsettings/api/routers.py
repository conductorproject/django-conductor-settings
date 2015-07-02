from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"collections", views.CollectionViewSet)
router.register(r"servers", views.ServerViewSet)
router.register(r"serverschemes", views.ServerSchemeViewSet)
router.register(r"resources", views.ResourceViewSet)
router.register(r"getlocations", views.GetLocationViewSet)
router.register(r"postlocations", views.PostLocationViewSet)
router.register(r"findlocations", views.FindLocationViewSet)
