import easygui

# Dictionary to store all details of the tasks. The key is the Task ID.
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

# Dictionary stores the details of the Team Members and the tasks they 
# are assigned
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
    """
    Displays the main menu and handles user navigation.
    This function provides a menu of choices to the user. Based on the
    user's selection, it calls the corresponding function. The loop
    continues until the user chooses to 'Logout' or closes the window.
    """
    # Dictionary maps the menu options to the corresponding functions.
    menu_options = {
        "Add Task": add_tasks,
        "Update Task": update_task,
        "Search Members or Tasks": search_members_or_tasks,
        "Output Tasks": print_tasks,
        "Generate Report": generate_report,
        "Logout": logout
    }
    # Gets the list of the menu options for a easygui button box
    menu_list = list(menu_options.keys())
    get_input = ""

    # Loop until user chooses "Logout"
    while get_input != "Logout":

    # Display main menu buttonboxes
        user_choice = easygui.buttonbox(
            "Welcome to the 'Task Management System' (TMS), \
pick an option",
choices=menu_list)
        # To allow for exiting through closing the window
        if user_choice == None:
            get_input = "Logout"
         # If 'Logout' is clicked, call the logout function.
        elif user_choice == "Logout":
            menu_options["Logout"]()
            get_input = "Logout"
        else:
            get_input = user_choice
            menu_options[user_choice]()

def get_task_title():
    """
    Prompts the user to enter a task title and validates the input, 
    until a string is entered.
    """
    while True:
        # Prompts for input for task title
        task_title = easygui.enterbox("Enter Task Title:")

        # Returns to the main menu_choice function if 'Cancel' or main 
        # window is closed.
        if task_title == None:
            return 

        # Validates the input to see whether the input is not empty.
        if task_title == "":
            easygui.msgbox("Field must be filled out.")

        # Validates the input to see whether the input is not an 
        # integer.
        elif task_title.isdigit():
            easygui.msgbox("Enter a string, not just numbers.")

        # If validation is passed, it will return the task title to the 
        # new_tasks function.
        else:
            return task_title

def get_task_description():
    """
    Prompts the user to enter a task description and validates the 
    input, until a string is entered.
    """
    while True:
        # Prompts for input for task description
        task_description = easygui.enterbox("Enter Task Description:")

        # Returns to the main menu_choice function if 'Cancel' or main 
        # window is closed.
        if task_description == None:
            return 
        
        # Validates the input to see whether the input is not empty.
        if task_description == "":
            easygui.msgbox("Field must be filled out.")

        # Validates the input to see whether the input is not an 
        # integer.
        elif task_description.isdigit():
            easygui.msgbox("Enter a string, not just numbers.")

        # If validation is passed, it will return the task title to the 
        # new_tasks function.
        else:
            return task_description

def get_task_assignee():
    """
    Prompts the user to select an assignee from a list of team members.
    """
    # Dictionary  for mapping member names to their ID for easy check.
    assignee_name_to_id = {
        member["Name"]: member_id for member_id, member \
        in team_members.items()
    }

    assignee_options = list(assignee_name_to_id.keys()) + ["None"]

    # Prompts for input from choicebox with team member names.
    selected_assignee = easygui.choicebox("Select Task Assignee:", \
    choices=assignee_options)

    # If 'Cancel' or the main window is closed, it will return to the 
    # main menu_choice function's GUI.
    if selected_assignee == None:
        return 

    if selected_assignee == "None":
        return "None"
        
    # If validation has passed, it will return the ID to the 
    # corresponding selected member name.
    return assignee_name_to_id[selected_assignee]

def get_task_priority():
    """
    Prompts the user to enter a task priority and validates it.
    The priority must be a number between 1 and 3.
    """
    while True:

        # Prompts for input for task priority
        task_priority = easygui.integerbox(
            msg="Enter Task Priority (1 = Low, 2 = Medium, 3 = High):",
            title="Task Priority",
            lowerbound=1,
            upperbound=3
        )
        

        # If 'Cancel' or the main window is closed it will return to the 
        # main menu_choice function's GUI
        if task_priority == None:
            return 
        
        return task_priority
        
def get_task_status():
    """
    Prompts the user to select a task status from a list of options:
    "In Progress", "Blocked", "Completed", "Not Started".
    """
    # Prompts for an input from the choicebox with the status options
    return easygui.choicebox(
        "Choose Task Status:",
        choices=["In Progress", "Blocked", "Completed", "Not Started"]
    )
