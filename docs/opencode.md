# OpenCode Integration

This project includes [OpenCode](https://opencode.ai/) AI integration for enhanced development workflow.

## What is OpenCode?

OpenCode is an open-source AI coding agent that helps you write code in your terminal, IDE, or desktop. It supports multiple LLM providers and includes features like:

- LSP integration for intelligent code understanding
- Custom agents for specialized tasks
- Reusable skills for common patterns
- Multi-session support

## Project Configuration

### AGENTS.md

The `AGENTS.md` file at the project root provides instructions for AI coding agents:

- Project overview and stack
- Build/test/lint commands
- Code style guidelines
- Commit conventions
- Project structure

This file is automatically loaded by OpenCode when working in this repository.

## Custom Agents

Custom agents are defined in `.opencode/agents/`:

### Reviewer Agent

Location: `.opencode/agents/reviewer.md`

A code review agent with read-only permissions:

- Analyzes code quality
- Checks type safety
- Reviews test coverage
- Identifies security issues

**Usage:**

```
@reviewer review this function for potential issues
```

### Creating New Agents

Create a markdown file in `.opencode/agents/`:

```markdown
---
description: Description of what the agent does
mode: subagent
model: anthropic/claude-sonnet-4-20250514
temperature: 0.1
permission:
  edit: deny   # or allow, ask
  bash: deny
  write: deny
tools:
  write: false
  edit: false
---

System prompt for the agent...
```

## Skills

Skills are reusable instructions in `.opencode/skills/`:

### Test Generator Skill

Location: `.opencode/skills/test-generator/SKILL.md`

Generates pytest tests following project conventions:

- Proper markers (`@pytest.mark.unit`)
- Type hints on test functions
- Google-style docstrings
- Fixture usage
- Parametrized tests

**Usage:**

OpenCode automatically discovers skills. The agent can invoke them when needed:

```
Generate tests for the UserService class using the test-generator skill
```

### Creating New Skills

Create a `SKILL.md` file in `.opencode/skills/<skill-name>/`:

```markdown
---
name: skill-name
description: What the skill does
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: category
---

# Skill Name

Detailed instructions for using this skill...

## When to Use

Describe when this skill should be applied...

## How to Use

Step-by-step instructions...
```

## Best Practices

### Working with Agents

1. **Be specific** - Give clear, detailed instructions
2. **Use the right agent** - Use `@reviewer` for reviews, `@general` for search
3. **Review changes** - Always review AI-generated code before committing

### Using Skills

1. **Reference by name** - "Use the test-generator skill"
2. **Provide context** - Include the code to be processed
3. **Follow conventions** - Skills follow project patterns

### AGENTS.md Maintenance

Keep `AGENTS.md` updated when:

- Adding new commands
- Changing project structure
- Updating conventions
- Adding new dependencies

## Configuration

### opencode.json

For global configuration, create `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-20250514",
  "agent": {
    "build": {
      "model": "anthropic/claude-sonnet-4-20250514"
    }
  }
}
```

### Per-Project Settings

Project-specific settings in `.opencode/opencode.json`:

```json
{
  "model": "openai/gpt-4",
  "permission": {
    "bash": {
      "*": "ask",
      "just *": "allow",
      "just": "allow"
    }
  }
}
```

## Resources

- [OpenCode Documentation](https://opencode.ai/docs)
- [OpenCode GitHub](https://github.com/anomalyco/opencode)
- [Agents Documentation](https://opencode.ai/docs/agents)
- [Skills Documentation](https://opencode.ai/docs/skills)
