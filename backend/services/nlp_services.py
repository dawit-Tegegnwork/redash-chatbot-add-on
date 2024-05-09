# nlp_services.py

from celery import Celery
import openai

# Initialize Celery
celery = Celery('nlp_services', broker='redis://localhost:6379/0')

# Initialize OpenAI API
openai.api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual OpenAI API key

@celery.task
def generate_sql_query(natural_language_query, table_schema):
    """
    Generate SQL query based on the natural language query and table schema.
    """
    # Prepare prompt for GPT model
    prompt = f"Generate SQL query for the following natural language query: '{natural_language_query}'. The table schema is as follows: {table_schema}."
    
    # Send request to GPT model for query generation
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify GPT model (e.g., Davinci)
        prompt=prompt,
        max_tokens=100,  # Adjust max_tokens as needed
        n=1,  # Number of completions to generate
        stop=None,  # Optional stop sequence to end the completion
        temperature=0.7  # Controls randomness of output
    )

    # Extract generated SQL query from response
    generated_query = response.choices[0].text.strip()

    return generated_query
