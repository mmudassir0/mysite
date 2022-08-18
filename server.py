from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     return render_template('index.html',name=username,post_id=post_id)

@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
    
#     return "Form submitted"

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file =database.write(f'\n{email}\t,{subject}\t,{message}')

def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        pint('try again')