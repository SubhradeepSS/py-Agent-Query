import pickle

from helpers.error import print_Error_Msg
from helpers.agent.models import Agent
from helpers.issue.input_func import issues_input
from helpers.agent.input_func import agents_input
from helpers.agent.edit.edit_main import edit_agent_func

from typing import List

Agent_List:List[Agent] = []
ID_list:List[int] = []

# LOAD EXISTING AGENT DATA (IF AVAILABLE)
try:
    pickle_file = open("agents.pickle","rb")
    Agent_List = pickle.load(pickle_file)
    pickle_file.close()

    view_agents = None
    while True:
        view_agents = input('\nDo you want to view existing agents[y for yes/n for no]? ')
        print()
        if view_agents == 'y' or view_agents == 'n':
            break
        else:
            print_Error_Msg()

    if view_agents == 'y':
        print('\nFollowing Agents are available:-\n')

        for a in Agent_List:
            detail = f"ID: {a.id}\nStatus: "
            
            if a.status:
                detail += 'Available'
            else:
                detail += 'Not Available'

            print(detail + f"\nRoles: {a.roles}\nAvailable since: {a.available_since}\n")

            ID_list.append(a.id)
        print()

except:
    print("\nNo Agents present in Database.Please create agents first to check available agents for issues\n")



# MAIN FUNCTION FOR THE PROGRAM
def main():
    
    # ASKING USER WHETHER TO CREATE NEW AGENT
    new_agent = None
    while True:
        new_agent = input('\nDo you want to create new agents[y for yes/n for no]? ')
        print()
        if new_agent == 'y' or new_agent == 'n':
            break
        else:
            print_Error_Msg()

    if new_agent == 'y':
        agents_input(Agent_List, ID_list)
    else:
        if not Agent_List:
            ip = None

            while True:
                # NO AGENTS ARE CREATED SO FIRST CREATE AGENTS AND THEN CHECK FOR AGENTS' AVAILABILITY FOR ISSUE
                ip = input('\nDo you really want to quit creating agents, as currently database does not contain any agent and issue query is not possible for an empty database of agents[y for yes/n for no]? ')
                print()
                if ip == 'y' or ip == 'n':
                    break
                else:
                    print_Error_Msg()

            if ip == 'n':
                agents_input(Agent_List, ID_list)


    if Agent_List:
        # ASKING USER WHETHER TO CHECK AVAILABLE AGENTS FOR ISSUE
        while True:
            new_issue = input('\nDo you want to check available agents for issues[y for yes/n for no]? ')
            if new_issue == 'y' or new_issue == 'n':
                break
            else:
                print_Error_Msg()

        print()
        if new_issue == 'y':
            issues_input(Agent_List)


        # IF USER WANTS TO EDIT ANY AGENTS' INFO
        edit_agent = None
        while True:
            edit_agent = input('\nDo you want to edit any agent info[y for yes/n for no]? ')
            print()
            if edit_agent == 'y' or edit_agent == 'n':
                break
            else:
                print_Error_Msg()

        if edit_agent == 'y':
            edit_agent_func(Agent_List)


        # SAVING FINAL AGENT LIST
        pickle_file = open("agents.pickle","wb")
        pickle.dump(Agent_List,pickle_file)
        pickle_file.close()
        
main()