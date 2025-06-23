# Lakeflow Jobs

## Overview
Lakeflow Jobs is the native, enterprise-grade orchestrator for the Databricks Data Intelligence Platform. As the evolution of Databricks Workflows, it is a mature and trusted solution for coordinating all your data and AI workloads, from data ingestion and transformation to machine learning and business intelligence.

Lakeflow Jobs allows you to build, manage, and monitor complex workflows with a visual, DAG-based interface, ensuring reliability and observability for your most mission-critical processes.

## Resources
### Blogs & Docs
- **Official Documentation**: [Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/)

### Sessions & Videos
| | |
|---|---|
| [![Keynote: Announcing Lakeflow](https://img.youtube.com/vi/0pys27kA67U/0.jpg)](https://www.youtube.com/watch?v=0pys27kA67U&t=3835s) | **Keynote: Announcing Lakeflow**<br/>The main keynote announcement covers all of Lakeflow, including Jobs. |
| [![Data Triggers and Advanced Control Flow in Lakeflow Jobs](https://img.youtube.com/vi/2Y27Z1imxIc/0.jpg)](https://www.youtube.com/watch?v=2Y27Z1imxIc&t=5s) | **Data Triggers and Advanced Control Flow in Lakeflow Jobs**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/data-triggers-and-advanced-control-flow-lakeflow-jobs) |

## Why It Matters
Effective orchestration is the backbone of any data platform. Lakeflow Jobs provides a single, unified orchestrator that is deeply aware of the data it manages, which allows for:
- **Simplified Operations**: Eliminate the need for external orchestrators, reducing cost and complexity.
- **Increased Reliability**: Use powerful control flow logic and data-aware triggers to build robust, resilient workflows.
- **End-to-End Observability**: Monitor the entire data and AI lifecycle, from ingestion to dashboard updates, in one place.

## Key Features
- **Comprehensive Task Support**: Natively orchestrate a wide variety of tasks, including Notebooks, SQL queries, Lakeflow Pipelines, dbt transformations, and even updating AI/BI dashboards.
- **Advanced Control Flow**: Go beyond simple sequential jobs with support for branching (if/else), looping (for-each), and passing parameters between tasks.
- **Data-Aware Triggers**: Run jobs based on file arrivals in cloud storage or, with the new **Table Update Triggers**, run a job only when a specific source table has been updated.
- **Serverless Compute**: Leverage serverless jobs for automatic optimization, better performance, and lower cost.
- **Unified Monitoring**: Get a holistic view of all job runs, task statuses, and historical performance through the UI, system tables, and alerts.

![alt text](https://www.databricks.com/sites/default/files/inline-images/jobs-UI-DAIS2025.png?v%3D1749425940)

## Related Features
- [Declarative Pipelines](../declarative-pipelines/)
- [Lakeflow Connect](../managed-connectors/)
- [Unity Catalog](../../unity-catalog/) 