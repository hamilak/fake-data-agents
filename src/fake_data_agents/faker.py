import os
import json

from fake_data_agents.core.agents import AgentManager
from fake_data_agents.core.providers import DataProviders

def generate_fake_data(llm_type: str, data_type: str) -> str:

    """
    Generate fake data using the specified LLM type and data type.

    Args:
        llm_type (str): The type of LLM (openai, gemini, perplexity, llama).
        data_type (str): The type of data to generate (e.g., person, address, job).
        api_key (str, optional): API key for the selected LLM. Defaults to None.

    Returns:
        str: JSON-formatted string with generated fake data.
    """

    recipe_manager = AgentManager()

    # Validate inputs
    llm_type = llm_type.strip().lower()
    data_type = data_type.strip().lower()

    if llm_type not in ["openai", "gemini", "perplexity", "llama"]:
        raise ValueError(f"Invalid LLM type: {llm_type}. Supported types are: openai, gemini, perplexity, llama.")

    if data_type not in DataProviders.prompts.keys():
        raise ValueError(f"Invalid data type: {data_type}. Supported data types are: {', '.join(DataProviders.prompts.keys())}.")

    # Generate the fake data using the specified LLM and data type
    # try:
    generated_data = recipe_manager.generate(llm_type, data_type)
    # Return the result as a JSON-formatted string
    result = {
        "llm_type": llm_type,
        "data_type": data_type,
        "generated_data": generated_data
    }
    return result
    # return json.dumps(result, indent=4)
    # except Exception as e:
        # raise ValueError(f"An error occurred while generating data: {str(e)}")


# def 

# Example usage as a function call
if __name__ == "__main__":
    # Example input arguments (these would come from somewhere else in your code or tests)
    llm_type = "gemini"
    data_type = "person"
    
    # Call the function and print the JSON output
    try:
        result = generate_fake_data(llm_type, data_type)
        print(result)
    except ValueError as e:
        print(e)
