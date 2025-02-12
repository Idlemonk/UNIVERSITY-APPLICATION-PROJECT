import bcrypt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import dash
import dash_core_components as dcc
from dash import html
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import PyPDF2 as p2
import django as dj
import textblob as tb
import tensorflow as tf
import spacy as sp
import nltk as n
from fastapi import FastAPI, HTTPException
import httpx
import os
import asyncio
import openai
from dotenv import load_dotenv
import mysql.connector
import re
from fastapi import FastAPI, APIRouter, Depends
from routers import user, application, document, notification, payment, interview
from models.user import User
from services.user_service import create_user, get_user 
from pydantic import BaseModel


class UniversityAdmissionDashboard:
    def __init__(self):
        """Initialize the dashboard with user details"""
        self.profile = {}
        self.application_status = "Not Submitted"  # Default status
        self.documents = {}
        self.notifications = []
        self.payments = []
        self.interviews = []

    def update_profile(self):
        print("\n=== Update Profile ===")
        phone = input("Enter your Phone Number: ")
        address = input("Enter your Address: ")
        dob = input("Enter your Date of Birth (YYYY-MM-DD): ")
        self.profile = {
            "Phone": phone,
            "Address": address,
            "Date of Birth": dob
        }
        print("Profile updated successfully.")

    def submit_application(self):
        print("\n=== Submit Application ===")
        program = input("Enter the Program Name: ")
        degree_level = input("Enter Degree Level (e.g., BSc, MSc, PhD): ")
        self.application_status = "Submitted"
        print(f"Application for {program} ({degree_level}) submitted successfully.")

    def check_application_status(self):
        print(f"\nCurrent application status: {self.application_status}")

    def upload_document(self):
        print("\n=== Upload Documents ===")
        doc_name = input("Enter Document Name (e.g., Transcript, ID Proof): ")
        file_path = input(f"Enter File Path for {doc_name}: ")
        self.documents[doc_name] = {"File Path": file_path, "Status": "Pending"}
        print(f"{doc_name} uploaded successfully.")

    def check_document_status(self):
        print("\n=== Document Status ===")
        doc_name = input("Enter Document Name to Check Status: ")
        print(self.documents.get(doc_name, "Document not found."))

    def add_notification(self, message):
        self.notifications.append(message)

    def get_notifications(self):
        if self.notifications:
            print("\n=== Notifications ===")
            for i, note in enumerate(self.notifications, 1):
                print(f"{i}. {note}")
        else:
            print("\nNo new notifications.")

    def make_payment(self):
        print("\n=== Make Payment ===")
        amount = input("Enter Payment Amount: ")
        method = input("Enter Payment Method (Credit Card, Bank Transfer): ")
        payment_details = {"Amount": amount, "Method": method, "Status": "Completed"}
        self.payments.append(payment_details)
        print("Payment successful.")

    def get_payment_history(self):
        print("\n=== Payment History ===")
        if self.payments:
            for payment in self.payments:
                print(payment)
        else:
            print("No payments made.")

    def schedule_interview(self):
        print("\n=== Schedule Interview ===")
        date = input("Enter Interview Date (YYYY-MM-DD): ")
        time = input("Enter Interview Time (HH:MM AM/PM): ")
        self.interviews["Interview"] = {"Date": date, "Time": time}
        print(f"Interview scheduled for {date} at {time}.")

    def get_interview_details(self):
        print("\n=== Interview Details ===")
        print(self.interviews.get("Interview", "No interview scheduled."))

