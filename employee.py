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
        if current_project not in self.__project_backlog:
            self.__project_backlog.append(current_project)

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


class SoftwareDeveloper(Employee):
    """
    A Software Developer who works on projects using a programming language.
    Inherits from Employee and adds developer-specific behavior.
    """
    def __init__(self, id, name, profession, current_project, current_language):
        """
        Initializes a Software Developer.

        :param id: Unique identifier
        :param name: Name of the developer
        :param profession: Job title
        :param current_project: The currently active project
        :param current_language: The language currently being used
        """
        super().__init__(id, name, profession, current_project)
        self.__language = current_language
        self.__programming_languages = [current_language]

    def work(self):
        """
        Overrides the Employee work method to include the language being used.
        Prints what the developer is currently working on and in what language.

        :return: None
        """
        print(f"Working on {self._Employee__current_project} in {self.__language}.")

    def learn_language(self, language):
        """
        Adds a new language to the developer's known languages list if not already known.

        :param language: The new programming language to learn (string)
        :return: None
        """
        if language not in self.__programming_languages:
            self.__programming_languages.append(language)
        else:
            print(f"{language} is already known.")
