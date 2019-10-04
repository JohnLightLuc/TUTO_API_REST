
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')
# router.register('choise', PollViewSet, base_name='choise')



urlpatterns = [
    # ...
]

urlpatterns += router.urls

# from django.urls import path
# from .apiviews import PollList, PollDetail, ChoiceList, CreateVote # ...

# urlpatterns = [
#     path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
#     path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

# ]