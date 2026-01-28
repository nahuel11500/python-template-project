---
name: test-generator
description: Generate comprehensive pytest tests from Python source code
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: testing
---

# Test Generator Skill

Generate comprehensive pytest test suites from Python source code following project conventions.

## What I Do

- Analyze Python functions, classes, and modules
- Generate pytest test cases with proper markers (`@pytest.mark.unit`, `@pytest.mark.integration`)
- Create appropriate fixtures for test setup
- Follow the project's testing conventions and structure
- Ensure proper type hints in test code
- Generate docstrings for test functions

## When to Use Me

Use this skill when you need to:
- Create tests for new functionality
- Improve test coverage for existing code
- Generate test boilerplate following project patterns

## Test Structure

Tests should follow this structure:

```python
"""Tests for module_name."""

import pytest

from python_template.module import function_to_test


@pytest.mark.unit
class TestFunctionName:
    """Tests for function_name."""

    def test_basic_functionality(self) -> None:
        """Test basic expected behavior."""
        result = function_to_test(input_value)
        assert result == expected_value

    def test_edge_case(self) -> None:
        """Test edge case handling."""
        result = function_to_test(edge_input)
        assert result == edge_expected

    def test_error_handling(self) -> None:
        """Test error cases raise appropriate exceptions."""
        with pytest.raises(ValueError, match="expected message"):
            function_to_test(invalid_input)
```

## Conventions

1. **File naming**: `test_<module_name>.py`
2. **Class naming**: `Test<FunctionOrClassName>`
3. **Method naming**: `test_<behavior_description>`
4. **Markers**: Always use `@pytest.mark.unit` or `@pytest.mark.integration`
5. **Type hints**: All test functions should have `-> None` return type
6. **Docstrings**: One-line description of what the test verifies

## Fixture Usage

Use fixtures from `conftest.py` when available:

```python
@pytest.mark.unit
def test_with_client(self, client: TestClient) -> None:
    """Test API endpoint using test client fixture."""
    response = client.get("/endpoint")
    assert response.status_code == 200
```

## Parametrized Tests

For testing multiple inputs:

```python
@pytest.mark.unit
@pytest.mark.parametrize(
    "input_value,expected",
    [
        ("input1", "output1"),
        ("input2", "output2"),
        ("input3", "output3"),
    ],
)
def test_multiple_inputs(self, input_value: str, expected: str) -> None:
    """Test function with various inputs."""
    result = function_to_test(input_value)
    assert result == expected
```

## Coverage Requirements

- Project requires **90% minimum coverage**
- Focus on testing:
  - Happy paths
  - Edge cases
  - Error conditions
  - Boundary values
