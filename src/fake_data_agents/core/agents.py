from fake_data_agents.core.providers import DataProviders, ResponseProviders
from fake_data_agents.recipe.llm import (
    OpenAIRecipe, GeminiRecipe, PerplexityRecipe, LLaMARecipe
)

class AgentManager:
    def __init__(self):
        self.llm_classes = {
            "openai": OpenAIRecipe,
            "gemini": GeminiRecipe,
            "perplexity": PerplexityRecipe,
            "llama": LLaMARecipe
        }

    def get_llm(self, llm_type: str):
        llm_class = self.llm_classes.get(llm_type.lower())
        if llm_class is None:
            raise ValueError(f"LLM type '{llm_type}' is not supported.")
        return llm_class()
    
    def generate(self, llm_type: str, data_type: str):
        # Get the LLM instance based on the user's choice
        llm = self.get_llm(llm_type)
        
        # Get the appropriate prompt for the requested data type
        prompt = DataProviders.get_prompt(data_type)
        if "Unknown" in prompt:
            raise ValueError(f"Data type '{data_type}' is not supported.")
        initial_output = llm.generate(prompt)
        final_prompt = ResponseProviders.get_prompt() + initial_output

        final_output = llm.generate(final_prompt)
        return final_output

