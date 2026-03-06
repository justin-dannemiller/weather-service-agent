from pydantic import BaseModel, Field

class ToolError(BaseModel):
    code: str = Field(..., description="The error code for the tool error")
    message: str = Field(..., description="The message explaining the error")

class ToolTraceEntry(BaseModel):
    tool_name: str = Field(..., description="The name of tool that was executed")
    input: dict = Field(..., description="The input arguments passed to the tool")
    success: bool = Field(..., description="Whether the tool execution was successful")
    output: dict = Field(None, description="The output of the tool execution") | None
    error: ToolError | None = None
    duration_ms: int = Field(..., description="The duration of the tool execution in milliseconds")