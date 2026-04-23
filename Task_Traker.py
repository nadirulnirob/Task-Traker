class TaskManager:
    def __init__(self):
        self.tasks=[]
    
    def Add_Task (self):
        Title=input("EnterTask Title : ")
        Description=input("Enter Task Description : ")
        task={ "Title" : Title,"Description": Description}
        self.tasks.append(task)
        print("Your Task Added successfully\n")

    def View_task (self):
        if len(self.tasks)==0:
            print("There are no task availabe")
        else:
            print("Task is : ")
            for i in range(len(self.tasks)):
                print(f"{i+1}.{self.tasks[i]['Title']}-{self.tasks[i]['Description']}")
    def delete_Task(self):
        if len(self.tasks)==0:
            print("No Task Available\n")
        else:
            self.View_task()
            try:
                n=int(input("Enter Task No. for Delete: \n"))
                if n>0 and n<=len(self.tasks):
                    self.tasks.pop(n-1)
                    print("Task Deleted \n")
                else:
                    print("Wrong Task No.\n")
            except Exception as e:
                print("Error: ",e)

t=TaskManager()
c=1
while c==1:
    print("=====Task tracker=====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    a=input("Enter Choice : ")
    if a=="1":
        t.Add_Task()
    elif a=="2":
        t.View_task()
    elif a=="3":
        t.delete_Task()
    elif a=="4":
        print("Exiting...")
        c=0           
    else:
        print("Somethings wrong .Try Again\n")
    


