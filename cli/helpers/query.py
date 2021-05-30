from random import randint
from operator import attrgetter
from typing import List
from .agent.models import Agent

# FUNCTION TO RETURN THE AGENT(S) FOR THE SPECIFIC ISSUES
def query_func(roles:List[str], mode:int, Agent_List:List[Agent]) -> List[Agent]:
    agents:List[Agent] = []
    for agent in Agent_List:
        if agent in agents or not agent.status:
            continue
        
        f:int = 0
        for role in roles:
            if role not in agent.roles:
                f = 1
                break
        
        if f == 0:
            agents.append(agent)

    if not agents or mode == 1:                                 # RETURNING EMPTY / ALL MATCHING ROLE(S) AGENTS
        return agents
    
    if mode == 3:
        return [ agents[randint(0, len(agents) - 1)] ]             # RETURNING A RANDOM AGENT OUT OF MATCHING ROLE(S) AGENTS
    
    return [ min(agents, key=attrgetter('available_since')) ]  # RETURNING THE MATCHING ROLE(S) AGENT WITH LEAST BUSY TIME / MINIMUM "AVAILABLE SINCE TIME"
