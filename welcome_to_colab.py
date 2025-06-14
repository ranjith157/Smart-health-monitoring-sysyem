




import random
import time
import csv
from datetime import datetime

# Function to simulate sensor readings
def get_sensor_data():
    heart_rate = random.randint(50, 120)      # beats per minute
    temperature = round(random.uniform(95.0, 103.0), 1)  # Fahrenheit
    spo2 = random.randint(85, 100)            # SpO2 percentage
    return heart_rate, temperature, spo2

# Function to analyze and determine if any vitals are abnormal
def analyze_data(hr, temp, spo2):
    alerts = []
    if hr < 60 or hr > 100:
        alerts.append(f"⚠️ Abnormal Heart Rate: {hr} BPM")
    if temp < 97.0 or temp > 99.5:
        alerts.append(f"⚠️ Abnormal Temperature: {temp} °F")
    if spo2 < 95:
        alerts.append(f"⚠️ Low SpO2 Level: {spo2}%")
    return alerts

# Function to log data
def log_data(hr, temp, spo2, alerts):
    with open("health_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([now, hr, temp, spo2, "; ".join(alerts)])

# Main loop
print("🔄 Starting Smart Health Monitoring System...\n")
print("Timestamp\t\tHeartRate\tTemp(F)\tSpO2\tAlerts")

try:
    while True:
        hr, temp, spo2 = get_sensor_data()
        alerts = analyze_data(hr, temp, spo2)
        log_data(hr, temp, spo2, alerts)
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\t{hr}\t\t{temp}\t{spo2}\t{' | '.join(alerts) if alerts else '✔ Normal'}")
        time.sleep(5)  # check every 5 seconds

except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped by user.")



seconds_in_a_day = 24 * 60 * 60
seconds_in_a_day



seconds_in_a_week = 7 * seconds_in_a_day
seconds_in_a_week



import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

fig = plt.figure(figsize=(4, 3), facecolor='w')
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Sample Visualization", fontsize=10)

data = io.BytesIO()
plt.savefig(data)
image = F"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Sample Visualization"
display.display(display.Markdown(F"""![{alt}]({image})"""))
plt.close(fig)

