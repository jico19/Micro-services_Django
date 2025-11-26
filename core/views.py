from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from google import genai
from .serializer import UserInputSerializer

client = genai.Client()


class SampleView(APIView):
    # make this asynchrounous function later
    def get(self, request):
        
        res = client.models.generate_content(
            model="gemini-2.5-flash",     
            contents="do you know 67? like the meme?"
        )
        
        return Response({"message": res.text})