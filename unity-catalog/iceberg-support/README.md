# Apache Iceberg Support in Unity Catalog

- **Official Blog Post**: [Announcing full Apache Iceberg™ support in Databricks](https://www.databricks.com/blog/announcing-full-apache-iceberg-support-databricks)
- **Official Documentation**: [What is Apache Iceberg in Databricks?](https://docs.databricks.com/aws/en/iceberg/)

## Resources
- [Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/databricks-apache-icebergtm-managed-and-foreign-tables-unity-catalog)
- [Data + AI Summit Session Video](https://www.youtube.com/watch?v=Y70RTULwb30)

  [![Apache Iceberg Support in Unity Catalog](https://img.youtube.com/vi/Y70RTULwb30/mqdefault.jpg)](https://www.youtube.com/watch?v=Y70RTULwb30)

- [Iceberg REST Catalog API](https://iceberg.apache.org/spec/#rest-catalog-api)
- [Unity Catalog Documentation](https://docs.databricks.com/data-governance/unity-catalog/index.html)

## Overview
Unity Catalog now provides full Apache Iceberg™ support, unlocking the complete Apache Iceberg and Delta Lake ecosystems. This Public Preview introduces two major capabilities: **Managed Iceberg Tables** and **Lakehouse Federation** for external Iceberg catalogs. These features enable organizations to break down data silos and resolve ecosystem incompatibilities while maintaining enterprise-grade governance and security.

![Unity Catalog Iceberg Architecture](https://www.databricks.com/sites/default/files/inline-images/announcing-full-iceberg-support-databricks-blog-imgs-4.png?v%3D1749625362)
## Key Features

### Managed Iceberg Tables
- **Fully Open Iceberg Catalog**: Write and read Iceberg tables using Databricks or external engines via Unity Catalog's Iceberg REST Catalog API
- **Predictive Optimization**: Automatic table maintenance including Liquid Clustering, snapshot expiration, and file optimization
- **Platform Integration**: Seamless integration with DBSQL, Mosaic AI, Delta Sharing, and Materialized Views
- **Open Ecosystem Access**: Compatible with any Iceberg client (Apache Spark™, Apache Flink, Trino, PyIceberg, etc.)

### Lakehouse Federation
- **External Catalog Access**: Query and govern Iceberg tables managed by external catalogs (AWS Glue, Hive Metastores, Snowflake Horizon Catalog)
- **Unified Governance**: Apply Unity Catalog's fine-grained access controls, lineage, and auditing across all data
- **Zero-Copy Access**: Access external Iceberg tables without data duplication

### Core Capabilities
- **Schema Evolution**: Support for Iceberg's advanced schema evolution capabilities, including the `VARIANT` type for semi-structured data.
- **Time Travel**: Access to historical data versions and snapshots
- **Partition Evolution**: Dynamic partition management and optimization
- **ACID Transactions**: Full transactional support for data consistency

### Upcoming in Iceberg V3
- **Deletion Vectors**: Enabling merge-on-read semantics for improved performance.
- **Row IDs**: Facilitating incremental data processing.
- **Write Defaults**: Enhancing concurrency and write performance.

## Why It Matters
- **Breaks Data Silos**: Connect to Unity Catalog from any engine and access all data across catalogs and formats
- **Future-Proof Architecture**: Leverage the entire Lakehouse ecosystem with open standards
- **Unified Governance**: Single interface for data discovery and governance across all data assets
- **Performance Optimization**: Out-of-box performance with Predictive Optimization
- **Vendor Lock-in Prevention**: Use your chosen engines regardless of catalog restrictions

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

## Best Practices
- **Table Properties**: Use appropriate Iceberg table properties for your use case
- **Versioning Strategy**: Implement proper snapshot management and retention policies
- **Performance Monitoring**: Monitor table performance and leverage Predictive Optimization
- **Governance**: Follow Unity Catalog governance best practices for access control and lineage
- **Federation**: Use Lakehouse Federation to unify governance across external catalogs
- **Open Standards**: Leverage the Iceberg REST Catalog API for maximum ecosystem compatibility

## Launch Partners
The following partners support Unity Catalog's Iceberg capabilities:
- Atlan, Buf, CelerData, Clickhouse, dbt Labs, dltHub, Fivetran, Informatica, PuppyGraph, Redpanda, RisingWave, StreamNative

## Related Features
- [UC Metrics](../uc-metrics/)
- [Attribute-Based Access Control (ABAC)](../abac/)
- [Tag Policies](../tag-policies/)
- [Data Classification](../data-classification/)
- [Anomaly Detection](../anomaly-detection/)