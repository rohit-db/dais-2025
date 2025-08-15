from databricks.connect import DatabricksSession
from pyspark.sql.functions import col, current_timestamp

# Initialize the DatabricksSession
spark = DatabricksSession.builder.remote(serverless=True).getOrCreate()

print("DatabricksSession initialized successfully.")
print("Spark version:", spark.version)

spark.sql("select sum(quantity) from rohitb_demo.pilot_demo.sales_transactions limit 10").show()