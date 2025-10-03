from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

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
        frontier.add(root, Grid.heuristic_manhattan(grid, root.state))

        while not frontier.is_empty():
            n = frontier.pop()
            
            if(Grid.objective_test(grid, n.state)):
                return Solution(n, reached)
            
            for action in Grid.actions(grid, n.state):
                s2 = Grid.result(grid, n.state, action)
                c2 = n.cost + Grid.individual_cost(grid, n.state, action)

                if s2 not in reached or c2 < reached[s2]:
                    n2 = Node("", s2, c2, n, action)
                    reached[s2] = c2
                    frontier.add(n2, Grid.heuristic_manhattan(grid, n2.state))

        return NoSolution(reached)
