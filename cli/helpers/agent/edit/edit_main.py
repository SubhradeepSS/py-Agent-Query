from ...error import print_Error_Msg
from .edit_specific import edit_specific_agent
from ...agent.models import Agent

from typing import List

# FUNCTION INVOKED IF USER WANTS TO EDIT AGENT(S) INFO
def edit_agent_func(Agent_List: List[Agent]) -> None:
    n_edits:int = 0
    
    while True:
        try:
            n_edits = int(input('\nEnter the number(Integer) of agents you want to edit: '))
            print()
            break
        except:
            print_Error_Msg()
    
    id:int = 0
    for _ in range(n_edits):
        while True:
            try:
                id = int(input('Enter the ID(Integer) of the agent you want to edit: '))
                if edit_specific_agent(id, Agent_List):
                    break
                else:
                    print("AGENT WITH ENTERED ID DOESN'T EXIST!!!")
            except:
                print_Error_Msg()
        print()
