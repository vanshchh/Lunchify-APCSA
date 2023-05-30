#Made by Vansh Chhabra and Zachary Cheng 

from flask import Flask, request, render_template
import webbrowser
import smtplib
from email.mime.text import MIMEText

'''
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()

subject = "Lunch Orders"
body = "This is the body of the text message"
sender = "sender@gmail.com"
recipients = ["recipient1@gmail.com"]
password = "password"

send_email(subject, body, sender, recipients, password)
'''

app = Flask(__name__)

id_food = {}

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/order')
def info():
    return render_template('order.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/order', methods=['POST'])
def id_num_food():
    #open file to add order to it
    f = open('order.txt', 'a')
    
    #get ID from user
    id = request.form['id']

    if id == '':
        f.close()
        return render_template('order.html')
    
    #checking if ID is in dictionary
    if id in id_food.keys():

        #getting what the user ordered
        food_type = request.form['food_type']
        #
        val = id_food[id]
        val += ", " + food_type
        id_food[id] = val
        lst = val.split(",")
        if len(lst) > 1:
            pay = len(lst) - 1
        f.write(id + ": " + val + "\n")
        f.close()
        return render_template('order.html', pay=pay)
    
    food_type = request.form['food_type']
    id_food[id] = food_type 
    f.write(id + ": " + food_type + "\n")
    f.close()

    return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)