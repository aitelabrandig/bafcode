from flask import session
from core import MasterAgent
from .utils import TaskList

class Manager:
    
    @staticmethod
    def process(task, data):
        """
        Process client input and manage tasks.

        Args:
        - client_input (dict): Input from the client containing the message.

        Returns:
        - list: List of tasks from the session.
        """
        
        # Check if the task list is empty or not initialized
        if not session.get('task_list'):
            task_list = TaskList.generateTaskList(task, data)
            session['task_list'] = task_list
        
        master_agent = MasterAgent()

        # Continue processing tasks while there are pending tasks
        while TaskList.checkPendingTasks():
            next_task = TaskList.getTheNextTask()
            if not next_task:
                break

            str_next_task = str(next_task)
            task_result = master_agent.process(str_next_task, data)
            TaskList.saveTaskResults(task_result, next_task)
            TaskList.changeTaskStatus(next_task)

        return session.get('task_list')
