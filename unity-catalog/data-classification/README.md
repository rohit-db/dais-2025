# Data Classification

## Overview
Data Classification is an intelligent service within Unity Catalog that automatically scans, classifies, and tags sensitive information across your entire data estate. Using advanced AI models, it can identify common types of Personally Identifiable Information (PII), financial data, and other sensitive categories directly within your tables.

This automated process is the foundation of a proactive data governance strategy. By automatically identifying and tagging sensitive data as it lands in the lakehouse, it enables other governance features, like Tag Policies and Attribute-Based Access Control (ABAC), to apply the correct security and access rules without manual intervention. This ensures that your most critical data is protected from the moment it arrives.

## Resources

### Blogs & Docs
*   [What's new with Databricks Unity Catalog at Data + AI Summit 2025](https://www.databricks.com/blog/whats-new-databricks-unity-catalog-data-ai-summit-2025)
*   [Official Documentation: Classify your data using Unity Catalog](https://docs.databricks.com/en/data-governance/unity-catalog/classify.html)

### Sessions & Videos
| | |
|---|---|
| [![Automated Data Governance Deep Dive](https://img.youtube.com/vi/o529ypvgJkk/0.jpg)](https://www.youtube.com/watch?v=o529ypvgJkk&t=1s) | **Unleash the Power of Automated Data Governance: Classify, Tag, and Protect Your Most Critical Data**<br/>[Data + AI Summit Session Details](https://www.databricks.com/dataaisummit/session/unleash-power-automated-data-governance-classify-tag-and-protect-your) |

## Why It Matters

Data Classification intelligently detects and tags sensitive data across your data 
estate, automatically identifying PII, PHI, and other sensitive information within 24 
hours. It integrates with ABAC to automatically protect sensitive data based on access 
control policies.

*   **Proactive Security**: Automatically find and protect sensitive data before it becomes a risk, rather than waiting for manual discovery.
*   **Enables Scalable Governance**: Provides the foundational layer of intelligence required to implement tag-based governance policies at scale.
*   **Reduces Manual Toil**: Frees data stewards from the tedious and error-prone task of manually identifying and tagging sensitive data columns.
*   **Aids Compliance**: Helps organizations meet regulatory requirements (like GDPR, CCPA, and HIPAA) by maintaining a real-time inventory of sensitive data.


## Product Availability
- **Data Classification**: Available in Beta on AWS, Azure, and GCP
- **Automated PII Detection**: Available in Beta
- **Tag-Based Policies**: Available in Beta
- **ABAC Integration**: Available in Beta
- **Governance Hub Integration**: Available in Beta

## Key Features
*   **Automated Sensitive Data Detection**: AI-powered models automatically scan and identify sensitive data types across Unity Catalog.
*   **Continuous Scanning**: New and modified data is automatically scanned, typically within 24 hours, to ensure classification is always up-to-date.
*   **Automatic Tagging**: Once sensitive data is identified, the system automatically applies the appropriate Unity Catalog tags (e.g., `PII`, `Financial_Data`).
*   **Foundation for Policy Enforcement**: The tags applied by the classification service are used by ABAC and Tag Policies to enforce access controls.
*   **Centralized Monitoring**: View classification results and manage policies from a central governance hub.

## Related Features
*   [Attribute-Based Access Control (ABAC)](../abac/)
*   [Tag Policies](../tag-policies/)
*   [Anomaly Detection](../anomaly-detection/)
*   [Unity Catalog Metrics](../uc-metrics/) 