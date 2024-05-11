from openai import OpenAI

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_sql_query(natural_language_query, table_schema):
    """
    Generate SQL query based on the natural language query and table schema.
    """
    # Prepare prompt for GPT model
    prompt = f"Generate SQL query for the following natural language query: '{natural_language_query}'. The table schema is as follows: {table_schema}."

    try:
        # Send request to GPT model for query generation
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  
            prompt=prompt,
            max_tokens=200,  
            n=1,  
            stop=None,  
            temperature=0.5
        )

        # Extract generated SQL query from response
        generated_query = response.choices[0].text.strip()

        return generated_query

    except Exception as e:
        # Handle OpenAI API errors
        print("Error:", e)
        return None
