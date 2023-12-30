from collections import deque


class State:
    def __init__(self, state: list, depth: int = 0, parent=None) -> None:
        self.state = state
        self.parent = parent
        self.depth = depth
        self.index = state.index(0)

    def __repr__(self) -> str:
        return f"{self.state[:3]}\n{self.state[3:6]}\n{self.state[6:]}\n"

    def get_available_moves(self) -> list:
        match self.index:
            case 0:
                return ["down", "right"]
            case 1:
                return ["down", "left", "right"]
            case 2:
                return ["down", "left"]
            case 3:
                return ["up", "down", "right"]
            case 4:
                return ["up", "down", "left", "right"]
            case 5:
                return ["up", "down", "left"]
            case 6:
                return ["up", "right"]
            case 7:
                return ["up", "left", "right"]
            case 8:
                return ["up", "left"]

    def gen_children(self):
        moves = self.get_available_moves()
        zi = self.index  # index of zero
        children = []
        for move in moves:
            match move:
                case "up":
                    new_state = self.state[:]
                    new_state[zi], new_state[zi - 3] = (
                        new_state[zi - 3],
                        new_state[zi],
                    )
                    s1 = State(state=new_state, parent=self.state, depth=self.depth + 1)
                    children.append(s1)
                case "down":
                    new_state = self.state[:]
                    new_state[zi], new_state[zi + 3] = (
                        new_state[zi + 3],
                        new_state[zi],
                    )
                    s2 = State(state=new_state, parent=self.state, depth=self.depth + 1)
                    children.append(s2)

                case "left":
                    new_state = self.state[:]
                    new_state[zi], new_state[zi - 1] = (
                        new_state[zi - 1],
                        new_state[zi],
                    )
                    s3 = State(state=new_state, parent=self.state, depth=self.depth + 1)
                    children.append(s3)

                case "right":
                    new_state = self.state[:]
                    new_state[zi], new_state[zi + 1] = (
                        new_state[zi + 1],
                        new_state[zi],
                    )
                    s4 = State(state=new_state, parent=self.state, depth=self.depth + 1)
                    children.append(s4)
        return children


def main():
    INITIAL = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    GOAL = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Perform BFS
    n1 = State(INITIAL)
    dq = deque([n1])
    visited = set()
    while dq:
        for elem in dq:
            # Check if goal state has been reached
            if elem.state == GOAL:
                for vist in visited:
                    print(vist)
                print("Goal reached:")
                print(elem)
                exit(0)

        # Expand the left most node to get its children
        # Add that node to the list of visited nodes
        # Pop the node of which children has been obtained
        children = dq[0].gen_children()
        visited.add(tuple(dq[0].state))
        dq.extend(children)
        dq.popleft()

        # Make a copy of deque such that modification can be made while iterating
        # Remove visited nodes if any reappear in the deque
        copy_dq = dq.copy()
        for elem in copy_dq:
            if tuple(elem.state) in visited:
                dq.remove(elem)


if __name__ == "__main__":
    main()
