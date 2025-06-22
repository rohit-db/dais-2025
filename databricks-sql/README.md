# What's New in Databricks SQL: Latest Features and Live Demos

- **Official Blog Post**: [Databricks SQL Accelerates Customer Workloads by 5x in Just Three Years](https://www.databricks.com/blog/databricks-sql-accelerates-customer-workloads-5x-just-three-years)
- **Official Documentation**: [Databricks SQL Documentation](https://docs.databricks.com/sql/)

## Resources
- [Data + AI Summit Session](https://www.databricks.com/dataaisummit/session/whats-new-databricks-sql-latest-features-and-live-demos)
- [What's New in Databricks SQL: Latest Features and Live Demos](https://www.youtube.com/watch?v=q9Pv9GuTv38&t=800s)

  [![What's New in Databricks SQL](https://img.youtube.com/vi/q9Pv9GuTv38/mqdefault.jpg)](https://www.youtube.com/watch?v=q9Pv9GuTv38&t=800s)

- [Databricks SQL Serverless](https://docs.databricks.com/sql/admin/sql-endpoints.html)
- [Unity Catalog Documentation](https://docs.databricks.com/data-governance/unity-catalog/index.html)

## Overview
Databricks SQL (DBSQL) is a data warehouse built on lakehouse architecture, operating on cloud storage with formats like Delta Lake and Iceberg, governed by Unity Catalog, and integrated with other Databricks apps and third-party tools. Over half of workloads come from external tools like PowerBI and Tableau.

![Databricks SQL Performance](https://www.databricks.com/sites/default/files/inline-images/image1_53.png?v%3D1749568188)

## Performance Improvements
- **5x Performance Gains Since 2022**: 100-second dashboards now complete in 20 seconds
- **25% Additional Boost**: Latest release delivers 25% better performance automatically
- **Zero Configuration**: All optimizations delivered automatically with no tuning required

## AI-Powered Engine Optimizations

### Predictive Query Execution (PQE)
- **Real-time Monitoring**: Continuously monitors running tasks, collecting metrics like spill size and CPU usage
- **Intelligent Intervention**: Cancels and replans stages on the spot to avoid wasted work
- **Predictable Performance**: Faster queries with fewer surprises, especially for complex pipelines
![alt text](https://www.databricks.com/sites/default/files/inline-images/image2_44.png?v%3D1749568188)

### Photon Vectorized Shuffle
- **Column-based Shuffle**: Higher cache and memory efficiency
- **Optimized Memory Access**: Reduces distance between random memory accesses
- **Performance Gains**: 1.5x higher throughput in CPU-bound workloads like large joins

### Automatic Liquid Clustering
- **AI-Driven Optimization**: Automatically determines and adjusts clustering columns based on query patterns
- **Performance Benefits**: Up to 20x query performance improvements and 50% lower storage costs

### Automatic Statistics
- **Predictive Optimization**: Automatically runs statistics collection for managed tables
- **Performance Improvement**: Up to 33% better query performance

## SQL Language & ETL Enhancements

### Stored Procedures & Scripting
- **Public Preview**: Support for complex logic, DDL/DML, and parameter handling
- **Migration Friendly**: Easier migration from legacy warehouses

### Temporary Tables
- **Session-Scoped**: Managed by Unity Catalog for data governance
- **ETL Optimization**: Ideal for intermediate ETL steps

### Multi-Statement Transactions
- **Private Preview**: Atomic operations across multiple tables with high concurrency
- **Data Consistency**: Ensures ACID compliance across operations

### Geospatial SQL
- **80+ Spatial Expressions**: Comprehensive spatial analysis capabilities
- **New Data Types**: Geometry and geography types for spatial data (private preview)

## AI Functions & Multimodal Capabilities

### AI Analyze Sentiment
- **Built-in Function**: Sentiment analysis on text columns accessible to SQL analysts

### AI Parse Document
- **Document Analysis**: Extracts and analyzes content from PDFs and unstructured documents
- **Structured Output**: Converts unstructured data into queryable format

### AI Query & Gen
- **Image Analysis**: Caption generation and visual content analysis
- **Model Integration**: Supports Llama 4, Claude, and other models

### LLM Integration
- **AI Gateway**: Register and call any LLM from SQL with 3x throughput vs competitors
- **Model Context Protocol (MCP)**: LLM agents can query DBSQL data directly (private preview)

## Materialized Views & Data Transformation

### Enhanced Materialized Views
- **Incremental Refresh**: Supports left outer, full outer, and inner joins
- **Cost Reduction**: Lower refresh costs and improved BI performance

### dbt Integration
- **Orchestration**: Orchestrate dbt Cloud tasks directly in Databricks Jobs (private preview)

## BI & Spreadsheet Integrations

### PowerBI & Tableau
- **One-click Integration**: Seamless connection for Tableau Cloud
- **PowerBI Tasks**: Integrated PowerBI tasks in Databricks Jobs

### Google Sheets & Excel
- **Direct Querying**: Query spreadsheets with no configuration required

## Observability & Cost Management

### Cost Observability
- **Attributed Costs**: Materialized views and dashboards show cost per query, user, and statement
- **Granular Tracking**: Detailed cost breakdown for optimization

### Default Warehouses
- **Workspace-wide Defaults**: Admins can set default warehouses for cost control

### Query Labels
- **Tagging System**: Tag queries for better tracking and cost attribution

### Warehouse Timeouts
- **Statement Timeouts**: Set timeouts at warehouse level to prevent runaway queries

## Alerts & Governance

### Alerts v2
- **Unified UI**: Consistent alert management interface with alert history
- **Git Sync**: Version-controlled alert configurations with Terraform support

### Warehouse Management
- **Multi-warehouse Monitoring**: Tools for monitoring multiple warehouses and teams

## Why It Matters
- **5x Performance**: Real-world customer workloads see 5x improvement since 2022
- **25% Additional Boost**: Latest release delivers 25% better performance automatically
- **Zero Configuration**: All optimizations delivered automatically with no tuning required
- **Cost Efficiency**: Higher performance at lower cost compared to traditional approaches
- **AI-Powered**: Leverages AI for automatic optimization and intelligent query execution
- **Enterprise Ready**: Built-in governance, security, and monitoring capabilities

## Customer Success Stories

### Performance Improvements
> "Databricks SQL has delivered a 5x performance gain across real-world customer workloads—turning a 100-second dashboard into a 20-second one."

### Cost Optimization
> "The latest release brings that 20-second dashboard down to around 15 seconds with zero additional cost."

## Best Practices
- **Leverage Serverless**: Use DBSQL Serverless for instant elasticity and zero infrastructure management
- **Enable Automatic Features**: Turn on automatic Liquid Clustering and Statistics for optimal performance
- **Use Query Labels**: Implement proper tagging for cost tracking and resource management
- **Monitor Performance**: Utilize system tables and observability features for optimization
- **Implement Governance**: Use Unity Catalog for data governance and access control
- **Optimize Materialized Views**: Leverage incremental refresh for better BI performance
- **Use AI Functions**: Incorporate AI capabilities for enhanced analytics and document processing

## Technical Architecture
- **Lakehouse Foundation**: Built on Delta Lake and Iceberg formats
- **Unity Catalog Integration**: Unified governance across all data assets
- **Photon Engine**: Native C++ engine for vectorized processing
- **Predictive Optimization**: AI-driven performance tuning
- **Open Ecosystem**: Compatible with external tools and engines

## Related Features
- [Unity Catalog Iceberg Support](../unity-catalog/iceberg-support/)
- [LakeFlow](../lakeflow/)
- [Mosaic AI](../mosaic-ai/)
- [Agent Bricks](../mosaic-ai/agent-bricks/)
- [AI Functions in SQL](../mosaic-ai/ai-functions-in-sql/)
