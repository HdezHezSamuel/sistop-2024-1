#!/usr/bin/python3
import threading
import time
import random

num_jugadores = 3
multiplex = threading.Semaphore(num_jugadores)
activos = []
mut_activos = threading.Semaphore(1)

def multiplexado(x):
    print('%02d: Inicio ejecución' % x)
    multiplex.acquire()

    # ↓ Manejo de mutex para modificar el arreglo activos
    mut_activos.acquire()
    activos.append(x)
    mut_activos.release()

    print('%02d: inicio porción compartida; estamos: %s' % (x, activos))
    time.sleep(random.random())

    # ↓ Manejo de mutex para modificar el arreglo activos
    mut_activos.acquire()
    activos.remove(x)
    mut_activos.release()

    print('%02d: termino porción compartida' % x)
    multiplex.release()

print('- = { ¡ COMBATE MULTIJUGADOR ! } = -')
print('¡Bienvenidos concursantes! Ahora van a agarrarse a catorrazos...')
print('¡De %d en %d!' % (num_jugadores, num_jugadores))
for i in range(10):
    threading.Thread(target=multiplexado, args=[i]).start()
