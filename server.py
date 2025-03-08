from flask import Flask
import os
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests from different origins



@app.route('/send_sos')
def send_sos():
    script_path = "C:/Users/devda/OneDrive/Desktop/alvas/sos_alert.py"  # Update the path if needed

    if os.path.exists(script_path):  # Check if script exists
        result = os.system(f'python "{script_path}"')  # Run the script
        return "🚀 SOS Alert Sent Successfully!" if result == 0 else "❌ Error Sending SOS"
    else:
        return "❌ Error: sos_alert.py not found!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Allow external access if needed
