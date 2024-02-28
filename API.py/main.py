import ui
import api

    

def main():
    continuar = 's'
    while continuar.lower() == 's':
        # Obtener la entrada del usuario
        nombre_departamento, limite_registros = ui.atencion()

        # Obtener datos del CSV
        resultados_df = api.obtener_datos_csv(limite_registros, nombre_departamento) 

        # Mostrar resultados

        # Preguntar al usuario si desea hacer otra consulta
        continuar = input("¿Desea hacer otra consulta? (s/n): ")

if __name__ == "__main__":
    main()
