from groq import Groq
from dotenv import load_dotenv
import os
from resume_prompts import *

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = Groq(api_key=api_key)

def candidate_evaluation(candidate_profile_json, job_description_json):
    prompt = CANDIDATE_EVALUATION.format(
        resume_json=candidate_profile_json,
        jd_json=job_description_json
    )
    
    response = model.chat.completions.create(
        messages=[            
            {"role": "user", "content": prompt},
        ],
        model="llama-3.1-8b-instant",
    )
    
    return response.choices[0].message.content