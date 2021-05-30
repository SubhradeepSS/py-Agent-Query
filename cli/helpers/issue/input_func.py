from ..error import print_Error_Msg
from ..query import query_func

from typing import List

from ..agent.models import Agent

# FUNCTION FOR TAKING ISSUES AS INPUT
def issues_input(Agent_List: List[Agent]) -> None:
    no_issues:int = 0
    
    while True:
        try:
            no_issues = int(input('Enter the number(Integer) of issue queries: '))
            break
        except:
            print_Error_Msg()
    print()

    print('\nEnter the details of the issues as stated\n')

    for i in range(no_issues):
        print(f"Enter details of Issue {i+1}")
        
        roles = list(input('Enter the roles(comma separated) with which the issue is dealing: ').split(','))

        mode:int = 0
        while True:
            try:
                mode = int(input('Enter the mode of issue distribution(1 for available, 2 for least_busy, 3 for random): '))
                if mode == 1 or mode == 2 or mode == 3:
                    break
                else:
                    print_Error_Msg()
            except:
                print_Error_Msg()
        
        
        print('Agent(s) for the issue:', end=' ')

        if not query_func(roles, mode, Agent_List):
            print('No agents available for the issue\n')
            continue

        queried_agents:List[Agent] = query_func(roles, mode, Agent_List)

        if mode == 1:
            for i in queried_agents:
                print(i.id, end=' ')
            print()
        else:
            print(queried_agents[0])
        
        print()