def new_tasks():
    """
    Receives the necessary details for creating a new task.
    This function calls individual 'get' functions to collect the title,
    description, assignee, priority, and status for a new task. If 
    cancelled at any point this process will end
    """

    # Each 'get' function is called in order. If 'Cancel or main
    #  window is closed, this function will immediately return 
    # to the main menu_choice function GUI, stopping the function.

    # Get Task Title
    task_title = get_task_title()
    if task_title == None: 
        return

    # Get Task Description
    task_description = get_task_description()
    if task_description == None: 
        return

    # Get Task Assignee
    task_assignee = get_task_assignee()
    if task_assignee == None: 
        return

    # Get Task Priority
    task_priority = get_task_priority()
    if task_priority == None: 
        return

    # Get Task Status
    task_status = get_task_status()
    if task_status == None: 
        return

    # Returns a dictionary with all the task details.
    return {
        "Title": task_title,
        "Description": task_description,
        "Assignee": task_assignee,
        "Priority": task_priority,
        "Status": task_status
    }


def add_tasks():
    """
    Adds a new task to the 'tasks' dictionary. After receiving the 
    details from the new_task function, it then assigns a new task ID 
    and adds the details to the 'tasks' dictionary.
    """

    # Gets all the task details for the new task
    task_data = new_tasks()
    
    # If 'Cancel' or the main window is closed it will return to the 
    # main menu_choice function's GUI
    if task_data == None:
        return

    # Creates a new ID based on the task ID of the rest of the tasks
    task_id = f"T{len(tasks) + 1}"
    tasks[task_id] = task_data

    # Adds the new task ID to the selected assignees assigned tasks
    if task_data["Status"] != "Completed" and task_data["Assignee"] \
        in team_members:
        team_members[task_data["Assignee"]]\
        ["Tasks_Assigned"].append(task_id)
    easygui.msgbox(f"Task '{task_data['Title']}' \
has been added with ID {task_id}.")

def update_task_title(task_id):
    """
    Updates the input of task title in the selected task and 
    validates the new input on whether its an integer or empty
    """
    while True:
        # Prompts for new input for the task title
        updated_title = easygui.enterbox("Enter New Task Title:")

        # If 'Cancel' or the main window is closed, it will return to 
        # the main menu_choice function's GUI.
        if updated_title == None:
            return

        # Validates the  newinput to see whether the input is not empty.
        if updated_title == "":
            easygui.msgbox("Field must be filled out.")

        # Validates the new input to see whether the input is not an
        # integer
        elif updated_title.isdigit():
            easygui.msgbox("Enter a string, not just numbers.")

         # If validated, it will update the title and exit the loop
        else:
            tasks[task_id]["Title"] = updated_title
            easygui.msgbox("Task Title has been updated.")
            break 


def update_task_description(task_id):
    """
    Updates the input of task description in the selected task and 
    validates the new input on whether its an integer or empty
    """
    while True:
        # Prompts for new input for the task description
        updated_description = easygui.enterbox("Enter New Task \
Description:")

        # If 'Cancel' or the main window is closed, it will return to 
        # the main menu_choice function's GUI.
        if updated_description == None:
            return

        # Validates the input to see whether the input is not empty.
        if updated_description == "":
            easygui.msgbox("Field must be filled out.")

        # Validates the new input to see whether the input is not an
        # integer
        elif updated_description.isdigit():
            easygui.msgbox("Enter a string, not just numbers.")

        # If validated, it will update the description and exit the 
        # loop.
        else:
            tasks[task_id]["Description"] = updated_description
            easygui.msgbox("Task Description has been updated.")
            break 


def update_task_priority(task_id):
    """
    Updates the input of task priority in the selected task and 
    validates the new input on whether its an string or empty
    """
    while True:
        # Prompts for new input for the task priority
        updated_priority = easygui.integerbox(
            msg="Enter New Task Priority (1 = Low, 2 = Medium, \
3 = High):",
            title="Updated_Task_Priority",
            lowerbound=1,
            upperbound=3
        )

        # If 'Cancel' or the main window is closed, it will return to 
        # the update_task function's GUI.
        if updated_priority == None:
            return  

        # If validation passes, it will exit the loop and
        # return the priority as an integer.
        tasks[task_id]["Priority"] = updated_priority  
        easygui.msgbox("Task Priority has been updated.")
        break

