from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize explored with the initial state
        reached = {} # conjunto de estados alcanzados
        reached[root.state] = True # me marca si el estado fue alcanzado

#         # Initialize frontier with the root node
#         # TODO Complete the rest!!

          # Si la salida coincide con el objetivo..
        if Grid.objective_test(grid, root.state):
            return Solution(root, reached, root.cost)

        # la frontera se maneja como una pila 
        frontier = StackFrontier()
        frontier.add(root)
       
       
        while not frontier.is_empty():
           parent_n = frontier.remove()
            # expandimos el nodo según todas las acciones posibles
            for action in Grid.actions(grid,parent_n.state):
                new_state = Grid.result(grid,parent_n.state, action)
                if new_state not in reached:
                    child_n = Node("", new_state, parent_n.cost + Grid.individual_cost(grid, parent_n.state, action), parent_n, action)

                    if Grid.objective_test(grid, new_state):
                        return Solution(child_n, reached, child_n.cost)

                    reached[new_state] = True
                    frontier.add(child_n)

       

        # Si agotamos la frontera sin hallar solución
        return NoSolution(reached)




