from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class FullstackTeam():
    """FullstackTeam crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'],
            verbose=True,
        )

    @agent
    def system_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['system_architect'],
            verbose=True,
        )

    @agent
    def tech_lead(self) -> Agent:
        return Agent(
            config=self.agents_config['tech_lead'],
            verbose=True,
        )

    @agent
    def backend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_engineer'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe", 
            max_execution_time=500, 
            max_retry_limit=3 
        )
    
    @agent
    def frontend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_engineer'],
            verbose=True,
        )
    
    @agent
    def test_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['test_engineer'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe", 
            max_execution_time=500, 
            max_retry_limit=3 
        )

    @agent
    def devops_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['devops_engineer'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe", 
            max_execution_time=500, 
            max_retry_limit=3 
        )

    @task
    def define_requirements(self) -> Task:
        return Task(
            config=self.tasks_config['define_requirements'],
        )

    @task
    def design_architecture(self) -> Task:
        return Task(
            config=self.tasks_config['design_architecture'],
        )

    @task
    def develop_backend(self) -> Task:
        return Task(
            config=self.tasks_config['develop_backend'],
        )

    @task
    def develop_frontend(self) -> Task:
        return Task(
            config=self.tasks_config['develop_frontend'],
        ) 

    @task
    def test_application(self) -> Task:
        return Task(
            config=self.tasks_config['test_application'],
        ) 

    @task
    def deploy_application(self) -> Task:
        return Task(
            config=self.tasks_config['deploy_application'],
        )

    @task
    def final_approval(self) -> Task:
        return Task(
            config=self.tasks_config['final_approval'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Full Stack crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )







# -----------------------------
# Create Crew
# -----------------------------
def create_crew():
    return Crew(
        agents=list(agents.values()),
        tasks=list(tasks.values()),
        process=Process.sequential,  # critical for ordered execution
        verbose=True,
    )