def update_task_status(task_id):
    """
    Updates the input of task status in the selected task through the 
    choice box
    """

    edited_task = tasks[task_id]
    current_assignee_id = edited_task["Assignee"]

    # Lists the choice of options that 
    status_choices = ["In Progress", "Blocked", "Completed", \
    "Not Started"]

    # Prompts for an input from the choicebox with the status options
    updated_status = easygui.choicebox("Choose new status:",
                                       choices=status_choices,)

    # If 'Cancel' or the main window is closed, it will return to the 
    # main menu_choice function's GUI.
    if updated_status == None:
        return

    # Update the task's status in the tasks dictionary.
    edited_task["Status"] = updated_status 

    # If the new status is "Completed", it removes the task 
    # from the task assignee's list.
    if updated_status == "Completed":
        if current_assignee_id in team_members and task_id \
                in team_members[current_assignee_id]["Tasks_Assigned"]:
            team_members[current_assignee_id]\
            ["Tasks_Assigned"].remove(task_id)
    # If the status is not "Completed", ensure the task is
    #  in the task assignee's list by appending the value
    else:
        if current_assignee_id in team_members and task_id \
                not in team_members[current_assignee_id]\
                ["Tasks_Assigned"]:
            team_members[current_assignee_id]\
            ["Tasks_Assigned"].append(task_id)

    easygui.msgbox("Task Status has been updated.")


def update_task_assignee(task_id):
    """
    Updates the input of task assignee in the selected task through the 
    choice box
    """

    edited_task = tasks[task_id]
    previous_assignee_id = edited_task["Assignee"]
    current_status = edited_task["Status"]

    # Creates a dictionary to attach team member names to their 
    # corresponding IDs.
    assignee_name_to_id = {member["Name"]: member_id for member_id, \
    member in team_members.items()}
    assignee_name_options = list(assignee_name_to_id.keys())

    # Prompts selection of a new assignee.
    selected_assignee = easygui.choicebox("Choose new assignee:",
                                      "Update Assignee",
                                      choices=assignee_name_options)
    
    # If 'Cancel' or the main window is closed, it will return to 
    # the update_task function's GUI.
    if selected_assignee == None:
        return

    # Gets the ID of the newly selected team member/assignee.
    new_assignee_id = assignee_name_to_id[selected_assignee]

     # Checks if the team member/assignee had changed
    if new_assignee_id == previous_assignee_id:
        easygui.msgbox("No change was made, as the same assignee was \
selected.")
        return

     # Update the task's assignee ID.
    edited_task["Assignee"] = new_assignee_id

     # Removes the task from the previous assignee's task list.
    if previous_assignee_id in team_members and task_id in \
            team_members[previous_assignee_id]["Tasks_Assigned"]:
        team_members[previous_assignee_id]\
        ["Tasks_Assigned"].remove(task_id)

    # Add the task to the new team member/assignee's list, 
    # unless the task is "Completed".
    if current_status != "Completed":
        if new_assignee_id in team_members and task_id not in \
                team_members[new_assignee_id]\
                ["Tasks_Assigned"]:
            team_members[new_assignee_id]\
                ["Tasks_Assigned"].append(task_id)

    # Displays message to show that the Task Assignee Update has been 
    # Completed
    easygui.msgbox(f"Task assignee has been updated to \
{selected_assignee}.")


def finish_update():
    """
    A placeholder function that allow exiting the update_task function
    loop. This function only is used to break the update loop when
    "Finish Updating" is selected.
    """
    return


def update_task():
    """
    Manages and displays update options for a selected task.
    """
    # Attaches task titles to their IDs to allow selection by title.
    title_to_id = {task_info["Title"]: task_id for
                   task_id, task_info in tasks.items()}

    # Prompts the selection to choose which task to edit
    title_choice = easygui.choicebox("Choose the task to edit:",
                                     choices=list(title_to_id.keys()))
    
    # If 'Cancel' or the main window is closed, it will return to 
    # main menu_choice function GUI
    if title_choice == None:
        return
    task_id = title_to_id[title_choice]

    # Dictionary that attaches the update options to their functions.
    update_options = {
        "Update Title": update_task_title,
        "Update Description": update_task_description,
        "Update Priority": update_task_priority,
        "Update Status": update_task_status,
        "Update Assignee": update_task_assignee,
        "Finish Updating": finish_update
    }


    while True:
        current_title = tasks[task_id]["Title"]
        # Prompts the user for what they want to update for the selected
        # task.
        update_choice = easygui.buttonbox(
            f"What do you want to update for '{current_title}'?",
            title="Update Menu",
            choices=list(update_options.keys())
        )
        # If the main window is closed or "Finish Updating" is pressed, 
        # it will break the loop and return to the main menu_choice 
        # function.
        if update_choice == None or update_choice == "Finish Updating":
            break  


        update_options[update_choice](task_id) 

def return_task_title():
    """
    Gets the list of all task titles from the 'tasks' dictionary.
    """
    task_titles = [task["Title"] for task in tasks.values()]
    return task_titles

