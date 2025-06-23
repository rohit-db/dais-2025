# Lakeflow Declarative Pipelines

## Overview
Lakeflow Declarative Pipelines are the next evolution of ETL, built on the new open standard of **Spark Declarative Pipelines**. This represents a fundamental shift from imperative coding (telling the system *how* to do something) to a declarative model (telling the system *what* you want to achieve). The system then handles the complex, low-level implementation details like data serialization, clustering, and execution optimization.

This managed experience on Databricks is 100% source-compatible with the open standard and 100% backward-compatible with existing Delta Live Tables (DLT) pipelines, ensuring a smooth upgrade path. It is accessible through a new, purpose-built **IDE for Data Engineering**.

## Resources
### Blogs & Docs
- **Official Documentation**: [Declarative Pipelines (DLT)](https://docs.databricks.com/aws/en/dlt/)

### Sessions & Videos
| | |
|---|---|
| [![Keynote: Announcing Lakeflow](https://img.youtube.com/vi/0pys27kA67U/0.jpg)](https://www.youtube.com/watch?v=0pys27kA67U&t=3835s) | **Keynote: Announcing Lakeflow**<br/>The main keynote announcement covers all of Lakeflow, including Declarative Pipelines. |
| [![Introducing Lakeflow: The Future of Data Engineering](https://img.youtube.com/vi/lq8w9kpbGB4/0.jpg)](https://www.youtube.com/watch?v=lq8w9kpbGB4&t=6s) | **Introducing Lakeflow: The Future of Data Engineering**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/introducing-lakeflow-future-data-engineering-databricks) |
| [![Authoring Data Pipelines with the new Editor](https://img.youtube.com/vi/eF34sUvYdxw/0.jpg)](https://www.youtube.com/watch?v=eF34sUvYdxw&t=1s) | **Authoring Data Pipelines with the new Editor**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/authoring-data-pipelines-new-lakeflow-declarative-pipelines-editor) |

## The IDE for Data Engineering
The new IDE is a modern, integrated environment designed to streamline the entire pipeline development lifecycle. It brings everything you need into a single, context-aware view.
- **Side-by-Side View**: See your code and the resulting pipeline DAG (Directed Acyclic Graph) in one place.
- **Instant Data Previews**: Click on any component in the DAG to see a live preview of the data flowing through it.
- **Context-Aware Debugging**: The IDE surfaces issues inline, allowing you to click directly on an error and be taken to the exact line of code causing it.
- **AI-Assisted Authoring**: Leverage built-in AI assistance for authoring code and configuring your pipeline.
- **Integrated Git**: Native Git integration supports rapid, iterative development and version control.

![alt text](https://www.databricks.com/sites/default/files/inline-images/All-3-panels-Data-Previews-SQL-code.png?v%3D1749425940)

## Why It Matters
Declarative Pipelines fundamentally simplify the process of building reliable ETL. By focusing on the "what" instead of the "how," you get:
- **Reduced Complexity**: The framework automates the most difficult parts of pipeline development, such as change data capture (CDC), error handling, and performance tuning.
- **Increased Productivity**: The new IDE provides a focused, efficient development loop, eliminating the need to constantly switch between browser tabs and lose context.
- **Improved Reliability**: Declarative pipelines are easier to test, debug, and maintain, leading to higher-quality data outcomes.

## Related Features
- [Lakeflow Designer](../lakeflow-designer/)
- [Lakeflow Connect](../managed-connectors/)
- [Unity Catalog](../../unity-catalog/) 