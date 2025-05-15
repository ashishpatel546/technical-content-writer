
from langchain_community.tools import BraveSearch
from langchain_community.utilities import BraveSearchWrapper
from crewai.tools import BaseTool
import json
from pydantic import Field
from crewai_tools import BraveSearchTool


def get_search_tool():
    """Tool to search the web using Brave Search"""
    return BraveSearchTool(n_results=10)

# Create a placeholder that will be replaced with the actual tool