class UniversityWebsite:
    def __init__(self):
        self.create_account = {}
        self.signed_in_users = {}
        self.contact_information = {}

    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def sign_up(self, username, first_name, maiden_name, last_name, password, email, state_of_origin, residential_address):
        if username in self.create_account:
            print("Username already exists. Please choose a different username.")
        elif not self.is_valid_email(email):
            print("Invalid email address. Please enter a valid email.")
        else:
            hashed_password = self.hash_password(password)
            self.create_account[username] = {
                "first_name": first_name,
                "maiden_name": maiden_name,
                "last_name": last_name,
                "password": hashed_password,
                "email": email,
                "state_of_origin": state_of_origin,
                "residential_address": residential_address
            }
            full_name = f"{first_name} {last_name}"
            self.contact_information[username] = {
                "full_name": full_name,
                "email": email,
                "state_of_origin": state_of_origin,
                "residential_address": residential_address
            }
            print("Account created successfully!")

    def sign_in(self, identifier, password):
        account = self.create_account.get(identifier)
        if account and bcrypt.checkpw(password.encode('utf-8'), account['password']):
            print("Sign in successful!")
            self.signed_in_users[identifier] = account
        else:
            print("Incorrect username/email or password. Please try again.")

class AssignUniversity:
    def __init__(self):
        self.university_lists = []
        self.choose_university = {}
        self.jamb_score = {}
        self.state_of_origin = {}
        self.state_or_residence = {}

    def choose_university(self, university_lists):
        self.university_lists = university_lists
        return self.university_lists

    def score(self, jamb_score):
        self.jamb_score = jamb_score
        self.choose_university[links] = university_url
        print("Link added successfully!")

    def remove_link(self, links):
        if links in self.choose_university:
            del self.choose_university[links]
            print("Link removed successfully!")
        else:
            print("Link not found.")

    def assigning_university_based_on_score(self, score):
        if score >= 250:
            return ["University A", "University B", "University C"]
        elif score >= 200:
            return ["University D", "University E", "University F"]
        else:
            return ["University G", "University H", "University I"]

class ApplyForUniversityAdmission:
    def __init__(self):
        self.choose_course = {}
        self.second_course_choice = {}
        self.third_course_choice = {}
        self.faculty = {}
        self.departments = {}

    def choose_faculty_and_dept(self):
        choose_course = {
            "faculty_of_engineering": ("civil_engineering", "mechanical_engineering", "chemical_engineering", "agricultural_engineering"),
            "faculty_of_science": ("biology", "chemistry", "physics", "mathematics"),
            "faculty_of_commerce": ("business_admin", "finance", "marketing", "operations_research"),
            "faculty_of_medicine": ("pharmacy", "nursing", "medical_lab"),
            "faculty_of_social_science": ("psychology", "sociology", "theology")
        }
        for faculty, departments in choose_course.items():
            print(f"Available departments in {faculty}: {', '.join(departments)}")
            chosen_department = input("Please choose a department: ")
            if chosen_department in departments:
                self.choose_course[faculty] = chosen_department
                print(f"You have been assigned to the {faculty} in the {chosen_department} department.")
            else:
                print("Invalid department chosen. Please try again.")

    def second_course_choice(self):
        print("Please choose your second course.")
        self.choose_faculty_and_dept()

    def third_course_choice(self):
        print("Please choose your third course.")
        self.choose_faculty_and_dept()

load_dotenv()
OPENAI_API_KEY = os.getenv('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')
if not isinstance(OPENAI_API_KEY, str):
    raise ValueError("OPENAI_API_KEY must be a string")


# FastAPI setup
app = FastAPI()

app.include_router (user.router)
app.include_router(application.router)
app.include_router(jamb.router)
app.include_router(document.router)
app.include_router(notification.router)
app.include_router(payment.router)
app.include_router(interview.router)


@app.post("/ask")
async def ask(question: str):
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="API key not set")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": question}
            ],
            api_key = OPENAI_API_KEY
        )
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

router = APIRouter()
@router.post("/users/")
async def sign_up(user: User):
    return create_user(user)

@router.get("/users/{user_id}")
async def read_user(user_id: int):
    return get_user(user_id)

class User(BaseModel):
    username: str
    first_name: str
    maiden_name: str
    last_name: str
    password: str
    email: str
    state_of_origin: str
    residential_address: str


def create_user(user: User):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    # Store user in database (this is a placeholder)
    return {"message": "User created successfully"}

