import bcrypt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import dash
import dash_core_components as dcc
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

class UniversityAdmissionDashboard:
    def __init__(self):
        """Initialize the dashboard with user details"""
        print("\n=== Welcome to the University Admission Portal ===\n")
        self.username = input("Enter your Username: ")
        self.name = input("Enter your Full Name: ")
        self.email = input("Enter your Email: ")
        self.profile = {}
        self.application_status = "Not Submitted"  # Default status
        self.documents = {}
        self.notifications = []
        self.payments = []
        self.interviews = {}

    # 1. User Profile Management
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

    # 2. Application Management
    def submit_application(self):
        print("\n=== Submit Application ===")
        program = input("Enter the Program Name: ")
        degree_level = input("Enter Degree Level (e.g., BSc, MSc, PhD): ")
        self.application_status = "Submitted"
        print(f"Application for {program} ({degree_level}) submitted successfully.")

    def check_application_status(self):
        print(f"\nCurrent application status: {self.application_status}")

    # 3. Document Upload & Verification
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

    # 4. Notifications & Alerts
    def add_notification(self, message):
        self.notifications.append(message)

    def get_notifications(self):
        if self.notifications:
            print("\n=== Notifications ===")
            for i, note in enumerate(self.notifications, 1):
                print(f"{i}. {note}")
        else:
            print("\nNo new notifications.")

    # 5. Payment & Fee Management
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

    # 6. Interview & Exam Scheduling
    def schedule_interview(self):
        print("\n=== Schedule Interview ===")
        date = input("Enter Interview Date (YYYY-MM-DD): ")
        time = input("Enter Interview Time (HH:MM AM/PM): ")
        self.interviews["Interview"] = {"Date": date, "Time": time}
        print(f"Interview scheduled for {date} at {time}.")

    def get_interview_details(self):
        print("\n=== Interview Details ===")
        print(self.interviews.get("Interview", "No interview scheduled."))

# ==== Run the Program ====
dashboard = UniversityAdmissionDashboard()

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
    print("11. Exit")

    choice = input("\nEnter your choice (1-11): ")

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
        print("\nExiting the dashboard. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 11.")

# Additional classes and methods

class UniversityWebsite:
    def __init__(self):
        self.greetings = []
        self.create_account = {}
        self.signed_in_users = {}
        self.contact_information = {}
        self.plan_for_university = {}
        self.apply_to_university = {}
        self.pay_for_university = {}

    def is_valid_email(self, email):
        return "@" in email and "."

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

# FastAPI setup
app = FastAPI()

load_dotenv()
OPENAI_API_KEY = getenv('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')

@app.post("/ask")
async def ask(question: str):
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="API key not set")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





