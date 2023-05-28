from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from news import models
from news.api import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

# Refresh TokenObtainPairView (add user)
class AuthorizateView(TokenObtainPairView):
    serializer_class = serializers.AuthorizateSerializer
    
class RegistrationAPIView(generics.GenericAPIView):
    
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegistrationSerializer




    def post(self, request):
        # Паттерн создания сериализатора, валидации и сохранения - довольно
        # стандартный, и его можно часто увидеть в реальных проектах.
        serializer = self.get_serializer(data=request.data)  
        serializer.is_valid(raise_exception=True)


        serializer.save()
        user=models.Author.objects.get(email=serializer.data['email'],)
        refresh = RefreshToken.for_user(user)
        return Response({'user':serializer.data,      
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    }, status=status.HTTP_201_CREATED)




class WeddingListCreateAPIVew(APIView):
    serializer_class = serializers.WeddingSerilizer
    permission_classes = (AllowAny,)
    
    def get(self, request):
        articles = models.Wedding.objects.all()
        serializer = serializers.WeddingSerilizer(articles, many=True)
        return Response(serializer.data)

   
class WeddingPostNews(generics.GenericAPIView):
    serializer_class = serializers.WeddingSerilizer
    permission_classes = (AllowAny,)
    
    def post(self,request):
        # Паттерн создания сериализатора, валидации и сохранения - довольно
        # стандартный, и его можно часто увидеть в реальных проектах.
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
       
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
  
          
    