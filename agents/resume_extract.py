from groq import Groq
from dotenv import load_dotenv
import os
from resume_prompts import *
from pdfminer.high_level import extract_text

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = Groq(api_key=api_key)

def extract_candidate_details(resume_file):
    resume_text = extract_text(resume_file)
    prompt = EXTRACT_CANDIDATE_DETAILS.format(resume_text=resume_text)
    
    response = model.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an expert resume parser. Extract relevant candidate details from the resume provided.",
            },
            {"role": "user", "content": prompt},
        ],
        model="llama-3.1-8b-instant",
       
    )
    
    return response.choices[0].message.content
