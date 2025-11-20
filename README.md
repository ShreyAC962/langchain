Github Repository for Reflexion Agent

Development Timeline

This github project follows the structure of this section's lectures, demonstrating key concepts in building a Reflexion Agent:

Add initial project structure - Corresponds to Project Setup

Set up the foundation with project configuration files (.gitignore, main.py, pyproject.toml, poetry.lock)

Create chains for AI-powered research functionality - Corresponds to Actor Agent

Implemented the first component of our agent architecture - the Actor

Added chains.py with prompt templates for generating detailed answers

Created schemas.py with Pydantic models for structured data handling

Enhance chains for answer revision capabilities - Corresponds to Revisor Agent

Implemented the second component - the Revisor for self-reflection

Added ReviseAnswer class to schemas.py for improved response structure

Updated chain prompts to incorporate critique and citation requirements

Add dependencies and tools for graph nodes - Corresponds to ToolNode - Executing Tools

Integrated search functionality to enhance response accuracy

Added required dependencies for the complete graph workflow

Implement the complete message graph - Corresponds to Building our LangGraph Graph

Connected Actor and Revisor agents in a complete LangGraph workflow

Defined graph nodes for drafting, tool execution, and revision

Established state management and conditional edge routing for reflection


