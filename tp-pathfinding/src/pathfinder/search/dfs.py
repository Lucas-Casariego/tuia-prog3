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
            return Solution(root, explored, root.cost)

        # la frontera se maneja como una pila 
        frontier = StackFrontier()
        frontier.add(root)
       
       
        while not frontier.is_empty():
            n = frontier.remove()
            # expandimos el nodo según todas las acciones posibles
            for action in Grid.actions(grid, n.state):
                s2 = Grid.result(grid, n.state, action)
                if s2 not in reached:
                    n2 = Node("", s2, n.cost + Grid.individual_cost(grid, n.state, action), n, action)

                    if Grid.objective_test(grid, s2):
                        return Solution(n2, reached, n2.cost)

                    reached[s2] = True
                    frontier.add(n2)

       

        # Si agotamos la frontera sin hallar solución
        return NoSolution(reached)




