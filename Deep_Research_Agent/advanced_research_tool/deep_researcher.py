from agents import Runner, trace, gen_trace_id
from research_agent import research_agent
from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from senior_research_agent import senior_research_agent, ReportData
from email_agent import email_agent
import asyncio

class DeepResearcher:

    async def run(self, user_query: str):
        """ Execute the deep research workflow and stream updates """
      
        print("Initiating research workflow...")
        
        search_strategy = await self.plan_searches(user_query)
        yield "Search plan ready, initiating execution..."
        
        collected_data = await self.perform_searches(search_strategy)
        yield "Search execution done, preparing report..."
        
        final_report = await self.report(user_query, collected_data)
        yield "Report generation completed, dispatching email..."
        
        await self.send_email(final_report)
        yield "Email successfully sent, workflow complete"
        
        yield final_report.markdown_report
        

    async def plan_searches(self, user_query: str) -> WebSearchPlan:
        """ Create a plan of searches for the given query """
        print("Generating search strategy...")
        
        response = await Runner.run(
            planner_agent,
            f"Query: {user_query}",
        )
        
        print(f"Total searches planned: {len(response.final_output.searches)}")
        return response.final_output_as(WebSearchPlan)
    
    async def perform_searches(self, search_strategy: WebSearchPlan) -> list[str]:
        """ Execute all planned searches """
        print("Executing search operations...")
        
        completed_count = 0
        async_jobs = [asyncio.create_task(self.search(task)) for task in search_strategy.searches]
        
        aggregated_results = []
        
        for job in asyncio.as_completed(async_jobs):
            output = await job
            if output is not None:
                aggregated_results.append(output)
            
            completed_count += 1
            print(f"Progress: {completed_count}/{len(async_jobs)} searches done")
        
        print("All search operations finished")
        return aggregated_results

    async def search(self, task_item: WebSearchItem) -> str | None:
        """ Execute a single search task """
        payload = f"Search term: {task_item.query}\nReason: {task_item.reason}"
        
        try:
            response = await Runner.run(
                research_agent,
                payload,
            )
            return str(response.final_output)
        except Exception:
            return None

    async def write_report(self, user_query: str, aggregated_results: list[str]) -> ReportData:
        """ Generate a report based on search results """
        print("Compiling report...")
        
        payload = f"Original query: {user_query}\nSummarized search results: {aggregated_results}"
        
        response = await Runner.run(
            senior_research_agent,
            payload,
        )

        print("Report compilation complete")
        return response.final_output_as(ReportData)
    
    async def send_email(self, report_data: ReportData) -> None:
        print("Preparing email content...")
        
        response = await Runner.run(
            email_agent,
            report_data.markdown_report,
        )
        
        print("Email dispatch completed")
        return report_data