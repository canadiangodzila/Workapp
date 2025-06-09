# Task Logger App

A simple command-line application to log and view daily tasks for supervisors.

## Setup

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Add a task:

```bash
python -m task_logger.cli add "Follow up with team" 
```

List tasks:

```bash
python -m task_logger.cli list
```
