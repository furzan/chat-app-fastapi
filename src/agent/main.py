from agents import Runner, set_tracing_disabled, SQLiteSession
from src.agent.my_agents.assistant_agent import agent

set_tracing_disabled(True)

async def clear_session_data(session: SQLiteSession):
    await session.clear_session()

async def get_session_data(session: SQLiteSession):
    user_data = await session.get_items()
    result = []
    for user in user_data:
        result.append({
            "role": user["role"],
            "content": user["content"]
        })
    return result



async def runagent(input: str, session: SQLiteSession):
    res =await Runner.run(
        starting_agent= agent,
        input= input,
        session=session)

    return res.final_output

