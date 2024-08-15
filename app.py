from flask import Flask, request, render_template

app = Flask(__name__)

# Variables to store the latest sensor data
latest_dust_density = ""
latest_gas_concentration = ""

@app.route('/')
def index():
    return render_template('index.html', dust_density=latest_dust_density, gas_concentration=latest_gas_concentration)

@app.route('/update', methods=['POST'])
def update():
    global latest_dust_density, latest_gas_concentration
    data = request.form.get('sensor_data')
    if data:
        print(f"Data received at /update endpoint: {data}")  # Debugging line
        if "Dust Density Percentage:" in data:
            latest_dust_density = data.split(': ')[1]  # Extract the percentage value
        elif "Gas Concentration Percentage:" in data:
            latest_gas_concentration = data.split(': ')[1]  # Extract the concentration value
        print(f"Updated Dust Density: {latest_dust_density}, Gas Concentration: {latest_gas_concentration}")  # Debugging line
        return "Data received"
    else:
        return "No data received", 400

@app.route('/data')
def data():
    return f"Dust Density: {latest_dust_density}\nGas Concentration: {latest_gas_concentration}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
