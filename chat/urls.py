from django.urls import path, re_path

from .views import ChannelDetailView, private_messages, DetailMs, Inbox

UUID_CANAL_REGEX = r'channel/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'
# app_name = 'worktions'
urlpatterns= [
    re_path(UUID_CANAL_REGEX, ChannelDetailView.as_view() ),
    path("chat/<str:username>", private_messages),
    path("ms/<str:username>", DetailMs.as_view(), name="detailms"),
    path("inbox", Inbox.as_view(), name="inbox")
]