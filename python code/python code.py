from random import randint
from operator import attrgetter
import pickle
import sys

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

class Issue:
    def __init__(self, roles):
        self.roles = roles

Agent_List = None
ID_list = []

try:
    pickle_file = open("agents.pickle","rb")
    Agent_List = pickle.load(pickle_file)
    pickle_file.close()
    print('\nFollowing Agents are available:-\n')
    for a in Agent_List:
        print(f"ID: {a.id}\nStatus: {a.status}\nRoles: {a.roles}\nAvailable since: {a.available_since}\n")
        ID_list.append(a.id)
    print()
except:
    print("\nNo Agents present in Database.Please create agents first to check available agents for issues\n")
    Agent_List = []


def agents_input():
    n = int(input('Enter the number of agents to create: '))
    print()

    print('Enter the details of the agents as stated\n')

    for i in range(n):
        id = int(input('Enter the ID of the agent you want to create: '))
        while id in ID_list:
            id = int(input('This ID is already present.Please enter another ID: '))
        ID_list.append(id)

        s_input = input('Enter 1 if agent is available else 0: ')

        status, available_since = False, None
        if s_input == '1':
            status = True
            available_since = float(input('Enter the time since last availability(in Decimal): '))
        
        roles = list(input('Enter roles of agent(separated by comma): ').split(','))

        Agent_List.append(Agent(roles=roles,id=id,status=status,available_since=available_since))
        
        print()


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

    if mode == 1:
        return agents
    
    elif mode == 3:
        return agents[randint(0,len(agents)-1)]
    
    return min(agents, key=attrgetter('available_since'))
    # min_agent = agents[0]
    # for i in range(1,len(agents)):
    #     if agents[i].available_since < min_agent.available_since:
    #         min_agent = agents[i]
    
    # return min_agent


def issues_input():
    no_issues = int(input('Enter the number of issue queries: '))
    print()

    print('Enter the details of the issues as stated\n')

    for i in range(no_issues):
        print(f"Enter details of Issue {i+1}")
        
        roles = list(input('Enter the roles(comma separated) with which the issue is dealing: ').split(','))
        mode = int(input('Enter the mode of issue distribution(1 for available, 2 for least_busy, 3 for random): '))
        
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


def main():
    new_agent = input('Do you want to create new agents[y for yes/n for no]? ')
    print()
    if new_agent == 'y':
        agents_input()
    else:
        if not Agent_List:
            ip = input('\nDo you really want to quit creating agents, as currently database does not contain any agent and issue query is not possible for an empty database of agents?[y for yes/n for no] ')
            print()
            if ip == 'n':
                agents_input()

    if Agent_List:
        pickle_file = open("agents.pickle","wb")
        pickle.dump(Agent_List,pickle_file)
        pickle_file.close()

        new_issue = input('\nDo you want to check available agents for issues[y for yes/n for no]? ')
        print()
        if new_issue == 'y':
            issues_input()

main()