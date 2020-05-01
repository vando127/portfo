from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def func():
    return render_template("index.html")


@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def sub():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            dbcsv(data)
            return redirect('./thank_you.html')
        except:
            return "Data not saved to database."
    else:
        return 'check your code idiot'


def db(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def dbcsv(data):
    with open('database.csv', 'a', newline='') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
