class Node:
    def __init__(self, rel_pos, row):
        assert rel_pos <= row

        self.rel_pos = rel_pos
        self.row = row
        self.idx = self.get_abs_idx()

    def get_abs_idx(self):
        return self.rel_pos + self.row * (self.row+1) // 2

    def left_child(self):
        return Node(self.rel_pos, self.row+1)

    def right_child(self):
        return Node(self.rel_pos+1, self.row+1)

    def parent_on_left(self):
        # caller node is right child of the parent
        return Node(self.rel_pos-1, self.row-1)

    def parent_on_right(self):
        # caller node is left child of the parent
        return Node(self.rel_pos, self.row-1)

    def get_value(self, triangle):
        return triangle.get_by_index(self.get_abs_idx())


class Triangle:
    def __init__(self, input_lst: list, rows: int):
        assert len(input_lst) == rows * (rows+1) // 2

        self.lst = input_lst
        self.rows = rows
        self.root = Node(0, 0)

    def get_by_index(self, idx):
        if abs(idx) < len(self.lst):
            return self.lst[idx]

    def get_root(self):
        return self.root

    def find_best_route(self):
        # dynamic programming approach

        # initialize costs list with some big numbers
        costs = [1_000_000] * len(self.lst)
        costs[0] = self.lst[0]

        moves = ['_'] * len(self.lst)

        self.go_deeper_recursively(self.root, costs, moves)
        self.pprint_costs(costs)
        # self.pprint_costs(moves)
        return self.find_best_moves(costs, moves)

    def find_best_moves(self, costs, moves):
        best_moves_reverse = []
        lowest_final_cost = min(costs[-self.rows:])
        rel_pos = costs[-self.rows:].index(lowest_final_cost)
        cur_node = Node(rel_pos, self.rows-1)
        best_moves_reverse.append(moves[cur_node.idx])
        for _ in range(self.rows-1):
            if best_moves_reverse[-1] == 'l':
                cur_node = cur_node.parent_on_right()
            else:
                cur_node = cur_node.parent_on_left()
            best_moves_reverse.append(moves[cur_node.idx])
        return best_moves_reverse[::-1], lowest_final_cost

    def pprint_costs(self, costs):
        for i in range(self.rows):
            for j in range(i+1):
                idx = i*(i+1)//2 + j
                print(costs[idx], end=' ')
            print()

    def go_deeper_recursively(self, cur_node: Node, costs, moves):
        if cur_node.row >= self.rows-1:
            return

        left_node = cur_node.left_child()
        if costs[left_node.idx] > left_node.get_value(self) + costs[cur_node.idx]:
            costs[left_node.idx] = left_node.get_value(self) + costs[cur_node.idx]
            moves[left_node.idx] = 'l'
            self.go_deeper_recursively(left_node, costs, moves)

        right_node = cur_node.right_child()
        if costs[right_node.idx] > right_node.get_value(self) + costs[cur_node.idx]:
            costs[right_node.idx] = right_node.get_value(self) + costs[cur_node.idx]
            moves[right_node.idx] = 'r'
            self.go_deeper_recursively(right_node, costs, moves)
