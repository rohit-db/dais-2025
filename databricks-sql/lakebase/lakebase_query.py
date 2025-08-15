import psycopg2

from databricks.sdk import WorkspaceClient
import uuid

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

"""
In this example, we're using the Databricks Workspace client to manage database instances.
To use this script, you need to:

1. Configure the Databricks CLI with your workspace credentials:
   - Install the Databricks CLI: `pip install databricks-cli`
   - Configure credentials: `databricks configure --profile <profile-name>`
   - Enter your workspace URL and personal access token when prompted

2. Update the PROFILE variable below to match your configured profile name

For more information on configuring the Databricks CLI, see:
https://docs.databricks.com/dev-tools/cli/index.html
"""

INSTANCE_NAME = "rb-demo-lakebase"
USER_NAME = "rohit.bhagwat@databricks.com"
PROFILE = "az-demo"


w = WorkspaceClient(profile=PROFILE)


instance = w.database.get_database_instance(name=INSTANCE_NAME)
cred = w.database.generate_database_credential(request_id=str(uuid.uuid4()), instance_names=[INSTANCE_NAME])

# Connection parameters
conn = psycopg2.connect(
    host = instance.read_write_dns,
    dbname = "databricks_postgres",
    user = USER_NAME,
    password = cred.token,
    sslmode = "require"
)

# Execute query
with conn.cursor() as cur:
    logger.info("Executing query")
    cur.execute("SELECT * from coffee_operations.coffee_shops")
    logger.info("Fetching results")
    rows = cur.fetchall()
    logger.info(f"Found {len(rows)} rows")
    for row in rows:
        logger.info(row)
conn.close()