def get_user(user_id: int):
    # Retrieve user from database (this is a placeholder)
    return {"message": "User retrieved successfully"}


def submit_application(program: str, degree_level: str):
    # Logic to submit application (this is a placeholder)
    return {"message": f"Application for {program} ({degree_level}) submitted successfully"}

def check_application_status():
    # Logic to check application status (this is a placeholder)
    return {"message": "Current application status: Submitted"}


def upload_document(doc_name: str, file_path: str):
    # Logic to upload document (this is a placeholder)
    return {"message": f"{doc_name} uploaded successfully"}

def check_document_status(doc_name: str):
    # Logic to check document status (this is a placeholder)
    return {"message": "Document status: Pending"}
    
    
def add_notification(message: str):
    # Logic to add notification (this is a placeholder)
    return {"message": "Notification added successfully"}

def get_notifications():
    # Logic to get notifications (this is a placeholder)
    return {"message": "No new notifications"}


def make_payment(amount: str, method: str):
    # Logic to make payment (this is a placeholder)
    return {"message": "Payment successful"}

def get_payment_history():
    # Logic to get payment history (this is a placeholder)
    return {"message": "No payments made"}


def schedule_interview(date: str, time: str):
    # Logic to schedule interview (this is a placeholder)
    return {"message": f"Interview scheduled for {date} at {time}"}

def get_interview_details():
    # Logic to get interview details (this is a placeholder)
    return {"message": "No interview scheduled"}  



# Create instances of all classes
dashboard = UniversityAdmissionDashboard()
website = UniversityWebsite()
assigner = AssignUniversity()
applicant = ApplyForUniversityAdmission()

# Main loop to synchronize all classes
while True:
    print("\n=== Dashboard Menu ===")
    print("1. Update Profile")
    print("2. Submit Application")
    print("3. Check Application Status")
    print("4. Upload Document")
    print("5. Check Document Status")
    print("6. View Notifications")
    print("7. Make Payment")
    print("8. View Payment History")
    print("9. Schedule Interview")
    print("10. View Interview Details")
    print("11. Sign Up")
    print("12. Sign In")
    print("13. Assign University Based on Score")
    print("14. Choose Faculty and Department")
    print("15. Choose Second Course")
    print("16. Choose Third Course")
    print("17. Exit")

    choice = input("\nEnter your choice (1-17): ")

    if choice == "1":
        dashboard.update_profile()
    elif choice == "2":
        dashboard.submit_application()
    elif choice == "3":
        dashboard.check_application_status()
    elif choice == "4":
        dashboard.upload_document()
    elif choice == "5":
        dashboard.check_document_status()
    elif choice == "6":
        dashboard.get_notifications()
    elif choice == "7":
        dashboard.make_payment()
    elif choice == "8":
        dashboard.get_payment_history()
    elif choice == "9":
        dashboard.schedule_interview()
    elif choice == "10":
        dashboard.get_interview_details()
    elif choice == "11":
        username = input("Enter Username: ")
        first_name = input("Enter First Name: ")
        maiden_name = input("Enter Maiden Name (optional): ")
        last_name = input("Enter Last Name: ")
        password = input("Enter Password: ")
        email = input("Enter Email: ")
        state_of_origin = input("Enter State of Origin: ")
        residential_address = input("Enter Residential Address: ")
        website.sign_up(username, first_name, maiden_name, last_name, password, email, state_of_origin, residential_address)
    elif choice == "12":
        identifier = input("Enter Username or Email: ")
        password = input("Enter Password: ")
        website.sign_in(identifier, password)
    elif choice == "13":
        score = int(input("Enter JAMB Score: "))
        assigned_universities = assigner.assigning_university_based_on_score(score)
        print(f"Assigned Universities: {assigned_universities}")
    elif choice == "14":
        applicant.choose_faculty_and_dept()
    elif choice == "15":
        applicant.second_course_choice()
    elif choice == "16":
        applicant.third_course_choice()
    elif choice == "17":
        print("\nExiting the dashboard. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 17.")