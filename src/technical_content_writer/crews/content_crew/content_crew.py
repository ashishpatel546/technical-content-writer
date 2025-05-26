from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os

from technical_content_writer.tools.search_tool import get_search_tool

@CrewBase
class ContentCrew():
    """ContentCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @property
    def LLM_MODEL(self):
        return f'openai/{os.getenv("MODEL", "gpt-4")}'
    
    @property
    def OpenAIGPT4OMini(self):
        return LLM(self.LLM_MODEL, temperature=0.7, stream=True)

    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_writer'], # type: ignore[index]
            verbose=True,
            tools=[get_search_tool()],
            llm = self.OpenAIGPT4OMini
        )

    @agent
    def content_editor(self) -> Agent:
        return Agent(
            config=self.agents_config['content_editor'], # type: ignore[index]
            verbose=True,
            tools=[get_search_tool()],
            llm = self.OpenAIGPT4OMini
        )

    @agent
    def markdown_formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['markdown_formatter'], # type: ignore[index]
            verbose=True,
            llm = self.OpenAIGPT4OMini
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def write_section_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_section_task'], # type: ignore[index]
        )

    @task
    def review_section_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_section_task'], # type: ignore[index]
            # output_file='report.md'
        )

    @task
    def markdown_formatting_task(self) -> Task:
        return Task(
            config=self.tasks_config['markdown_formatting_task'], # type: ignore[index]
            # output_file='report.md'
        )


    @crew
    def crew(self) -> Crew:
        """Creates the ContentCrew crew"""

        return Crew(
            name="Content Crew",
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            )
