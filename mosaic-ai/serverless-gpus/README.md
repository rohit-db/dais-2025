# Serverless GPU Compute

## Overview

Serverless GPU Compute represents a major step forward in making powerful AI workloads more accessible and cost-effective. This fully managed service eliminates the complexity of GPU infrastructure management, providing on-demand, auto-scaling access to high-performance GPUs directly within the Databricks serverless platform.

Whether you're training models, fine-tuning LLMs, or running large-scale inference, Serverless GPU Compute provides the performance you need without the operational overhead. You can run notebooks and jobs on powerful GPUs like the NVIDIA A10G (currently in Beta) and H100 (coming soon) without being locked into long-term reservations, paying only for the compute you use.

## Resources

### Blogs & Docs
*   [Mosaic AI Announcements at Data + AI Summit 2025](https://www.databricks.com/blog/mosaic-ai-announcements-data-ai-summit-2025)
*   [Official Documentation: Serverless compute](https://docs.databricks.com/en/compute/serverless-compute/index.html)

### Sessions & Videos

| | |
| --- | --- |
| [![Simplifying Training and GenAI Finetuning using Serverless GPU Compute](https://img.youtube.com/vi/pQMeeQ_jGY0/0.jpg)](https://www.youtube.com/watch?v=pQMeeQ_jGY0&t=2s) | **Simplifying Training and GenAI Finetuning using Serverless GPU Compute**<br/>[View Session Details](https://www.databricks.com/dataaisummit/session/simplifying-training-and-genai-finetuning-using-serverless-gpu-compute) |

## Why It Matters

*   **Eliminates Infrastructure Complexity**: Frees AI teams from managing GPU drivers, clusters, and capacity, allowing them to focus on building models.
*   **Cost-Effective Performance**: Pay-as-you-go pricing and auto-scaling ensure you get the performance you need without paying for idle resources or long-term commitments.
*   **Accelerates AI Development**: On-demand access to powerful GPUs allows for faster iteration on training, fine-tuning, and inference workloads.
*   **Secure and Governed**: Fully integrated into the Databricks platform, all workloads are secured and governed by Unity Catalog.

## Key Features

*   **Fully Managed Service**: No infrastructure for you to manage; Databricks handles the setup, maintenance, and scaling.
*   **On-Demand GPUs**: Get instant access to NVIDIA A10G GPUs (Beta), with H100 GPUs coming soon.
*   **Serverless Notebooks & Jobs**: Run both interactive development and scheduled production jobs on GPU-powered serverless compute.
*   **Auto-Scaling**: Compute resources automatically scale up and down based on workload demand.
*   **Unity Catalog Integration**: All jobs and data access are fully governed by Unity Catalog's fine-grained permissions.

## Related Features
*   [Model Serving](../model-serving/)
*   [MLflow 3.0](../mlflow-3.0/)
*   [Agent Bricks](../agent-bricks/)
*   [Unity Catalog](../../unity-catalog/README.md)
