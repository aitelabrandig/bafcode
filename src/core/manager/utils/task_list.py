from llms import LLM
from prompts import ManagerPromptPrompt
from flask import session
import json


class TaskList:
    def __init__(self):
        self.task_list = []
        self.task_results = []
        session['task_list'] = self.task_list


    @staticmethod
    def generateTaskList(task, data):
       prompt = ManagerPromptPrompt.manager_prompt_prompt(task)
       generated_task_list = LLM.llm.process(task, prompt, data)
       
        # Convert the plain text JSON string to a Python list/dictionary
       task_list = json.loads(generated_task_list)
       session['task_list'] = task_list
       return  session['task_list']
       

    @staticmethod
    def changeTaskStatus(task):
        
        for task in session['task_list']:
            if task['id'] == task['id']:
                task['status'] = 'completed'
                break
            print('Task status changed to completed')

    @staticmethod
    def deleteTask(client_input):
        pass

    @staticmethod
    def changeTaskStatus(target_task):
        for task in session['task_list']:
            if task['id'] == target_task['id']:
                task['status'] = 'completed'
                print('Task status changed to completed')
                break
              
    @staticmethod
    def saveTaskResults(results, target_task):
        for task in session['task_list']:
            if task['id'] == target_task['id']:
                task['results'] = results
                print('Results saved')
                break


    @staticmethod
    def getTheNextTask():
        # Get the next task from the task list which is not completed
        current_task = None
        for task in session['task_list']:
            if task['status'] != 'completed':
                current_task = task
                break
        return current_task
    
    @staticmethod
    def checkPendingTasks():
        
        pending_tasks = False
        for task in session['task_list']:
            if task['status'] != 'completed':
                pending_tasks = True
                break
           
        return pending_tasks