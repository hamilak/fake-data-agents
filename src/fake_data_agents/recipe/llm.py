import os
import openai
import google.generativeai as genai
from dotenv import load_dotenv

from fake_data_agents.recipe.base import LLMRecipe

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

openai.api_key =  os.getenv('OPENAI_KEY')

class OpenAIRecipe(LLMRecipe):
    def generate(self, prompt: str):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages= [{ "role": 'user', "content": prompt }]
        )
        return response.choices[0].message.content.strip()

class GeminiRecipe(LLMRecipe):
    def generate(self, prompt: str):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text

class PerplexityRecipe(LLMRecipe):
    def generate(self, prompt: str):
        return "Perplexity-generated response"

class LLaMARecipe(LLMRecipe):
    def generate(self, prompt: str):
        return "LLaMA-generated response"
