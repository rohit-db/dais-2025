# Tag Policies

## Overview
Tag Policies are a core component of automated data governance in Unity Catalog. This feature allows administrators to enforce rules and access controls based on the tags applied to data assets. When combined with Data Classification and Attribute-Based Access Control (ABAC), it creates a powerful system for managing security at scale.

Instead of applying permissions to thousands of individual tables or columns, administrators can create a single policy that applies to all assets sharing a specific tag (e.g., `PII`, `Confidential`). This tag-based approach ensures that governance is applied consistently and automatically as new data assets are created and classified.

## Resources

### Blogs & Docs
*   [What's new with Databricks Unity Catalog at Data + AI Summit 2025](https://www.databricks.com/blog/whats-new-databricks-unity-catalog-data-ai-summit-2025)
*   [Official Documentation: Apply tags to Unity Catalog securable objects](https://docs.databricks.com/en/data-governance/unity-catalog/tags.html)

### Sessions & Videos
| | |
|---|---|
| [![Automated Data Governance Deep Dive](https://img.youtube.com/vi/o529ypvgJkk/0.jpg)](https://www.youtube.com/watch?v=o529ypvgJkk&t=12s) | **Unleash the Power of Automated Data Governance: Classify, Tag, and Protect Your Most Critical Data**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/unleash-power-automated-data-governance-classify-tag-and-protect-your) |

## Why It Matters
*   **Scalable Governance**: Allows you to govern thousands of data assets with a small number of policies, dramatically reducing manual effort.
*   **Consistent Policy Application**: Ensures that all data of a certain type (e.g., all PII) is protected in the same way, regardless of where it resides.
*   **Automated Security**: When new data is ingested and automatically classified with a tag, the relevant security policies are instantly applied without human intervention.
*   **Simplified Auditing**: Makes it easier to demonstrate compliance by showing auditors the policies applied to specific data classifications.

## Key Features
*   **Tag-Based Policies**: Create access rules that are dynamically enforced based on the tags applied to schemas, tables, and columns.
*   **Integration with ABAC**: Works seamlessly with Attribute-Based Access Control to create rich, context-aware policies (e.g., "Allow users from the 'Finance' group to see columns tagged 'Financial_Data'").
*   **Centralized Management**: Define and manage all tags and tag-based policies within the central Unity Catalog governance model.
*   **Automated Application**: Policies are automatically enforced across the entire Databricks platform.

## Related Features
*   [Attribute-Based Access Control (ABAC)](../abac/)
*   [Data Classification](../data-classification/)
*   [Anomaly Detection](../anomaly-detection/)
*   [Unity Catalog Metrics](../uc-metrics/) 