# 📊 ExcelMailer  
### *Role-Based Excel & PDF Distribution System (Demo Deployment)*

![Django](https://img.shields.io/badge/Backend-Django-092E20?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python)
![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap-7952B3?style=for-the-badge&logo=bootstrap)

---

## 🌐 Live Demo

🔗 **Website:** https://excelmailer-2.onrender.com/  
🔗 **GitHub Repository:** https://github.com/mr-robot369/ExcelMailer.git  

---

## 🔑 Demo Login Credentials

### 👤 Department Head (Demo User)
- **Username:** `mr-robot`  
- **Password:** `mrrobo@123`

### 👑 Admin (Dummy Credentials)
- **Username:** `admin`  
- **Password:** `admin@1234`

> ⚠️ These are **dummy credentials** provided only for demo and evaluation purposes.

---

## 🧩 About the Project

**ExcelMailer** is a secure, role-based internal web application built with **Django** that automates the distribution of Excel sheets and PDF reports to specific members.

The system ensures:
- Correct data reaches the correct person
- Full audit trail of every distribution
- Zero risk of accidental data leakage

This deployment runs in **DEMO MODE**, meaning no real emails are sent.

---

## 🚀 Key Features

- 🔐 **Closed System** – No public signup; accounts created by Admin only  
- 🧑‍💼 **Role-Based Access** – Admin → Department Head → Members  
- 📑 **Excel Sheet Mapping** – One sheet per member  
- 👀 **Preview Before Send** – Prevents mistakes  
- 📄 **Excel & PDF Support**  
- 📊 **Email Logs & CSV Export**  
- 🕒 **Timezone-Aware Timestamps (IST)**  

---

## 🧠 Workflow Overview

1. **Admin** creates Departments & Department Heads  
2. **Department Head** adds Members and maps Excel sheet names  
3. Upload master Excel file  
4. Preview sheets  
5. Send Excel/PDF (simulated in demo mode)  
6. Review logs & export reports  

---

## 📧 Email Behavior (Demo Mode)

This project is deployed in **safe demo mode**:

- ❌ No real emails are sent  
- ✅ Django Console Email Backend is used  
- ✅ Email logic executes fully  
- ✅ Email logs are recorded in the database  

This prevents spam and misuse while allowing complete functionality to be demonstrated.

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap 5 (Dark UI)
- **Excel Processing:** OpenPyXL, Pandas
- **PDF Generation:** ReportLab
- **Database:** SQLite (Demo)
- **Hosting:** Render (Docker-based)

---

## ⚠️ Hosting Notes

- Hosted on **Render free tier**
- SQLite database included for demo
- Uploaded files may reset on redeploy
- Intended for **portfolio & demonstration use**

---

## 🧑‍💻 Author

**Anubhav Shukla**  
*MSc Data Science | Django & Python Developer*

🔗 GitHub: https://github.com/mr-robot369  

---

⭐ If you find this project useful, consider starring the repository!
