from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

# Define the CSV file path
CSV_FILE = 'complaints.csv'

# Create the CSV file and add headers if it doesn't exist
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['First Name', 'Last Name', 'Email', 'Phone', 'Message'])

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        print(f"Received data: {data}")  # Log received data
        
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([data['firstName'], data['lastName'], data['email'], data['phone'], data['message']])
        
        return jsonify({'message': 'Data saved successfully'}), 200
    except Exception as e:
        print(f"Error: {e}")  # Log the error
        return jsonify({'message': 'Error occurred', 'error': str(e)}), 500

if __name__ == '__main__':
    initialize_csv()  # Ensure the CSV file is initialized
    app.run(debug=True)
