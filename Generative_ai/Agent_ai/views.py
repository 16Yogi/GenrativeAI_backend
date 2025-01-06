from .models import user
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from anthropic import Anthropic
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import ToolNode
from langgraph.graph import END, StateGraph, MessagesState
# from langgraph.checkpoint import MemorySaver
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic
from langchain_anthropic import AnthropicLLM
from django.views.decorators.cache import cache_page
import logging
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from langchain_google_genai import GoogleGenerativeAI
from pathlib import Path
from dotenv import load_dotenv
import json
from langchain_core.messages import AIMessage, HumanMessage
from langchain_google_vertexai.vision_models import VertexAIImageGeneratorChat
from PIL import Image
import io
import anthropic
# from some_anthropic_sdk import Client
import logging
import base64
import httpx
logger = logging.getLogger(__name__)

# Create your views here.@csrf_exempt
@csrf_exempt
def google_gemani_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('text')  
            # Initialize the AI with the necessary API key
            print("this is new ai ")
            llm = GoogleGenerativeAI(
                model="gemini-1.5-flash", google_api_key="AIzaSyA7_l5ILYh4Y0iEr9Ya-xafFAfMO-6SXpo"
            )
            
            # Updated system message for English teaching
            system_message = SystemMessage(
                content=(
                    "You are an advanced English AI assistant specializing in teaching grammar and sentence structure. "
                    "Your primary role is to help users correct grammar mistakes, improve sentence clarity, and enhance their writing skills. "
                    "When given a sentence, you should analyze it for grammar errors, awkward phrasing, and other mistakes, and then provide a corrected version along with explanations. "
                    "Ensure that the explanations are clear, concise, and easy for the user to understand. "
                    "You should provide feedback in a friendly, encouraging, and human-like manner, focusing on improving the user's command of English. "
                    "If a user submits multiple sentences, review each one and provide individual feedback. "
                    "Your guidance should also offer tips on how to avoid common grammatical mistakes. "
                    "Make sure to explain the rules behind the corrections, so users can learn from their mistakes and avoid them in the future."
                )
            )

            # Human message from the user input
            messages = [
                system_message,
                HumanMessage(content=user_input)
            ]

            # Invoke the language model to process the user's input and return corrections
            response_data = llm.invoke(messages)
            print(response_data)  # Debugging, ensure response is correct

            # Return the response from the language model
            return JsonResponse({'response_data': response_data})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid method'}, status=405)
