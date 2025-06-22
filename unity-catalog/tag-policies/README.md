# Tag Policies

- **Official Blog Post**: [What's new with Databricks Unity Catalog at Data + AI Summit 2025](https://www.databricks.com/blog/whats-new-databricks-unity-catalog-data-ai-summit-2025)
- **Official Documentation**: [Unity Catalog Tag Policies Documentation](https://docs.databricks.com/tag-policies)

## Resources
- [Data + AI Summit Session](https://www.databricks.com/dataaisummit/session/unleash-power-automated-data-governance-classify-tag-and-protect-your)
- [Video: Automated Data Governance Deep Dive](https://www.youtube.com/watch?v=o529ypvgJkk&t=12s)

   [![Automated Data Governance YouTube Link](https://img.youtube.com/vi/o529ypvgJkk/mqdefault.jpg)](https://www.youtube.com/watch?v=o529ypvgJkk&t=12s)

## Overview

Tag Policies enable automated data governance through intelligent classification and tag-based rules. AI-powered detection automatically identifies sensitive data (PII, PHI, financial), while single policies apply consistently across all matching data assets.

## Key Features

- **Automated Classification**: AI-powered detection of sensitive data types
- **Tag-Based Policies**: Single policy applies to all data with matching tags
- **ABAC Integration**: Works seamlessly with attribute-based access control
- **Governance Hub**: Centralized visibility into tagged data and policies
- **Real-Time Updates**: Changes propagate instantly across all tagged assets

## Product Availability
- **Tag Policies**: Available in Public Preview on AWS, Azure, and GCP
- **Automated Classification**: Available in Public Preview
- **Governance Hub**: Available in Public Preview

## Use Cases

- **PII Protection**: Automatically mask all columns tagged as "PII" based on user attributes
- **Financial Data Governance**: Apply strict access controls to "financial" or "confidential" data
- **Cross-Catalog Consistency**: Ensure same protection levels across all catalogs
- **Compliance Automation**: Enforce regulatory requirements based on data classification

## Related Features
- [Attribute-Based Access Control (ABAC)](../abac/)
- [Data Classification](../data-classification/)
- [Anomaly Detection](../anomaly-detection/)
- [Unity Catalog Metrics](../uc-metrics/) 