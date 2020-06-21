from random import randint
from operator import attrgetter
import pickle

class Agent:
    def __init__(self, roles, id, status=False, available_since=None):
        self.status = status
        self.id = id
        if self.status:
            self.available_since = available_since
        else:
            self.available_since = None
        self.roles = roles
    
    def __str__(self):
        return str(self.id)


def print_Error_Msg():
    print('PLEASE ENTER INPUT OF CORRECT TYPE AS STATED!!!')


Agent_List = None
ID_list = []

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
    Agent_List = []


# FUNCTION FOR CREATING NEW AGENT
def agents_input():
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


# FUNCTION TO RETURN THE AGENT(S) FOR THE SPECIFIC ISSUES
def func(roles, mode):
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
    # min_agent = agents[0]
    # for i in range(1,len(agents)):
    #     if agents[i].available_since < min_agent.available_since:
    #         min_agent = agents[i]
    
    # return min_agent


# FUNCTION FOR TAKING ISSUES AS INPUT
def issues_input():
    no_issues = None
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

        mode = None
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

        if func(roles,mode) is None:
            print('No agents available for the issue\n')
            continue

        if mode == 1:
            for i in func(roles,mode):
                print(i.id, end=' ')
            print()
        else:
            print(func(roles,mode))
        
        print()


# FUNCTION TO EDIT THE AGENT WITH ID = id
def edit_specific_agent(id):
    for agent in Agent_List:
        if agent.id == id:
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
            
            agent.status = status
            agent.available_since = available_since
            agent.roles = roles
            print('EDITTING SUCCESSFULL!!')

            return True
    
    return False

# FUNCTION INVOKED IF USER WANTS TO EDIT AGENT(S) INFO
def edit_agent_func():
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
                if edit_specific_agent(id):
                    break
                else:
                    print("AGENT WITH ENTERED ID DOESN'T EXIST!!!")
            except:
                print_Error_Msg()
        print()

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
        agents_input()
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
                agents_input()


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
            issues_input()


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
            edit_agent_func()


        # SAVING FINAL AGENT LIST
        pickle_file = open("agents.pickle","wb")
        pickle.dump(Agent_List,pickle_file)
        pickle_file.close()
        
main()