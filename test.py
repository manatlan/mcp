import dotenv
dotenv.load_dotenv()

from pydantic_ai import Agent
import datetime

agent = Agent(  
    'google-gla:gemini-1.5-flash',
    # system_prompt='get_heure_actuelle() renvoie l\'heure actuelle. Réponds en français.',  
)

@agent.tool_plain
def get_current_time() -> str:
    return datetime.datetime.now().isoformat()

result = agent.run_sync('current time ?')  
print(result.output)