# Attribute-Based Access Control (ABAC)

- **Official Blog Post**: [What's new with Databricks Unity Catalog at Data + AI Summit 2025](https://www.databricks.com/blog/whats-new-databricks-unity-catalog-data-ai-summit-2025)
- **Official Documentation**: [Unity Catalog ABAC Documentation](https://docs.databricks.com/abac)

## Resources
- [Data + AI Summit Session](https://www.databricks.com/dataaisummit/session/unleash-power-automated-data-governance-classify-tag-and-protect-your)
- [Video: Automated Data Governance Deep Dive](https://www.youtube.com/watch?v=o529ypvgJkk&t=12s)

   [![Automated Data Governance YouTube Link](https://img.youtube.com/vi/o529ypvgJkk/mqdefault.jpg)](https://www.youtube.com/watch?v=o529ypvgJkk&t=12s)

## Overview

Attribute-Based Access Control (ABAC) provides dynamic, context-aware policy enforcement based on user attributes, resource characteristics, and environmental factors. Unlike traditional RBAC, ABAC adapts to changing conditions and scales across large data estates.

## Key Features

- **Dynamic Policy Evaluation**: Real-time access decisions based on multiple attributes
- **Automated Enforcement**: Policies apply across entire data estate automatically
- **Request for Access (RFA)**: Streamlined workflow for data access requests
- **Governance Hub Integration**: Centralized monitoring and compliance tracking
- **Performance Optimized**: Efficient evaluation without impacting query performance

## Product Availability
- **ABAC**: Available in Public Preview on AWS, Azure, and GCP
- **Governance Hub**: Available in Public Preview
- **Request for Access**: Available in Public Preview

## Use Cases

- **PII Protection**: Mask sensitive data based on user role, location, and data sensitivity
- **Time-Based Access**: Grant access to financial data only during business hours
- **Compliance Enforcement**: Ensure only certified users access regulated data
- **Cross-Domain Governance**: Apply consistent policies across business units

## Related Features
- [Tag Policies](../tag-policies/)
- [Data Classification](../data-classification/)
- [Anomaly Detection](../anomaly-detection/)
- [Unity Catalog Metrics](../uc-metrics/)