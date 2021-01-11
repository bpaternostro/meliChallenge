README:
 - El proceso se ejecuta desde el “main.py” y va a solicitar un ingreso de caracteres separados por "," (sin espacios en blanco).
 - Como la API de Meli únicamente devuelve 50 resultados por "request". El proceso arma un “array” con el ingreso de al menos 3 productos. Luego ejecuta una solicitud por cada producto ingresado.
 - Como no sabía en qué ambiente iba a ser ejecutado el script. Generé una carpeta "output" dentro del proyecto para alojar el archivo ".hyper" resultante.
 - En el table definition:
	- Normalicé todas las respuestas que no disponían del atributo "campo_catalog_listing" = False
	- Debido al separador de decimales. Definí los campos "price" y "original_price" como texto. 
	- Defini como texto, aquellas columnas que contenían embebidas listas de objetos. Esto también se podría haber resuelto creando varias tablas y aplicando JOINS.
 - Las pruebas unitarias se encuentran dentro de la carpeta TEST\Test.py
