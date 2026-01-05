# 📊 ExcelMailer – Secure Excel & PDF Distribution System

ExcelMailer is a **role-based internal web application** built with **Django** that enables departments to **securely distribute Excel sheets or PDFs to specific members via email**, with full audit logging, preview functionality, and exportable reports.

This system is designed for **institutions, universities, departments, and organizations** where sensitive Excel data must be sent **accurately, securely, and traceably**.

---

## 🚀 Why ExcelMailer?

Manual Excel distribution often causes:
- ❌ Wrong sheet sent to wrong person  
- ❌ No preview before sending  
- ❌ No audit trail or accountability  
- ❌ Data leakage across departments  
- ❌ No error visibility  

**ExcelMailer eliminates these problems.**

---

## 🧠 How the System Works

Admin / Manager  
→ Creates Department & Department Head  
→ Department Head logs in (no admin access)  
→ Adds Members (mapped to Excel sheet names)  
→ Uploads Excel file (multiple sheets)  
→ Previews sheets before sending  
→ Sends Excel or PDF via email  
→ System logs every email (success / failure)  
→ Logs can be viewed & exported as CSV  

---

## 👥 User Roles & Permissions

### 🔐 Super Admin
- Full Django admin access
- Manages all data
- Views all email logs

### 🧑‍💼 Manager
- Admin panel access
- Creates departments
- Creates department heads

### 🧑‍🏫 Department Head
- ❌ No admin access
- Logs in via frontend
- Manages members
- Uploads Excel files
- Previews sheets
- Sends Excel / PDF
- Views & exports email logs

---

## ✨ Key Features

### 🔐 Authentication & Security
- No public signup
- Credentials created by admin
- Role-based access control
- Department-level data isolation

### 📂 Excel Management
- Upload Excel files with multiple sheets
- Each file linked to uploader & department
- Sheet-level processing

### 👥 Member Management
- Add members via dashboard
- Map members to Excel sheet names
- Full CRUD (create, list, delete)

### 👀 Sheet Preview
- Preview Excel sheets before sending
- Displays first few rows of data
- Prevents accidental or wrong sends

### 📤 Email Distribution
- Send **Excel sheets** or **PDF versions**
- One-click distribution
- SMTP-based secure email sending

### 🧾 Email Logs (Audit Trail)
- Logs every email (per recipient)
- Status: success / failure
- Error messages stored
- Timestamped records

### 📥 Export Logs
- Export email logs as CSV
- Excel & Google Sheets compatible

---

## 🛠 Tech Stack

- **Backend:** Django  
- **Frontend:** Django Templates + Bootstrap  
- **Database:** SQLite (default)  
- **Email:** SMTP  
- **Excel Processing:** openpyxl  
- **PDF Generation:** reportlab  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
git clone https://github.com/mr-robot369/Excel-Email-Send.git  
cd Excel-Email-Send  

### 2️⃣ Create Virtual Environment
python -m venv venv  
source venv/bin/activate (Linux/Mac)  
venv\Scripts\activate (Windows)  

### 3️⃣ Install Dependencies
pip install -r requirements.txt  

### 4️⃣ Configure Email Settings
Set environment variables:

EMAIL_FROM=your_email@gmail.com  
EMAIL_USER=your_email@gmail.com  
EMAIL_PASS=your_app_password  

### 5️⃣ Run Migrations
python manage.py makemigrations  
python manage.py migrate  

### 6️⃣ Create Superuser
python manage.py createsuperuser  

### 7️⃣ Run Server
python manage.py runserver  

Open: http://127.0.0.1:8000/

---

## 🧪 How to Use

1. Login as Admin  
2. Create Department  
3. Create Department Head  
4. Department Head logs in  
5. Add Members  
6. Upload Excel  
7. Preview Sheets  
8. Send Excel/PDF  
9. View Email Logs  
10. Export Logs  

---

## 🔮 Future Enhancements
- Async email sending (Celery)
- Duplicate send prevention
- Sheet-member mismatch warnings
- Analytics dashboard

---

## 👨‍💻 Author

**Anubhav Shukla**  
MSc Data Science | Django & Python Developer  
