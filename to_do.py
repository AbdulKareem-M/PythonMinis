def display_task(tasks):
    if not tasks:
        print('Your to-do list is empty')
    else:
        print('Your To-Do list:')
        for i, task in enumerate(tasks, start=1):
            print(f'{i}. {task}')
        print()


def add_task(tasks):
    task = input('Enter a new task: ')
    tasks.append(task)
    print(f'Task {task} added to the list!')


def delete_task(tasks):
    if not tasks:
        print('Your To-Do list is empty! Nothing to delete')
        return
    display_task(tasks)
    try:
        task_num = int(input('Enter the task number to delete: '))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task {removed_task} deleted Successfully')
        else:
            print('Invalid task number')
    except ValueError:
        print('Please enter a valid number')


def to_do_list():
    tasks = []
    while True:
        print('To-Do List Menu:')
        print('1. View Tasks')
        print('2. Add New Task')
        print('3.Delete Task')
        print('4. Exit')
        choice = input('Enter your choice (1/2/3/4): ')

        if choice == '1':
            display_task(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice =='3':
            delete_task(tasks)
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Make sure you input a numer from the above options.')

    
to_do_list()