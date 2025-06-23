# Databricks Lakebridge

## Overview
Lakebridge is a free, open, and extensible migration tool designed to simplify and accelerate enterprise data warehouse (EDW) migrations to Databricks SQL. It provides an end-to-end, automation-first toolkit that addresses the most complex parts of a migration—including assessment, code conversion, validation, and reconciliation.

By automating up to 80% of migration tasks, Lakebridge helps organizations overcome the common risks and bottlenecks of modernization. It provides a clear, predictable, and fast path to move from legacy, proprietary systems to Databricks' open and unified platform.

## Resources
### Blogs & Open Source
- **Official Announcement**: [Introducing Lakebridge: Free, Open Data Migration to Databricks SQL](https://www.databricks.com/blog/introducing-lakebridge-free-open-data-migration-databricks-sql)
- **Official GitHub Repo**: [github.com/databrickslabs/lakebridge](https://github.com/databrickslabs/lakebridge)

### Sessions & Videos
| | |
|---|---|
| [![Keynote: Announcing Lakebridge](https://img.youtube.com/vi/0pys27kA67U/0.jpg)](https://www.youtube.com/watch?v=0pys27kA67U&t=5792s) | **Keynote: Announcing Lakebridge**<br/>The official announcement and demo from Data + AI Summit 2025. |
| [![Comprehensive Data Warehouse Migrations to Databricks SQL](https://img.youtube.com/vi/1isEz2qjRX0/0.jpg)](https://www.youtube.com/watch?v=1isEz2qjRX0&t=6s) | **Comprehensive Data Warehouse Migrations to Databricks SQL**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/comprehensive-data-warehouse-migrations-databricks-sql) |

## Why It Matters
Migrating from a legacy data warehouse is often a high-risk, high-effort undertaking due to complex proprietary SQL, hidden dependencies, and a lack of documentation. Lakebridge directly addresses these challenges by:
- **Reducing Risk and Uncertainty**: Provides detailed analysis and reporting on your legacy environment upfront, allowing for accurate project scoping and planning.
- **Accelerating Timelines**: Automates the most time-consuming parts of a migration, including code translation and data validation, accelerating project timelines by up to 2x.
- **Modernizing on Open Standards**: Converts proprietary SQL dialects (like Teradata BTEQ, Oracle PL/SQL, or Microsoft T-SQL) into open, ANSI-compliant SQL that runs seamlessly on Databricks. This frees you from vendor lock-in and prepares your architecture for the future.

## Key Components
Lakebridge delivers an end-to-end migration experience through three core components:
1.  **Analyzer**: Scans legacy data warehouse metadata and code to inventory all objects (tables, views, stored procedures, ETL jobs) and classify them by complexity. This provides a clear understanding of the migration scope from day one.
2.  **Converter**: Intelligently translates legacy SQL scripts and ETL workflows into performant, compatible Databricks SQL or Spark SQL. It leverages a battle-tested engine that has powered hundreds of successful enterprise migrations.
3.  **Validator**: Ensures data accuracy and correctness post-migration with built-in data reconciliation tools, giving business leaders confidence in the results.

## What's Next
Databricks is committed to delivering a fully GenAI-powered migration experience. Upcoming enhancements for Lakebridge include:
- **Mosaic AI–Powered Code Conversion**: Leveraging large language models with reinforcement learning to continuously improve translation accuracy.
- **Dedicated Data Migration Module**: Tools to automate and optimize the physical data movement workflows.
- **Graphical User Interface (GUI)**: An intuitive interface for tracking migration progress and viewing validation insights.

## Related Features
- [Lakebase](../lakebase/)
- [Unity Catalog](../../unity-catalog/)
- [Databricks SQL](./) 