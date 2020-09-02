from random import randint
from operator import attrgetter

# FUNCTION TO RETURN THE AGENT(S) FOR THE SPECIFIC ISSUES
def query_func(roles, mode, Agent_List):
    agents = []
    for agent in Agent_List:
        if agent in agents or not agent.status:
            continue
        f = 0
        for role in roles:
            if role not in agent.roles:
                f = 1
                break
        
        if f == 0:
            agents.append(agent)

    if not agents:
        return None

    if mode == 1:                                           # RETURNING ALL MATCHING ROLE(S) AGENTS
        return agents
    
    elif mode == 3:
        return agents[randint(0,len(agents)-1)]             # RETURNING A RANDOM AGENT OUT OF MATCHING ROLE(S) AGENTS
    
    return min(agents, key=attrgetter('available_since'))   # RETURNING THE MATCHING ROLE(S) AGENT WITH LEAST BUSY TIME / MINIMUM "AVAILABLE SINCE TIME"
