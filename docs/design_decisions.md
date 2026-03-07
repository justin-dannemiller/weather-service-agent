### Why a lightweight agent implementation instead of LangChain.

For this project, I implemented a small custom agent loop consistenting of a planner, executor, and an orchestrating agent rather than relying on a framework such as LangChain.

The goal was to keep the system architecture explicit and easy to reason about while still following the same conceptual design used in framework-level tool-based LLM agents.

This approach provided several advantages for a project of this size and for a limited development period:

    - **Transparency:** The planning loop, tool execution, and error handling are fully visible in the code rather than abstracted behind a framework.
    - **Minimal dependencies:** The system only requires a small number of components, so introducing a full orchestration framework would add some unnecessary complexity.
    - **Structured Observability:** The custom designed tool calls return structured trace entries which capture inputs, outputs, errors, and execution timing, allowing the efficient establishment of observability and logging in the system

Note that in larger systems, a framework like LangChain is very valuable for standardizing these patterns and agent-tool-executor pipeline, but for this project, a lightweight implementation keeps the architecture simple and transparent