def get_task_details(selected_task_title):
    """
    Gets the selected task by its title and displays all its details 
    in a message box.
    """
    # Loops through tasks to find the selected task title.
    for task_id, task_info in tasks.items():
        if task_info["Title"] == selected_task_title:
            # Format the task details into a readble format
                task_details = f"Task ID: {task_id}\n" + \
                "\n".join(f"{key}: {value}" for key, value in \
                task_info.items())

                # Display the details in an easygui message box.
                easygui.msgbox(task_details, title="Task Details")


def search_tasks(search_choice):
    """
    Handles task search option, and displays the chosen task details of 
    the selected task title.
    """
    # Validates whether the user chose to search for "Task"
    if search_choice != "Task":
        return  

    # Get a list of all task titles.
    task_titles = return_task_title()

    # Prompt the user to select a task from the list.
    selected_task_title = easygui.choicebox("Select a Task:", \
    choices=task_titles)

    # If 'Cancel' or the main window is closed, it will return to 
    # main menu_choice function GUI
    if selected_task_title == None:
        return

    # Calls the function to display the details for the selected task.
    get_task_details(selected_task_title)   


def search_member_output(member_info, member_id, info_summary):
    """
     Displays team member details and assigneed tasks.
    """

     # Formats all member details into a singular string.
    member_details = (
        f"Name: {member_info['Name']}\n"
        f"ID: {member_id}\n"
        f"Email: {member_info['Email']}\n\n"
        f"Assigned Tasks:\n{info_summary}"
    )
    # Displays the selected tasks details in the message box.
    easygui.msgbox(member_details, title="Team Member Details")



def get_members_tasks(member_info):
    """
     Returns a string listing all tasks assigned to a member.
    """

    assigned_tasks = member_info["Tasks_Assigned"]

    # Creates a list and formats the strings for each members task
    task_assignments = [
        f"- {tasks[task_id]['Title']} ({task_id})"
        for task_id in assigned_tasks
        if task_id in tasks and tasks[task_id]["Status"] != "Completed"
    ]

    # Joins the list into a single string 
    return "\n".join(task_assignments)
       
    assigned_tasks = member_info["Tasks_Assigned"]

   
        
   

def search_members(search_choice):
    """
    Manages the team member search and displays their info.
    """
     # Validates whether the user chose to search for "Team Member"
    if search_choice != "Team Member":
        return

    # Gets a list of all team member names.
    member_names = [member["Name"] for member in team_members.values()]

    # Prompts for the selection to see Team Member/Assignee's details
    selected_assignee = easygui.choicebox("Select a Team Member:", \
    choices=member_names)
        
    # Find the selected member in the 'team_members' dictionary.
    for member_id, member_info in team_members.items():
        if member_info["Name"] == selected_assignee:

            # Gets the formatted list of their tasks.
            task_summary = get_members_tasks(member_info)

            # Displays the team members/assignee details and tasks.
            search_member_output(member_info, member_id, task_summary)
            break



def search_members_or_tasks():
    """ 
     Allows user to search for tasks or team members.
    """
     # Prompts the selection of a button to choose for specfic search 
     #  type e.g. "Task" or "Team Member"
    search_choice = easygui.buttonbox("Search:", \
        choices=["Task", "Team Member", "Cancel"])

    # If 'Cancel' or the main window is closed, it will return to 
    # main menu_choice function GUI
    if search_choice == None:
        return

    # Calls the functions based on the selected choice
    search_tasks(search_choice)
    search_members(search_choice)



def print_tasks():
    """
    Prints all tasks and their details.
    """
    output_details = []

    # Loops over each task in the tasks dictionary.
    for task_id, task_info in tasks.items():
        output_details.append(f"--- {task_info['Title']} ({task_id}) \
---")
         # Loop through the details (key and value) of the current task.
        for key, value in task_info.items():
            output_details.append(f"{key}: {value}")

        # Adds a blank line for better readability between tasks.
        output_details.append("")
    easygui.msgbox("\n".join(output_details), title="Task Details")

def generate_report():
    """
     Generates a summary report of the number of tasks in each status.
    """
    # Creates a dictionary to count statuses.
    status_counts = {"Not Started": 0, \
    "In Progress": 0, "Blocked": 0, "Completed": 0}

    # Loops through all tasks and counts +1 for each status.
    for task in tasks.values():
        status_counts[task["Status"]] += 1

     # Formatted string for Generated Report.
    easygui.msgbox(f"Generated Progress Report:\n\n \
Number of tasks completed: {status_counts['Completed']}\n \
Number of tasks in progress: {status_counts['In Progress']}\n \
Number of tasks blocked: {status_counts['Blocked']}\n \
Number of tasks not started: {status_counts['Not Started']}")

def logout():
        """
        Exits the program.
        """
        exit()

menu_choice() 
          
    

