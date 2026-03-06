## Planning Document
- I want to implement the parts with the least dependencies first, such as the tool input/output schemas, the tools, etc. write tests on these parts, and then expand to the more dependency-heavy parts like the API, agent, etc.

Implementation order:
1) Define tool Input/Output Schema in the /models folder
2) Create tools in the /tools folder
3) Define unit test(s) for each tool in the /test folder outside the weather_service_agent package
4) Implement the LangChain agent in /services folder
5) Create function for running agent and giving final LLM response
6) Add integration test to /test folder which tests the agent.
7) Add FastAPI router and route
8) Add test in /test to test endpoint
9) Add evaluation harness for evaluation the system
10) Add logging