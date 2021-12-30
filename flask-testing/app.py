from os import link
from scraper import scr
from flask import Flask,render_template,request,send_file
import requests
from bs4 import BeautifulSoup
import csv
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    link=request.form['text']
    values=scr(link)
    return render_template('download.html',value=values,filename='data.csv')

@app.route('/download/')
def download():
    return send_file('data.csv',attachment_filename='data.csv')
        