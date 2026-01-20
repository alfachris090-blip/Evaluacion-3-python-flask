#programa para calcular edad futura y años transcurridos
print("=== calculadora de edades===")
# pedir datos al usuario
nombre=input("¿cual es tu nombre?")
edad_actual=int(input("cuantos años tienes?")) #convertimos el texto a numeros
#hacer calculos
edad_en_5 = edad_actual + 5
edad_hace_3 = edad_actual - 3
#mostrar resultados
print("¡hola,",nombre,"aqui estan tus datos:!")
print("Edad actual:", edad_actual,"años")
print("edad en 5 años:", edad_en_5,"años")
print("edad hace 3 años:",edad_hace_3,"años")