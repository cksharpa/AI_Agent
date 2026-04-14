from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field
from typing import List

class TrendingCompany(BaseModel):
    name: str = Field(description="Company name")
    ticker: str = Field(description="Stock ticker symbol")
    reason: str = Field(description="Why the company is trending")


class TrendingCompanyList(BaseModel):
    companies: List[TrendingCompany] = Field(description="List of companies trending in the news")


class CompanyResearch(BaseModel):
    name: str = Field(description="Company name")
    market_position: str = Field(description="Current market position and competitive analysis")
    future_outlook: str = Field(description="Future outlook and growth prospects")
    investment_potential: str = Field(description="Investment potential for investment")


class CompanyResearchList(BaseModel):
    research_list: List[CompanyResearch]= Field(description="Detailed research on all trending companies")

@CrewBase
class StockSelector:
    """Stock Selector Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def news_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["news_analyst"],
            )

    @agent
    def research_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["research_analyst"],
            )

    @agent
    def stock_selector(self) -> Agent:
        return Agent(
            config=self.agents_config["stock_selector"])

    @task
    def news_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["news_analysis"],
            output_pydantic=TrendingCompanyList,
        )

    @task
    def research_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["research_analysis"],
            output_pydantic=CompanyResearchList,
        )

    @task
    def selection_decision(self) -> Task:
        return Task(
            config=self.tasks_config["selection_decision"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Stock Selector crew"""

        orchestrator = Agent(
            config=self.agents_config['orchestrator'],
            allow_delegation=True
        )

        return Crew(
            agentss=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_agent=orchestrator,
            verbose=True,
        )