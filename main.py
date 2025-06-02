import os
import google.generativeai as genai

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

# Configure the Gemini API (still needed for the underlying library)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

llm = genai.GenerativeModel("gemini-2.5-flash-preview-05-20") #Code execution|Structured outputs|Caching|Function calling|Search grounding|Thinking

# might use best model for desired effect later
llmtts = genai.GenerativeModel("gemini-2.5-flash-preview-tts") #Audio generation
llmimage = genai.GenerativeModel("gemini-2.0-flash-preview-image-generation") #Image generation|Structured outputs|Caching
llm1 = ChatOpenAI(model="gpt-3.5-turbo")
llm2 = ChatAnthropic(model="claude-3-5-sonnet-20241022") #need apikey $

response = llm.generate_content("What is the meaning of life?")
print(response.text)

# todo: Ian next add STRUCTURED OUTPUT



