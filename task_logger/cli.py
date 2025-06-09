import argparse
import os
import sqlite3
from datetime import datetime

db_path = os.path.join(os.path.dirname(__file__), 'tasks.db')

def init_db():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, description TEXT)')
    conn.commit()
    conn.close()

def add_task(description):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('INSERT INTO tasks (date, description) VALUES (?, ?)', (datetime.now().isoformat(), description))
    conn.commit()
    conn.close()
    print('Task added.')

def list_tasks():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    for row in cur.execute('SELECT id, date, description FROM tasks ORDER BY id DESC'):
        print(f"{row[0]} - {row[1]} - {row[2]}")
    conn.close()

def main():
    parser = argparse.ArgumentParser(description='Task Logger')
    subparsers = parser.add_subparsers(dest='command', required=True)

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', help='Task description')

    subparsers.add_parser('list', help='List tasks')

    args = parser.parse_args()
    init_db()
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list':
        list_tasks()

if __name__ == '__main__':
    main()
