"""
Author: Telaprolu Abhinaya Sri
Internship: Python Programming May Batch A54
Task 1:
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists
Description: 
This script implements to-do list application using command line interface.
    One can track their to-do list,add a new task,
    delete a task,update their to-do list.
"""
from time import sleep

# An empty list for storing the tasks is initialized.
tasks = []

# Method toDoList() for interacting with the application.
def toDoList():
    print("\t\t\t**** TO-DO LIST APPLICATION **** \t\t\t\t")
    while True:
        print('\n')
        print("\t OPTIONS")
        # Options display for the user.
        print("\t1. Track your to-do list")
        print("\t2. Add new task")
        print("\t3. Delete a task")
        print("\t4. Update your to-do list")
        print("\t5. Mark task as completed")
        print("\t6. Exit Application")
        
        # Taking input from the user for choice
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print('\n')
            print("Tracking your to-do list application...")
            sleep(1)  # Allow time for the user to see the message
            track()
        elif choice == 2:
            # Prompt user to enter the name of the task to be added
            task = input("Enter the name of the task to be added: ")
            add(task)
        elif choice == 3:
            if len(tasks) == 0:
                print("To-do list is empty. Hence there are no tasks to be deleted.")
                sleep(1)  # Allow time for the user to see the message
            else:
                track()
                # Prompt user to enter the index of task to be deleted
                deletion_index = int(input("Please enter the index of task to be deleted: "))
                delete(deletion_index)
        elif choice == 4:
            if len(tasks) == 0:
                print("The to-do list is empty. Hence there are no tasks to update.")
                sleep(1)  # Allow time for the user to see the message
            else:
                track()
                # Prompt user to enter the index of task to be updated
                updation_index = int(input("Please enter the index of task to be updated: "))
                update(updation_index)
        elif choice == 5:
            if len(tasks) == 0:
                print("The to-do list is empty. Hence there are no tasks to mark as completed.")
                sleep(1)  # Allow time for the user to see the message
            else:
                track()
                # Prompt user to enter the index of task to be marked as completed
                completion_index = int(input("Please enter the index of task to be marked as completed: "))
                mark_completed(completion_index)
        elif choice == 6:
            print("Saving your tasks......")
            sleep(1)  # Simulate saving process
            print("Exiting the application......")
            sleep(1)  # Simulate exiting process
            print("Application closed")
            sleep(1)
            break
        else:
            print("Please enter a valid choice.")
            sleep(1)  # Allow time for the user to see the message

# Function to display the tasks in the to-do list
def track():
    if len(tasks) == 0:
        print("The to-do list is empty...")
        sleep(1)  # Allow time for the user to see the message
    else:
        print("The tasks in your to-do list...")
        print('\n')
        for i in range(len(tasks)):
            task_status = "✓" if tasks[i]["status"] else "✗"
            print(f"{i + 1}. {tasks[i]['name']} [{task_status}]")
        print('\n')
        sleep(2)  # Allow time for the user to see the list

# Function to add a new task to the to-do list
def add(new_task):
    tasks.append({"name": new_task, "status": False})
    print("New task is successfully added...")
    sleep(1)  # Allow time for the user to see the message

# Function to delete a task from the to-do list based on its index
def delete(index):
    tasks.pop(index - 1)
    print("Task is successfully deleted...")
    sleep(1)  # Allow time for the user to see the message

# Function to update a task in the to-do list based on its index
def update(index):
    print("Enter the updated task: ")
    updated_task = input()
    tasks[index - 1]["name"] = updated_task
    print("Task is successfully updated...")
    sleep(1)  # Allow time for the user to see the message

# Function to mark a task as completed based on its index
def mark_completed(index):
    tasks[index - 1]["status"] = True
    print("Task is successfully marked as completed...")
    sleep(1)  # Allow time for the user to see the message

# Start the To-Do List application
if __name__ == "__main__":
    toDoList()
