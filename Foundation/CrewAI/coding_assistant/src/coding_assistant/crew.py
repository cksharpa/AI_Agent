from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Coding_Assistant:
    """Coding Assistant Crew"""

    agents_config = "config/agents.yaml"
    tasks_config =  "config/tasks.yaml"

    @agent
    def coding_assistant(self) -> Agent:
        return Agent(
            config=self.agents_config['coding_assistant'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=30, 
            max_retry_limit=3 
    )


    @task
    def coding_task(self) -> Task:
        return Task(
            config=self.tasks_config['coding_task'],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Coding Assistant crew"""


        return Crew(
            agents=self.agents, 
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
