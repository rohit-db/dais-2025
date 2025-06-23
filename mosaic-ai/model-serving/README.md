# High-Scale Model Serving

## Overview

Databricks Model Serving provides a highly scalable and reliable service for deploying and querying AI models in production. It is designed to handle the most demanding enterprise workloads, from real-time recommendation engines to interactive chatbots, by delivering high throughput and low latency.

Recent enhancements have pushed the boundaries of performance even further. The infrastructure now supports over 250,000 queries per second (QPS) for traditional ML models. For LLM serving, Databricks has introduced a new proprietary, in-house inference engine with custom kernels to accelerate the performance of popular open-source models like Llama. This makes serving LLMs on Databricks easier, faster, and more cost-effective than ever before.

## Resources

### Blogs & Docs
*   [Mosaic AI Announcements at Data + AI Summit 2025](https://www.databricks.com/blog/mosaic-ai-announcements-data-ai-summit-2025)
*   [Official Documentation: Model Serving](https://docs.databricks.com/en/machine-learning/model-serving/index.html)

### Sessions & Videos

| | |
| --- | --- |
| [![Building and Scaling Production AI Systems with Mosaic AI](https://img.youtube.com/vi/9C-iZqa3ORc/0.jpg)](https://www.youtube.com/watch?v=9C-iZqa3ORc) | **Building and Scaling Production AI Systems with Mosaic AI**<br/>[View Session Details](https://www.databricks.com/dataaisummit/session/building-and-scaling-production-ai-systems-mosaic-ai) |

## Why It Matters

*   **Power Enterprise-Scale AI**: Serve real-time AI applications that can handle massive, production-level traffic without compromising on performance.
*   **Focus on Models, Not Infrastructure**: Offload the challenges of managing complex serving infrastructure, reliability, and scaling to Databricks.
*   **Faster, Cheaper LLM Inference**: The new proprietary inference engine provides superior performance and total cost of ownership compared to DIY serving solutions.
*   **Single, Unified Platform**: Deploy, manage, and govern all of your models—from classic ML to GenAI—within a single, integrated platform.

## Key Features

*   **Massive Throughput**: Enhanced infrastructure supports over 250,000 queries per second (QPS) for online ML workloads.
*   **Proprietary LLM Inference Engine**: A new, high-performance engine for serving LLMs that is up to 1.5x faster than open-source alternatives like vLLM on common workloads.
*   **Fully Managed Service**: Databricks handles all the underlying infrastructure, reliability, and scaling challenges.
*   **Optimized for All Models**: Built to serve any ML model, including scikit-learn, PyTorch, TensorFlow, and large language models.
*   **Integrated Governance**: All model endpoints are governed by Unity Catalog, providing centralized access control and management.

## Related Features
*   [Serverless GPU Compute](../serverless-gpus/)
*   [AI Gateway](../ai-gateway/)
*   [MLflow 3.0](../mlflow-3.0/)
*   [Unity Catalog](../../unity-catalog/README.md)