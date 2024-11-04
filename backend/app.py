from flask import Flask, request, jsonify, send_file
import psycopg2
from psycopg2 import sql
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os
import uuid

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)
DB_URL = 'postgresql://postgres:postgres@localhost:5432/user_db'

UPLOAD_FOLDER = 'Documents'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 



def db_connection():
    try:
        connection = psycopg2.connect(DB_URL)
        return connection
    except Exception as e:
        print(f"Database connection error: {e}")
        return None



@app.route('/register', methods=['POST'])
def register():
    # Get form data
    email = request.form.get('email')
    password = request.form.get('password')

    with db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql.SQL("SELECT * FROM user_auth WHERE email = %s"), (email,))
            user = cursor.fetchone()

            if user:
                return jsonify({"message": "User already exists"}), 400

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            cursor.execute(
                sql.SQL("INSERT INTO user_auth (email, password) VALUES (%s, %s)"),
                (email, hashed_password)
            )
            connection.commit()

    return jsonify({"message": "User registered successfully"}), 201



@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')  
    password = data.get('password')

    with db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql.SQL("SELECT password FROM user_auth WHERE email = %s"), (email,))
            user = cursor.fetchone()

            if user and bcrypt.check_password_hash(user[0], password):
                return jsonify({"message": "Login successful"}), 200

    return jsonify({"message": "Invalid credentials"}), 401


@app.route('/upload_details', methods=['POST'])
def upload_details():
    try:    
        # Check if the 'resume' file is in the request
        if 'resume' not in request.files:
            print("No file part") 
            return jsonify({"message": "No file uploaded"   }), 400
        
        file = request.files['resume']  # Use 'resume' instead of 'file'
        
        # Check if the file has a filename
        if file.filename == '':
            print("No file selected")
            return jsonify({"message": "No file selected"}), 400

        # Save the file to the specified local filesystem
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Collect other form data
        form_data = request.form.to_dict()
        print(file_path)
        print(form_data)

        # Add the file path to the form data (optional, if needed in DB)
        form_data['resume'] = file_path

        # Insert data into the database
        conn = db_connection()
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO user_details ( resume, first_name, last_name, email, phone_number, address,education,college ,year_of_passing,technical_skills,internship_experience_in_months,experience,position,company_name,notice_period)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            form_data.get('resume'),
            form_data.get('firstName'),
            form_data.get('lastName'),
            form_data.get('email'),
            form_data.get('phone'),
            form_data.get('address'),
            form_data.get('education'),
            form_data.get('college'),
            form_data.get('yearPassing'),
            form_data.get('technicalSkills'),
            form_data.get('internExperience'),
            form_data.get('experience'),
            form_data.get('position'),
            form_data.get('companyName'),
            form_data.get('noticePeriod'),
            
            
        ))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Resume and details uploaded successfully!"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "Error uploading data"}), 500


@app.route('/api/user_details/<email>', methods=['GET'])
def get_user_details(email):
    with db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM user_details WHERE email = %s", (email,))
            result = cursor.fetchone()

    if result:
        user_details = {
            "id": result[0],
            "resume": result[1],
            "first_name": result[2],
            "last_name": result[3],
            "email": result[4],
            "phone_number": result[5],
            "address": result[6],
            "education": result[7],
            "college": result[8],
            "year_of_passing": result[9],
            "technical_skills": result[10],
            "internship_experience_in_months": result[11],
            "experience": result[12],
            "position": result[13],
            "company_name": result[14],
            "notice_period": result[15],
        }
        return jsonify(user_details), 200
    else:
        return jsonify({'error': 'User details not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
