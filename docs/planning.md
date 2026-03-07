## Planning Document
- I want to implement the parts with the least dependencies first, such as the tool input/output schemas, the tools, etc. write tests on these parts, and then expand to the more dependency-heavy parts like the API, agent, etc.

### Implementation order:
1) Define Input/Output Schema for each tool
2) Create temperature, weather_conditions, weather_advice tools
3) Define and run unit test(s) for each tool
4) Develop a @tool decorator that automatically builds a tool registry
5) Develop the Tool Executor responsible for executing tools and return the results or errors
6) Define and run unit tests on the executor
7) Create a lightweight LLM service wrapper around an external, API-based LLM, such as Grok 4
8) Implement the Planner which uses the LLM service to determine which tool to call and how
9) Define and run a unit tests on the Planner
10) Create an Agent which defines the simple loop orchestrating the entire workflow
    - Workflow spans from receiving the user prompt, to using the planner to generate the planned tool call, to using the executor to execute the tool, and repeating this process until termination
11) Add and run an integration test validating the Agent and its workflow
12) Add FastAPI router and /health and run route
13) Add simple test for the routes
14) Add evaluation harness for evaluation the system
15) Add logging
