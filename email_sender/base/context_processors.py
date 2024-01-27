from django.shortcuts import render
from . forms import EmailQueryForm
from langchain_google_genai import ChatGoogleGenerativeAI
import os

MODEL = os.environ.get("MODEL")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

def generate_email_message(query):
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-pro")
        query_with_email_content = f"act as content writer: {query}"
        result = llm.invoke(query_with_email_content)
        return result.text if hasattr(result, 'text') else str(result)
    except Exception as e:
        # Log the exception or handle it appropriately
        print(f"Error generating email message: {e}")
        return "An error occurred while generating the email message."

def email_query(request):
    if request.method == 'POST':
        form = EmailQueryForm(request.POST)
        if form.is_valid():
            user_query = form.cleaned_data['query']
            generated_email_message = generate_email_message(user_query)
            return render(request, 'home.html', {'form': form, 'generated_email_message': generated_email_message})
    else:
        form = EmailQueryForm()

    return render(request, 'home.html', {'form': form})
