# ======================================
# Relacionar autos y calificaciones (Con PySpark)
# ======================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id, row_number, col
from pyspark.sql.window import Window

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("RelacionAutosCalificaciones") \
    .getOrCreate()

# ===========================
# 1️. Cargar los archivos CSV
# ===========================
ruta_autos = "/home/vagrant/PaginaWebCarros-Spark/autos_limpiov8.csv"
ruta_calificaciones = "/home/vagrant/PaginaWebCarros-Spark/calificaciones.csv"

autos_df = spark.read.option("header", True).csv(ruta_autos)
calificaciones_df = spark.read.option("header", True).csv(ruta_calificaciones)

# ===========================
# 2️. Asignar ID artificial a autos
# ===========================
# Crea un índice incremental que simula el ID autoincrement de SQL
windowSpec = Window.orderBy(monotonically_increasing_id())
autos_df = autos_df.withColumn("id_vehiculo", row_number().over(windowSpec))

# ===========================
# 3️. Preparar y unir DataFrames
# ===========================
autos_df = autos_df.withColumn("id_vehiculo", col("id_vehiculo").cast("int"))
calificaciones_df = calificaciones_df.withColumn("carroId", col("carroId").cast("int"))

union_df = autos_df.join(calificaciones_df, autos_df.id_vehiculo == calificaciones_df.carroId, "inner")

# ===========================
# 4️. Seleccionar columnas finales
# ===========================
resultado_df = union_df.select(
    autos_df["id_vehiculo"],
    autos_df["Model"].alias("vehiculo"),
    autos_df["Year"].alias("anio")
)

# ===========================
# 5️. Guardar resultado
# ===========================
# Guardar como un solo archivo CSV
ruta_salida = "/home/vagrant/PaginaWebCarros-Spark/autos_relacionados.csv"

# Para que Spark no genere múltiples part-xxxxx.csv
resultado_df.coalesce(1).write.option("header", True).mode("overwrite").csv(ruta_salida)

print(f"✅ Archivo generado en: {ruta_salida}")

spark.stop()
