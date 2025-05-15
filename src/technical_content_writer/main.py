from json import load
import os
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY environment variable not set.")
BRAVE_API_KEY = os.getenv("BRAVE_API_KEY")
if BRAVE_API_KEY is None:
    raise ValueError("BRAVE_API_KEY environment variable not set.")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ['BRAVE_API_KEY'] = BRAVE_API_KEY

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from technical_content_writer.crews.content_crew.content_crew import ContentCrew


class ContentState(BaseModel):
    topic: str = ''
    content: str = ""
    audience_level: str = ""
    current_year: int = datetime.now().year



class ContentGeneraterFlow(Flow[ContentState]):

    @start()
    def get_topic_from_user(self):
        print("Welcome to Content Writer")
        self.state.topic = input("What topic do you want to write about? ")
        while True:
            audience = input("Who is your target audience? (beginner/intermediate/advanced) ").lower()
            if audience in ["beginner", "intermediate", "advanced"]:
                self.state.audience_level = audience
                break
            print("Please enter 'beginner', 'intermediate', or 'advanced'")

        print(f"\nUser inputs:\n Topic: {self.state.topic}\nAudience level: {self.state.audience_level} audience...\n")

        return self.state

    @listen(get_topic_from_user)
    def generate_content(self, state: ContentState):
        print("Generating content")
        result = (
            ContentCrew()
            .crew()
            .kickoff(inputs={"topic": state.topic, "audience_level": state.audience_level, "current_year": state.current_year})
        )

        print("Content generated", result.raw)
        self.state.content = result.raw
        return self.state
                

    @listen(generate_content)
    def save_content(self, state):
        print("Saving content")
        os.makedirs("content_folder", exist_ok=True)
        timestamp = time.time()
        with open(f"content_folder/{timestamp}_{self.state.topic}_content.md", "w") as f:
            f.write(state.content)


generator_flow = ContentGeneraterFlow()
def kickoff():
    generator_flow.kickoff()


def plot():
    generator_flow.plot()


if __name__ == "__main__":
    kickoff()
