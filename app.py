from flask import Flask, render_template, request, redirect, url_for
import os
import pdfplumber
import docx
import pandas as pd
from resume_parser import extract_skills
from load_jobs import load_jobs_from_csv

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load jobs from CSV
jobs = load_jobs_from_csv("jobs.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "resume" not in request.files:
        return redirect(url_for("index"))

    file = request.files["resume"]
    if file.filename == "":
        return redirect(url_for("index"))

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    skills = extract_skills(filepath)
    matched_jobs = [job for job in jobs if any(skill in job["skills"] for skill in skills)]

    return render_template("results.html", skills=skills, jobs=matched_jobs)

if __name__ == "__main__":
    app.run(debug=True)