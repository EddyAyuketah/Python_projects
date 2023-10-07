import random
import time
import os

class ManufacturingMonitor:
    def __init__(self, duration):
        self.temperature_sensor = TemperatureSensor()
        self.pressure_sensor = PressureSensor()
        self.vibration_sensor = VibrationSensor()
        self.duration = duration
        self.alert_count = 0

    def monitor(self):
        start_time = time.time()
        while time.time() - start_time < self.duration:
            temperature = self.temperature_sensor.get_temperature()
            pressure = self.pressure_sensor.get_pressure()
            vibration = self.vibration_sensor.get_vibration()

            # Process data and trigger alerts based on thresholds
            if temperature > 70:
                self.trigger_alert("High temperature detected!")
            if pressure > 100:
                self.trigger_alert("High pressure detected!")
            if vibration > 10:
                self.trigger_alert("Excessive vibration detected!")

            clear_console()
            self.display_metrics(temperature, pressure, vibration)
            time.sleep(1)

    def trigger_alert(self, message):
        self.alert_count += 1

    def display_metrics(self, temperature, pressure, vibration):
        print("=" * 30)
        print("Metrics:")
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Pressure: {pressure:.2f} PSI")
        print(f"Vibration: {vibration:.2f} units")
        print(f"Alerts Count: {self.alert_count}")
        print("=" * 30)

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class TemperatureSensor:
    def get_temperature(self):
        # Simulate temperature reading from a sensor
        return random.uniform(50, 90)

class PressureSensor:
    def get_pressure(self):
        # Simulate pressure reading from a sensor
        return random.uniform(80, 120)

class VibrationSensor:
    def get_vibration(self):
        # Simulate vibration reading from a sensor
        return random.uniform(0, 20)

if __name__ == "__main__":
    duration = 60  # Monitor for 1 minute
    monitor = ManufacturingMonitor(duration)
    monitor.monitor()
