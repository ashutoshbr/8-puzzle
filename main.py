class State:
    def __init__(self, state: list, depth: int = 0, parent=None) -> None:
        self.state = state
        self.parent = parent
        self.depth = depth
        self.index = state.index(0)

    def __repr__(self) -> str:
        return f"{self.state[:3]}\n{self.state[3:6]}\n{self.state[6:]}"

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


INITIAL = [1, 2, 3, 4, 0, 5, 6, 7, 8]
GOAL = [0, 1, 2, 3, 4, 5, 6, 7, 8]

n1 = State(INITIAL)
print(n1)
print(n1.get_available_moves())
children = n1.gen_children()
for child in children:
    print(child)
    print("\n")
