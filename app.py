from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    
    with open('reports.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            data.get('firstName'),
            data.get('lastName'),
            data.get('email'),
            data.get('phone'),
            data.get('message'),
            data.get('victim'),
            data.get('witness')
        ])
    
    return jsonify({'message': 'Data saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)
