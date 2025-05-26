import os
import time
from datetime import datetime
from dotenv import load_dotenv

from technical_content_writer.crews.content_crew.content_crew import ContentCrew

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



class ContentState(BaseModel):
    topic: str = ''
    content: str = ""
    audience_level: str = ""
    current_year: int = datetime.now().year



class ContentGeneraterFlow(Flow[ContentState]):

    # @start()
    # def get_topic_from_user(self):
    #     print("Welcome to Content Writer")
    #     self.state.topic = input("What topic do you want to write about? ")
    #     while True:
    #         audience = input("Who is your target audience? (beginner/intermediate/advanced) ").lower()
    #         if audience in ["beginner", "intermediate", "advanced"]:
    #             self.state.audience_level = audience
    #             break
    #         print("Please enter 'beginner', 'intermediate', or 'advanced'")

    #     print(f"\nUser inputs:\n Topic: {self.state.topic}\nAudience level: {self.state.audience_level} audience...\n")

    #     return self.state

    @start()
    def generate_content(self, state: ContentState):
        print("Generating content")
        crew = ContentCrew().crew()
        result = crew.kickoff(inputs={"topic": state.topic, "audience_level": state.audience_level, "current_year": state.current_year})
        print("Content generated", result.raw)
        self.state.content = result.raw
        print('Usage metrics:')
        print(crew.usage_metrics)
        return self.state
                

    def process_content(self, content):
        """Process content to clean up markdown formatting"""
        if content is None:
            return ""
            
        # Check for markdown code blocks and remove them
        if "```markdown" in content:
            parts = content.split("```markdown", 1)
            if len(parts) > 1:
                content = parts[1]
        
        # Remove trailing markdown code block markers
        if content.endswith("```"):
            content = content[:-3]
            
        # Clean up any extra whitespace
        content = content.strip()
        return content

    @listen(generate_content)
    def serve_content(self, state):
        content = self.process_content(state.content)
        print('____________________________________________________________')
        print(content)
        print('____________________________________________________________')
        return content
    
    @listen(generate_content)
    def stream_content(self, state, delay=0.5):
        """Stream content in chunks with a delay between paragraphs"""
        content = self.process_content(state.content)

        #Write the content to a file for debugging purposes
        with open(f"content_folder_{state.topic}", "w") as f:
            f.write(content)
        paragraphs = content.split('\n\n')
        
        result = ""
        for paragraph in paragraphs:
            if paragraph.strip():  # Skip empty paragraphs
                result += paragraph + "\n\n"
                time.sleep(delay)  # Delay between chunks
                yield result  # Each yield must be a string, not a generator object
        

generator_flow = ContentGeneraterFlow()
def kickoff():
    generator_flow.kickoff()


def plot():
    generator_flow.plot()


if __name__ == "__main__":
    kickoff()
