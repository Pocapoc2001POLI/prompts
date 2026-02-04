# Mosaic RLM System Prompts

A comprehensive Python module containing the Mosaic Recursive Language Model (RLM) system prompt that combines instructions from the RLM paper (Appendix D), memory system integration, and multi-step task execution patterns.

## Features

- **Complete RLM Implementation**: Full instructions from the RLM paper's Appendix D
- **Memory System Integration**: Built-in `memory_search()` and `memory_count()` functions
- **5 Context Processing Strategies**: Adaptive approaches for different context sizes
- **6 Task Patterns**: Proven patterns for various task types
- **5 Helper Functions**: Easy-to-use functions for different scenarios
- **Comprehensive Code Examples**: Working examples for all strategies and patterns

## Installation

Simply import the module:

```python
import prompts
```

## Quick Start

### Basic Usage

```python
import prompts

# Get the main system prompt
prompt = prompts.get_system_prompt()
print(f"Prompt length: {len(prompt)} characters")
```

### Context-Aware Prompts

```python
# For small documents (< 500K chars)
prompt = prompts.get_system_prompt_with_context(
    context_type='text',
    context_length=100000,
    context_structure='Research paper'
)

# For medium documents (500K-2M chars)
prompt = prompts.get_system_prompt_with_context(
    context_length=1500000
)

# For large documents (> 2M chars)
prompt = prompts.get_system_prompt_with_context(
    context_length=5000000
)
```

### Specialized Prompts

```python
# For research and writing tasks
research_prompt = prompts.get_system_prompt_for_research(
    topic="Artificial Intelligence in Healthcare",
    document_type="research paper"
)

# For code analysis or generation
code_prompt = prompts.get_system_prompt_for_code(
    task_description="Implement a REST API for user authentication"
)

# For document analysis
analysis_prompt = prompts.get_system_prompt_for_analysis(
    context_description="Annual financial report with tables and charts"
)
```

## Core Components

### Environment Capabilities

The system has access to:
- **Python REPL**: Persistent state across executions
- **Memory System**: `memory_search()` and `memory_count()`
- **Recursive LLM Queries**: `llm_query()` and `llm_query_batched()`
- **Standard Python**: All standard library functionality

### 6 Core Principles

1. **Execute, Don't Describe** - Do the task, don't just plan it
2. **Decompose Complex Tasks** - Break down into manageable steps
3. **Verify Progress** - Use print() to show work
4. **Use Variables as Buffers** - Store intermediate results
5. **Check Memory First** - Leverage existing knowledge
6. **Think Step by Step** - Show reasoning process

### 5 Context Processing Strategies

1. **Strategy 1: Small Context** (< 500K chars) - Direct feed to sub-LLM
2. **Strategy 2: Medium Context** (500K-2M chars) - Chunk and aggregate
3. **Strategy 3: Large Context** (> 2M chars) - Targeted search
4. **Strategy 4: Structured Content** - Structure-aware chunking (Markdown, JSON, etc.)
5. **Strategy 5: Iterative Reading** - Sequential with state maintenance

### 6 Task Patterns

- **Pattern A**: Simple Questions
- **Pattern B**: Document/Context Analysis
- **Pattern C**: Multi-Step Tasks
- **Pattern D**: Research & Writing
- **Pattern E**: Code Analysis/Generation
- **Pattern F**: Information Aggregation

## API Reference

### `get_system_prompt()`

Returns the main Mosaic RLM system prompt.

**Returns**: `str` - The complete system prompt

```python
prompt = prompts.get_system_prompt()
```

### `get_system_prompt_with_context(context_type, context_length, context_structure, context_preview)`

Returns the system prompt with context information injected.

**Parameters**:
- `context_type` (str, optional): Type of context ('text', 'code', 'markdown', 'json', etc.)
- `context_length` (int, optional): Length of context in characters
- `context_structure` (str, optional): Description of context structure
- `context_preview` (str, optional): Brief preview of context

**Returns**: `str` - System prompt with context info

```python
prompt = prompts.get_system_prompt_with_context(
    context_type='markdown',
    context_length=750000,
    context_structure='Technical documentation with sections',
    context_preview='# Introduction\n\nThis document...'
)
```

### `get_system_prompt_for_research(topic, document_type)`

Returns the system prompt optimized for research and writing tasks.

**Parameters**:
- `topic` (str): The research topic
- `document_type` (str): Type of document (default: "research paper")

**Returns**: `str` - System prompt optimized for research/writing

```python
prompt = prompts.get_system_prompt_for_research(
    topic="Quantum Computing Applications",
    document_type="thesis"
)
```

### `get_system_prompt_for_code(task_description)`

Returns the system prompt optimized for code analysis or generation tasks.

**Parameters**:
- `task_description` (str): Description of the code task

**Returns**: `str` - System prompt optimized for code tasks

```python
prompt = prompts.get_system_prompt_for_code(
    task_description="Analyze this codebase for security vulnerabilities"
)
```

### `get_system_prompt_for_analysis(context_description)`

Returns the system prompt optimized for document/context analysis tasks.

**Parameters**:
- `context_description` (str): Description of what context will be provided

**Returns**: `str` - System prompt optimized for analysis tasks

```python
prompt = prompts.get_system_prompt_for_analysis(
    context_description="Scientific research paper on climate change"
)
```

## Examples

See the included example files:

- `demo_usage.py` - Complete usage demonstrations
- `test_prompts.py` - Test suite showing all features
- `validate.py` - Comprehensive validation script

Run them with:

```bash
python demo_usage.py
python test_prompts.py
python validate.py
```

## System Prompt Structure

The main system prompt (`MOSAIC_SYSTEM_PROMPT`) contains:

1. **Environment Capabilities** - Available tools and functions
2. **Core Principles** - 6 guiding principles for optimal performance
3. **Context Processing Strategies** - 5 strategies for different context sizes
4. **Task Patterns** - 6 patterns for different task types
5. **Special Case Handling** - How to handle edge cases
6. **Output Format** - Using `FINAL()` and `FINAL_VAR()`
7. **Critical Rules** - Essential guidelines
8. **Code Examples** - Working examples for each strategy and pattern

Total length: ~20,000 characters with 18+ Python code examples.

## Use Cases

This prompt system is designed for:

- **PDF/Document Analysis**: Upload and analyze documents of any size
- **Research & Writing**: Write papers, theses, reports from scratch
- **Code Analysis**: Analyze repositories and codebases
- **Multi-Step Tasks**: Complex agentic workflows
- **Q&A with Memory**: Simple questions leveraging memory recall

## Testing

Run the test suite:

```bash
python test_prompts.py
```

Run comprehensive validation:

```bash
python validate.py
```

## License

See repository license.

## Contributing

Contributions welcome! Please ensure all tests pass before submitting PRs.

## References

Based on:
- The RLM paper "Recursive Language Models" (Appendix D system prompts)
- The "Context Is All You Really Need" research roadmap
- The Mosaic brain.py implementation
