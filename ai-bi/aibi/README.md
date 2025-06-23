# AI/BI: Dashboards and Genie

## Overview
AI/BI from Databricks reinvents business intelligence by combining generative AI with a unified governance layer. It enables everyone, from business users to expert analysts, to understand and query data through an intuitive, conversational interface. The two key components are:
- **AI/BI Genie**: An agentic, text-to-SQL system that allows users to ask data questions in natural language and get instant, accurate answers.
- **AI/BI Dashboards**: An intuitive experience for creating and distributing interactive dashboards with compelling visualizations and AI-powered insights.

Both are built on the Databricks Data Intelligence Platform and leverage Unity Catalog for a robust, governed semantic layer, ensuring that insights are both accessible and trustworthy.

## Resources
### Blogs & Docs
- [Blog: AI/BI Genie is now Generally Available](https://www.databricks.com/blog/aibi-genie-now-generally-available)
- [Docs: AI/BI Release Notes (2025)](https://docs.databricks.com/aws/en/ai-bi/release-notes/2025)
- [Docs: Official Dashboards Documentation](https://docs.databricks.com/dashboards)
- [Docs: Official Genie Documentation](https://docs.databricks.com/genie)

### Sessions & Videos
| | |
|---|---|
| [![AI/BI Genie: A Look Under the Hood](https://img.youtube.com/vi/PAQtKwcygV0/0.jpg)](https://www.youtube.com/watch?v=PAQtKwcygV0) | **AI/BI Genie: A Look Under the Hood**<br/>[Data + AI Summit Session](https://www.databricks.com/dataaisummit/session/aibi-genie-look-under-hood-everyones-friendly-neighborhood-genai) |
| [![AI/BI Dashboards and AI/BI Genie](https://img.youtube.com/vi/9XN_A-AOwyU/0.jpg)](https://www.youtube.com/watch?v=9XN_A-AOwyU) | **AI/BI Dashboards and AI/BI Genie: Dashboards and Last-Mile Analytics, Made Easy**<br/>[Data + AI Summit Session](https://www.databricks.com/dataaisummit/session/aibi-dashboards-and-aibi-genie-dashboards-and-last-mile-analytics-made) |
| [![Driving Trusted Insights with AI/BI and Unity Catalog Metric Views](https://img.youtube.com/vi/jBcBWC-TxNQ/0.jpg)](https://www.youtube.com/watch?v=jBcBWC-TxNQ&t=7s) | **Driving Trusted Insights with AI/BI and Unity Catalog Metric Views**<br/>[Data + AI Summit Session](https://www.databricks.com/dataaisummit/session/driving-trusted-insights-aibi-and-unity-catalog-metric-views) |
| [![Securely Deploying AI/BI to All Users in Your Enterprise](https://img.youtube.com/vi/J0nbX195Au8/0.jpg)](https://www.youtube.com/watch?v=J0nbX195Au8&t=5s) | **Securely Deploying AI/BI to All Users in Your Enterprise**<br/>[Data + AI Summit Session](https://www.databricks.com/dataaisummit/session/securely-deploying-aibi-all-users-your-enterprise) |

## How It Works
The AI/BI system provides two complementary experiences built on a shared foundation of governed data and semantics in Unity Catalog.
-   **AI/BI Dashboards** provide the canvas for creating and sharing curated, interactive visualizations and reports. Authors can build rich, pixel-perfect dashboards that deliver key insights, while consumers can explore and filter the data to answer their own questions.
-   **AI/BI Genie** acts as a conversational, agentic engine for ad-hoc data exploration. It uses a multi-LLM, retrieval-augmented generation (RAG) process to understand natural language questions, generate SQL, and deliver accurate answers. It learns from user feedback and semantic context stored in its Knowledge Store.

Together, they allow organizations to serve the full spectrum of BI needs—from standardized reporting to flexible, conversational analytics—all from a single, trusted platform.

## What's New in 2025
The AI/BI platform is rapidly evolving. Key updates in 2025 include:
- **Public Preview of Unity Catalog Metric Views**, creating a centralized semantic layer for consistent, reusable business metrics across both Dashboards and Genie.
- **Genie's Chain-of-Thought Reasoning**, which breaks down complex questions into smaller steps to generate more robust and accurate SQL.
- **Enhanced Curation for Genie**, including support for column synonyms, value dictionaries, and the ability to hide irrelevant columns to simplify the data model.
- **New Dashboard Capabilities** like direct file uploads to Unity Catalog, custom dashboard themes, and the ability to create new calculated measures without modifying underlying SQL.

For a full list of updates, see the [AI/BI Release Notes (2025)](https://docs.databricks.com/aws/en/ai-bi/release-notes/2025).

## Key Features
### AI/BI Dashboards
- **Interactive Visualizations**: Build and share rich, responsive dashboards with a wide array of chart types.
- **Custom Themes & Calculations**: Customize dashboard appearance with themes and create new measures on the fly without changing the dataset's SQL.
- **Direct Data Uploads**: Authors can upload files like CSVs directly to Unity Catalog from the dashboard interface.
- **Service Principal Publishing**: Automate the publishing of dashboards using service principal credentials.

### AI/BI Genie
- **Conversational Interface**: Ask questions of your data in natural language and receive answers in text, tables, and charts.
- **Agentic Text-to-SQL System**: Uses multiple LLMs, retrieval, and user feedback for a flexible and accurate analytics experience.
- **Curated Knowledge Store**: Package data and semantics (metrics, instructions, certified assets, value dictionaries, synonyms) to provide contextual and accurate answers.
- **Editable Filters & Responses**: Refine Genie's answers by directly editing filter values in the UI.

### Shared Capabilities
- **Unified Governance with UC Metric Views**: Natively integrated with Unity Catalog to centralize and govern key business metrics, ensuring consistency and trust.
- **Databricks One**: A simplified, consolidated experience for business users to safely access AI/BI Dashboards and Genie spaces.
- **Deep Research (Upcoming)**: A new mode in Genie to tackle complex "why" questions by creating research plans and analyzing multiple hypotheses.

## Why It Matters
- **Democratizes Data**: Makes data analytics accessible to users of all technical skill levels, fostering a "human + AI" collaborative environment.
- **Increases Efficiency**: Reduces the time from question to insight, freeing up analysts to focus on higher-value work.
- **Ensures Trust & Consistency**: Guarantees consistency and trust in data by centralizing metric logic in Unity Catalog. This eliminates siloed, inconsistent definitions across different tools and dashboards.
- **Deeper Insights**: Moves beyond "what happened" to "why it happened" with AI-driven analysis.

## Related Features
- Unity Catalog
- Databricks Apps
- Databricks One
- AI Functions in SQL
