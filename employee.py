class Employee:
    """
    A blueprint for an Employee with details such as
    ID, Name, Profession, Current Projects and Project Backlog
    """
    def __init__(self, id, name, profession, current_project, project_backlog=None):
        """
        Initialises the employee class with
        :param id: a unique identifier for the employee
        :param name: Name of the employee
        :param profession: The Role of employment
        :param current_project: Projects that require/available to swap into
        """
        self.__id = id
        self.__name = name
        self.__profession = profession
        self.__current_project = current_project
        self.__project_backlog = project_backlog if project_backlog is not None else []

    def work(self):
        """
        Prints a message indicating the employee is working on their current project.

        :return: None
        """
        print(f"Working on {self.__current_project}")

    def assign_project(self, project):
        """
        Adds a new project to the employee's backlog if it's not already present.

        :param project: Name of the project to assign (string)
        :return: None
        """
        if project not in self.__project_backlog:
            self.__project_backlog.append(project)
            print(f"{project} added to project backlog")
        else:
            print(f"{project} already in the project backlog")

    def swap_project(self, project):
        """
        Swaps the current project with a project from the backlog at the given index.

        The current project is added back to the backlog, and the selected backlog
        project becomes the new current project.

        :param project: Index (int) of the project in the backlog to swap in
        :return: None
        """
        if project >= 0 and project < len(self.__project_backlog):
            old_project = self.__current_project
            new_project = self.__project_backlog[project]

            self.__current_project = new_project
            self.__project_backlog.pop(project)
            self.__project_backlog.append(old_project)
            print(f"Switched to project '{new_project}'. Moved '{old_project}' to backlog.")

        else:
            print("Invalid Project index. No project swapped.")