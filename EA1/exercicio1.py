from pymongo import MongoClient

from threading import Thread
from random import randint
from time import sleep



client = MongoClient('mongodb://localhost:27017', )
db = client['bancoiot']

def atualiza(timer, temperatura):
    nova_serie_temporal = [timer,temperatura]
    nova_serie_temporal.append({
        'intervalo': timer,
        'valorSensor': temperatura
    })


def ler_sensor1(timer):
    while True:
        
        sensores = db.sensores

        temperatura = randint(30, 40)
        sensor_alarmado = True 
        if temperatura > 38:
            atualiza(
                timer,
                temperatura
            )

        sensores.update_one(
            {'nomeSensor': "sensor 1"},
            {'$set': {
                'valorSensor': temperatura,
                'sensorAlarmado': sensor_alarmado,
            }}
        )

        print(f'sensor 1 está com ' + str(temperatura))

        sleep(timer)
        
def ler_sensor2(timer):
    while True:
        
        sensores = db.sensores

        temperatura = randint(30, 40)
        sensor_alarmado = True 
        if temperatura > 38:
            atualiza(timer,temperatura)

        sensores.update_one(
            {'nomeSensor': "sensor 2"},
            {'$set': {
                'valorSensor': temperatura,
                'sensorAlarmado': sensor_alarmado
            }}
        )

        print(f'sensor 2 está com ' + str(temperatura))

        sleep(timer)
        
def ler_sensor3(timer):
    while True:
        
        sensores = db.sensores

        temperatura = randint(30, 40)
        sensor_alarmado = True 
        if temperatura > 38:
            atualiza(timer,temperatura)

        sensores.update_one(
            {'nomeSensor': "sensor 3"},
            {'$set': {
                'valorSensor': temperatura,
                'sensorAlarmado': sensor_alarmado
            }}
        )

        print(f'sensor 3 está com ' + str(temperatura))

        sleep(timer)
        
        


x = Thread(target=ler_sensor1, args=(1,))
y = Thread(target=ler_sensor2, args=(1,))
z = Thread(target=ler_sensor3, args=(1,))

x.start()
y.start()
z.start()