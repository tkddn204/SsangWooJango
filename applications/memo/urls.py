from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MemoList.as_view(), name='memo_list'),
    url(r'^(?P<pk>\d+)/$', views.MemoDetail.as_view(), name='memo_detail'),
    url(r'^bbs/$', views.BbsList.as_view(), name="bbs"),
    url(r'^bbs/(?P<pk>\d+)/$', views.BbsDetail.as_view(), name='bbs_detail'),
]
