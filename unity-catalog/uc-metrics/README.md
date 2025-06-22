# Unity Catalog Metrics

- **Official Blog Post**: [What's new with Databricks Unity Catalog at Data + AI Summit 2025](https://www.databricks.com/blog/whats-new-databricks-unity-catalog-data-ai-summit-2025)
- **Official Documentation**: [Unity Catalog Metrics Documentation](https://docs.databricks.com/uc-metrics)

## Resources
- [Data + AI Summit Session](https://www.databricks.com/dataaisummit/session/introduction-unity-catalog-metrics-define-your-business-metrics-once)
- [Video: Introduction to Unity Catalog Metrics](https://www.youtube.com/watch?v=gMCFWSTgUoQ)

   [![Unity Catalog Metrics YouTube Link](https://img.youtube.com/vi/gMCFWSTgUoQ/mqdefault.jpg)](https://www.youtube.com/watch?v=gMCFWSTgUoQ)

## Overview

Unity Catalog Metrics solves "metric sprawl" by enabling you to define business metrics once as "metric views" in Unity Catalog, then trust them everywhere. Define dimensions and measures using SQL, then query at any grain without creating new views.

Organizations face "metric sprawl"—the same business metric (like revenue per active customer) is defined differently across teams, tools, and dashboards. This leads to:
- **Inconsistent KPIs** across different teams and tools
- **Repeated logic** with slight variations in each implementation
- **Unreliable insights** due to conflicting metric definitions
- **Maintenance overhead** when changes require updates in multiple places




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