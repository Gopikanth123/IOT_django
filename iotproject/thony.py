import machine
import urequests
import ujson
import time

# Database and server details
DB_URL = "http://your_server_url/insert_data.php"
DB_HEADERS = {"Content-Type": "application/json"}
DB_DATA = {
    "can_number": "your_can_number",
    "name": "your_name",
    "fat": 0.0,
    "snf": 0.0,
    "clr": 0.0,
    "adc_water": 0.0,
}

# # ADC Pin on Pyboard
# ADC_PIN = "X1"

# def read_adc(pin):
#     adc = machine.ADC(pin)
#     value = adc.read()
#     return value

def send_data_to_server(data, csrf_token):
    response = urequests.post(DB_URL, headers=DB_HEADERS, data=ujson.dumps(data))
    return response

def main():
    while True:
        # Read ADC values
        # adc_value = read_adc(ADC_PIN)

        # Update data with ADC value
        # DB_DATA["adc_water"] = adc_value

        # Send data to the server
        csrf_token = "your_csrf_token"  # Replace with your actual CSRF token
        received_data = send_data_to_server(DB_DATA, csrf_token)

        print("Data sent to server. Response:", received_data.text)

        # Wait for some time before the next reading
        time.sleep(60)  # Adjust the interval as needed

if __name__ == "__main__":
    main()
