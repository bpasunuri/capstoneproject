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

def GetEmp():
    if request.method == 'GET':
        return render_template('GetEmp.html')
    elif request.method == 'POST':
        try:
            with db_conn.cursor() as cursor:
                employee_ids = request.form.get('emp_ids', '').split(',')
                location = request.form.get('location', '')

                conditions = []
                params = []

                if employee_ids:
                    conditions.append('emp_id IN %s')
                    params.append(tuple(employee_ids))

                if location:
                    conditions.append('location = %s')
                    params.append(location)

                where_clause = ' AND '.join(conditions)
                if where_clause:
                    where_clause = 'WHERE ' + where_clause

                select_sql = f"SELECT * FROM employee {where_clause}"
                cursor.execute(select_sql, params)
                result = cursor.fetchall()
                return render_template('GetEmpOutput.html', data=result)
        except Exception as e:
            return str(e)

            
if __name__ == '__main__':
    # Set the template folder
    app.template_folder = 'templates'
    
    # Run the Flask application
    app.run(host='0.0.0.0', port=8081, debug=True)