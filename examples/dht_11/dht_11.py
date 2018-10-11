import time

import Adafruit_DHT as DHT

# GPIO Pin number
DHT_SENSOR_PIN = 4

# Sensor type
DHT_SENSOR = DHT.DHT11

while True:
    humidity, temperature = DHT.read_retry(DHT_SENSOR, DHT_SENSOR_PIN)

    print ('Humidity: ' + str(humidity))
    print ('Temperature: ' + str(temperature))

    # Five seconds between each reading
    time.sleep(5)