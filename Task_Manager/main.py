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
        'deadline':deadline,
        'status':'pending'
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

'''changing status of the task
    marking the task as completed
    toggle the task whether it is completed or pending
    '''

def toggleStatus(index_of_task):
    
    
    if index_of_task < 0 or index_of_task >= len(tasks):
        print("Invalid task index")
        return
    elif tasks[index_of_task] =='completed':
        tasks[index_of_task] ='pending'
    else:
        tasks[index_of_task]='completed'



"""Adding task priorities and deadline filters"""


#iterator: Act like a loop
def filter_by_priority(priority_level):
    priority_level = priority_level.lower()
    ''' filtered_tasks = [task for task in tasks if task['priority'] == priority_level]   list comprehension

    filtered_tasks = []
    for task in tasks:
        if task['priority'] == priority_level:
            filtered_tasks.append(task)
    return filtered_tasks'''

#lambda function:Single line function
    filtered_task=list(filter(lambda task:task['priority'] == priority_level,tasks))
    






