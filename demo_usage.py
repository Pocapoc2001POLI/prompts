"""
Example usage of the prompts.py module

This script demonstrates how to use the various prompt generation functions.
"""

import prompts


def demo_basic_usage():
    """Demonstrate basic prompt retrieval"""
    print("=" * 60)
    print("DEMO 1: Basic Prompt Retrieval")
    print("=" * 60)
    
    prompt = prompts.get_system_prompt()
    print(f"Prompt length: {len(prompt)} characters")
    print(f"First 200 characters:\n{prompt[:200]}...")
    print()


def demo_context_aware_prompts():
    """Demonstrate context-aware prompt generation"""
    print("=" * 60)
    print("DEMO 2: Context-Aware Prompts")
    print("=" * 60)
    
    # Small document
    prompt_small = prompts.get_system_prompt_with_context(
        context_type='text',
        context_length=100000,
        context_structure='Research paper',
        context_preview='Abstract: This paper presents...'
    )
    print("Small context (100K chars):")
    print("- Recommended: Strategy 1 (Direct processing)")
    print(f"- Prompt length: {len(prompt_small)} characters\n")
    
    # Medium document
    prompt_medium = prompts.get_system_prompt_with_context(
        context_type='markdown',
        context_length=1500000,
        context_structure='Technical documentation with sections'
    )
    print("Medium context (1.5M chars):")
    print("- Recommended: Strategy 2 (Chunk and aggregate)")
    print(f"- Prompt length: {len(prompt_medium)} characters\n")
    
    # Large document
    prompt_large = prompts.get_system_prompt_with_context(
        context_type='code',
        context_length=5000000,
        context_structure='Complete code repository'
    )
    print("Large context (5M chars):")
    print("- Recommended: Strategy 3 (Targeted search)")
    print(f"- Prompt length: {len(prompt_large)} characters\n")


def demo_specialized_prompts():
    """Demonstrate specialized prompt generation"""
    print("=" * 60)
    print("DEMO 3: Specialized Prompts")
    print("=" * 60)
    
    # Research prompt
    research_prompt = prompts.get_system_prompt_for_research(
        topic="Artificial Intelligence in Healthcare",
        document_type="research paper"
    )
    print(f"Research prompt for AI in Healthcare:")
    print(f"- Length: {len(research_prompt)} characters")
    print(f"- Includes: Pattern D (Research & Writing)\n")
    
    # Code prompt
    code_prompt = prompts.get_system_prompt_for_code(
        task_description="Implement a REST API for user authentication"
    )
    print(f"Code prompt for REST API implementation:")
    print(f"- Length: {len(code_prompt)} characters")
    print(f"- Includes: Pattern E (Code Analysis/Generation)\n")
    
    # Analysis prompt
    analysis_prompt = prompts.get_system_prompt_for_analysis(
        context_description="Annual financial report with tables and charts"
    )
    print(f"Analysis prompt for financial report:")
    print(f"- Length: {len(analysis_prompt)} characters")
    print(f"- Includes: Pattern B (Document/Context Analysis)\n")


def demo_prompt_structure():
    """Show the structure of the main prompt"""
    print("=" * 60)
    print("DEMO 4: Prompt Structure Overview")
    print("=" * 60)
    
    prompt = prompts.MOSAIC_SYSTEM_PROMPT
    
    sections = [
        ("Environment Capabilities", prompt.count("Python REPL") > 0),
        ("Core Principles (6 principles)", prompt.count("Execute, Don't Describe") > 0),
        ("Context Processing Strategies (5 strategies)", prompt.count("Strategy 1:") > 0),
        ("Task Patterns (6 patterns)", prompt.count("Pattern A:") > 0),
        ("Special Case Handling", prompt.count("When context variable exists") > 0),
        ("Output Format", prompt.count("FINAL(") > 0),
        ("Critical Rules", prompt.count("Critical Rules") > 0),
        ("Code Examples", prompt.count("chunk_size = len(context)") > 0),
    ]
    
    print("Main prompt includes:")
    for section_name, has_section in sections:
        status = "✓" if has_section else "✗"
        print(f"  {status} {section_name}")
    
    print(f"\nTotal prompt length: {len(prompt):,} characters")
    print()


def main():
    """Run all demos"""
    print("\n")
    print("=" * 60)
    print("PROMPTS.PY USAGE DEMONSTRATIONS")
    print("=" * 60)
    print()
    
    demo_basic_usage()
    demo_context_aware_prompts()
    demo_specialized_prompts()
    demo_prompt_structure()
    
    print("=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)
    print("\nFor more information, see the docstrings in prompts.py")
    print("or run: python -c 'import prompts; help(prompts)'")
    print()


if __name__ == '__main__':
    main()
