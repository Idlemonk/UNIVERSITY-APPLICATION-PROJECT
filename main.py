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





UNIVERSITY: tuple = [('https://www.4icu.org/ng/a-z/')]



        # jamb score come with 4 subjects  with each score totalling 400
        # for example 
Student_A =  {"ENG" : 80,
        "Math" : 70,
        "Govt" : 80,
        "History" : 80}
        # Think of how to write the code needed  to assign to a candidate list of universities close to her state of origin 2 Federal 2 state university  
        
# the instance of this class would be User_Account = University_Website()          
# links can be stored as values in this given code, and could support 5 codes for each range.     
# replace values with university website links  
# how to extract each university with it's links


load_dotenv()
app = FastAPI()

OPENAI_API_KEY = os.getenv('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')

@app.post("/ask")
async def ask(question: str):
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="API key not set")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": question}
        ])
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

def greetings(self):
    print("Hello! Welcome to the University Website. How can we help you today?")
    print("We are here to help you plan your university experience.")
    print("Please select one of the following options:")
    print("1. Greetings")
    print("2. Create an account")
    print("3. Sign in")
    print("4. Contact Information")
    print("5. Plan for University")
    print("6. Apply to University")
    print("7. Pay for University")
    print("8. Exit")

    option = input("Please select an option: ")
    if option == "1":
        self.greetings()
    elif option == "2":
        self.create_account()
    elif option == "3":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        email = input("Enter your email: ")
        self.sign_in(username, password, email)
    elif option == "4":
        self.contact_information()
    elif option == "5":
        self.plan_for_university()
    elif option == "6":
        self.apply_to_university()
    elif option == "7":
        self.pay_for_university()
    elif option == "8":
        self.assigning_university_based_on_score()
    else:
        print("Thank you for visiting the University Website. Goodbye!")

# this class is about what the website is all about in general.
class University_website:
    def __init__(self):
        # What else does my website do?
        self.greetings = []
        self.create_account = {}
        self.signed_in_users = {}
        self.contact_information = {}
        self.plan_for_university = {}
        self.apply_to_university = {}
        self.pay_for_university = {}
    pass
    def is_valid_email(self, email):
            # Basic email validation
            return "@" in email and "." in email
    
    
    def hash_password(self, password):
        # Hash the password using bcrypt
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password
    def sign_up(self, username, first_name, maiden_name, last_name, password, email, state_of_origin, residential_address, ):
        if username in self.create_account:
            print("Username already exists. Please choose a different username.")
        elif not self.is_valid_email(email):
            print("Invalid email address. Please enter a valid email.")
        else:
            hashed_password = self.hash_password(password)
            self.create_account[username] = {"first_name": first_name, "maiden_name": maiden_name, "last_name": last_name,
                "password": hashed_password, 'email': email, "state_of_origin": state_of_origin, "residential_address":residential_address}
            
            
            full_name = f"{first_name} {last_name}"
            self.contact_information[username] = {
                "full_name": full_name,
                "email": email,
                "state_of_origin": state_of_origin,
                "residential_address": residential_address
            }
            print("Account created successfully!")
            
            
            
    def state_of_origin(self, origin):
        if origin in self.create_account:
            print("State of origin already exists. Please choose a different state.")
        else:
            self.create_account[origin] = {"state_of_origin": origin}
            print("State of origin added successfully!")
        origin = input("your state of origin")
        return origin

    def residential_address(self, address):
        if address in self.create_account:
            print("Residential address already exists. Please choose a different address.")
        else:
            self.create_account[address] = {"residential_address": address}
            print("Residential address added successfully!")
            address = input("your residential address")
            return address

    # correct this sign_in codes 
    def sign_in(self, username, password, email):
        if username in self.create_account or email in self.create_account:
            account = self.create_account.get(username) or self.create_account.get(email)
            if bcrypt.checkpw(password.encode('utf-8'), account['password']):
                print("Sign in successful!")
            else:
                print("Incorrect password. Please try again.")
        else:
            print("Username or email not found. Please sign up.")
        if username in self.signed_in_users or email in self.signed_in_users:
            del self.signed_in_users[username]
            del self.signed_in_users[email]
        # De-authentication logic here
        if username or email in self.sign_in:
            del self.sign_in[username][email]
        return True

#best possible universities
class assign_university:
    def __init__(self) -> None:        
        self.university_lists = []
        self.choose_university = {}
        self. jamb_score = {}
        self.state_of_origin = {}
        self.state_or_residence = {}
        self.assigning_university_based_on_score = {}

        pass
    def choose_university(self, university_lists):
        self.university_lists = university_lists
        return self.university_lists

    def score(self, jamb_score):
        self.jamb_score = jamb_score
        return self.jamb_score 
        self.choose_university[links] = university_url
        print("Link added successfully!")
    pass
# replace values with university website links
def remove_link(self, links):
    if links in self.choose_university:
        del self.choose_university[links]
        print("Link removed successfully!")
    else:
        print("Link not found.")
    pass
def assigning_university_based_on_score(self, score):
                if score >= 250:
                    return ["University A", "University B", "University C"]
                elif score >= 200:
                    return ["University D", "University E", "University F"]
                else:
                    return ["University G", "University H", "University I"]
#apply to the assigned universities 
class apply_for_University_admission:
    def __init__(self):
        self.choose_course = {}      
        self.second_course_choice = {}
        self.third_course_choice = {}
        self.faculty = {}
        self.departments = {}
    def choose_faculty_and_dept(self, choose_course, faculty, departments):
        choose_course = {
            "faculty_of_law": ("law"),
            "faculty_of_engineering": ("civil_engineering", "mechanical_engineering", "chemical_engineering", "agro_engineering"),
            "faculty_of_science": ("biology", "chemistry", "physics", "mathematics"),
            "faculty_of_commerce": ("business_admin", "finance", "marketing", "operations_research"),
            "faculty_of_medicine": ("pharmacy", "nursing", "medical_lab"),
            "faculty_of_social_science": ("psychology", "sociology", "theology")
        }
        print (choose_course)
        for faculty, departments in choose_course.items():
            departments = choose_course[faculty]
            print(f"Available departments in {faculty}: {', '.join(departments)}")
            chosen_department = input("Please choose a department: ")
            if chosen_department in departments:  
                self.choose_course[faculty] = chosen_department 
                print(f"You have been assigned to the {faculty} in the {chosen_department} department.")
            else:
                print("Invalid department chosen. Please try again.")
            return self.choose_course
        
    def second_course_choice(self):
        print("Please choose your second course.")
        self.handle_course_selection()
        return self.second_course
        
        # after the first course, students can choose their second course
        pass
    def third_course_choice(self):
        print("Please choose your third course.")
        self.handle_course_selection()
        return self.third_course
        # after the second course, students can choose their third course
        pass
    
#Course chosen has to be offered by University of choice
# Ignore or Accept suggested university
# if ignore choose university and check if they offer the course you selected     
# if offered Submit Jamb_score, O'level results with contact information.
# Turn on Email and sms notification for reminder 
# Be able to track admission progress and new updates
    def handle_university_application(self):
        
        
        pass





