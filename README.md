# Task Logger App

A simple command-line application to log and view daily tasks for supervisors.

The HTML pages now include a basic login system that stores accounts in your
browser's `localStorage`. Open `login.html` to sign in or create a new account.
Once logged in you can access `index.html` to select a shift and enter logs.

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

### Web interface

1. Open `login.html` in your browser and sign in or create a new account.
2. After logging in you will be redirected to `index.html` where you can choose
   the date and shift.
3. Submit the form to record the shift details. Entries are stored in your
   browser's `localStorage` along with the supervisor name.
