# Boot.dev AI Agent

A command-line AI coding agent built in Python while working through Boot.dev's **Build an AI Agent in Python** course.

The project demonstrates how an LLM can use tools to inspect files, modify code, execute Python programs, and iteratively work toward a solution.

## Course

[Build an AI Agent in Python — Boot.dev](https://www.boot.dev/courses/build-ai-agent-python)

This project follows the course's core architecture while using the **official OpenAI Python SDK with the direct OpenAI API**, rather than OpenRouter.

## Features

- **LLM-powered CLI:** Accept coding tasks through command-line prompts.
- **Filesystem inspection:** List files and directories.
- **File reading:** Read file contents with a configurable character limit.
- **File writing:** Create and overwrite files.
- **Python execution:** Run Python scripts and capture their output and errors.
- **Tool calling:** Let the LLM choose which available function to invoke.
- **Agent loop:** Execute multiple tool calls until the model returns a final response, with a limit of 20 iterations.
- **Verbose mode:** Inspect tool calls, arguments, token usage, and execution results.

## Tech Stack

- Python
- OpenAI Python SDK
- OpenAI API (`gpt-5.4-mini`)
- `uv` for dependency and environment management
- `python-dotenv` for environment configuration

## Getting Started

### Prerequisites

- Python
- [`uv`](https://docs.astral.sh/uv/)
- An OpenAI API key

### Installation

Clone the repository, then navigate to its root directory.

Install the project dependencies:

```bash
uv sync
```

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace the placeholder with your own API key. Never commit your `.env` file or expose your API key publicly.

## Usage

Run the agent with a coding task:

```bash
uv run main.py "Explain how the calculator renders results to the console."
```

Enable verbose output to inspect the agent's execution:

```bash
uv run main.py "List the files in the calculator project." --verbose
```

You can also ask it to investigate and fix a bug:

```bash
uv run main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20."
```

The agent can inspect the calculator code, modify files using its tools, and execute Python scripts when needed.

## Architecture

The project separates the LLM interaction from the functions it can execute.

- `main.py` — CLI entry point, conversation history, model requests, and agent loop.
- `prompts.py` — System prompt defining the agent's behavior.
- `call_function.py` — Function dispatch and tool-result message construction.
- `config.py` — Shared configuration, including the file-content limit.
- `functions/` — Implementations of the filesystem and Python execution tools.
- `calculator/` — Sample Python calculator application used to test the agent.
- `test_*.py` — Tests for the individual tools.

### Agent workflow

1. Receive a task from the user.
2. Send the conversation and available tool definitions to the LLM.
3. Execute any requested tool calls.
4. Append assistant messages and tool results to the conversation history.
5. Repeat until the model returns a final response or the iteration limit is reached.

## Learning Progress

| Commit | Milestone |
|---|---|
| `feat: complete chapter 1` | CLI chatbot and token usage tracking |
| `feat: add agent filesystem tools` | Filesystem and Python execution tools |
| `feat: implement agent tool execution` | Tool schemas, selection, and dispatch |
| `feat: implement agent loop` | Multi-step tool execution and iterative bug fixing |

## Security Considerations

This is a learning project, not a production-hardened coding agent.

The agent can write files and execute Python code. Working-directory checks help restrict file operations, but they are not a complete security sandbox. Run it only in directories where you understand and accept the potential impact of its actions.

## Purpose

The goal of this project is to understand the fundamentals of LLM-powered agents: tool calling, conversation state, function execution, feedback loops, and iterative problem-solving.
