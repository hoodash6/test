class Todolist:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task has been added {self.tasks}")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'task is removed {task}')
        else:
            print('task not found')

    def show_task(self):
        for task in self.tasks:
            print("- " + task)

    def menw(self):
        while True:
            print("Choose the option below ")
            print("1 - Add a new task")
            print("2 - Remove a task")
            print("3 - Show all tasks")
            print("4 - Exit")
            option = input()

            if option == '1':
                add_new_task = input("Enter the to do list.. ")
                self.add_task(add_new_task)
            elif option == '2':
                removetask = input("Enter the task to remove from list.. ")
                self.remove_task(removetask)
            elif option == '3':
                self.show_task()
            elif option == '4':
                break
            else:
                print("Invalid Option choose correct option again")


new_todotask = Todolist()
new_todotask.menw()
# new_todotask.add_task('cook dinner')
# new_todotask.add_task('play game')
new_todotask.show_task()
#new_todotask.remove_task('cook dinner')




