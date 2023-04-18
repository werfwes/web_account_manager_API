from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from .models import TwitterAccounts
from .serializers import TwitterSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
def index_page(request):
    return render(request, 'index.html')


class GetTwitterAPIView(generics.ListAPIView):
    # ЛОГИКА ЗДЕСЬ!
    queryset = TwitterAccounts.objects.all()
    serializer_class = TwitterSerializer


class TwitterSendAccountAPI(APIView):
    def post(self, request):
        try:
            post_new = TwitterAccounts.objects.create(
                login=request.data['login'],
                password=request.data['password'],
                email=request.data['email'],
                phone=request.data['phone'],
                is_crypto=request.data['is_crypto']
            )
            return Response({
                'status': 'OK',
                'post': model_to_dict(post_new)
            })
        except KeyError as e:
            return Response({
                'status': 'FAIL',
                'exception': f'Key Error ({str(e)})'
            })
        except Exception as e:
            return Response({
                'status': 'FAIL',
                'exception': str(e)
            })
