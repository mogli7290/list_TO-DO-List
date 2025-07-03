tasks=[]

while True:
  print("----To_Do_List----")
  print("add task")
  print("view task")
  print("delete task")
  print("exit")

  choice=input("\n    give yr option")

  if choice == "1":
    task=input("add task you wnat")
    tasks.append(task)
    print(f"'{task}' added")

  elif choice == "2":
    if len(tasks)== 0:
      print("no task there")
    else:
      for i in range(len(tasks)):
        print(f"{i+1}.{tasks[i]}")

  elif choice == "3":
    if len(tasks)== 0:
      print("no tasks")

    else:
       for i in range(len(tasks)):
         print(f"'{i+1}'.'{tasks[i]}'")
       tasknum = input("task to delete")
       if tasknum.isdigit():
        tasknum=int(tasknum)
        if 1 <= tasknum <= len(tasks):
          removed = tasks.pop(tasknum - 1)
          print(f"{removed} deleted")
        else:
          print("enter proper no")
       else:
        print("enter number")     
  elif choice == "5":
    break