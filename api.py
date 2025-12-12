from fastapi import FastAPI, UploadFile, File, Form
import uvicorn
from agents.resume_extract import extract_candidate_details
from agents.job_desc_extract import extract_job_description_details
from agents.candidate_evluation import candidate_evaluation
import json

app = FastAPI()

@app.post("/screening/")
def candidate_screening(resume: UploadFile = File(...), job_desc: str = Form(...)):
     candidate_res = extract_candidate_details(resume.file)
     job_res = extract_job_description_details(job_desc)
     evaluation_data = candidate_evaluation(candidate_res, job_res)      
     result_json = json.dumps(evaluation_data)   
     return evaluation_data