class LLMRecipe:
    def __init__(self, api_key=None):
        self.api_key = api_key
    
    def generate(self, prompt: str):
        """
        Implement this method in each specific LLM class.
        """
        raise NotImplementedError("This method should be implemented in subclasses.")
