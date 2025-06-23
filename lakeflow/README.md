# Databricks Lakeflow

## Overview
Databricks Lakeflow is a unified and intelligent solution for all data engineering workloads, deeply integrated into the Databricks Data Intelligence Platform. It addresses the core challenges of modern data engineering—complexity, fragmentation, and governance—by unifying data ingestion, transformation, and orchestration into a single, seamless experience.

Lakeflow empowers data teams to build reliable, production-grade data pipelines through a suite of powerful tools designed for every user, from data engineers to analysts. It's built on a foundation of open standards and is designed to bring the application *to* the data, not the other way around.

The core components of Lakeflow are:
-   **Lakeflow Connect**: Reliable, managed data ingestion from any source.
-   **Lakeflow Pipelines**: Declarative ETL pipelines for any data practitioner.
-   **Lakeflow Jobs**: Robust, enterprise-grade workflow orchestration.

## Resources
### Blogs & Docs
- **GA Announcement**: [Announcing the General Availability of Databricks Lakeflow](https://www.databricks.com/blog/announcing-general-availability-databricks-lakeflow)
- **Lakeflow Designer**: [Announcing Lakeflow Designer for No-Code ETL](https://www.databricks.com/blog/announcing-lakeflow-designer-no-code-etl)
- **Official Documentation**: 
  - [What is Lakeflow?](https://docs.databricks.com/en/lakeflow/index.html)
  - [Lakeflow Connect](https://docs.databricks.com/aws/en/ingestion/overview)
  - [Declarative Pipelines (DLT)](https://docs.databricks.com/aws/en/dlt/)
  - [Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/)

### Sessions & Videos
| | |
|---|---|
| [![Keynote: Announcing Lakeflow](https://img.youtube.com/vi/0pys27kA67U/0.jpg)](https://www.youtube.com/watch?v=0pys27kA67U&t=3835s) | **Keynote: Announcing Lakeflow**<br/>The official announcement and demo from Data + AI Summit 2025 (from 1:03:55 to 1:22:00). |
| [![Introducing Lakeflow: The Future of Data Engineering](https://img.youtube.com/vi/lq8w9kpbGB4/0.jpg)](https://www.youtube.com/watch?v=lq8w9kpbGB4&t=6s) | **Introducing Lakeflow: The Future of Data Engineering**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/introducing-lakeflow-future-data-engineering-databricks) |
| [![Lakeflow for Data & AI Innovation](https://img.youtube.com/vi/XEJ_d9X0Bdg/0.jpg)](https://www.youtube.com/watch?v=XEJ_d9X0Bdg&t=11s) | **Lakeflow as a Foundation for Data & AI Innovation**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/databricks-lakeflow-foundation-data-ai-innovation-your-industry) |
| [![Authoring Data Pipelines with the new Editor](https://img.youtube.com/vi/eF34sUvYdxw/0.jpg)](https://www.youtube.com/watch?v=eF34sUvYdxw&t=1s) | **Authoring Data Pipelines with the new Editor**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/authoring-data-pipelines-new-lakeflow-declarative-pipelines-editor) |
| [![Data Triggers and Advanced Control Flow](https://img.youtube.com/vi/2Y27Z1imxIc/0.jpg)](https://www.youtube.com/watch?v=2Y27Z1imxIc&t=5s) | **Data Triggers and Advanced Control Flow in Lakeflow Jobs**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/data-triggers-and-advanced-control-flow-lakeflow-jobs) |

## Why It Matters
Data engineering is often plagued by a patchwork of disconnected tools for ingestion, transformation, and orchestration. This fragmented approach creates complexity, introduces governance gaps, and slows down teams. Lakeflow solves this by:
- **Unifying the Stack**: Provides a single, end-to-end solution, eliminating the cost and effort of integrating multiple tools.
- **Simplifying Development**: Abstracting away low-level operational complexity so teams can focus on business logic, not boilerplate code.
- **Democratizing Data Engineering**: With tools like Lakeflow Designer (no-code) and the new Declarative Pipelines IDE, both engineers and analysts can build production-quality pipelines.
- **Ensuring Governance**: Because Lakeflow is built into the Data Intelligence Platform, all pipelines are natively governed by Unity Catalog, providing complete visibility and control.

## Core Components
- **[Lakeflow Connect](./managed-connectors/)**: Managed ingestion with a growing library of connectors for databases, enterprise apps, and file sources. Includes **Zerobus**, a new high-throughput API for direct, low-latency streaming to the lakehouse.
- **[Declarative Pipelines](./declarative-pipelines/)**: The next evolution of Delta Live Tables, built on the open standard of **Spark Declarative Pipelines**. A new, purpose-built **IDE for Data Engineering** streamlines development, debugging, and collaboration.
- **[Lakeflow Designer](./lakeflow-designer/)**: A no-code, AI-powered visual pipeline builder that empowers any user to build reliable, production-grade data pipelines.
- **[Lakeflow Jobs](./jobs/)**: The evolution of Databricks Workflows, providing robust orchestration for all data and AI assets. Features include advanced control flow (branching, looping), new data-aware triggers, and unified monitoring.

## Related Features
- [Unity Catalog](../unity-catalog/)
- [Databricks SQL](../databricks-sql/)
- [AI/BI: Dashboards & Genie](../ai-bi/aibi/) 