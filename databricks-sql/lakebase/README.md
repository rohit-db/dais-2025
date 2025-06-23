# Databricks Lakebase

## Overview
Databricks Lakebase is a new category of operational database: a fully-managed, serverless PostgreSQL database built for the AI era and deeply integrated with the Databricks Data Intelligence Platform. It combines the familiarity and rich ecosystem of Postgres with a modern, scalable architecture that separates compute and storage.

Lakebase is designed to solve the challenges of traditional OLTP databases, which are often siloed, slow to provision, and don't fit into a modern, Git-based developer workflow. By integrating a transactional database directly with the lakehouse, Lakebase makes it seamless to build and power intelligent applications, serve features for machine learning models, and analyze fresh operational data without complex ETL pipelines.

## Resources
### Blogs & Docs
- **Official Announcement**: [Announcing Lakebase Public Preview](https://www.databricks.com/blog/announcing-lakebase-public-preview)
- **Conceptual Overview**: [What is a Lakebase?](https://www.databricks.com/blog/what-is-a-lakebase)
- **Official Documentation**: [Databricks OLTP (Lakebase)](https://docs.databricks.com/aws/en/oltp/)

### Sessions & Videos
| | |
|---|---|
| [![Keynote: Announcing Lakebase](https://img.youtube.com/vi/ul8cRLIP_Vk/0.jpg)](https://www.youtube.com/watch?v=ul8cRLIP_Vk&t=1560s) | **Keynote: Announcing Lakebase**<br/>The official announcement and demo from Data + AI Summit 2025, from the 26:00 to 58:00 mark. |
| [![Race to Real-Time: Low-Latency Streaming ETL Meets Next-Gen Databricks OLTP](https://img.youtube.com/vi/2ObpxTyXVe0/0.jpg)](https://www.youtube.com/watch?v=2ObpxTyXVe0) | **Race to Real-Time: Streaming ETL Meets OLTP**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/race-real-time-low-latency-streaming-etl-meets-next-gen-databricks-oltp) |


## Why It Matters
For decades, a hard wall has existed between operational databases (OLTP) and analytical platforms (OLAP). This creates data silos, increases complexity, and slows down the development of data-driven applications. Lakebase breaks down this wall by:
- **Unifying Stacks**: Eliminates the need for separate operational and analytical data platforms.
- **Modernizing Development**: Introduces Git-like branching for databases, allowing for instant, zero-copy clones for development, testing, and CI/CD at virtually no cost.
- **Accelerating AI Applications**: Makes it trivial to serve features from the lakehouse to an online application or, conversely, to sync application data back to the lakehouse for training and analytics.

## Key Features
### Built on Open Source Postgres
- **Familiar & Powerful**: Leverages the world's most popular open-source database, providing a rich ecosystem of tools, libraries, and extensions.
- **AI-Ready Extensions**: Includes support for popular extensions like **PostGIS** for geospatial data and **pgvector** for similarity search in vector embeddings.

### Scalable Serverless Architecture
- **Separation of Compute and Storage**: Allows for independent, elastic scaling of compute and storage, delivering low-latency (<10ms) and high-concurrency (>10k QPS) transactions.
- **Fully Managed**: No infrastructure to provision or maintain. Includes multi-zone high availability and point-in-time recovery.

### Integrated with the Lakehouse
- **Unified Governance**: Natively integrated with Unity Catalog for a single, consistent way to manage identity, access control, and security for both operational and analytical data.
- **Fully Managed Data Sync**: Easily configure bidirectional data synchronization between Lakebase and Unity Catalog tables (one-off, triggered, or continuous).
- **Native Databricks Apps Integration**: Use Lakebase as the transactional backend for building and deploying full-stack applications directly on Databricks.

## Use Cases
- **Serving Features**: Use Lakebase as an online store to serve ML features and models to applications with low latency.
- **Powering Intelligent Applications**: Build standalone applications (e.g., order processing, chatbots, workflow tools) that transact directly against Lakebase.
- **Analyzing Operational Data**: Sync fresh operational data from your applications back to the lakehouse in near real-time for large-scale analytics and model training.

## Related Features
- [Databricks Apps](../../ai-bi/databricks-apps/)
- [Unity Catalog](../../unity-catalog/)
- [AI/BI: Dashboards & Genie](../../ai-bi/aibi/)
