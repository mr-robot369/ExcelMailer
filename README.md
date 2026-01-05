# 📊 ExcelMailer
### *Enterprise-Grade Excel & PDF Distribution Engine*

[![Django](https://img.shields.io/badge/Backend-Django-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap-7952B3?style=for-the-badge&logo=bootstrap)](https://getbootstrap.com/)
[![Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)

**ExcelMailer** is a secure, role-based internal web application designed to eliminate the risks associated with manual data sharing. Built with **Django**, it empowers organizations to slice master Excel files and securely distribute individual sheets or PDF reports to specific members with clinical precision.

---

## 🎯 The Problem & The Solution

Manual distribution of sensitive data is prone to human error, lack of accountability, and data leakage.

| The Pain Points ❌ | The ExcelMailer Solution ✅ |
| :--- | :--- |
| Sending the wrong sheet to the wrong person | **Precision Mapping:** Members are hard-linked to specific sheet names. |
| No visibility on delivery success/failure | **Real-time Logs:** Full audit trail with detailed error reporting. |
| Data leakage across departments | **Department Isolation:** Siloed data access based on roles. |
| Lack of audit trails for compliance | **CSV Exports:** One-click exportable distribution reports. |

---

## 🧠 System Logic & Workflow

ExcelMailer operates on a strictly controlled permission model to ensure data integrity.

1.  **Admin:** Defines a **Department** and assigns a **Department Head**.
2.  **Dept Head:** Manages **Members**, mapping them to their respective **Excel Sheet Names**.
3.  **Upload:** Head uploads the master **Excel File**.
4.  **Verification:** Uses the **Preview** tool to verify data accuracy before broadcast.
5.  **Execution:** Selects format (Excel/PDF) and triggers the automated distribution.
6.  **Audit:** Reviews and **Exports Logs** to track distribution success.

---

## ✨ Core Features

* **Closed-Loop Security:** No public sign-ups; all accounts are provisioned by administrators to maintain a secure environment.
* **Sheet-to-Member Mapping:** Seamlessly link specific members to individual sheet names within a master file.
* **Live Preview Console:** Inspect the first few rows of data before triggering a broadcast to prevent accidental data exposure.
* **Multi-Format Support:** Distribute raw `.xlsx` sheets or professionally formatted `.pdf` documents natively.
* **Comprehensive Audit Trail:** Logs every outbound email with timestamps and delivery status (Success/Failure).
* **Analytical Exports:** Export email logs to CSV for external compliance reviews or internal processing.

---

## 🛠 Tech Stack

* **Backend:** [Django](https://www.djangoproject.com/) (Python)
* **Excel Engine:** [Openpyxl](https://openpyxl.readthedocs.io/)
* **PDF Engine:** [ReportLab](https://www.reportlab.com/)
* **Frontend:** HTML5, CSS3, [Bootstrap 5](https://getbootstrap.com/) (Midnight Dark Theme)
* **Database:** SQLite (Default/Development)
* **Email Service:** SMTP Integration

---

## ⚙️ Installation & Setup

### 1. Environment Setup
```bash
git clone [https://github.com/mr-robot369/Excel-Email-Send.git](https://github.com/mr-robot369/Excel-Email-Send.git)
cd Excel-Email-Send
python -m venv venv

# Linux/Mac
source venv/bin/activate 
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

### 2. Configuration
Configure your SMTP settings in your environment variables:
- `EMAIL_FROM`: Your distribution email address.
- `EMAIL_USER`: Your SMTP username.
- `EMAIL_PASS`: Your App Password.

### 3. Initialize System
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 👨‍💻 Author

**Anubhav Shukla**
*MSc Data Science | Django & Python Developer*

[LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/mr-robot369)
