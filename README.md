# Scraper de clima

Este script utiliza la librería BeautifulSoup para extraer información sobre el clima de una ciudad específica de un sitio web. La información extraída incluye la temperatura, la hora de salida del sol y la hora del atardecer. Los datos son almacenados en una base de datos SQLite3.

## Uso
1. Asegúrate de tener las siguientes dependencias instaladas: `beautifulsoup4`, `sqlite3`, `requests`.
2. Ejecuta el script con Python, proporcionando como argumento la ciudad deseada. Por ejemplo: `python main.py.
3. La información del clima se guardará en una base de datos llamada `db`.

## Personalización
- El script utiliza una URL específica para obtener la información del clima. Si deseas utilizar una URL diferente, cambia la variable `url` en el código.
- La estructura de la tabla en la base de datos se puede modificar editando la función `crear_tabla()`.
- El formato de fecha y hora se puede ajustar modificando la función `formatear_fecha()`.

## Notas
- El script solo extrae información para la ciudad especifica. Si deseas obtener información para varias ciudades, tendrás que ejecutar el script varias veces con diferentes argumentos.
- El script solo extrae información si la información está disponible en el sitio web. Si la información no se encuentra, el script mostrará un mensaje de error y no almacenará ningún dato en la base de datos.
