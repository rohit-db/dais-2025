#!/usr/bin/env python3

import psycopg2
import logging
from databricks.sdk import WorkspaceClient
import uuid

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

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_coffee_shops_table_only(conn: psycopg2.connect):
    """Create only the coffee shops table and add sample data"""

    try:
        # Connect to database
        conn.autocommit = True
        logger.info("✅ Connected to database")
        
        with conn.cursor() as cursor:
            # Step 1: Create schema
            cursor.execute("CREATE SCHEMA IF NOT EXISTS coffee_operations")
            logger.info("✅ Created schema: coffee_operations")
            
            # Step 2: Create coffee shops table
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS coffee_operations.coffee_shops (
                shop_id VARCHAR(10) PRIMARY KEY,
                shop_name VARCHAR(100) NOT NULL,
                city VARCHAR(50) NOT NULL,
                state_province VARCHAR(50),
                country VARCHAR(50) NOT NULL,
                time_zone VARCHAR(50) NOT NULL,
                latitude NUMERIC(10,7),
                longitude NUMERIC(11,7),
                seating_capacity INTEGER,
                is_premium_location BOOLEAN DEFAULT FALSE,
                is_active BOOLEAN DEFAULT TRUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(create_table_sql)
            logger.info("✅ Created coffee_shops table")
            
            # Step 3: Insert sample data
            sample_coffee_shops = [
                ('CS001', 'Brew & Bean Downtown', 'San Francisco', 'CA', 'United States', 'America/Los_Angeles', 37.7749, -122.4194, 45, True),
                ('CS002', 'Mocha Haven Central', 'New York', 'NY', 'United States', 'America/New_York', 40.7128, -74.0060, 32, True),
                ('CS003', 'Espresso Corner', 'Seattle', 'WA', 'United States', 'America/Los_Angeles', 47.6062, -122.3321, 28, False)
            ]
            
            for shop in sample_coffee_shops:
                cursor.execute("""
                    INSERT INTO coffee_operations.coffee_shops 
                    (shop_id, shop_name, city, state_province, country, time_zone, 
                     latitude, longitude, seating_capacity, is_premium_location)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (shop_id) DO NOTHING
                """, shop)
            
            logger.info("✅ Inserted sample coffee shop data")
            
            # Step 4: Verify data
            cursor.execute("SELECT shop_id, shop_name, is_premium_location FROM coffee_operations.coffee_shops")
            results = cursor.fetchall()
            
            logger.info("📊 Data verification:")
            for row in results:
                logger.info(f"  {row[0]}: {row[1]} (Premium: {row[2]})")
            
        conn.close()
        logger.info("✅ Test completed successfully!")
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")

if __name__ == "__main__":

    w = WorkspaceClient(profile=PROFILE)

    instance = w.database.get_database_instance(name=INSTANCE_NAME)
    cred = w.database.generate_database_credential(request_id=str(uuid.uuid4()), instance_names=[INSTANCE_NAME])

    conn = psycopg2.connect(
        host = instance.read_write_dns,
        dbname = "databricks_postgres",
        user = USER_NAME,
        password = cred.token,
        sslmode = "require"
    )
    create_coffee_shops_table_only(conn)
