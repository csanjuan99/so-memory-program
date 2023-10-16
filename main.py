import tkinter as tk
import numpy as np


def sumar_matrices():
    # Generar matrices aleatorias de 10000x10000
    matriz1 = np.random.rand(10000, 10000)
    matriz2 = np.random.rand(10000, 10000)

    # Sumar las matrices
    resultado = matriz1 + matriz2

    # Guardar el resultado en un archivo CSV (opcional)
    np.savetxt("resultado.csv", resultado, delimiter=",")

    # Mostrar un mensaje de éxito
    resultado_label.config(text="Matrices sumadas y resultado guardado en 'resultado.csv'")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sumar Matrices")

# Crear un botón para realizar la suma
sumar_boton = tk.Button(ventana, text="Sumar Matrices", command=sumar_matrices)
sumar_boton.pack(pady=20)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()
