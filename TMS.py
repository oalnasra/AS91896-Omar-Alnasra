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
        "Description": "Fix the navigation menu to be more \
user-friendly",
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
        "Description": "Create a page with information about \
the company",
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
            "Welcome to the 'Task Management System' (TMS), \
pick an option",
choices=options)
        if user_choice == None:
            get_input = "Logout"
        elif user_choice == "Logout":
            choices["Logout"]()
            get_input = "Logout"
        else:
            get_input = user_choice
            choices[user_choice]()

def get_task_title():
    while True:
        task_title = easygui.enterbox("Enter Task Title:")
        if task_title is None:
            return None
        if task_title == "":
            easygui.msgbox("Field must be filled out.")
        elif task_title.isdigit():
            easygui.msgbox("Enter a string, not just numbers.")
        else:
            return task_title

def get_task_description():
    while True:
        task_description = easygui.enterbox("Enter Task Description:")
        if task_description == None:
            return 
        if task_description == "":
            easygui.msgbox("Field must be filled out.")
        elif task_description.isdigit():
            easygui.msgbox("Enter a string, not just numbers.")
        else:
            return task_description

def get_task_assignee():
    name_to_id = {
        member["Name"]: member_id for member_id, member in team_members.items()
    }
    selected_name = easygui.choicebox("Select Task Assignee:", choices=list(name_to_id.keys()))
    if selected_name == None:
        return 
    return name_to_id[selected_name]


def get_task_priority():
    while True:
        task_priority = easygui.enterbox("Enter Task Priority (1 = Low, 2 = Medium, 3 = High):")
        if task_priority == None:
            return 
        if task_priority == "":
            easygui.msgbox("Field must be filled.")
        elif not task_priority.isdigit():
            easygui.msgbox("Enter a number, not a string.")
        elif task_priority not in ["1", "2", "3"]:
            easygui.msgbox("Enter a number between 1 and 3.")
        else:
            return int(task_priority)

def get_task_status():
    return easygui.choicebox(
        "Choose Task Status:",
        choices=["In Progress", "Blocked", "Completed", "Not Started"]
    )
def new_tasks():
    task_title = get_task_title()
    if task_title == None: 
        return

    task_description = get_task_description()
    if task_description == None: 
        return

    task_assignee = get_task_assignee()
    if task_assignee == None: 
        return

    task_priority = get_task_priority()
    if task_priority == None: 
        return

    task_status = get_task_status()
    if task_status == None: 
        return

    return {
        "Title": task_title,
        "Description": task_description,
        "Assignee": task_assignee,
        "Priority": task_priority,
        "Status": task_status
    }


def add_tasks():
    validate_input = new_tasks()
    
    if validate_input == None:
        return

    task_id = f"T{len(tasks) + 1}"
    tasks[task_id] = validate_input

    if validate_input["Assignee"] in team_members:
        team_members[validate_input["Assignee"]]\
        ["Tasks_Assigned"].append(task_id)
    easygui.msgbox(f"Task '{validate_input['Title']}' \
has been added with ID {task_id}.")


def update_task_title(task_id):
    while True:
        updated_title = easygui.enterbox("Enter New Task Title:")
        if updated_title == None:
            return
        if updated_title == "":
            easygui.msgbox("Field must be filled out.")
        elif updated_title.isdigit():
            easygui.msgbox("Enter a string, not just numbers.")
        else:
            tasks[task_id]["Title"] = updated_title
            easygui.msgbox("Task Title has been updated.")
            break

 

def update_task_description(task_id):
    while True:
        updated_description = easygui.enterbox("Enter New Task Description:")
        if updated_description == None:
            return
        if updated_description == "":
            easygui.msgbox("Field must be filled out.")
        elif updated_description.isdigit():
            easygui.msgbox("Enter a string, not just numbers.")
        else:
            tasks[task_id]["Description"] = updated_description
            easygui.msgbox("Task Description has been updated.")
            break


            

def update_task_priority(task_id):
    while True:
        updated_priority = easygui.enterbox("Enter New Task Priority (1 = Low, 2 = Medium, 3 = High):")
        if updated_priority == None:
            return
        if updated_priority == "":
            easygui.msgbox("Field must be filled.")
        elif not updated_priority.isdigit():
            easygui.msgbox("Enter a number, not a string.")
        elif updated_priority not in ["1", "2", "3"]:
            easygui.msgbox("Enter a number between 1 and 3.")
        else:
            tasks[task_id]["Priority"] = int(updated_priority)
            easygui.msgbox("Task Priority has been updated.")
            break


