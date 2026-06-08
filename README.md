# Copilot CLI Playground

A sandbox repo for testing and experimenting with Copilot CLI features.

## Purpose

This repository is a personal playground for trying Copilot CLI prompts, workflows, and small code changes in a low-risk environment. It is intentionally lightweight so you can explore how the CLI behaves across different file types and common development tasks.

## Features to Test

Use this repo to experiment with capabilities such as:

- Code generation for small scripts and utilities
- Code review and explanation of existing samples
- Refactoring suggestions
- Test creation for sample code
- Bug fixing and error handling improvements
- Documentation updates and markdown editing
- Repository exploration and summarization
- Prompt-driven edits across multiple files

## Directory Structure

The repository is organized by language and content type:

```text
copilot-cli-playground/
├── config/
│   └── .gitkeep
├── js-samples/
│   ├── async-function.js
│   ├── error-handling.js
│   └── hello-world.js
├── markdown-samples/
│   ├── architecture.md
│   └── documentation.md
├── py-samples/
│   ├── api-client.py
│   ├── data-processing.py
│   └── hello-world.py
├── tests/
│   └── .gitkeep
├── .gitignore
└── README.md
```

### Sample directories

- `js-samples/` - JavaScript examples for simple generation, refactoring, async flows, and error handling tasks.
- `py-samples/` - Python examples for explanation, cleanup, testing, and small feature additions.
- `markdown-samples/` - Documentation files for summarization, rewriting, and formatting experiments.
- `tests/` - Reserved for future automated tests generated or updated with Copilot CLI.
- `config/` - Reserved for future configuration files, templates, or environment examples.

## Getting Started

1. Open the repository in your terminal.
2. Browse the sample folders to pick a file type or scenario.
3. Run Copilot CLI prompts against a specific file or the full repo.
4. Try small, reversible experiments such as adding tests, refactoring code, or improving documentation.

Example:

```bash
cd ~/Documents/Repos/copilot-cli-playground
ls
```

## CLI Examples

Here are a few prompts and commands to try:

```bash
cd ~/Documents/Repos/copilot-cli-playground
```

```bash
copilot explain py-samples/data-processing.py
```

```bash
copilot review js-samples/error-handling.js
```

```bash
copilot "Add unit tests for py-samples/data-processing.py in the tests directory"
```

```bash
copilot "Refactor js-samples/async-function.js to use a more realistic async pattern"
```

```bash
copilot "Summarize the purpose of each folder in this repository"
```

## Notes

- This is a personal playground for experimentation.
- The samples are intentionally small and easy to modify.
- Empty `tests/` and `config/` directories are placeholders for future exercises.
