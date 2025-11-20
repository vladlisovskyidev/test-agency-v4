from agents import ModelSettings
from openai.types.shared import Reasoning
from agency_swarm import Agent
from agents.extensions.models.litellm_model import LitellmModel

example_agent = Agent(
    name="HelpManager",
    description="A helpful and knowledgeable assistant that provides comprehensive support and guidance across various domains.",
    instructions="./instructions.md",
    tools_folder="./tools",
    files_folder="./files",
    model=LitellmModel(
        model="openai/gpt-5",  # Add openai/ prefix
    ),
    model_settings=ModelSettings(
        max_tokens=25000,
        reasoning=Reasoning(
            effort="medium",
            summary="auto",
        ),
    ),
)
