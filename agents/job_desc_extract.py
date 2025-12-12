from groq import Groq
from dotenv import load_dotenv
import os
from resume_prompts import *

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = Groq(api_key=api_key)


def extract_job_description_details(job_desc_text):
    prompt = EXTRACT_JD_DETAILS.format(jd_text=job_desc_text)
    
    response = model.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an expert job description analyzer. Extract relevant job details from the job description provided.",
            },
            {"role": "user", "content": prompt},
        ],
        model="llama-3.1-8b-instant",
       
    )
    
    return response.choices[0].message.content