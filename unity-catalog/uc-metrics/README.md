# Unity Catalog Metrics

## Overview
Unity Catalog Metrics provide a universal semantic layer for the Databricks Data Intelligence Platform, solving the critical challenge of "metric sprawl." It allows organizations to define key business metrics—like "Monthly Recurring Revenue" or "Active Users"—once, in a centralized and governed location. Once defined, these metrics can be reliably reused across the entire platform, from AI/BI Dashboards and Genie to SQL queries and third-party tools.

This "define-once, use-everywhere" approach eliminates the inconsistencies and maintenance burdens that arise when different teams create their own versions of the same KPI. By creating a single source of truth for business logic, Unity Catalog Metrics ensures that everyone in the organization is making decisions based on the same, trusted numbers.

## Resources

### Blogs & Docs
*   [What's new with Databricks Unity Catalog at Data + AI Summit 2025](https://www.databricks.com/blog/whats-new-databricks-unity-catalog-data-ai-summit-2025)
*   [Official Documentation: Unity Catalog Metrics](https://docs.databricks.com/en/data-governance/unity-catalog/index.html#metrics)
*   [Documentation: Metric Views](https://docs.databricks.com/aws/en/metric-views/)

### Sessions & Videos
| | |
|---|---|
| [![Introduction to Unity Catalog Metrics](https://img.youtube.com/vi/gMCFWSTgUoQ/0.jpg)](https://www.youtube.com/watch?v=gMCFWSTgUoQ) | **Introduction to Unity Catalog Metrics: Define Your Business Metrics Once**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/introduction-unity-catalog-metrics-define-your-business-metrics-once) |

## Why It Matters
*   **Ensures Consistency and Trust**: Eliminates conflicting metric definitions across different teams and tools, providing a single source of truth for KPIs.
*   **Reduces Redundant Work**: Prevents analysts and data scientists from having to constantly re-implement the same business logic.
*   **Accelerates Analytics**: Business users get faster, more reliable answers from dashboards and conversational AI because the logic is already defined and certified.
*   **Simplifies Governance**: Centralizes the management and security of critical business logic, making it easier to audit and control.

## Key Features
Unity Catalog Metrics solves "metric sprawl" by enabling you to define business 
metrics once as "metric views" in Unity Catalog, then trust them everywhere. Define 
dimensions and measures using SQL, then query at any grain without creating new views.

*   **Centralized Metric Definition**: Define metrics and dimensions once as "metric views" in Unity Catalog using standard SQL.
*   **Multi-Grain Queries**: Query metrics at any time grain (e.g., daily, monthly, quarterly) from a single metric view without creating redundant copies of the data.
*   **Governed and Secure**: Apply fine-grained access controls, certifications, and data lineage to your business metrics just like any other data asset in Unity Catalog.
*   **Platform-Wide Access**: Consume metrics from AI/BI Dashboards, AI/BI Genie, SQL queries, and a growing ecosystem of partner tools.
*   **Materialization (Upcoming)**: The ability to pre-compute frequently used metric aggregations to improve query performance.
*   **No-Code and Code Interfaces**: Both technical and non-technical users can define and use metrics through SQL or a graphical interface.

![A diagram showing how a Metric View works in Unity Catalog](https://docs.databricks.com/aws/en/assets/images/what-is-f1090f388428085b3a7cd9a6876f7649.png)

![What's a Metric view](https://docs.databricks.com/aws/en/assets/images/what-is-f1090f388428085b3a7cd9a6876f7649.png)

## Unity Catalog Metrics
- **Centralized Definition**: Define metrics once as "metric views" in Unity Catalog
- **Multi-Grain Queries**: Query metrics at any grain (daily, monthly, quarterly) without new views
- **Governance**: Apply fine-grained access controls, certification, and lineage tracking
- **Multi-Tool Access**: Accessible from dashboards, Genie, SQL APIs, and partner tools
- **Materialization**: Pre-compute frequently used metric slices for performance
- **No-Code and Code Interfaces**: Both technical and non-technical users can define and use metrics

### Challenges with Traditional SQL Views
- **Fragmentation**: Each team creates their own SQL view, leading to many slightly different versions
- **Complexity**: Multiple tables/views for different time grains (daily, monthly, yearly) confuse analysts
- **Limited Portability**: Logic embedded in BI dashboards or LLM prompts isn't easily reused
- **Maintenance Overhead**: Changes require updating logic in multiple places

## Product Availability
- **Unity Catalog Metrics**: Available in Public Preview on AWS, Azure, and GCP
- **Metric Definition**: Available in Public Preview

## Use Cases

- **Revenue Analysis**: Define "Monthly Recurring Revenue" once, use across all dashboards
- **Customer Metrics**: Consistent "Customer Acquisition Cost" calculation for all teams
- **Time-Grain Flexibility**: Query "Active Users" at daily, monthly, or yearly grains
- **Natural Language**: Use Genie to ask "What's our revenue by quarter?" against governed metrics

## Related Features
- [Attribute-Based Access Control (ABAC)](../abac/)
- [Tag Policies](../tag-policies/)
- [Data Classification](../data-classification/)
- [Data Quality Monitoring](../anomaly-detection/) 