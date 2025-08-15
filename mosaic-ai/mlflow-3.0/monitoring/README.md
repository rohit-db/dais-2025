# Agent Monitoring with MLflow 3.0

## Overview

MLflow 3.0 introduces powerful new capabilities for monitoring and observing AI agents in production. This section demonstrates how to implement comprehensive agent monitoring using MLflow's new observability features, including trace logging, metrics collection, and centralized monitoring dashboards.

## Reference Implementation

For a complete, production-ready implementation of agent monitoring with MLflow 3.0, see the official Databricks Solutions repository:

**[Agent Monitoring Demo App](https://github.com/databricks-solutions/agent-monitoring-demo-app)**

This repository provides:
- **Full-stack application** with FastAPI backend and React frontend
- **MLflow 3.0 integration** for comprehensive agent tracing
- **Databricks Apps deployment** ready for production
- **Real-time monitoring dashboard** for agent performance
- **Complete development workflow** with hot reload and testing

### Sessions & Videos

| | |
| --- | --- |
| [![MLflow 3.0: AI and MLOps on Databricks](https://img.youtube.com/vi/UezTglxJC88/0.jpg)](https://www.youtube.com/watch?v=UezTglxJC88&t=4s) | **MLflow 3.0: AI and MLOps on Databricks**<br/>[View Session Details](https://www.databricks.com/dataaisummit/session/mlflow-30-ai-and-mlops-databricks) |


## Key Features Demonstrated

### 1. Cross-Platform Agent Observability
```python
import mlflow

# Monitor any agent, anywhere
with mlflow.observe() as run:
    # Your agent logic here
    response = agent.process_request(user_input)
    
    # Automatic trace logging
    mlflow.log_metric("response_time", response_time)
    mlflow.log_param("model_version", "claude-3-sonnet")
```

### 2. Centralized Monitoring Dashboard
- Real-time agent performance metrics
- Trace visualization and debugging
- Cost and usage analytics
- Error tracking and alerting

### 3. Production Deployment
- Databricks Apps integration
- Environment configuration management
- Automated deployment scripts
- Health monitoring and logging

## Core Code Examples

### Basic Agent Monitoring Setup
```python
# server/agents/databricks_assistant/agent.py
import mlflow
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models import ChatDatabricks
from openai.types.chat import ChatCompletionMessageParam

@mlflow.trace(span_type='LLM')
def databricks_agent(messages: List[ChatCompletionMessageParam]) -> Dict[str, Any]:
    """A LangChain agent that can explore Databricks catalogs and answer questions."""
    # Initialize the LLM
    llm = ChatDatabricks(
        endpoint='databricks-claude-sonnet-4',
        max_tokens=1000,
        temperature=0.1,
    )

    # Create the prompt template
    prompt = ChatPromptTemplate.from_messages([
        ('system', SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
    ])

    # Create tools and agent
    tools = create_catalog_tools()
    agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Execute the agent (MLflow tracing happens automatically)
    result = agent_executor.invoke({"messages": formatted_messages})
    
    return {
        'choices': [{'message': {'role': 'assistant', 'content': result['output']}}]
    }
```

### FastAPI Integration with MLflow Tracing
```python
# server/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import mlflow
from .agents.databricks_assistant import databricks_agent

app = FastAPI()

class AgentRequestOptions(BaseModel):
    """Request options for the agent API."""
    inputs: Dict[str, Any]

class QueryAgentResponse(BaseModel):
    """Response from the agent API."""
    response: Dict[str, Any]
    trace_id: str

@app.post("/api/agent")
async def agent(options: AgentRequestOptions) -> QueryAgentResponse:
    """Agent API with automatic MLflow tracing."""
    # Log agent requests for monitoring
    user_message = ''
    if options.inputs.get('messages'):
        user_message = options.inputs['messages'][-1].get('content', '')[:100]
    
    logger.info(f"Agent request received: '{user_message}...'")

    try:
        # The @mlflow.trace decorator handles tracing automatically
        response = databricks_agent(**options.inputs)
        trace_id = mlflow.get_last_active_trace_id()
        
        logger.info(f'Agent response generated successfully. Trace ID: {trace_id}')
        
        return QueryAgentResponse(
            response=response,
            trace_id=trace_id,
        )
    except Exception as e:
        logger.error(f'Agent request failed: {str(e)}')
        raise
```

### Environment Configuration
```python
# .env.local example
DATABRICKS_HOST="your-workspace.cloud.databricks.com"
DATABRICKS_TOKEN="your-token"
DATABRICKS_APP_NAME="your-agent-app"
MLFLOW_EXPERIMENT_ID="your-experiment-id"
DATABRICKS_AGENTS_MONITORING_DESTINATION="your.monitoring.schema.table"
```

### Frontend Integration
```typescript
// client/src/components/AgentChat.tsx
const sendMessage = async (message: string) => {
  try {
    const response = await fetch('/api/agent', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
        inputs: { 
          messages: [{ role: 'user', content: message }] 
        } 
      })
    });
    
    const data = await response.json();
    
    // Store trace ID for debugging and feedback
    console.log('MLflow Trace ID:', data.trace_id);
    
    return data.response.choices[0].message.content;
  } catch (error) {
    console.error('Agent request failed:', error);
    throw error;
  }
};

// Log user feedback with trace ID
const logFeedback = async (traceId: string, assessmentName: string, assessmentValue: any) => {
  await fetch('/api/log_assessment', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      trace_id: traceId,
      assessment_name: assessmentName,
      assessment_value: assessmentValue
    })
  });
};
```

For the complete implementation with full error handling, deployment scripts, and advanced features, see the [reference implementation](https://github.com/databricks-solutions/agent-monitoring-demo-app).

## Quick Start

1. **Clone the reference implementation:**
   ```bash
   git clone https://github.com/databricks-solutions/agent-monitoring-demo-app
   cd agent-monitoring-demo-app
   ```

2. **Set up your environment:**
   ```bash
   ./setup.sh
   ```

3. **Deploy to Databricks Apps:**
   ```bash
   ./deploy.sh
   ```

## Integration with Your Existing Stack

The demo app demonstrates how to integrate MLflow 3.0 monitoring with:
- **Unity Catalog** for governance and access control
- **Databricks SQL** for analytics and reporting
- **LakeFlow** for data pipeline monitoring
- **Mosaic AI** components for enhanced agent capabilities

## Customization Guide

The reference implementation is designed to be easily adaptable:

1. **Modify agent behavior** in `server/agents/databricks_assistant.py`
2. **Update monitoring metrics** in the MLflow integration layer
3. **Customize the dashboard** in `client/src/App.tsx`
4. **Add new endpoints** following the existing patterns


## Resources

- [MLflow 3.0 Documentation](https://mlflow.org/docs/latest/index.html)
- [Databricks Apps Documentation](https://docs.databricks.com/apps/index.html)
- [Agent Monitoring Best Practices](https://docs.databricks.com/machine-learning/mlflow/agent-monitoring.html)

## Next Steps

1. Explore the [reference implementation](https://github.com/databricks-solutions/agent-monitoring-demo-app) to understand the complete architecture
2. Adapt the monitoring patterns to your specific use cases
3. Integrate with your existing Unity Catalog and governance framework
4. Deploy your own monitored agents using the provided templates 