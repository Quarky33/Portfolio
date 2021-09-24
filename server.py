from flask import Flask, render_template, request, redirect
import csv
from csv import DictWriter

app = Flask(__name__)

# print(__name__)

@app.route('/index.html')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode= 'a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode= 'a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter= ',', quotechar='"' , quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])  

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        try:
           data = request.form.to_dict()
           write_to_csv(data)
           return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'

    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username']),
    #                     request.form['password']):
    #         return log_the_user_in(request.form['username...000'])
    #     else:
    #         error = 'Invalid username and/or password'
    # return render_template('login.html',error = error)
        



# @app.route('/about.html')
# def about():
#     return render_template('about.html',)

# @app.route('/services.html')
# def services():
#     return render_template('services.html',)

# @app.route('/contact.html')
# def contacts():
#     return render_template('contact.html',)

# @app.route('/components.html')
# def componants():
#     return render_template('components.html',)

# @app.route('/project.html')
# def projects():
#     return render_template('project.html',)

# @app.route("/favicon.ico")
# def blog():
#     return "I LOVE English breakfast!!!"

