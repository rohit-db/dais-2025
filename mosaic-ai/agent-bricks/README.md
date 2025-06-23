# Agent Bricks: Auto-Optimized Agents Using Your Data

## Overview
Agent Bricks is a platform for building AI agents that are optimized for enterprise data and tasks. Users specify their problem and data, and Agent Bricks builds the best agent system based on quality and cost trade-offs. Rather than managing the overwhelming complexity of agent development, teams can focus on what matters most: defining their agent's purpose and providing strategic guidance on quality through natural language feedback. Agent Bricks handles the rest, automatically generating evaluation suites and auto-optimizing the quality.

Based on experiences working with customers to ship AI into production, Agent Bricks addresses three key challenges:
- **Evaluation is difficult**: Many enterprise AI tasks are difficult to evaluate, for both humans and automated LLM judges
- **Too many knobs**: Agents are complex AI systems with many components, each with their own optimization parameters
- **Cost and quality**: Teams often find that high-quality agents are too expensive to scale into production

## Resources

### Blogs & Docs
*   [Introducing Agent Bricks: Auto-Optimized Agents Using Your Data](https://www.databricks.com/blog/introducing-agent-bricks)
*   [Mosaic AI Announcements at Data + AI Summit 2025](https://www.databricks.com/blog/mosaic-ai-announcements-data-ai-summit-2025)
*   [Official Documentation](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/)

### Sessions & Videos

| | |
| --- | --- |
| [![Building and Scaling Production AI Systems with Mosaic AI](https://img.youtube.com/vi/9C-iZqa3ORc/0.jpg)](https://www.youtube.com/watch?v=9C-iZqa3ORc) | **Building and Scaling Production AI Systems with Mosaic AI**<br/>[View Session Details](https://www.databricks.com/dataaisummit/session/building-and-scaling-production-ai-systems-mosaic-ai) |
| [![Agent Bricks YouTube Link](https://img.youtube.com/vi/w8y_CGo1KQU/0.jpg)](https://www.youtube.com/watch?v=w8y_CGo1KQU&t=208s) | **Agent Bricks: Building Multi-Agent Systems for Structured and Unstructured Information**<br/>[View Session Details](https://www.databricks.com/dataaisummit/session/agent-bricks-building-multi-agent-systems-structured-and-unstructured) |

## Use Cases
![Agent Bricks](https://www.databricks.com/sites/default/files/styles/max_1000x1000/public/2025-06/DAIS25-What-s-New-in-Mosaic-AI-OG-02-2.png?itok%3D3GmqQ_D2%26v%3D1749593010)

Agent Bricks is optimized for common industry use cases, including:
- **Structured Information Extraction**: Parse and extract data from complex documents
- **Knowledge Assistance**: Build conversational agents over documents with high accuracy
- **Custom Text Transformation**: Transform and process text according to specific business rules
- **Orchestrated Multi-Agent Systems**: Coordinate multiple agents for complex workflows


## Product Availability
- **Information Extraction**: Currently in beta and available now
- **Knowledge Assistant**: Currently in beta and available now
- **Multi-Agent Supervisor**: Coming soon after Data + AI Summit 2025
- **Genie**: Available for conversational analytics over structured data
- **Agent Bricks Platform**: Full platform available in beta

## Key Features

### Auto-Optimized Agents
- **Declarative Task Definition**: Describe your agent's purpose in natural language and connect your data sources
- **Automatic Evaluation**: Agent Bricks automatically creates evaluation benchmarks specific to your task, including synthetic data generation and custom LLM judges
- **Intelligent Optimization**: Searches through and combines various optimization techniques such as prompt engineering, model fine-tuning, reward models, and test-adaptive optimization (TAO)
- **Cost-Quality Balance**: Ensures agents are both highly effective and cost-effective, with options for cost-optimized or quality-optimized models

### Agent Learning from Human Feedback (ALHF)
- **Rich Context Guidance**: Receive natural language guidance (e.g., "ignore all data before May 1990")
- **Intelligent Translation**: Algorithms translate guidance into technical optimizations across retrieval algorithms, prompts, vector database filtering, and agentic patterns
- **Natural Language Feedback**: Unlike traditional ML that uses numerical feedback, Agent Bricks incorporates natural language feedback for more precise and business-relevant improvements
- **Democratized Development**: Allows domain experts to contribute directly to system improvement without deep technical expertise

### Multi-Agent Systems
- **Supervisor Agent**: Coordinates multiple sub-agents and tools, handling complex queries that span structured and unstructured data
- **Domain Specialization**: Each agent specializes in a specific domain (structured or unstructured data)
- **Built-in Governance**: Ensures data access is controlled per agent with proper security policies
- **Complex Query Handling**: Can handle multi-step queries that require data from multiple sources

### Knowledge Assistant (Unstructured Data)
- **High-Quality RAG**: Designed for retrieval-augmented generation over unstructured data (docs, support tickets, etc.)
- **Built-in Metrics**: Includes comprehensive evaluation and production-grade endpoints
- **Advanced Parsing**: Outperforms other RAG solutions due to advanced parsing, chunking, and embedding strategies
- **Continuous Improvement**: Quality improves over time with expert feedback, even with a small number of labeled examples
- **Real-World Performance**: Customers have seen 40% increase in answer accuracy and 800% faster implementation

### Genie (Structured Data)
- **Conversational Analytics**: Enables natural language interactions over structured data
- **Business Context**: Tailored to business context and governed by data policies
- **Topic-Specific Spaces**: Create Genie spaces for specific topics (e.g., plans, billing) with sample questions and SQL examples
- **Data Governance**: Built-in data access controls and policy enforcement

### Production-Ready Capabilities
- **Enterprise-Grade Security**: Built-in security, monitoring, and deployment capabilities
- **Continuous Learning**: Performance continues to improve over time through continual learning
- **Quality Measurement**: Unique ability to measure, build, and continually improve quality
- **Cost Optimization**: Achieve higher quality at lower cost compared to DIY approaches

## Why It Matters
- **From Lab to Production**: Transform development timelines from weeks to a single day
- **Higher Quality Results**: Achieve significantly higher quality agents compared to other products in the space
- **Lower Costs**: Build higher-quality and lower-cost systems, up to 10x lower cost in some cases
- **Trusted in Production**: Used by Flo Health, AstraZeneca, and more to scale safe, accurate AI
- **Democratized AI**: Domain experts can create specialized agents without deep ML expertise
- **Natural Language Access**: Enable natural language interactions across all types of enterprise data

## Customer Success Stories

### Flo Health
> "Agent Bricks enabled us to double our medical accuracy over standard commercial LLMs, while meeting Flo Health's high internal standards for clinical accuracy, safety, privacy, and security." 
> 
> — Roman Bugaev, CTO, Flo Health

### AstraZeneca
> "With Agent Bricks, our teams were able to parse through more than 400,000 clinical trial documents and extract structured data points, without writing a single line of code. In just under 60 minutes, we had a working agent that can transform complex unstructured data usable for Analytics." 
> 
> — Joseph Roemer, Head of Data & AI, Commercial IT, AstraZeneca

### Hawaiian Electric
> "Agent Bricks significantly outperformed our original open-source implementation in both LLM-as-judge and human evaluation accuracy metrics." 
> 
> — Joel Wasson, Enterprise Data & Analytics, Hawaiian Electric

### North Dakota University System
> "Agent Bricks allowed us to build a cost-effective agent we could trust in production. With custom-tailored evaluation, we confidently developed an information extraction agent that parsed unstructured legislative calendars, saving 30 days of manual trial-and-error optimization." 
> 
> — Ryan Jockers, Assistant Director of Reporting and Analytics

## Practical Implementation

### Multi-Agent System Example: Telco Customer Support
A comprehensive example demonstrates building a multi-agent system for a telecom company with specialized agents:
- **Account Info Agent**: Handles customer account information
- **Billing Agent**: Manages billing-related queries
- **Products Agent**: Provides product information and recommendations
- **Tech Support Agent**: Handles technical support issues
- **Supervisor Agent**: Routes queries to the appropriate sub-agent

The system can handle complex scenarios such as:
- Answering technical support questions with context from multiple data sources
- Routing queries to appropriate specialized agents
- Combining structured data (customer plans, usage) with unstructured data (support tickets, documentation)
- Multi-step queries like checking a customer's plan, data usage, and suggesting solutions for speed issues

## Technical Architecture
- **Powered by MLflow 3**: Automatic creation of evaluation datasets and custom judges
- **Mosaic AI Research**: Built on the latest research in agent learning and optimization
- **Unity Catalog Integration**: Seamless integration with Databricks' data governance platform
- **Open Ecosystem**: Compatible with existing Databricks tools and workflows
- **Multi-Agent Coordination**: Advanced routing and coordination between specialized agents

## Related Features
- [MLflow 3.0](../mlflow-3.0/)
- [AI Gateway](../ai-gateway/)
- [Model Serving](../model-serving/)
- [Vector Search](../vector-search/)
- [AI Functions in SQL](../ai-functions-in-sql/)
