import os
import json

from fake_data_agents.core.agents import AgentManager
from fake_data_agents.core.providers import DataProviders

def generate_fake_data(llm_type: str, data_type: str) -> str:

    recipe_manager = AgentManager()

    llm_type = llm_type.strip().lower()
    data_type = data_type.strip().lower()

    if llm_type not in ["openai", "gemini", "perplexity", "llama"]:
        raise ValueError(f"Invalid LLM type: {llm_type}. Supported types are: openai, gemini, perplexity, llama.")

    if data_type not in DataProviders.prompts.keys():
        raise ValueError(f"Invalid data type: {data_type}. Supported data types are: {', '.join(DataProviders.prompts.keys())}.")

    generated_data = recipe_manager.generate(llm_type, data_type)
    result = {
        "llm_type": llm_type,
        "data_type": data_type,
        "generated_data": generated_data
    }
    return result


if __name__ == "__main__":
    llm_type = "gemini"
    data_type = "person"
    
    try:
        result = generate_fake_data(llm_type, data_type)
        print(result)
    except ValueError as e:
        print(e)
