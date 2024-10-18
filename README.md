# LLM Synthetic Data Generator

This project provides a flexible framework for generating synthetic data using various language models (LLMs) such as OpenAI, Gemini, Perplexity, and LLaMA. Users can specify the LLM they want to use and the type of fake data they need (e.g., name, address, job, credit card, etc.).

## Features

- Supports multiple LLMs: OpenAI, Gemini, Perplexity, LLaMA.
- Generates a wide range of synthetic data types including names, addresses, job titles, credit card info, phone numbers, and more.
- Easily extendable to support additional LLMs or data types.
- Centralized `DataPrompts` class to manage prompts for different data types.
- User-friendly interface to choose the desired LLM and data type.

## Supported Data Types

The following data types can be generated:

- Address
- Automotive
- Bank
- Barcode
- Color
- Company
- Credit Card
- Currency
- Date/Time
- Emoji
- File
- Geo (Geographic Location)
- Internet (IP, Domain, URL)
- ISBN
- Job
- Lorem Ipsum
- Miscellaneous
- Passport
- Person
- Phone Number
- Profile
- Python Code Snippets
- SBN (Standard Book Number)
- SSN (Social Security Number)

## Installation

You can install with any package manager:

- Pip

```bash
pip install fake-data-agents
```

- Poetry 

```bash
poetry add fake-data-agents
```

- uv

```bash
uv add fake-data-agents
```

To set up the project locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fake-data-agents.git
cd fake-data-agents
```

### 2. Install dependencies

Make sure you have Python 3.12 installed. Install the required dependencies with `uv`:

```bash
uv sync
```

Dependencies include:
- `openai` (for OpenAI API)
- Any other relevant LLM libraries (if using Gemini, Perplexity, LLaMA, etc.)

### 3. Set up API keys

For each LLM you plan to use, make sure you have the appropriate API keys. You can store them in environment variables for easy access.

### 4. Run the program

You can start the synthetic data generation by running the `faker.py` file:

```bash
python3 src/fake_data_agents/faker.py
```

You can also import generate_fake_data from faker.py in your project. It accepts llm type and the datatype you want to generate as arguments

## Usage
To generate synthetic data, you can use the `generate_fake_data` function from the `faker.py` module.

1. **Import the function**:  
   ```bash
   from faker import generate_fake_data
   ```

2. **Call the function with the required arguments**:
   - **`llm_type`**: The language model you want to use (e.g., "OpenAI", "Gemini", "Perplexity", "LLaMA").
   - **`data_type`**: The type of synthetic data to generate (e.g., "person", "address", "job", "credit card", etc.).
   - **`n_samples`**: The number of synthetic samples to generate.

   Example:
   ```bash
   generate_fake_data(llm_type="openai", data_type="person", n_samples=10)
   ```

Store API keys for your chosen LLM in .env file. 

The function will return and/or display the generated synthetic data based on the provided input.


### Adding New Data Types

To add new data types, modify the `DataPrompts` class in `data_prompts.py` by adding a new key-value pair for the new data type:

```python
class DataPrompts:
    prompts = {
        # Existing prompts...
        "new_data_type": "Generate a random new data type description.",
    }
```

### Adding New LLMs

To add a new LLM, create a new class in `llm_recipes.py` that implements the `generate` method for interacting with the new LLM API:

```
class NewLLMRecipe(LLMRecipe):
    def generate(self, prompt: str):
        # Implement the API call for the new LLM
        return "New LLM-generated response"
```

Then, register this new LLM class in the `RecipeManager`:

```python
self.llm_classes = {
    "openai": OpenAIRecipe,
    "gemini": GeminiRecipe,
    "perplexity": PerplexityRecipe# Add the new LLM here
}
```

## Future Improvements

- **UI/CLI Enhancements**: Create a more interactive command-line interface (CLI) or graphical user interface (GUI).
- **LLM Benchmarking**: Add functionality to compare the performance and quality of the different LLMs for generating specific data types.
- **Extended Data Types**: Add more data types or improve the complexity of existing prompts (e.g., full user profiles, company financial data).

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. You can also open issues if you encounter any problems or have feature requests.

### To contribute:
1. Fork the project.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add your feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
