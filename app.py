import jinja2
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
data = {"name": None}


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/thankyou')
def thank_you_page():  # put application's code here
    return render_template("thankyou.html", name=data["name"])


@app.route('/<string:page_name>')
def html_page(page_name):  # put application's code here
    try:
        return render_template("{}.html".format(page_name))
    except jinja2.exceptions.TemplateNotFound:
        return "Lol!"


def write_to_csv(data_to_write):
    with open("database.csv", newline="", mode="a") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data_to_write["name"], data_to_write["email"], data_to_write["subject"], data_to_write["message"]])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    global data
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/thankyou")


if __name__ == '__main__':
    app.run()
