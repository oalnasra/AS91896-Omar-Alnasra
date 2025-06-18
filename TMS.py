import easygui

tasks = {
    "T1": {
        "Title": "Design Homepage",
        "Description": "Create a mockup of the homepage",
        "Assignee": "JSM",
        "Priority": 3,
        "Status": "In Progress"
    },
    "T2": {
        "Title": "Implement Login page",
        "Description": "Create the Login page for the website",
        "Assignee": "JSM",
        "Priority": 3,
        "Status": "Blocked"
    },
    "T3": {
        "Title": "Fix navigation menu",
        "Description": "Fix the navigation menu to be more user-friendly",
        "Assignee": "None",
        "Priority": 1,
        "Status": "Not Started"
    },
    "T4": {
        "Title": "Add payment processing",
        "Description": "Implement payment processing for the website",
        "Assignee": "JLO",
        "Priority": 2,
        "Status": "In Progress"
    },
    "T5": {
        "Title": "Create an About Us page",
        "Description": "Create a page with information about the company",
        "Assignee": "BDI",
        "Priority": 1,
        "Status": "Blocked"
    }
}

team_members = {
    "JSM": {
        "Name": "John Smith",
        "Email": "John@techvision.com",
        "Tasks_Assigned": ["T1", "T2"]
    },
    "JLO": {
        "Name": "Jane Love",
        "Email": "Jane@techvision.com",
        "Tasks_Assigned": ["T4"]
    },
    "BDI": {
        "Name": "Bob Dillon",
        "Email": "Bob@techvision.com",
        "Tasks_Assigned": ["T5"]
    }
}
def menu_choice():
    choices = {
        "Add Task": add_tasks,
        "Update Task": update_task,
        "Search Task": search_tasks,
        "Search Member": search_members,
        "Output Tasks": print_tasks,
        "Generate Report": generate_report,
        "Logout": logout
    }

    options = list(choices.keys())
    get_input = ""

    while get_input != "Logout":
        user_choice = easygui.buttonbox(
            "Welcome to the 'Task Management System' (TMS), pick an option",
choices=options)
        if user_choice is None:
            get_input = "Logout"
        elif user_choice == "Logout":
            choices["Logout"]()
            get_input = "Logout"
        else:
            get_input = user_choice
            choices[user_choice]()


def add_tasks():
        while True:
            task_title = easygui.enterbox("Enter Task Title: ")
            if task_title == None:
                return
            elif task_title == "":
                easygui.msgbox("Field must be filled out.") 
            elif task_title.isdigit():
                easygui.msgbox("Enter a string, not just numbers.")
            else:
                break
        while True:
            task_description = easygui.enterbox("Enter Task Description: ")
            if task_description == None:
                return
            elif task_description.isdigit():
                easygui.msgbox("Enter a string, not just numbers.")
                
            elif task_description == "":
                easygui.msgbox("Field must be filled out.")
            else:
                break
        while True:
            task_assignee = easygui.enterbox("Enter Task Assignee: ")
            if task_assignee == None:
                return
            elif task_assignee == "":
                easygui.msgbox("Field must be filled out.")
            elif task_assignee.isdigit():
                easygui.msgbox("Enter a string, not just numbers.")
            else:
                break
        while True:
            task_priority = easygui.enterbox("Enter Task Priority (1 = Low, 2 = Medium, 3 = High): ")
            if task_priority == None:
                return
            elif task_priority == "":
                easygui.msgbox("Field must be filled out.") 
            elif not task_priority.isdigit():
                easygui.msgbox("Enter a number, not string")
            elif task_priority not in ["1", "2", "3"]:
                easygui.msgbox("Enter a number between 1 and 3.")
            else:
                task_priority = int(task_priority)
                break
        while True:
            status = ["In Progress", "Blocked", "Completed"]
            task_status = easygui.choicebox("Choose Task Status:", choices=status)
            if task_status is None:
                return  
            else:
                break  


        task_id = f"T{len(tasks)+1}"
        tasks[task_id] = {
            "Title": task_title,
            "Description": task_description,
            "Assignee": task_assignee,
            "Priority": task_priority,
            "Status": task_status
        }

        easygui.msgbox(f"Task '{task_title}' has been added with ID {task_id}.")
        return

def update_task():
    pass
def search_tasks():
    pass
def search_members():
    pass
def print_tasks():
    output = []
    for task_id, task_info in tasks.items():
        output.append(f"--- {task_info['Title']} ({task_id}) ---")
        for key, value in task_info.items():
            output.append(f"{key}: {value}")
        output.append("")
    easygui.msgbox("\n".join(output), title="Task Details")
def generate_report():
    pass
def logout():
    pass



menu_choice() 
          
    

