from .models import Agent
from ..error import print_Error_Msg

# FUNCTION FOR CREATING NEW AGENT
def agents_input(Agent_List, ID_list):
    n = None
    while True:
        try:
            n = int(input('Enter the number(Integer) of agents to create: '))
            break
        except:
            print_Error_Msg()
    print()

    print('\nEnter the details of the agents as stated\n')

    for _ in range(n):
        id = None
        while True:
            try:
                id = int(input("Enter the ID(Integer) of the agent you want to create(NOTE: ID can't be changed): "))
                break
            except:
                print_Error_Msg()

        while id in ID_list:
            while True:
                try:
                    id = int(input('This ID is already present.Please enter another ID: '))
                    break
                except:
                    print_Error_Msg()

        ID_list.append(id)

        s_input = None
        while True:
            s_input = input('Enter 1 if agent is available else 0: ')
            if s_input == '1' or s_input == '0':
                break
            else:
                print_Error_Msg()

        status, available_since = False, None
        if s_input == '1':
            status = True
            while True:
                try:
                    available_since = float(input('Enter the last availability time(in Decimal) of the agent: '))
                    break
                except:
                    print_Error_Msg()
        

        roles = list(input('Enter roles of the agent(separated by comma): ').split(','))

        Agent_List.append(Agent(roles=roles,id=id,status=status,available_since=available_since))
        
        print()
