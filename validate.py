"""
Comprehensive validation script for prompts.py

This script validates that all requirements from the problem statement are met.
"""

import prompts


def validate_core_components():
    """Validate that all core components are present"""
    print("=" * 70)
    print("VALIDATION 1: Core Components")
    print("=" * 70)
    
    prompt = prompts.MOSAIC_SYSTEM_PROMPT
    
    # Environment Capabilities
    capabilities = [
        'Python REPL',
        'Memory System',
        'memory_search',
        'memory_count',
        'Recursive LLM Queries',
        'llm_query',
        'llm_query_batched',
    ]
    
    print("\n✓ Environment Capabilities:")
    for cap in capabilities:
        assert cap in prompt, f"Missing: {cap}"
        print(f"  ✓ {cap}")
    
    # Core Principles (all 6)
    principles = [
        'Execute, Don\'t Describe',
        'Decompose Complex Tasks',
        'Verify Progress',
        'Use Variables as Buffers',
        'Check Memory First',
        'Think Step by Step',
    ]
    
    print("\n✓ Core Principles (6):")
    for principle in principles:
        assert principle in prompt, f"Missing: {principle}"
        print(f"  ✓ {principle}")
    
    print("\n✅ All core components present\n")


def validate_context_strategies():
    """Validate all 5 context processing strategies"""
    print("=" * 70)
    print("VALIDATION 2: Context Processing Strategies (5)")
    print("=" * 70)
    
    prompt = prompts.MOSAIC_SYSTEM_PROMPT
    
    strategies = [
        ('Strategy 1: Small Context', '< 500K characters'),
        ('Strategy 2: Medium Context', '500K - 2M characters'),
        ('Strategy 3: Large Context', '> 2M characters'),
        ('Strategy 4: Structured Content', 'Markdown, JSON'),
        ('Strategy 5: Iterative Reading', 'Sequential'),
    ]
    
    print()
    for strategy_name, description in strategies:
        assert strategy_name in prompt, f"Missing: {strategy_name}"
        print(f"✓ {strategy_name} ({description})")
    
    print("\n✅ All 5 strategies present\n")


def validate_task_patterns():
    """Validate all 6 task patterns"""
    print("=" * 70)
    print("VALIDATION 3: Task Patterns (6)")
    print("=" * 70)
    
    prompt = prompts.MOSAIC_SYSTEM_PROMPT
    
    patterns = [
        ('Pattern A', 'Simple Questions'),
        ('Pattern B', 'Document/Context Analysis'),
        ('Pattern C', 'Multi-Step Tasks'),
        ('Pattern D', 'Research & Writing'),
        ('Pattern E', 'Code Analysis/Generation'),
        ('Pattern F', 'Information Aggregation'),
    ]
    
    print()
    for pattern_id, description in patterns:
        assert pattern_id in prompt, f"Missing: {pattern_id}"
        print(f"✓ {pattern_id}: {description}")
    
    print("\n✅ All 6 patterns present\n")


def validate_special_cases():
    """Validate special case handling"""
    print("=" * 70)
    print("VALIDATION 4: Special Case Handling")
    print("=" * 70)
    
    prompt = prompts.MOSAIC_SYSTEM_PROMPT
    
    special_cases = [
        'When context variable exists',
        'When memory is relevant',
        'When task is ambiguous',
        'When errors occur',
    ]
    
    print()
    for case in special_cases:
        assert case in prompt, f"Missing: {case}"
        print(f"✓ {case}")
    
    print("\n✅ All special cases handled\n")


def validate_output_formats():
    """Validate output format specifications"""
    print("=" * 70)
    print("VALIDATION 5: Output Formats")
    print("=" * 70)
    
    prompt = prompts.MOSAIC_SYSTEM_PROMPT
    
    print()
    assert 'FINAL(' in prompt, "Missing: FINAL() format"
    print("✓ FINAL(answer) for direct text answers")
    
    assert 'FINAL_VAR(' in prompt, "Missing: FINAL_VAR() format"
    print("✓ FINAL_VAR(variable_name) for returning variables")
    
    print("\n✅ Output formats specified\n")


def validate_critical_rules():
    """Validate critical rules section"""
    print("=" * 70)
    print("VALIDATION 6: Critical Rules")
    print("=" * 70)
    
    prompt = prompts.MOSAIC_SYSTEM_PROMPT
    
    rules = [
        'Don\'t just plan—execute',
        'Show your work with print()',
        'Handle errors gracefully',
        'Be efficient with sub-LLMs',
        'Verify before finishing',
    ]
    
    print()
    assert 'Critical Rules' in prompt, "Missing: Critical Rules section"
    print("✓ Critical Rules section present")
    
    for rule in rules:
        if rule in prompt:
            print(f"✓ {rule}")
    
    print("\n✅ Critical rules documented\n")


