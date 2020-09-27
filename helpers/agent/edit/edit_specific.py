from ...error import print_Error_Msg

# FUNCTION TO EDIT THE AGENT WITH ID = id
def edit_specific_agent(id, Agent_List):
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
