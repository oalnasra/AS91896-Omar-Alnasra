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
        "Search Members or Tasks": search_members_or_tasks,
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
        if user_choice == None:
            get_input = "Logout"
        elif user_choice == "Logout":
            choices["Logout"]()
            get_input = "Logout"
        else:
            get_input = user_choice
            choices[user_choice]()
def new_tasks():
    
    while True:
        task_title = easygui.enterbox("Enter Task Title:")
        if task_title == None:
            return  
        if task_title == "":
            easygui.msgbox("Field must be filled out.")
        elif task_title.isdigit():
            easygui.msgbox("Enter a string, not just numbers.")
        else:
            break

    
    while True:
        task_description = easygui.enterbox("Enter Task Description:")
        if task_description is None:
            return 
        if task_description == "":
            easygui.msgbox("Field must be filled out.")
        elif task_description.isdigit():
            easygui.msgbox("Enter a string, not just numbers.")
        else:
            break

    
    name_to_id = {member["Name"]: member_id for member_id, member in team_members.items()}
    selected_name = easygui.choicebox("Select Task Assignee:", choices=list(name_to_id.keys()))
    if selected_name == None:
        return 
    team_assignee = name_to_id[selected_name]

    while True:
        task_priority = easygui.enterbox("Enter Task Priority (1 = Low, 2 = Medium, 3 = High):")
        if task_priority == None:
            return 
        elif not task_priority.isdigit():
            easygui.msgbox("Enter a number, not string")
        elif task_priority not in ["1", "2", "3"]:
            easygui.msgbox("Enter a number between 1 and 3.")
        else:
            task_priority = int(task_priority)
            break

    
    status = easygui.choicebox("Choose Task Status:", choices=["In Progress", "Blocked", "Completed", "Not Started"])
    if status == None:
        return 

    return {
        "Title": task_title,
        "Description": task_description,
        "Assignee": team_assignee,
        "Priority": task_priority,
        "Status": status
    }

def add_tasks():
    
    validate_input = new_tasks()
    
    if validate_input == None:
        return

    task_id = f"T{len(tasks) + 1}"
    tasks[task_id] = validate_input

    if validate_input["Assignee"] in team_members:
        team_members[validate_input["Assignee"]]["Tasks_Assigned"].append(task_id)
    easygui.msgbox(f"Task '{validate_input['Title']}' has been added with ID {task_id}.")

def update_task():

    title_to_id = {info["Title"]: task_id for task_id, info in tasks.items()}
    title_choice = easygui.choicebox("Choose the task to edit:", choices=list(title_to_id.keys()))
    if title_choice == None: 
        return

    status_update = easygui.choicebox("Select new status:", choices=["In Progress", "Completed", "Blocked", "Not Started"])
    if status_update == None: 
        return
    
    new_assignee = easygui.choicebox("Assign to team member:", choices=list(team_members.keys()))
    if new_assignee == None: 
        return

    task_id = title_to_id[title_choice]
    current_assignee = tasks[task_id]['Assignee']

    if current_assignee in team_members and task_id in team_members[current_assignee]["Tasks_Assigned"]:
        team_members[current_assignee]["Tasks_Assigned"].remove(task_id)

    if status_update != "Completed":
        if task_id not in team_members[new_assignee]["Tasks_Assigned"]:
            team_members[new_assignee]["Tasks_Assigned"].append(task_id)
    
    tasks[task_id]["Status"] = status_update
    tasks[task_id]["Assignee"] = new_assignee

    easygui.msgbox(f"Task '{title_choice}' has been updated.")

def search_tasks(selected_choice):
    if selected_choice == "Task":
        task_titles = [task["Title"] for task in tasks.values()]
        selected_title = easygui.choicebox("Select a Task:", choices=task_titles)
        for task_id, task_info in tasks.items():
            if task_info["Title"] == selected_title:
                task_details = f"Task ID: {task_id}\n" + "\n".join(f"{key}: {value}" for key, value in task_info.items())
                easygui.msgbox(task_details, title="Task Details")

def search_members(selected_choice):
    if selected_choice == "Team Member":
        member_names = [member["Name"] for member in team_members.values()]
        selected_member = easygui.choicebox("Select a Team Member:", choices=member_names)
        for member_id, member_info in team_members.items():
            if member_info["Name"] == selected_member:
                assigned_tasks = member_info["Tasks_Assigned"]
                task_assignments = [f"- {tasks[task_id]['Title']} ({task_id})" for task_id in assigned_tasks if task_id in tasks]
                info_summary = "\n".join(task_assignments)
                member_info = f"Name: {member_info['Name']} \nID: {member_id}\nEmail: {member_info['Email']}\n\nAssigned Tasks:\n{info_summary}"
                easygui.msgbox(member_info, title="Team Member Details")

def search_members_or_tasks():
    selected_choice = easygui.buttonbox("Search:", choices=["Task", "Team Member", "Cancel"])
    if selected_choice is None:
        return
    search_tasks(selected_choice)
    search_members(selected_choice)

def print_tasks():
    output = []
    for task_id, task_info in tasks.items():
        output.append(f"--- {task_info['Title']} ({task_id}) ---")
        for key, value in task_info.items():
            output.append(f"{key}: {value}")
        output.append("")
    easygui.msgbox("\n".join(output), title="Task Details")
def generate_report():
    counted_status = {"Not Started": 0, "In Progress": 0, "Blocked": 0, "Completed": 0}
    for task in tasks.values():
        counted_status[task["Status"]] += 1

    easygui.msgbox(f"Generated Progress Report:\n\n \
Number of tasks completed: {counted_status['Completed']}\n \
Number of tasks in progress: {counted_status['In Progress']}\n \
Number of tasks blocked: {counted_status['Blocked']}\n \
Number of tasks not started: {counted_status['Not Started']}")

def logout():
    pass



menu_choice() 
          
    

