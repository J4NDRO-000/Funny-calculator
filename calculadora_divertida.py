#Proyecto vibecodeado zD, pero tiene su toque xd

import math
import webbrowser
import os
import re
import time
from datetime import datetime

def limpiar_pantalla():
    """Función para limpiar la pantalla"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_bienvenida():
    """Muestra mensaje de bienvenida con arte ASCII"""
    print("=" * 60)
    print("    🧮 CALCULADORA SÚPER INTELIGENTE 🧮")
    print("=" * 60)
    print("¡Bienvenido a la calculadora más cool del mundo!")
    print("Creada por: Jandrou")  
    print("-" * 60)

def detectar_formula_gauss(expresion):
    """
    Detecta si la expresión sigue el patrón n(n+1)/2 con números reales
    Ejemplos: 5(5+1)/2, 100*(100+1)/2, (50*(50+1))/2, 100(1+100)/2
    Permite permutaciones: n+1 o 1+n
    """
    # Limpiar espacios
    expr = expresion.replace(" ", "")
    
    # Patrones para detectar n(n+1)/2 y n(1+n)/2 con números
    patrones = [
        # Formato n(n+1)/2
        r'(\d+)\((\1)\+1\)/2',           # 5(5+1)/2
        r'(\d+)\*\((\1)\+1\)/2',         # 5*(5+1)/2  
        r'\((\d+)\*\((\1)\+1\)\)/2',     # (5*(5+1))/2
        
        # Formato n(1+n)/2 - números permutados
        r'(\d+)\(1\+(\1)\)/2',           # 5(1+5)/2
        r'(\d+)\*\(1\+(\1)\)/2',         # 5*(1+5)/2  
        r'\((\d+)\*\(1\+(\1)\)\)/2',     # (5*(1+5))/2
    ]
    
    for patron in patrones:
        match = re.search(patron, expr)
        if match:
            # Verificar que los números coincidan (n debe ser igual en ambos lugares)
            grupos = match.groups()
            if len(grupos) >= 2 and grupos[0] == grupos[1]:
                return True, int(grupos[0])
    
    return False, None

def activar_easter_egg(numero):
    """Activa el easter egg y abre la página de la NASA"""
    resultado_gauss = numero * (numero + 1) // 2
    
    print("\n" + "🚀" * 20)
    print("¡WOOOOW! ¡Has descubierto el EASTER EGG secreto!")
    print(f"¡Has usado la fórmula de GAUSS con n={numero}!")
    print(f"El resultado es {resultado_gauss} (suma de 1 hasta {numero})")
    print("¡Esta es la fórmula más elegante de las matemáticas!")
    print("🚀" * 20)
    print("\n¡Te mereces trabajar en la NASA! Abriendo página de empleos...")
    
    # Countdown dramático antes de abrir la página
    print("\n🎯 Preparando para lanzarte al espacio en:")
    for i in range(10, 0, -1):
        print(f"⏰ {i}...", end="", flush=True)
        time.sleep(1)
    print("\n🚀 ¡DESPEGUE!")
    
    try:
        webbrowser.open('https://www.nasa.gov/careers/')
        print("✅ ¡Página de empleos de NASA abierta!")
        print("🌟 ¡Buena suerte, futuro astronauta!")
    except:
        print("❌ No se pudo abrir el navegador, pero aquí está el link:")
        print("🔗 https://www.nasa.gov/careers/")
    
    input("\nPresiona ENTER para regresar a la realidad terrestre...")

def calculadora_basica():
    """Calculadora básica para menores de 18"""
    while True:
        limpiar_pantalla()
        print("\n📱 CALCULADORA BÁSICA (Modo Niño)")
        print("Operaciones disponibles: +, -, *, /")
        print("Escribe 'menu' para volver al menú principal")
        print("Escribe 'salir' para cerrar la calculadora")
        print("-" * 40)
        
        while True:
            try:
                expresion = input("\n➤ Ingresa tu operación: ").strip()
                
                if expresion.lower() == 'menu':
                    return 'menu'
                elif expresion.lower() == 'salir':
                    return 'salir'
                    
                # Verificar easter egg con la fórmula de Gauss
                es_gauss, numero = detectar_formula_gauss(expresion)
                if es_gauss:
                    activar_easter_egg(numero)
                    continue
                
                # Evaluar expresión básica (solo operaciones seguras)
                if any(op in expresion for op in ['+', '-', '*', '/']):
                    # Verificar que solo contenga números y operadores básicos
                    caracteres_permitidos = "0123456789+-*/.() "
                    if all(c in caracteres_permitidos for c in expresion):
                        resultado = eval(expresion)
                        print(f"✅ Resultado: {resultado}")
                    else:
                        print("❌ Solo se permiten operaciones básicas (+, -, *, /)")
                else:
                    print("❌ Ingresa una operación válida (+, -, *, /)")
                    
            except ZeroDivisionError:
                print("❌ Error: No se puede dividir por cero")
            except:
                print("❌ Error: Operación inválida")

def calculadora_cientifica():
    """Calculadora científica para mayores de 18"""
    while True:
        limpiar_pantalla()
        print("\n🔬 CALCULADORA CIENTÍFICA (Modo Adulto Responsable)")
        print("Funciones disponibles:")
        print("• Básicas: +, -, *, /")
        print("• Científicas: sin(), cos(), tan(), log(), sqrt(), pow()")
        print("• Constantes: pi, e")
        print("• Ejemplo: sin(pi/2), sqrt(16), log(100)")
        print("• Escribe 'menu' para volver al menú principal")
        print("• Escribe 'salir' para cerrar la calculadora")
        print("-" * 50)
        
        while True:
            try:
                expresion = input("\n➤ Ingresa tu operación: ").strip()
                
                if expresion.lower() == 'menu':
                    return 'menu'
                elif expresion.lower() == 'salir':
                    return 'salir'
                    
                # Verificar easter egg con la fórmula de Gauss
                es_gauss, numero = detectar_formula_gauss(expresion)
                if es_gauss:
                    activar_easter_egg(numero)
                    continue
                
                # Preparar el entorno para funciones matemáticas
                funciones_matematicas = {
                    'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                    'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
                    'log': math.log, 'log10': math.log10,
                    'sqrt': math.sqrt, 'pow': pow,
                    'pi': math.pi, 'e': math.e,
                    'abs': abs, 'round': round
                }
                
                # Evaluar la expresión con las funciones matemáticas disponibles
                resultado = eval(expresion, {"__builtins__": {}}, funciones_matematicas)
                print(f"✅ Resultado: {resultado}")
                    
            except ZeroDivisionError:
                print("❌ Error: No se puede dividir por cero")
            except NameError as e:
                print(f"❌ Error: Función no reconocida. Funciones disponibles: sin, cos, tan, log, sqrt, etc.")
            except:
                print("❌ Error: Operación inválida")

def obtener_edad():
    """Obtiene la edad del usuario con validación"""
    while True:
        try:
            edad = int(input("🎂 ¿Cuál es tu edad? "))
            if edad < 0:
                print("❌ La edad no puede ser negativa. ¡No viajes en el tiempo! -_-")
                continue
            elif edad > 150:
                print("❌ ¿En serio? ¿Más de 150 años? ._.")
                continue
            return edad
        except ValueError:
            print("❌ Por favor, ingresa un número válido")

def mostrar_menu_principal():
    """Muestra el menú principal"""
    limpiar_pantalla()
    print("\n" + "=" * 50)
    print("           🏠 MENÚ PRINCIPAL")
    print("=" * 50)
    print("1. 📱 Calculadora Básica")
    print("2. 🔬 Calculadora Científica") 
    print("3. 🎂 Cambiar Edad")
    print("4. ❌ Salir")
    print("-" * 50)

def main():
    """Función principal con navegación completa"""
    limpiar_pantalla()
    mostrar_bienvenida()
    
    # Obtener edad inicial del usuario
    edad = obtener_edad()
    
    while True:
        mostrar_menu_principal()
        
        try:
            opcion = input("➤ Selecciona una opción (1-4): ").strip()
            
            if opcion == "1":
                # Calculadora básica
                print(f"\n📱 Accediendo a calculadora básica...")
                input("Presiona ENTER para continuar...")
                resultado = calculadora_basica()
                if resultado == 'salir':
                    break
                    
            elif opcion == "2":
                # Calculadora científica
                if edad >= 18:
                    print(f"\n🔬 Accediendo a calculadora científica...")
                    input("Presiona ENTER para continuar...")
                    resultado = calculadora_cientifica()
                    if resultado == 'salir':
                        break
                else:
                    print(f"\n❌ Lo siento, necesitas ser mayor de 18 años.")
                    print(f"Tu edad actual: {edad} años")
                    print("Pero hey, ¡la calculadora básica es súper divertida también! 😄, igual puedes cambiar tu edad ¬_¬")
                    input("Presiona ENTER para continuar...")
                    
            elif opcion == "3":
                # Cambiar edad
                print("\n🎂 Cambiando edad...")
                edad = obtener_edad()
                print(f"✅ Edad actualizada a {edad} años")
                input("Presiona ENTER para continuar...")
                
            elif opcion == "4":
                # Salir
                break
                
            else:
                print("❌ Opción inválida. Por favor selecciona 1, 2, 3 o 4.")
                input("Presiona ENTER para continuar...")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except:
            print("❌ Error inesperado. Intenta de nuevo.")
            input("Presiona ENTER para continuar...")
    
    # Mensaje de despedida
    limpiar_pantalla()
    print("\n" + "=" * 60)
    print("¡Gracias por usar la Calculadora Súper Inteligente!")
    print("¡Que tengas un día matemáticamente perfecto! 🧮✨")
    print("Creada con ❤️ por Jandro (Alejandro)")
    print("=" * 60)
    print("\n¡Presiona cualquier tecla para cerrar!")
    input()

if __name__ == "__main__":
    main()