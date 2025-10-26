import pdfplumber
import docx

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_skills(resume_path):
    skills_list = {"Python", "Java", "SQL", "Machine Learning", "NLP", "React", "Cloud", "Data Analysis"}
    
    if resume_path.endswith(".pdf"):
        text = extract_text_from_pdf(resume_path)
    elif resume_path.endswith(".docx"):
        text = extract_text_from_docx(resume_path)
    else:
        return []

    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]
    return found_skills