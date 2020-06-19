# CC3M2-Test1
Debería poder ejecutarse de la misma manera que el repositorio de Anthony Luzquiños. No es necesario entrar a venv. 
Instalación de dependencias:
```console
$ pip install -r requirements.txt
```
Si no se puede instalar glfw, usar:
```console
sudo apt-get install libglfw3
sudo apt-get install libglfw3-dev
```
Y reintentar `pip`.  
Permisos de ejecución:
```console
$ chmod u+x main.sh
```
Ejecución:
```console
$ ./main.sh
```
O ejecutar directamente `src/index.py`. El código con los puntos y la transformación está en `src/controllers/window.py`.

Presionar izquierda o derecha para girar la vista. Cualquier otra tecla para girar el cubo.