def update_task_status(task_id):
    edited_task = tasks[task_id]
    current_assignee_id = edited_task["Assignee"]

    status_choices = ["In Progress", "Blocked", "Completed", "Not Started"]
    updated_status = easygui.choicebox("Choose new status:", choices=status_choices)
    if updated_status == None:
        return

    edited_task["Status"] = updated_status

    if updated_status == "Completed":
        if current_assignee_id in team_members and task_id in team_members[current_assignee_id]["Tasks_Assigned"]:
            team_members[current_assignee_id]["Tasks_Assigned"].remove(task_id)
    else:
        if current_assignee_id in team_members and task_id not in team_members[current_assignee_id]["Tasks_Assigned"]:
            team_members[current_assignee_id]["Tasks_Assigned"].append(task_id)

    easygui.msgbox("Task Status has been updated.")


def update_task_assignee(task_id):
    
    edited_task = tasks[task_id]
    previous_assignee_id = edited_task["Assignee"]
    current_status = edited_task["Status"]

    assignee_choice = list(team_members.keys())
    new_assignee_id = easygui.choicebox("Choose new assignee:", choices=assignee_choice)
    if new_assignee_id == None or new_assignee_id == previous_assignee_id:
        return 

    edited_task["Assignee"] = new_assignee_id

    if previous_assignee_id in team_members and task_id in team_members[previous_assignee_id]["Tasks_Assigned"]:
        team_members[previous_assignee_id]["Tasks_Assigned"].remove(task_id)

    
    if current_status != "Completed":
        if new_assignee_id in team_members and task_id not in team_members[new_assignee_id]["Tasks_Assigned"]:
            team_members[new_assignee_id]["Tasks_Assigned"].append(task_id)

    easygui.msgbox("Task assignee has been updated.")

def update_finish():
    return

def update_task():

    title_to_id = {task_title_info["Title"]: task_id for task_id, task_title_info in tasks.items()}

    title_choice = easygui.choicebox("Choose the task to edit:", \
        choices=list(title_to_id.keys()))
    if title_choice == None: 
        return
    task_id = title_to_id[title_choice]


    update_options = {
        "Update Title": update_task_title,
        "Update Description": update_task_description,
        "Update Priority": update_task_priority,
        "Update Status": update_task_status,
        "Update Assignee": update_task_assignee,
        "Finish Updating": update_finish
    }

    while True:
        current_title = tasks[task_id]["Title"]
        choice = easygui.buttonbox(
            f"What do you want to update for '{current_title}'?",
            title="Update Menu",
            choices=list(update_options.keys())
        )

        if choice == None or choice == "Finish Updating":
            break  

    
        update_options[choice](task_id)

def get_task_titles():
    task_titles = [task["Title"] for task in tasks.values()]
    return task_titles

def task_details(selected_title):
    for task_id, task_info in tasks.items():
        if task_info["Title"] == selected_title:
                task_details = f"Task ID: {task_id}\n" + \
                "\n".join(f"{key}: {value}" for key, value in \
                task_info.items())
                easygui.msgbox(task_details, title="Task Details")


def search_tasks(selected_choice):
    if selected_choice != "Task":
        return  
    task_titles = get_task_titles()

    selected_title = easygui.choicebox("Select a Task:", choices=task_titles)
    if selected_title == None:
        return
    task_details(selected_title)   


def search_member_output(member_info, member_id, info_summary):
    member_details = (
        f"Name: {member_info['Name']}\n"
        f"ID: {member_id}\n"
        f"Email: {member_info['Email']}\n\n"
        f"Assigned Tasks:\n{info_summary}"
    )
    easygui.msgbox(member_details, title="Team Member Details")



def get_members_tasks(member_info):
    assigned_tasks = member_info["Tasks_Assigned"]
    task_assignments = [
        f"- {tasks[task_id]['Title']} ({task_id})"
        for task_id in assigned_tasks if task_id in tasks
    ]
    return "\n".join(task_assignments)
       

def search_members(selected_choice):
    if selected_choice != "Team Member":
        return
    member_names = [member["Name"] for member in team_members.values()]
    selected_name = easygui.choicebox("Select a Team Member:", \
    choices=member_names)
        
    for member_id, member_info in team_members.items():
        if member_info["Name"] == selected_name:
            task_summary = get_members_tasks(member_info)
            search_member_output(member_info, member_id, task_summary)
            break



def search_members_or_tasks():
    selected_choice = easygui.buttonbox("Search:", \
        choices=["Task", "Team Member", "Cancel"])
    if selected_choice == None:
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
    
    counted_status = {"Not Started": 0, \
    "In Progress": 0, "Blocked": 0, "Completed": 0}
    for task in tasks.values():
        counted_status[task["Status"]] += 1

    easygui.msgbox(f"Generated Progress Report:\n\n \
Number of tasks completed: {counted_status['Completed']}\n \
Number of tasks in progress: {counted_status['In Progress']}\n \
Number of tasks blocked: {counted_status['Blocked']}\n \
Number of tasks not started: {counted_status['Not Started']}")

def logout():
        exit()

menu_choice() 
          
    

