import g4f.debug,datetime
from g4f.integration.pydantic_ai import patch_infer_model
g4f.debug.logging = True

patch_infer_model()
from pydantic_ai import Agent

# Define the agent
agent = Agent(
    'g4f:gpt-4o-mini', # g4f:provider:model_name or g4f:model_name
    # "g4f:deepseek-v3",
    # "g4f:gemini-1.5-flash",
    # system_prompt='Be concise, reply with one sentence.',
)

@agent.tool_plain
def get_current_time() -> str:
    return datetime.datetime.now().isoformat()

result = agent.run_sync('current time ?')  
print(result.output)