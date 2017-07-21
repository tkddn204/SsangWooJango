from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from applications.memo.serializers import BbsSerializer
from rest_framework import generics

from applications.memo.models import Memo, Bbs


# 메인 페이지
def index(request):
    return HttpResponse("Hello, world!")


# 메모 리스트 페이지
class MemoList(ListView):
    model = Memo


# 메모 디테일 페이지
class MemoDetail(DetailView):
    model = Memo


# generics 에 목록과 생성 API 가 정의되어 있다
class BbsList(generics.ListCreateAPIView):
    queryset = Bbs.objects.all()
    serializer_class = BbsSerializer


# generics 에 상세, 수정, 삭제 API가 정의되어 있다
class BbsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bbs.objects.all()
    serializer_class = BbsSerializer
