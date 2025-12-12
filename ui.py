import streamlit as st
import requests

API_URL = "http://localhost:8000/screening/"

st.set_page_config(page_title="Resume Analyze Agent", page_icon=":robot_face:")
st.title("🤖 Resume Analyze Agent")   
upload_resume = st.file_uploader("Upload your resume", type=["pdf"])
if upload_resume is not None:
    st.success("Resume uploaded successfully!")
    job_desc = st.text_area("Enter the Job Description of the role you are applying for:",placeholder="Job Description...")
    if job_desc and upload_resume:
        if st.button("Process"):
            with st.spinner("Processing..."):
                try:                
                    files = {"resume": (upload_resume.name, upload_resume.getvalue(),'application/pdf')}
                    data = {"job_desc": job_desc}
                    response = requests.post(API_URL, files=files, data=data)
                    if response.status_code == 200:    
                        st.subheader("Evaluation Result:")
                        result = response.json()               
                        st.write(result.replace('{}',''))
                    else:
                        st.write("Error processing resume:", response.text)    
                except Exception as e:
                    st.error(f"An error occurred: {e}")        
            