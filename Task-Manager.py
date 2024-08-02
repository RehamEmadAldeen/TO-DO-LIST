import json

def load_tasks():
  try:
    with open("Tasks.json", "r") as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def save_tasks():
  with open("Tasks.json", "w") as file:
    json.dump(tasks, file)

def main():
  global tasks
  tasks = load_tasks()

  message = '''
  1- Add tasks to a list
  2- View Tasks
  3- Mark task as complete
  4- Remove Task
  5- Quit
  '''
  while True:
    print(message)
    choice = input('Enter your choice: ')

    if choice == '1':
      add_tasks()

    elif choice == '2':
      view_tasks()

    elif choice == '3':
      mark_task_complete()

    elif choice == '4':
      remove_task()

    elif choice == '5':
      save_tasks()
      break
    else:
      print('Invalid choice, please enter a number between 1 and 5')

def add_tasks():
  # get task from user
  addTask = input('Add your Task: ')

  # define task status
  task_info = {'task': addTask, 'completed': False}
  # add task to the list of tasks
  tasks.append(task_info)
  print("Task added successfully!")
  save_tasks()

def view_tasks():
  if not tasks:
    print("No tasks found!")
    return

  else:
    for i, task in enumerate(tasks):
      task_status = '✓' if task['completed'] else '✗'
      # windowns + dot -> emoji
      print(f'{i+1}. {task["task"]} {task_status}')

def mark_task_complete():
  # get list of incomplete tasks
  incomplete_tasks = [task for task in tasks if not task['completed']]

# check if the list is empty or not 
  if len (incomplete_tasks) == 0:
    print("There's no task to mark as complete")
    return

  for i, task in enumerate(incomplete_tasks):
    print(f'{i+1}. {task["task"]}')
    print('-'*30)

  # get the task from the user
  try:
    task_number = int(input('choose the task number to mark as complete: '))

    if task_number < 1 or task_number > len(incomplete_tasks):
      print ("Invalid Task Number")
      return


  # mark the task as completed 
    incomplete_tasks[task_number -1]["completed"] = True 

    print('Task marked as complete!')
  except ValueError:
    print("Invalid Input, Please enter a number")
    save_tasks()


def remove_task():
  # get list of tasks
  for i, task in enumerate(tasks):
    print(f'{i+1}. {task["task"]}')

  # get the task from the user
  task_number = int(input('choose the task number to remove: '))

  # remove the task
  del tasks[task_number -1]

  print('Task removed!')
  save_tasks()

main()