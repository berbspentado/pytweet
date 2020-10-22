from flask import Flask, render_template, request, redirect    #importing necessary flask modules
from .app import app                    #connection to app.py
from .database import db                #connection to db                              
from .models.models import User  # importing the models



@app.route("/")
def home():
    return render_template("index.html")
      


@app.route("/register")
def register():
    return render_template("register.html")
