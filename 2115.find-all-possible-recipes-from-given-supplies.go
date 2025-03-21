package leetcode


/*
 * @lc app=leetcode id=2115 lang=golang
 *
 * [2115] Find All Possible Recipes from Given Supplies
 */

// @lc code=start
func findAllRecipes(recipes []string, ingredients [][]string, supplies []string) []string {
	indegrees := map[string]int{}
	outEdges := map[string][]string{}

	// Build the graph from ingredients to recipes
	for i, recipe := range recipes {
		indegrees[recipe] = len(ingredients[i]) // Number of required ingredients
		for _, ingredient := range ingredients[i] {
			outEdges[ingredient] = append(outEdges[ingredient], recipe)
		}
	}

	// Initialize the queue with supplies
	queue := append([]string{}, supplies...)
	possibleRecipes := []string{}
	
	// Use two-pointer queue approach
	for front := 0; front < len(queue); front++ {
		curr := queue[front]
		for _, recipe := range outEdges[curr] {
			indegrees[recipe]--
			if indegrees[recipe] == 0 { // Recipe can be made
				queue = append(queue, recipe)
				possibleRecipes = append(possibleRecipes, recipe)
			}
		}
	}

	return possibleRecipes
}

// @lc code=end

