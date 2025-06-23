# Attribute-Based Access Control (ABAC)

## Overview
Attribute-Based Access Control (ABAC) is a powerful new capability in Unity Catalog that enables dynamic, fine-grained, and scalable data governance. Unlike traditional Role-Based Access Control (RBAC), which relies on static role definitions, ABAC makes access decisions based on a flexible combination of attributes attached to users, data assets, and the environment.

This allows organizations to create simple, intuitive policies that automatically adapt to changing conditions. For example, a single policy could grant access to data only if a user's `department` attribute matches the data's `department` tag, and only if they are accessing it from a trusted `location`. This approach dramatically simplifies the management of complex security requirements across a large and diverse data estate.

## Resources

### Blogs & Docs
*   [What's new with Databricks Unity Catalog at Data + AI Summit 2025](https://www.databricks.com/blog/whats-new-databricks-unity-catalog-data-ai-summit-2025)
*   [Official Documentation: Attribute-Based Access Control](https://docs.databricks.com/en/data-governance/unity-catalog/attribute-based-access-control.html)

### Sessions & Videos
| | |
|---|---|
| [![Automated Data Governance Deep Dive](https://img.youtube.com/vi/o529ypvgJkk/0.jpg)](https://www.youtube.com/watch?v=o529ypvgJkk&t=12s) | **Unleash the Power of Automated Data Governance: Classify, Tag, and Protect Your Most Critical Data**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/unleash-power-automated-data-governance-classify-tag-and-protect-your) |

## Why It Matters
*   **Simplifies Complex Governance**: Replaces thousands of complex, static role definitions with a small number of simple, intuitive policies.
*   **Scales with Your Organization**: Policies automatically apply to new users and new data assets as they are added, without requiring manual updates.
*   **More Secure and Precise**: Enables more granular and context-aware security rules than are possible with RBAC alone.
*   **Reduces Administrative Overhead**: Drastically reduces the time and effort required to manage data access controls at scale.

## Key Features
*   **Dynamic Policy Evaluation**: Access decisions are evaluated in real-time based on a combination of user, resource, and environmental attributes.
*   **Policies Written in SQL**: Define access policies using simple, standard SQL expressions.
*   **Centralized Governance**: All policies are managed and monitored centrally through Unity Catalog.
*   **Native Integration**: Works seamlessly across the entire Databricks platform, from SQL queries to notebooks to AI/BI dashboards.

## Related Features
*   [Tag Policies](../tag-policies/)
*   [Data Classification](../data-classification/)
*   [Anomaly Detection](../anomaly-detection/)
*   [Unity Catalog Metrics](../uc-metrics/)