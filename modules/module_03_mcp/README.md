# Workshop Module: MCP Servers with Maestro

## What is MCP?

The Model Context Protocol (MCP) is an open standard that defines how applications provide context and tools to Large Language Models. Instead of building custom integrations for every AI application, MCP provides a universal way to expose your data and functionality to AI agents.

**Key insight**: MCP turns your existing systems into AI-accessible tools without rebuilding infrastructure.

## Why MCP with Maestro?

Maestro acts as an MCP client, connecting to remote MCP servers to:

- **Discover tools dynamically**: Servers expose their capabilities; Maestro learns what's available
- **Execute tools on-demand**: During a conversation, Maestro calls the appropriate tools to answer queries
- **Access real-time data**: Query live systems without pre-indexing or data duplication
- **Maintain security**: Server-side authentication and controlled access to sensitive operations

## How Maestro Uses MCP Servers

1. **Registration**: You provide the MCP server URL and authentication
2. **Discovery**: Maestro connects and retrieves the list of available tools
3. **Planning**: During execution, Maestro decides which tools to invoke based on the query
4. **Invocation**: Maestro calls the appropriate tools with parameters
5. **Response**: Results are incorporated into the generated answer

## Remote MCP Servers

Remote MCP servers extend AI capabilities beyond local environments, providing:

- **Accessibility**: Reachable from any MCP client with internet connection
- **Centralized logic**: Server-side processing and authentication
- **Scalability**: Single server serves multiple clients and sessions
- **Security**: Controlled access through authentication headers

## Key Concepts

### Tool Discovery
MCP servers expose tools with complete metadata (name, description, parameters). Maestro automatically discovers available tools when connecting.

### Authentication
Secure your MCP servers using standard HTTP authentication:
- Bearer tokens in `Authorization` header
- API keys in custom headers
- OAuth tokens

### Tool Selection
Maestro's planning layer analyzes the query and selects appropriate tools from the discovered set. Clear tool descriptions improve selection accuracy.

### Multi-Path Exploration
Maestro may explore multiple approaches to solve a task, potentially calling the same tool multiple times. Design tools to handle this behavior:
- **Safe**: Read-only operations (get, search, list)
- **Caution**: State-changing operations (create, update, delete)

## When to Use MCP

### ✅ Ideal Use Cases
- **Internal systems**: Employee databases, CRM, project management
- **Multiple related operations**: CRUD operations on the same data model
- **Dynamic tool sets**: Tools that change or expand over time
- **Secure integrations**: Systems requiring authentication and authorization
- **Reusable services**: Share the same server across multiple AI applications

## Demo: Employee Management System

### The Use Case

We'll build an MCP server that exposes employee management tools, allowing Maestro to answer questions about departments, salaries, reporting structures, and more—all through natural language queries.

### What You'll Build

An MCP server with tools for:
- **get_employee_by_id**: Retrieve employee details
- **search_employee_by_name**: Find employees with fuzzy name matching
- **search_employees_by_department**: List all employees in a department
- **get_salary_range**: Find employees within salary bounds
- **get_employee_hierarchy**: View reporting relationships
- **get_department_statistics**: Aggregate department metrics


### Example Queries

Once connected, Maestro can answer:
- "What is Alice Johnson's salary?"
- "Show me all employees in Engineering making over $100k"
- "Who reports to the Engineering Manager?"
- "What's the average salary by department?"
- "Find all employees managed by EMP005"

Maestro automatically determines which tools to call and how to combine their results.

## Best Practices

1. **Clear tool descriptions**: Maestro uses these to decide when to invoke each tool
2. **Structured outputs**: Return JSON with consistent schema
3. **Limit exposed tools**: Use `allowed_tools` to scope what Maestro can access
4. **Design for idempotency**: Tools may be called multiple times
5. **Secure your endpoints**: Use proper authentication
6. **Descriptive parameter names**: Help Maestro understand what each parameter does

## Architecture Overview
```
User Query → Maestro (MCP Client)
                ↓
        1. Connect to MCP Server
        2. Discover available tools
        3. Analyze query
        4. Select & invoke tools
        5. Combine results
                ↓
        Natural Language Response
```

## Learning Objectives

By the end of this module:
1. Understand MCP architecture and benefits
2. Build a remote MCP server using FastMCP
3. Expose the server with ngrok for remote access
4. Connect Maestro to your MCP server
5. Test multi-tool queries and observe tool selection
6. Apply security best practices for production MCP servers

---

**Next**: Hands-on implementation of an Employee Management MCP server