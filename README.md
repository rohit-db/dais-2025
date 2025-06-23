# DAIS 2025 Announcements Repository

This repository organizes and summarizes all major product announcements from the **Databricks Data + AI Summit 2025**, grouped by key platform categories. 
It is designed as a field enablement toolkit.

---

## Key Resources
This section contains the primary, high-level resources covering all major announcements from the Data + AI Summit.

### General Resources
*   **Data + AI Summit Homepage**: [Watch sessions on-demand](https://www.databricks.com/dataaisummit/)
*   **Official Announcements Blog**: [All platform announcements](https://www.databricks.com/blog/category/platform/announcements?categories=announcements)
*   **Databricks Documentation**: [Main documentation portal](https://docs.databricks.com/aws/en/)

### Keynotes
| | |
| --- | --- |
| [![Data + AI Summit 2025 Main Keynote](https://img.youtube.com/vi/ul8cRLIP_Vk/0.jpg)](https://www.youtube.com/watch?v=UfbyzK488Hk) | **Data + AI Summit 2025 Main Keynote**<br/>Covers the Data Intelligence Platform vision and major announcements around Mosaic AI, Lakebase & Databricks Apps. |
| [![Data + AI Summit 2025 Day 2 Keynote](https://img.youtube.com/vi/0pys27kA67U/0.jpg)](https://www.youtube.com/watch?v=0pys27kA67U) | **Data + AI Summit 2025 Day 2 Keynote**<br/>Dives deeper into product announcements like Lakeflow, Unity Catalog, Databricks SQL & AI/BI. |

---

## Summary of Announcements

### Mosaic AI (GenAI & ModelOps)
- **Agent Bricks**: Auto-optimized domain-specific agents with evaluation and tuning built-in.
- **MLflow 3.0**: Unified experimentation, observability, and governance for GenAI and ML.
- **AI Functions in SQL**: Run GenAI functions (e.g. `ai_parse_document`) directly in SQL.
- **Vector Search**: Storage-optimized vector store with compute/storage separation.
- **Serverless GPUs**: Instant A10G GPU access for fine-tuning and inference.
- **Model Serving Enhancements**: High-QPS, lower-latency serving with in-house inference engine.
- **AI Gateway**: Central control for routing, safety, and usage across LLM endpoints.

📁 [`mosaic-ai/`](./mosaic-ai)

---

### Lakeflow (ETL, Pipelines, Orchestration)
- **Lakeflow**: Unify pipelines for ETL and orchestration.
- **Lakeflow Designer**: No-code interface for building ETL pipelines.
- **Declarative Pipelines**: Open-sourced DLT framework powered by Spark 4.0.
- **Managed Connectors**: New support for SQL Server, GA360, ServiceNow, and row-level ingestion API.

📁 [`lakeflow/`](./lakeflow)

---

### 📊 AI/BI (Apps & Dashboards)
- **Databricks Apps**: Secure, governed data apps using Python/JS frameworks.
- **Genie**: Conversational analytics with AI/BI Dash, powered by UC metrics and LLMs.
- **AI/BI Dashboards**: LLM-infused dashboards with UC-backed metrics.
- **Databricks One**: Secure, streamlined access for data consumers.

📁 [`ai-bi/`](./ai-bi)

---

### Unity Catalog (Governance Layer)
- **UC Metrics**: Semantic layer to define consistent metrics across dashboards & models.
- **Attribute-Based Access Control (ABAC)**: Fine-grained, dynamic policy enforcement.
- **Tag Policies**: Governance via tag-based rules.
- **Data Classification**: Auto-detect and classify sensitive data.
- **Anomaly Detection**: Identify abnormal usage patterns in governed datasets.
- **Iceberg Support**: Enhanced governance and compatibility with Apache Iceberg tables.

📁 [`unity-catalog/`](./unity-catalog)

---

### Databricks SQL
- **Lakebase**: Fully managed Postgres integrated into the Lakehouse.
- **Lakebridge**: Migration toolkit for 25+ legacy data warehouses.
- **Power Platform Connector**: Real-time access to Databricks from Power Apps, Copilot, etc.

📁 [`databricks-sql/`](./databricks-sql)

---

### Databricks Free Edition
- **Community Edition**: Free, hands-on Databricks learning workspace.

📁 [`free-edition/`](./free-edition)

---

## 📁 Resources
Additional reference materials, internal docs, blogs, and slide decks.

📁 [`_resources/`](./_resources)
