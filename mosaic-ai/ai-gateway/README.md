# Mosaic AI Gateway

## Overview

Mosaic AI Gateway, now Generally Available, provides a single, unified entry point for all your AI services and applications. It acts as a centralized control plane, allowing you to manage, govern, and monitor all of your LLMs—whether they are hosted on Databricks, by a third-party provider like Anthropic or OpenAI, or are open-source models—from one place.

The Gateway simplifies the complexity of managing a diverse portfolio of AI models. It provides a consistent interface for your developers while giving administrators the tools they need to enforce governance, track usage and costs, and ensure reliability across the entire AI application landscape. With new capabilities like automatic provider fallback and PII and safety guardrails, the AI Gateway is an essential component for any enterprise serious about deploying production-grade AI.

## Resources

### Blogs & Docs
*   [Mosaic AI Announcements at Data + AI Summit 2025](https://www.databricks.com/blog/mosaic-ai-announcements-data-ai-summit-2025)
*   [Official Documentation: AI Gateway](https://docs.databricks.com/en/machine-learning/ai-gateway/index.html)

### Sessions & Videos

| | |
| --- | --- |
| [![Taming the LLM Wild West: Unified Governance with Mosaic AI Gateway](https://img.youtube.com/vi/x_16hchSFXY/0.jpg)](https://www.youtube.com/watch?v=x_16hchSFXY&t=1s) | **Taming the LLM Wild West: Unified Governance with Mosaic AI Gateway**<br/>[View Session Details](https://www.databricks.com/dataaisummit/session/taming-llm-wild-west-unified-governance-mosaic-ai-gateway) |

## Why It Matters

*   **Centralized Control**: Manage all your LLMs, regardless of where they are hosted, through a single pane of glass.
*   **Consistent Governance & Security**: Enforce consistent access control, rate limiting, and safety policies across all your AI applications.
*   **Cost Management**: Track usage and spending across different models and providers to control costs and optimize your AI investments.
*   **Improved Reliability and Flexibility**: Automatically failover between different model providers to ensure your applications remain available, and easily swap models without changing application code.

## Key Features

*   **Now Generally Available**: The AI Gateway is production-ready and available for all customers.
*   **Unified Entry Point**: Provides a single API endpoint for all AI services, simplifying development.
*   **Centralized Credential Management**: Securely store and manage credentials for all your LLM providers in one place.
*   **Provider Fallback**: Automatically route requests to a backup model provider if the primary one fails, increasing application resilience.
*   **PII & Safety Guardrails**: Implement policies to detect and filter personally identifiable information (PII) and enforce safety standards.
*   **Rate Limiting & Usage Tracking**: Set usage limits to control costs and track detailed usage logs for chargebacks and analysis.

## Related Features
*   [Model Serving](../model-serving/)
*   [MLflow 3.0](../mlflow-3.0/)
*   [Agent Bricks](../agent-bricks/)
*   [Unity Catalog](../../unity-catalog/README.md)
