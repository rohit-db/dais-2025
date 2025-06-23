# Lakeflow Connect (Managed Connectors)

## Overview
Lakeflow Connect is the unified ingestion component of Lakeflow, providing reliable, managed data ingestion from a vast array of enterprise applications, databases, and real-time streams. It eliminates the need for data teams to build, host, and maintain fragile custom connectors or stitch together external services.

This is accomplished through a library of **Managed Connectors** and a new high-throughput API called **Zerobus**.

## Resources
### Blogs & Docs
- **Official Documentation**: [Lakeflow Connect](https://docs.databricks.com/aws/en/ingestion/overview)

### Sessions & Videos
| | |
|---|---|
| [![Keynote: Announcing Lakeflow](https://img.youtube.com/vi/0pys27kA67U/0.jpg)](https://www.youtube.com/watch?v=0pys27kA67U&t=3835s) | **Keynote: Announcing Lakeflow**<br/>The main keynote announcement covers all of Lakeflow, including Lakeflow Connect and Zerobus. |
| [![Getting Started With Lakeflow Connect](https://img.youtube.com/vi/TT-O-s28mGI/0.jpg)](https://www.youtube.com/watch?v=TT-O-s28mGI&t=5s) | **Getting Started With Lakeflow Connect**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/getting-started-lakeflow-connect) |
| [![Eliminate Hops in Your Streaming Architecture with Zerobus](https://img.youtube.com/vi/wrH5wWmFT94/0.jpg)](https://www.youtube.com/watch?v=wrH5wWmFT94&t=18s) | **Eliminate Hops in Your Streaming Architecture with Zerobus**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/eliminate-hops-your-streaming-architecture-zerobus-part-lakeflow) |
| [![Lakeflow Connect: Easy, Efficient Ingestion From Databases](https://img.youtube.com/vi/sZ3wVoedP64/0.jpg)](https://www.youtube.com/watch?v=sZ3wVoedP64&t=2s) | **Lakeflow Connect: Easy, Efficient Ingestion From Databases**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/lakeflow-connect-easy-efficient-ingestion-databases) |

## Key Features
### Managed Connectors
- **Broad Source Support**: A growing library of fully-managed, enterprise-grade connectors for sources like Salesforce, ServiceNow, Google Analytics, Oracle, SQL Server, and many more.
- **No-Code / Low-Code Interface**: Ingest data with point-and-click simplicity through a visual UI or automate ingestion via a robust API.
- **Handles Complexity**: The platform automatically manages operational complexities like schema drift, API changes, and error handling.

### Zerobus
- **High-Throughput Streaming API**: A new Lakeflow Connect API that allows developers to write event data directly to the lakehouse at very high throughput (100+ MB/s) with near real-time latency (<5 seconds).
- **Simplified Streaming Infrastructure**: Eliminates the need for external message bus infrastructure (like Kafka or Kinesis) for many common streaming use cases.

## Why It Matters
Data ingestion is often the most brittle and time-consuming part of data engineering. Lakeflow Connect solves this by:
- **Simplifying Connections**: Drastically reduces the time and effort required to connect to complex data sources.
- **Increasing Reliability**: Provides managed, battle-tested connectors that are more robust than custom-built scripts.
- **Unifying Governance**: All ingested data is immediately available in the lakehouse and governed by Unity Catalog, providing a single source of truth.

## Related Features
- [Declarative Pipelines](../declarative-pipelines/)
- [Lakeflow Designer](../lakeflow-designer/)
- [Unity Catalog](../../unity-catalog/)