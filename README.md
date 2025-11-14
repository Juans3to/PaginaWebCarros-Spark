## Pagina Web Carros - Spark

En este repositorio se encuentran los paso a seguir para ejecutar lo relacionado con Spark.

Para probarlo puede usar el vagrantfile que se encuentra adjunto y levantar la maquina virtual o usar la de su preferencia (Puede que haya que acomodar direcciones ip para ciertos comandos en tal caso).

Nota. Importante. Revisar el siguiente repositorio también:
https://github.com/Joseph46832/proyecto-docker

### Paso 1 ⬇️:

Clonar el repositorio:

```bash
git clone https://github.com/Juans3to/PaginaWebCarros-Spark.git
```

Descargar spark dentro de la carpeta. Visite el siguiente enlace para descargar la version que más se adapte a su comodidad:
https://dlcdn.apache.org/spark/

Ejemplo de descarga:

```bash
# Obtener:
wget https://dlcdn.apache.org/spark/spark-4.0.1/spark-4.0.1-bin-hadoop3.tgz

# Descomprimir:
tar -xvzf spark-4.0.1-bin-hadoop3.tgz 
```

Tener en cuenta descargado java tambien:
```bash
sudo apt install -y openjdk-18-jdk
```
> Revisar https://linuxhint.com/install-java-ubuntu-22-04/


### Paso 2 ✍🏻:

Levantar un master y worker.

Entrar a spark-4.0.1-bin-hadoop3/conf (Esta fue la version de Spark con la que se trabajó, adaptarla si descargó otra versión en tal caso) y cambiar las lineas de codigo que digan 192.168.100.3 por 192.168.100.4. Algo asi deberia quedar:

```bash
# --- CONFIGURACION ---
SPARK_LOCAL_IP=192.168.100.4
SPARK_MASTER_HOST=192.168.100.4
SPARK_MASTER_WEBUI_PORT=8080
```
> Puede configurar el puerto del master al que le parezca más conveniente.

Posteriormente:

Entrar a spark-4.0.1-bin-hadoop3/sbin y levantar un master y un worker.

```bash
./start-master.sh
./start-worker.sh spark://192.168.100.4:7077
```

### Paso 3 ✍🏻:

Volver a la raiz del proyecto (es decir a /home/vagrant/PaginaWebCarros-Spark) y ejecutar el siguiente comando:

```bash
/home/vagrant/PaginaWebCarros-Spark/spark-4.0.1-bin-hadoop3/bin/spark-submit relacion_autos.py
```

Como calificaciones registra el id del vehículo necesitamos relacionar el id con la marca/modelo al que se refiere para poder analizar. Porque usando el id solamente no nos dice nada en sí.

Por ende, lo relacionamos con el csv de autos y cruzamos para generar un nuevo csv que si podamos analizar directamente.

> Deberia quedar una carpeta llamada 'autos_relacionados' y dentro un csv con las columnas id_vehiculo,vehiculo,anio.

### Paso 4 ✍🏻:

Hay que lanzar una nueva aplicación spark en la ruta donde se encuentra la carpeta spark-submit (spark-4.0.1-bin-hadoop3/bin) con los siguientes comandos:

--master spark://192.168.100.4:7077 \
/home/vagrant/PaginaWebCarros-Spark/analisis_final_spark.py

y luego lanzar el dashboard (app.py) pero ya en terminal comun y corriente. Hacerlo en la raiz del proyecto.

```bash
cd /home/vagrant/PaginaWebCarros-Spark
python3 app.py
```
> Para visualizar: http://192.168.100.4:8081/dashboard

Y listo!

### Notas importantes 🗒️:

- Revisar los archivos de ejecución por si las direcciones ip no cuadran, puede que haya que reemplazar en vez de 192.168.100.3 por 192.168.100.4 y asi. Revisar los archivos para que no haya inconvenientes ✅

- La carpeta autos_relacionados que se encuentra adjunta es el ejemplo de como deberia quedar el archivo al hacer el 'Paso 3' de esta guía.

- En caso de ser necesario abrir 2 terminales, una para ejecutar app.py y otra el analisis_final_spark.py

- Tener descargado python3 en la maquina

```bash
# Comandos:
sudo apt update
sudo apt install python3
python3 --version
```