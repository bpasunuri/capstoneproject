from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb
)
output = {}
table = 'employee'

# Function to upload image to S3 bucket
def upload_to_s3(file, bucket_name, key):
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        s3.upload_fileobj(file, bucket_name, key)
        return True
    except Exception as e:
        print("Error uploading file to S3:", e)
        return False

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddEmp.html')

@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')

@app.route("/addemp", methods=['POST'])
def AddEmp():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    pri_skill = request.form['pri_skill']
    location = request.form['location']
    emp_image_file = request.files['emp_image_file']

    insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    if emp_image_file.filename == "":
        return "Please select a file"

    try:
        cursor.execute(insert_sql, (emp_id, first_name, last_name, pri_skill, location))
        db_conn.commit()
        emp_name = "" + first_name + " " + last_name
        
        # Upload image file to S3
        emp_image_file_name_in_s3 = "emp-id-" + str(emp_id) + "_image_file"
        if upload_to_s3(emp_image_file, bucket, emp_image_file_name_in_s3):
            print("File uploaded successfully to S3!")
        else:
            return "Failed to upload file to S3"

    except Exception as e:
        return str(e)

    finally:
        cursor.close()

    print("All modifications done...")
    return render_template('AddEmpOutput.html', name=emp_name)

@app.route("/getemp", methods=['POST'])
def GetEmpInfo():
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        try:
            with db_conn.cursor() as cursor:
                select_sql = f"SELECT * FROM employee WHERE emp_id = %s"
                cursor.execute(select_sql, (emp_id,))
                result = cursor.fetchone()
                if result:
                    # Render a template to display employee information
                    return render_template('EmpInfo.html', data=result)
                else:
                    return "Employee not found"
        except Exception as e:
            return str(e)

            
if __name__ == '__main__':
    # Set the template folder
    app.template_folder = 'templates'
    
    # Run the Flask application
    app.run(host='0.0.0.0', port=8081, debug=True)