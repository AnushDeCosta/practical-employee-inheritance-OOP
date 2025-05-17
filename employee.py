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

        :return:
        """

    def assign_project(self, project):
        """

        :param project:
        :return:
        """
        if project not in self.__project_backlog:
            self.__project_backlog.append(project)
            print(f"{project} added to project backlog")
        else:
            print(f"{project} already in the project backlog")

    def swap_project(self, project):
        """

        :param project:
        :return:
        """
        pass

