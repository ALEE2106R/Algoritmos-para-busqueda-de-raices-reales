import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Definir la función y su derivada
def f(t):
    return (3 * np.exp(0.68 * t)) / (10 * t) - 110

def f_prime(t):
    return (3 * (0.68 * np.exp(0.68 * t) * t - np.exp(0.68 * t))) / (10 * t ** 2)

# Inicializar variables para el método de Newton-Raphson
x_0 = 2  # Aproximación inicial desde t > 1
error_relativo = 1
iteracion = 0

# Crear lista para almacenar los resultados
resultados = []

# Realizar tres iteraciones del método de Newton-Raphson
while iteracion < 3:
    f_x0 = f(x_0)
    f_prime_x0 = f_prime(x_0)
    x_i = x_0 - f_x0 / f_prime_x0
    error_relativo = abs((x_i - x_0) / x_i)

    # Agregar resultados a la lista
    resultados.append([iteracion + 1, x_0, f_x0, f_prime_x0, x_i, error_relativo])

    # Actualizar para la siguiente iteración
    x_0 = x_i
    iteracion += 1

# Convertir los resultados en un DataFrame
columnas = ['Iteración', 'x_0', 'f(x_0)', "f'(x_0)", 'x_i', 'Error relativo']
df_resultados = pd.DataFrame(resultados, columns=columnas)

# Mostrar la tabla de resultados en una ventana emergente
def mostrar_tabla():
    ventana = tk.Tk()
    ventana.title("Resultados de Aproximación - Newton-Raphson")

    tabla = ttk.Treeview(ventana)
    tabla['columns'] = columnas
    tabla.column('#0', width=0, stretch=tk.NO)
    tabla.heading('#0', text='', anchor=tk.CENTER)
    
    for columna in columnas:
        tabla.column(columna, anchor=tk.CENTER, width=120)
        tabla.heading(columna, text=columna, anchor=tk.CENTER)
    
    for index, row in df_resultados.iterrows():
        tabla.insert(parent='', index='end', iid=index, values=list(row))
    
    tabla.pack()
    ventana.mainloop()

mostrar_tabla()

# Graficar la función para visualizar la solución
t_values = np.linspace(1, 10, 400)
p_values = (3 * np.exp(0.68 * t_values)) / (10 * t_values)

plt.figure(figsize=(10, 6))
plt.plot(t_values, p_values, label='p(t) = (3e^(0.68t)) / (10t)', color='b')
plt.axhline(y=110, color='r', linestyle='--', label='Población de 110 moscas blancas')
plt.xlabel('Días (t)')
plt.ylabel('Población de Moscas Blancas')
plt.title('Evolución de la Población de Moscas Blancas en Función del Tiempo')
plt.legend()
plt.grid()
plt.show()
