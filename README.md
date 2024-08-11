# Sailing Downstream

Welcome to the **Sailing Downstream** repository! This repository contains various tasks meant for mentorship purposes, covering different programming languages and tools. Below you will find instructions on how to set up, run, and test each task.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Tasks](#tasks)
  - [JavaScript Task](#javascript-task)
  - [OCaml Task](#ocaml-task)
  - [Python Task](#python-task)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository is designed to help you practice and enhance your programming skills through various tasks. Each task is organized into its own directory with the necessary files to complete it.

## Prerequisites

Before running any tasks, make sure you have the following installed on your system:

- **Node.js** (for JavaScript tasks)
- **OCaml** (for OCaml tasks)
- **Python** (for Python tasks)
- A terminal or command-line interface

You may also need specific package managers or tools such as `npm`, `opam`, or `pip` for dependency management.

## Tasks

### JavaScript Task

**Directory:** `javascript_task/`

This task involves working with JavaScript. To get started:

1. Navigate to the `javascript_task` directory:
   ```bash
   cd javascript_task
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the task:
   ```bash
   node index.js
   ```

### OCaml Task

**Directory:** `ocaml_task/`

This task is centered around OCaml. To run the OCaml task:

1. Navigate to the `ocaml_task` directory:
   ```bash
   cd ocaml_task
   ```
2. Install dependencies using `opam`:
   ```bash
   opam install . --deps-only
   ```
3. Build and run the task:
   ```bash
   dune exec ./main.exe
   ```

### Python Task

**Directory:** `python_task/`

This task focuses on Python. Follow these steps to run the Python task:

1. Navigate to the `python_task` directory:
   ```bash
   cd python_task
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the task:
   ```bash
   python main.py
   ```

## Running Tests

Each task includes its own test suite. To run the tests:

- **JavaScript Task:**
  ```bash
  npm test
  ```
- **OCaml Task:**
  ```bash
  dune runtest
  ```
- **Python Task:**
  ```bash
  pytest
  ```

Make sure to navigate to the appropriate directory before running the tests.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes. Ensure that all tests pass and that your code adheres to the project's style guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
