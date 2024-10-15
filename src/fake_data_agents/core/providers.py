class DataProviders:
    prompts = {
        "address": "Generate a realistic address.",
        "automotive": "Generate details about a random car (make, model, year).",
        "bank": "Generate realistic bank information (bank name, account number, and sort code).",
        "barcode": "Generate a random barcode number.",
        "color": "Generate a random color name and its hexadecimal value.",
        "company": "Generate a random company name and description.",
        "credit_card": "Generate realistic credit card information (number, expiration date, CVV).",
        "currency": "Generate a random currency name, symbol, and code.",
        "date_time": "Generate a random date and time.",
        "emoji": "Generate a random emoji and its description.",
        "file": "Generate a random file type and description.",
        "geo": "Generate a random geographic location (latitude and longitude).",
        "internet": "Generate random internet-related data (IP address, domain name, or URL).",
        "isbn": "Generate a random ISBN number.",
        "job": "Generate a random job title and job description.",
        "lorem": "Generate a random lorem ipsum text.",
        "misc": "Generate random miscellaneous data.",
        "passport": "Generate a random passport number and country.",
        "person": "Generate a realistic person's name, age, and gender.",
        "phone_number": "Generate a random phone number with country code.",
        "profile": "Generate a detailed user profile including name, address, job, and more.",
        "python": "Generate a random Python code snippet.",
        "sbn": "Generate a random SBN (Standard Book Number).",
        "ssn": "Generate a random SSN (Social Security Number).",
    }

    @classmethod
    def get_prompt(cls, data_type: str) -> str:
        return cls.prompts.get(data_type.lower(), "Unknown data type. Cannot generate prompt.")


class ResponseProviders:
    prompts = "Look at this prompt and the corresponding result and create a well format JSON output"

    @classmethod
    def get_prompt(cls) -> str:
        return cls.prompts