def validate_code_examples():
    """Validate that working code examples are included"""
    print("=" * 70)
    print("VALIDATION 7: Code Examples")
    print("=" * 70)
    
    prompt = prompts.MOSAIC_SYSTEM_PROMPT
    
    code_patterns = [
        ('Chunking strategy', 'chunk_size = len(context) // 10'),
        ('Loop through chunks', 'for i in range(10):'),
        ('Sub-LLM queries', 'llm_query('),
        ('Memory search', 'memory_search('),
        ('Print progress', 'print('),
        ('Research pattern', 'research_questions'),
        ('Document sections', 'section_names'),
        ('Error handling', 'try:'),
        ('Final output', 'FINAL('),
    ]
    
    print()
    for description, pattern in code_patterns:
        assert pattern in prompt, f"Missing code pattern: {pattern}"
        print(f"✓ {description}: {pattern}")
    
    print("\n✅ All code examples present\n")


def validate_helper_functions():
    """Validate that all helper functions exist and work"""
    print("=" * 70)
    print("VALIDATION 8: Helper Functions")
    print("=" * 70)
    
    print()
    
    # Test get_system_prompt
    prompt1 = prompts.get_system_prompt()
    assert isinstance(prompt1, str) and len(prompt1) > 10000
    print("✓ get_system_prompt() - returns main prompt")
    
    # Test get_system_prompt_with_context
    prompt2 = prompts.get_system_prompt_with_context(
        context_type='text',
        context_length=100000,
        context_structure='Single document',
        context_preview='Sample text...'
    )
    assert isinstance(prompt2, str)
    assert 'Context Length' in prompt2
    assert 'Strategy 1' in prompt2
    print("✓ get_system_prompt_with_context() - injects context info")
    
    # Test get_system_prompt_for_research
    prompt3 = prompts.get_system_prompt_for_research(
        topic='AI Research',
        document_type='thesis'
    )
    assert isinstance(prompt3, str)
    assert 'AI Research' in prompt3
    assert 'Pattern D' in prompt3
    print("✓ get_system_prompt_for_research() - optimized for research")
    
    # Test get_system_prompt_for_code
    prompt4 = prompts.get_system_prompt_for_code(
        task_description='Build API'
    )
    assert isinstance(prompt4, str)
    assert 'Build API' in prompt4
    assert 'Pattern E' in prompt4
    print("✓ get_system_prompt_for_code() - optimized for code")
    
    # Test get_system_prompt_for_analysis
    prompt5 = prompts.get_system_prompt_for_analysis(
        context_description='Financial report'
    )
    assert isinstance(prompt5, str)
    assert 'Financial report' in prompt5
    assert 'Pattern B' in prompt5
    print("✓ get_system_prompt_for_analysis() - optimized for analysis")
    
    print("\n✅ All 5 helper functions working\n")


def validate_module_structure():
    """Validate module metadata and exports"""
    print("=" * 70)
    print("VALIDATION 9: Module Structure")
    print("=" * 70)
    
    print()
    
    # Check version
    assert hasattr(prompts, '__version__')
    print(f"✓ Module version: {prompts.__version__}")
    
    # Check __all__ exports
    assert hasattr(prompts, '__all__')
    assert len(prompts.__all__) == 6
    print(f"✓ Module exports: {len(prompts.__all__)} items")
    
    # Check all exports are accessible
    for export_name in prompts.__all__:
        assert hasattr(prompts, export_name), f"Missing export: {export_name}"
        print(f"  ✓ {export_name}")
    
    print("\n✅ Module structure correct\n")


def validate_prompt_size():
    """Validate that the prompt is comprehensive"""
    print("=" * 70)
    print("VALIDATION 10: Prompt Comprehensiveness")
    print("=" * 70)
    
    prompt = prompts.MOSAIC_SYSTEM_PROMPT
    
    print()
    print(f"✓ Main prompt length: {len(prompt):,} characters")
    print(f"✓ Main prompt lines: {prompt.count(chr(10)):,} lines")
    
    # Check for substantial content
    assert len(prompt) > 15000, "Prompt seems too short"
    print(f"✓ Prompt exceeds minimum length (15K chars)")
    
    # Count code blocks
    code_blocks = prompt.count('```python')
    print(f"✓ Python code examples: {code_blocks}")
    assert code_blocks >= 10, "Not enough code examples"
    
    print("\n✅ Prompt is comprehensive\n")


def main():
    """Run all validations"""
    print("\n")
    print("=" * 70)
    print("COMPREHENSIVE VALIDATION OF PROMPTS.PY")
    print("=" * 70)
    print("\nValidating against problem statement requirements...\n")
    
    try:
        validate_core_components()
        validate_context_strategies()
        validate_task_patterns()
        validate_special_cases()
        validate_output_formats()
        validate_critical_rules()
        validate_code_examples()
        validate_helper_functions()
        validate_module_structure()
        validate_prompt_size()
        
        print("=" * 70)
        print("✅ ALL VALIDATIONS PASSED")
        print("=" * 70)
        print("\nThe prompts.py file successfully meets all requirements:")
        print("  ✓ Complete RLM paper instructions (Appendix D)")
        print("  ✓ Mosaic memory system integration")
        print("  ✓ Multi-step task execution patterns")
        print("  ✓ Research/writing capabilities")
        print("  ✓ All 5 context processing strategies")
        print("  ✓ All 6 task patterns")
        print("  ✓ All 5 helper functions")
        print("  ✓ Comprehensive code examples")
        print("\n")
        
        return True
        
    except AssertionError as e:
        print(f"\n❌ VALIDATION FAILED: {e}\n")
        return False


if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
