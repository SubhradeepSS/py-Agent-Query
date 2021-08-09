import unittest

from helpers.agent.models import Agent
from helpers.query import query_func



class TestAgentModel(unittest.TestCase):
    agent = Agent(['role_1'], 100)

    def test_invalid_agent_model(self):
        self.assertRaises(TypeError, Agent)

    def test_optional_status(self):
        self.assertEqual(self.agent.status, False)

    def test_available_since_for_false_status(self):
        self.assertIsNone(self.agent.available_since)

    def test_optional_available_since(self):
        self.assertEqual(0, Agent(['role_1'], 100, True).available_since)

    def test_role(self):
        self.assertEqual(self.agent.roles, ['role_1'])

    def test_id(self):
        self.assertEqual(self.agent.id, 100)



class TestQueryFunction(unittest.TestCase):
    agent_1 = Agent(['role_1'], 100, True, 2.45)
    agent_2 = Agent(['role_1', 'role_2'], 101, False)
    agent_3 = Agent(['role_2', 'role_3', 'role_1'], 102, True, 3.21)

    agents = [ agent_1, agent_2, agent_3 ]

    def test_all_available_mode(self):
        available_agents = query_func(['role_1'], 1, self.agents)
        self.assertEqual(available_agents, [ self.agent_1, self.agent_3 ])

    def test_least_busy_mode_list(self):
        least_busy_agent_list = query_func(['role_1'], 2, self.agents)
        self.assertEqual(1, len(least_busy_agent_list))

    def test_least_busy_mode_agent(self):
        least_busy_agent = query_func(['role_1'], 2, self.agents)[0]
        self.assertEqual(least_busy_agent.id, self.agent_1.id)

    def test_all_available_mode_for_multiple_roles(self):
        available_agents = query_func(['role_1', 'role_2'], 1, self.agents)
        self.assertEqual(available_agents, [ self.agent_3 ])

    def test_all_available_mode_for_non_matching_role(self):
        available_agents = query_func(['role_4'], 1, self.agents)
        self.assertEqual(available_agents, [])



if __name__ == '__main__':
    unittest.main()