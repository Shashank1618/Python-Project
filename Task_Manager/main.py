'''
Create a list -Store a list aof task


'''
tasks=[]   #Creating a task

#add task
""""""
def add_task(title,description,priority="low",deadline=None):
    task={
        'title':title,
        'description': description,
        'priority':priority,
        'deadline':deadline
    }

    tasks.append(task)

#calling a function or invoking a function
add_task("Give lab list","Name of the students present in the list","High","2024-11-13")


#printing a task
print(tasks)

#Displaying and listing a task
def list_task():
    if not tasks:
        pass
    else:
        for i,task in enumerate(tasks,start=1):
            print(f'{task['title']} -{task['priority']}')

list_task()


def delete_task(task_index):
    if task_index<0 or task_index>=len(tasks):
        print("Invalid task index")
        return
    else:
        removed=tasks.pop(task_index)
        print(f'Task {removed['title']} deleted')




