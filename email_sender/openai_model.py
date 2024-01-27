import os
from langchain_google_genai import ChatGoogleGenerativeAI

MODEL = os.environ.get("MODEL")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

def generate_email_message(query):
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    
    # Include email-related content in the query
    query_with_email_content = f"Just write a professional content not subject and regards: {query}"
    
    result = llm.invoke(query_with_email_content)
    return result.text if hasattr(result, 'text') else str(result)

# Example query from the user
user_query = "I want to write a message to pursue blood donors to donate blood"

# Generate only the email message content based on the user's query
generated_email_message = generate_email_message(user_query)

# Write the generated email message to a file
with open('generated_email_message.html', 'w', encoding='utf-8') as file:
    file.write(generated_email_message)

print(f'Generated email message written to generated_email_message.html')
