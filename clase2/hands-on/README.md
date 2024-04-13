# Hands-on - Creando imágenes de Docker

El uso de contenedores es una de las formas más populares en la actualidad para implementar servicios de Aprendizaje 
Automático. Esto se debe a que los contenedores proporcionan un entorno de ejecución aislado y consistente que 
permite a los desarrolladores encapsular todas las dependencias y configuraciones necesarias para ejecutar sus 
aplicaciones de manera confiable en cualquier entorno.

Al crear imágenes de Docker para proyectos de Aprendizaje Automático, podemos asegurarnos de que nuestras 
aplicaciones se ejecuten de manera uniforme y reproducible en diferentes entornos, desde el desarrollo local hasta 
la producción en la nube. Las imágenes de Docker contienen todo lo necesario para ejecutar una aplicación, incluidas 
las librerias, las dependencias del sistema operativo y el propio código de la aplicación.

Además, el uso de imágenes de Docker facilita la colaboración entre equipos de desarrollo y operaciones, ya que los 
desarrolladores pueden compartir fácilmente el entorno de ejecución de sus aplicaciones sin preocuparse por las 
diferencias en las configuraciones locales de cada desarrollador. Esto mejora la eficiencia y la consistencia en 
todo el ciclo de vida del desarrollo de software.

Para este hands-on, vamos a crear contenedores de Docker para cuatro casos, desde los más simples hasta los más 
complejos:

1. **Ejemplo sencillo**: Construiremos una imagen basada en la imagen oficial de Python 3.10 y ejecutaremos un script 
tipo "Hola, mundo".
2. **Servidor web sencillo**: Este ejemplo es un poco más complejo. Utilizaremos la misma imagen de Python, 
instalaremos Flask usando un archivo requirements.txt y crearemos una aplicación web básica.
3. **Wordpress + MariaDB**: En este caso, utilizaremos Docker Compose para cargar dos contenedores por separado. Uno 
contendrá la base de datos MariaDB y el otro el gestor de contenidos Wordpress. MariaDB es necesaria para que funcione 
Wordpress, por lo que configuraremos la conexión entre ellos. Utilizaremos las imágenes oficiales de ambos servicios.
4. **Servicio de Aprendizaje Automático + PostgreSQL**: En este caso, crearemos un servicio de Aprendizaje Automático 
utilizando Docker Compose. Utilizaremos dos servicios: uno para la base de datos (PostgreSQL), que cargaremos con 
datos, y otro para el servicio web utilizando Streamlit, que proporcionará un predictor de aumento de sueldos para 
empleados de una empresa ficticia. Utilizaremos la imagen oficial de PostgreSQL, pero crearemos nuestra propia imagen 
para el servicio de Aprendizaje Automático a partir de la imagen oficial de Python.
