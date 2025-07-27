# 📄 AI-Based Resume Shortlisting System

This project shortlists resumes based on a job description using NLP techniques like TF-IDF and cosine similarity.

---

## 🚀 Features

- Upload a job description
- Automatically compare with multiple resumes (PDF format)
- Score each resume based on keyword similarity
- Display results in a clean table format

---

## ⚙️ Technologies Used

- **Python**
- **scikit-learn** for TF-IDF vectorization & cosine similarity
- **PyPDF2** or **pdfplumber** for PDF parsing
- **tabulate** for clean console table output

---

## 📋 Sample Output

-----------------------------------------------------+
| Resume                        | Similarity Score   |
+----------------------------------------------------+
| jagannath-resume-may 2020.pdf | 0.7123             |
| kiran_Resume - May 2023.pdf   | 0.6531             |
| rashmi-May 2017.pdf           | 0.6219             |
| Sathwikaa_May 2022 - .pdf     | 0.5890             |
| Sharanya May 2017.pdf         | 0.5478             |
+----------------------------------------------------+
