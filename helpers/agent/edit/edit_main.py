from ...error import print_Error_Msg
from .edit_specific import edit_specific_agent

# FUNCTION INVOKED IF USER WANTS TO EDIT AGENT(S) INFO
def edit_agent_func(Agent_List):
    n_edits = None
    
    while True:
        try:
            n_edits = int(input('\nEnter the number(Integer) of agents you want to edit: '))
            print()
            break
        except:
            print_Error_Msg()
    
    id = None
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
