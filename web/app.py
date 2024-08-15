from flask import Flask, request, render_template

app = Flask(__name__)

# Variables to store the latest sensor data
latest_voltage = ""
latest_sensor_value = ""

@app.route('/')
def index():
    return render_template('index.html', voltage=latest_voltage, sensor_value=latest_sensor_value)

@app.route('/update', methods=['POST'])
def update():
    global latest_voltage, latest_sensor_value
    data = request.form.get('sensor_data')
    if data:
        # Split the data into voltage and sensor value (assuming a specific format)
        if "Voltage:" in data:
            latest_voltage = data
        else:
            latest_sensor_value = data
        print(f"Received sensor data: {data}")
        return "Data received"
    else:
        return "No data received", 400

@app.route('/data')
def data():
    return f"{latest_voltage}\n{latest_sensor_value}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Ensure the port matches your Python script
