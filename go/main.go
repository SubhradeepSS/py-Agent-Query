package main

import (
	"fmt"
	"math/rand"
	"strings"
)

type Agent struct {
	id              int
	is_available    bool
	available_since float64
	roles           []string
}

func contains(roles []string, role string) bool {
	for _, r := range roles {
		if r == role {
			return true
		}
	}
	return false
}

func main() {
	var no_agents, no_issues, query_mode int

	fmt.Printf("Enter the no of agents: ")
	fmt.Scan(&no_agents)

	agents := make([]Agent, no_agents)

	for idx := range agents {
		fmt.Printf("\nEnter data for agent %v\n", idx+1)

		var id int
		var is_available bool
		var available_since float64

		fmt.Printf("Enter id: ")
		fmt.Scan(&id)

		fmt.Printf("Enter is_available: ")
		fmt.Scan(&is_available)

		fmt.Printf("Enter available_since: ")
		fmt.Scan(&available_since)

		var roles string
		fmt.Printf("Enter the roles separated by comma: ")
		fmt.Scan(&roles)

		roles_splitted := strings.Split(roles, ",")

		agents[idx] = Agent{id, is_available, available_since, roles_splitted}

		// fmt.Println(agent.id, agent.is_available, agent.available_since, agent.roles)
	}

	fmt.Print(agents)

	fmt.Print("\n\nEnter the no of issues: ")
	fmt.Scan(&no_issues)

	for no_issues > 0 {
		no_issues--

		var roles string
		fmt.Printf("Enter the roles of issue separated by comma: ")
		fmt.Scan(&roles)

		fmt.Printf("Enter the issue selection mode(1 for available, 2 for least busy(highest available since), 3 for random): ")
		fmt.Scan(&query_mode)

		roles_splitted := strings.Split(roles, ",")

		var matching_agents []Agent

		for _, agent := range agents {
			if !agent.is_available {
				continue
			}

			is_matching := true
			for _, role := range roles_splitted {
				if !contains(agent.roles, role) {
					is_matching = false
					break
				}
			}

			if is_matching {
				matching_agents = append(matching_agents, agent)
			}
		}

		if len(matching_agents) == 0 {
			fmt.Println("No matching agents found")
			return
		}

		switch query_mode {
		case 1:
			fmt.Println(matching_agents)

		case 2:
			var req_agent Agent
			max_available_since := matching_agents[0].available_since

			for i := 1; i < len(matching_agents); i++ {
				if matching_agents[i].available_since > max_available_since {
					max_available_since = matching_agents[i].available_since
					req_agent = matching_agents[i]
				}
			}

			fmt.Println(req_agent)

		case 3:
			random_idx := rand.Intn(len(matching_agents))
			fmt.Println(matching_agents[random_idx])
		}
	}
}
