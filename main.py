import os
import re
import PyPDF2
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tabulate import tabulate

# Function to extract text from a PDF
def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
        return text
    except Exception as e:
        return ''

# Function to extract text from a DOCX
def extract_text_from_docx(file_path):
    try:
        doc = Document(file_path)
        text = ''
        for para in doc.paragraphs:
            text += para.text + ' '
        return text
    except Exception as e:
        return ''

# Function to clean and preprocess text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()

# Get resumes
resume_folder = 'resumes'
resume_files = [f for f in os.listdir(resume_folder) if f.lower().endswith(('.pdf', '.docx'))]

# Extract resume texts
resumes = []
for file in resume_files:
    path = os.path.join(resume_folder, file)
    if file.endswith('.pdf'):
        content = extract_text_from_pdf(path)
    else:
        content = extract_text_from_docx(path)
    resumes.append((file, clean_text(content)))

# Get job description
job_description = input("Paste the job description here:\n")
job_description = clean_text(job_description)

# Calculate similarity
results = []
for filename, resume_text in resumes:
    corpus = [job_description, resume_text]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    results.append((filename, round(similarity * 100, 2)))

# Sort results by score descending
results.sort(key=lambda x: x[1], reverse=True)

# Display as table
headers = ["Filename", "Similarity Score"]
print("\n📊 Resume Matching Results:")
print(tabulate(results, headers=headers, tablefmt="fancy_grid"))
