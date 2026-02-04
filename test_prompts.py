"""
Tests for prompts.py module
"""

import prompts


def test_get_system_prompt():
    """Test that get_system_prompt returns a non-empty string"""
    prompt = prompts.get_system_prompt()
    assert isinstance(prompt, str)
    assert len(prompt) > 1000
    assert "Mosaic RLM System Prompt" in prompt
    assert "Environment Capabilities" in prompt
    assert "Core Principles" in prompt
    assert "Context Processing Strategies" in prompt
    print("✓ get_system_prompt() works correctly")


def test_get_system_prompt_with_context():
    """Test context-aware prompt generation"""
    # Test with small context
    prompt_small = prompts.get_system_prompt_with_context(
        context_type='text',
        context_length=100000,
        context_structure='Single document'
    )
    assert "Strategy 1 (Direct processing)" in prompt_small
    assert "100,000 characters" in prompt_small
    print("✓ Small context prompt works")
    
    # Test with medium context
    prompt_medium = prompts.get_system_prompt_with_context(
        context_length=1000000
    )
    assert "Strategy 2 (Chunk and aggregate)" in prompt_medium
    print("✓ Medium context prompt works")
    
    # Test with large context
    prompt_large = prompts.get_system_prompt_with_context(
        context_length=5000000
    )
    assert "Strategy 3 (Targeted search)" in prompt_large
    print("✓ Large context prompt works")
    
    # Test with structured content
    prompt_structured = prompts.get_system_prompt_with_context(
        context_type='markdown',
        context_length=200000
    )
    assert "Strategy 4 (Structure-aware chunking)" in prompt_structured
    print("✓ Structured content prompt works")


def test_get_system_prompt_for_research():
    """Test research-specific prompt generation"""
    prompt = prompts.get_system_prompt_for_research(
        topic="Quantum Computing",
        document_type="thesis"
    )
    assert "Quantum Computing" in prompt
    assert "thesis" in prompt
    assert "Research Phase" in prompt
    assert "Pattern D" in prompt
    print("✓ Research prompt works correctly")


def test_get_system_prompt_for_code():
    """Test code-specific prompt generation"""
    prompt = prompts.get_system_prompt_for_code(
        task_description="Implement a binary search tree in Python"
    )
    assert "Implement a binary search tree" in prompt
    assert "Pattern E" in prompt
    assert "Code Quality Standards" in prompt
    print("✓ Code prompt works correctly")


def test_get_system_prompt_for_analysis():
    """Test analysis-specific prompt generation"""
    prompt = prompts.get_system_prompt_for_analysis(
        context_description="Research paper on machine learning"
    )
    assert "Research paper on machine learning" in prompt
    assert "Pattern B" in prompt
    assert "Analysis Phase" in prompt
    print("✓ Analysis prompt works correctly")


def test_prompt_contains_key_sections():
    """Test that the prompt contains all required sections"""
    prompt = prompts.MOSAIC_SYSTEM_PROMPT
    
    required_sections = [
        "Environment Capabilities",
        "Python REPL",
        "Memory System",
        "Recursive LLM Queries",
        "Core Principles",
        "Execute, Don't Describe",
        "Decompose Complex Tasks",
        "Verify Progress",
        "Use Variables as Buffers",
        "Check Memory First",
        "Think Step by Step",
        "Context Processing Strategies",
        "Strategy 1: Small Context",
        "Strategy 2: Medium Context",
        "Strategy 3: Large Context",
        "Strategy 4: Structured Content",
        "Strategy 5: Iterative Reading",
        "Task Patterns",
        "Pattern A: Simple Questions",
        "Pattern B: Document/Context Analysis",
        "Pattern C: Multi-Step Tasks",
        "Pattern D: Research & Writing",
        "Pattern E: Code Analysis/Generation",
        "Pattern F: Information Aggregation",
        "Special Case Handling",
        "Output Format",
        "Critical Rules",
    ]
    
    for section in required_sections:
        assert section in prompt, f"Missing required section: {section}"
    
    print(f"✓ All {len(required_sections)} required sections present")


def test_prompt_contains_code_examples():
    """Test that the prompt contains working code examples"""
    prompt = prompts.MOSAIC_SYSTEM_PROMPT
    
    required_code_patterns = [
        "chunk_size = len(context) // 10",
        "llm_query(",
        "memory_search(",
        "FINAL(",
        "for i in range(",
        "print(",
        "llm_query_batched(",
    ]
    
    for pattern in required_code_patterns:
        assert pattern in prompt, f"Missing code pattern: {pattern}"
    
    print(f"✓ All {len(required_code_patterns)} code patterns present")


def test_module_exports():
    """Test that all expected functions are exported"""
    expected_exports = [
        'MOSAIC_SYSTEM_PROMPT',
        'get_system_prompt',
        'get_system_prompt_with_context',
        'get_system_prompt_for_research',
        'get_system_prompt_for_code',
        'get_system_prompt_for_analysis',
    ]
    
    for export in expected_exports:
        assert hasattr(prompts, export), f"Missing export: {export}"
    
    print(f"✓ All {len(expected_exports)} exports available")


if __name__ == '__main__':
    print("Running prompts.py tests...\n")
    
    test_get_system_prompt()
    test_get_system_prompt_with_context()
    test_get_system_prompt_for_research()
    test_get_system_prompt_for_code()
    test_get_system_prompt_for_analysis()
    test_prompt_contains_key_sections()
    test_prompt_contains_code_examples()
    test_module_exports()
    
    print("\n✅ All tests passed!")
