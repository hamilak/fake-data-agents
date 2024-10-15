import os
import openai
import google.generativeai as genai
# from openai import OpenAI
from dotenv import load_dotenv

from fake_data_agents.recipe.base import LLMRecipe

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

openai.api_key =  os.getenv('OPENAI_KEY')

class OpenAIRecipe(LLMRecipe):
    def generate(self, prompt: str):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages= [{ "role": 'user', "content": prompt }]
        )
        return response.choices[0].message.content.strip()

# Implement similar classes for Gemini, Perplexity, and LLaMA
class GeminiRecipe(LLMRecipe):
    def generate(self, prompt: str):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text

class PerplexityRecipe(LLMRecipe):
    def generate(self, prompt: str):
        # Implement Perplexity-specific API call
        return "Perplexity-generated response"

class LLaMARecipe(LLMRecipe):
    def generate(self, prompt: str):
        # Implement LLaMA-specific API call
        return "LLaMA-generated response"
