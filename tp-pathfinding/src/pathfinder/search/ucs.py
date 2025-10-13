from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node

        frontier = PriorityQueueFrontier()
        frontier.add(root, root.cost)

        while not frontier.is_empty():
            parent_n = frontier.pop()

            if Grid.objective_test(grid, parent_n.state):
                return Solution(parent_n, reached, parent_n.cost)
            
            for action in Grid.actions(grid, parent_n.state):
                new_state = Grid.result(grid, parent_n.state, action)
                accum_cost = parent_n.cost + Grid.individual_cost(grid, parent_n.state, action)

                if new_state not in reached or accum_cost < reached[new_state]:
                    child_n = Node("", new_state, accum_cost, parent_n, action)
                    reached[new_state] = accum_cost
                    frontier.add(child_n, accum_cost)
        
        return NoSolution(reached)
