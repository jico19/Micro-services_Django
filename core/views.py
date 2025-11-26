from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google import genai
from .serializer import UserInputSerializer

client = genai.Client()


class SampleView(APIView):
    serializer_class = UserInputSerializer 
    
    # make this asynchrounous function later
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            validated_data = serializer.validated_data
            user_input = validated_data.get('input')
            
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input,
            )
            
            return Response({"chatbot response": response.text})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)