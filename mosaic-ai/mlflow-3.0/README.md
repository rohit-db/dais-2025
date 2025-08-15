# MLflow 3.0

## Overview

MLflow 3.0 is a major redesign of the popular open-source platform, rebuilt from the ground up for the era of Generative AI. It unifies the development lifecycle for all AI assets, from traditional machine learning models to the most sophisticated agentic systems. This release introduces powerful new capabilities for agent observability, prompt management, and unified governance, extending MLflow's industry-leading experimentation and lifecycle management to meet the unique challenges of building enterprise-grade AI applications.

With MLflow 3.0, organizations gain a single, consistent platform to manage the entire AI lifecycle. It provides the tools to experiment, package, deploy, and govern any model or agent, on any cloud or even on-premise. This ensures that as teams adopt new GenAI technologies, they can maintain the same level of rigor, control, and collaboration they've come to expect for traditional ML.

## Resources

### Blogs & Docs
*   [MLflow 3.0: Unified AI Experimentation, Observability, and Governance](https://www.databricks.com/blog/mlflow-30-unified-ai-experimentation-observability-and-governance)
*   [Mosaic AI Announcements at Data + AI Summit 2025](https://www.databricks.com/blog/mosaic-ai-announcements-data-ai-summit-2025)
*   [Official MLflow Documentation](https://mlflow.org/docs/latest/index.html)

### Sessions & Videos

| | |
| --- | --- |
| [![MLflow 3.0: AI and MLOps on Databricks](https://img.youtube.com/vi/UezTglxJC88/0.jpg)](https://www.youtube.com/watch?v=UezTglxJC88&t=4s) | **MLflow 3.0: AI and MLOps on Databricks**<br/>[View Session Details](https://www.databricks.com/dataaisummit/session/mlflow-30-ai-and-mlops-databricks) |

## Why It Matters

*   **Unified AI Lifecycle**: Provides a single pane of glass to manage everything from classic ML models to complex, multi-component AI agents.
*   **Observability Anywhere**: Monitor, debug, and govern AI agents deployed on any platform—Databricks, other clouds, or on-premise—from a central location.
*   **Streamlined Governance**: Simplifies the process of ensuring all AI assets are secure, compliant, and governed under a unified framework with Unity Catalog.
*   **Future-Proofs Your AI Strategy**: Offers a flexible, open-source standard that adapts to the rapid evolution of AI, preventing vendor lock-in.

## Key Features

*   **Redesigned for Generative AI**: Core MLflow concepts like runs, artifacts, and models have been updated to natively support GenAI constructs like prompts, traces, and evaluations.
*   **Cross-Platform Agent Observability**: The `mlflow.observe` API captures rich traces, metrics, and metadata from AI agents running anywhere, sending them to a central MLflow server for analysis.
*   **Prompt Registry**: A new governance hub for managing, versioning, testing, and deploying versioned prompts as part-of an LLM-based application.
*   **Full AI Lifecycle Management**: A single workflow to manage the entire lifecycle—from experimentation to production—for any AI asset, including LLMs, agents, and traditional models.
*   **Native Unity Catalog Integration**: Use Unity Catalog to govern all AI assets, including prompts, evaluations, and agents, with fine-grained access control.
*   **Open, Extensible Standard**: Built on an open-source core, allowing you to connect and manage assets across any tool, platform, or environment.

## Related Features
*   [Agent Monitoring](monitoring/) - Production-ready agent monitoring with MLflow 3.0
*   [Agent Bricks](../agent-bricks/)
*   [AI Gateway](../ai-gateway/)
*   [Model Serving](../model-serving/)
*   [Vector Search](../vector-search/)
*   [Unity Catalog](../../unity-catalog/README.md)
