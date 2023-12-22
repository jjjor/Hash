import random
import time
import threading

class Sensor:
    def __init__(self, sensor_id, readings):
        self.id = sensor_id
        self.readings = readings

    def __str__(self):
        return f"Sensor {self.id}\nReadings {self.readings}"

    def add_reading(self, reading):
        self.readings.append(reading)


class SensorData:
    def __init__(self, sensor_id, timestamp, value):
        self.id = sensor_id
        self.timestamp = timestamp
        self.value = value

    def __str__(self):
        return f"Sensor: {self.id} - Timestamp: {self.timestamp} - Value: {self.value}"


class HashTable:
    def __init__(self, lenght):
        self.lenght = lenght
        self.table = [None] * lenght
        self.lock = threading.Lock()

    def hash(self, sensor_id):
        return hash(sensor_id) % self.lenght

    def push(self, data):
        key = self.hash(data.id)
        with self.lock:
            if self.table[key] is None:
                self.table[key] = [data]
            else:
                self.table[key].append(data)

    def search(self, sensor_id):
        key = self.hash(sensor_id)
        with self.lock:
            return self.table[key]

    def __str__(self):
        return str(self.table)


def process_sensor_data(sensor, table_hash, qtd):
    for _ in range(qtd):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        value = random.uniform(20.0, 30.0)
        data = SensorData(sensor.id, timestamp, value)

        table_hash.push(data)
        time.sleep(random.uniform(1, 3))


if __name__ == "__main__":
    lenght_table_hash = int(input("Enter the length of the hash table: "))
    qtd = int(input("Enter the amount of dates to be inserted: "))

    hash_table = HashTable(lenght_table_hash)
    threads = []
    sensors = []

    sensor1 = Sensor(1, [])
    sensor1.add_reading(10)
    sensor2 = Sensor(2, [])
    sensor2.add_reading(20)
    sensor3 = Sensor(3, [])
    sensor3.add_reading(30)

    sensors.extend([sensor1, sensor2, sensor3])

    for sensor in sensors:
        thread = threading.Thread(
            target=process_sensor_data, args=(sensor, hash_table, qtd))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for sensor in sensors:
        print(sensor)

    print(hash_table)