# Apache Iceberg Support in Unity Catalog

## Overview
Unity Catalog now provides full, native support for the Apache Iceberg table format, enabling organizations to break down data silos and embrace a truly open lakehouse architecture. This capability allows you to manage all of your data—whether in Delta Lake or Iceberg format—under a single, unified governance model, accessible from any compatible engine or tool.

This release introduces two major features: **Managed Iceberg Tables** in Unity Catalog, and **Lakehouse Federation** for external Iceberg catalogs. This means you can create and govern Iceberg tables directly in Databricks, benefiting from performance optimizations like Liquid Clustering, or you can govern Iceberg tables that live in external catalogs like AWS Glue or a Hive Metastore, all without ever moving or copying the data.
![A diagram of the Unity Catalog Iceberg Architecture](https://www.databricks.com/sites/default/files/inline-images/announcing-full-iceberg-support-databricks-blog-imgs-4.png?v%3D1749625362)

## Resources

### Blogs & Docs
*   [Announcing full Apache Iceberg™ support in Databricks](https://www.databricks.com/blog/announcing-full-apache-iceberg-support-databricks)
*   [Official Documentation: Read and write Iceberg tables](https://docs.databricks.com/en/query/iceberg.html)
*   [Iceberg REST Catalog API Specification](https://iceberg.apache.org/spec/#rest-catalog-api)

### Sessions & Videos
| | |
|---|---|
| [![Apache Iceberg Support in Unity Catalog](https://img.youtube.com/vi/Y70RTULwb30/0.jpg)](https://www.youtube.com/watch?v=Y70RTULwb30) | **Databricks + Apache Iceberg™: Managed and Foreign Tables in Unity Catalog**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/databricks-apache-icebergtm-managed-and-foreign-tables-unity-catalog) |

## Why It Matters
*   **Eliminates Data Silos**: Provides a single point of access and governance for both Delta Lake and Apache Iceberg tables, regardless of where they are stored or managed.
*   **Prevents Vendor Lock-in**: Ensures you can use the best engine for the job, allowing any Iceberg-compatible tool to connect to and interact with your governed data.
*   **Unified Governance**: Extends Unity Catalog's enterprise-grade governance—including fine-grained access controls, auditing, and lineage—to your entire Iceberg data estate.
*   **High Performance on Open Formats**: Brings Databricks' world-class performance optimizations, like Predictive Optimization, to the Iceberg ecosystem.

## Key Features

### Managed Iceberg Tables
*   **Fully Open Iceberg Catalog**: Create, read, and write Iceberg tables using Databricks or any external engine through Unity Catalog's implementation of the Iceberg REST Catalog API.
*   **Predictive Optimization**: Automatically apply performance-enhancing table maintenance like Liquid Clustering, snapshot expiration, and file optimization to your Iceberg tables.
*   **Full Platform Integration**: Seamlessly use Iceberg tables with Databricks SQL, Mosaic AI, Delta Sharing, and Materialized Views.

### Lakehouse Federation for Iceberg
*   **External Catalog Access**: Query, govern, and manage Iceberg tables that reside in external catalogs like AWS Glue, Hive Metastores, or even a Snowflake Horizon Catalog.
*   **Zero-Copy and In-Place Governance**: Apply Unity Catalog's fine-grained security and governance to your external Iceberg tables without ever needing to move or replicate the data.

### Core Capabilities
- **Schema Evolution**: Support for Iceberg's advanced schema evolution capabilities, 
including the `VARIANT` type for semi-structured data.
- **Time Travel**: Access to historical data versions and snapshots
- **Partition Evolution**: Dynamic partition management and optimization
- **ACID Transactions**: Full transactional support for data consistency

### Upcoming in Iceberg V3
- **Deletion Vectors**: Enabling merge-on-read semantics for improved performance.
- **Row IDs**: Facilitating incremental data processing.
- **Write Defaults**: Enhancing concurrency and write performance.

## Code Examples
```sql
-- Create a Managed Iceberg table
CREATE TABLE catalog.schema.iceberg_table (
  id INT,
  name STRING,
  created_at TIMESTAMP
) USING iceberg;

-- Write data to Iceberg table
INSERT INTO catalog.schema.iceberg_table VALUES (1, 'example', CURRENT_TIMESTAMP());

-- Query with time travel
SELECT * FROM catalog.schema.iceberg_table TIMESTAMP AS OF '2024-01-01 10:00:00';

-- Schema evolution
ALTER TABLE catalog.schema.iceberg_table ADD COLUMNS (new_column STRING);
```

## Launch Partners
The following partners support Unity Catalog's Iceberg capabilities:
- Atlan, Buf, CelerData, Clickhouse, dbt Labs, dltHub, Fivetran, Informatica, 
PuppyGraph, Redpanda, RisingWave, StreamNative

## Related Features
*   [UC Metrics](../uc-metrics/)
*   [Attribute-Based Access Control (ABAC)](../abac/)
*   [Tag Policies](../tag-policies/)
*   [Data Classification](../data-classification/)
*   [Anomaly Detection](../anomaly-detection/)