N = 4
INT_MAX = 999999999999

class Node:
    def __init__(self, x, y, assigned, parent):

        # Armazena o no pai desse no
        self.parent = parent

        # Custo de todos nos anteriores + no atual
        self.path_cost = 0

        # Menor custo encontrado
        self.cost = 0

        # ID do trabalhador
        self.workerID = x
        
        # ID da tarefa
        self.jobID = y

        self.assigned = [0 for x in range(N)]

        for i in range(N):
            self.assigned[i] = assigned[i]
        self.assigned[y] = True


    def __gt__(self, other):
        return self.cost > other.cost


def calculate_cost(cost_matrix, x, y, assigned):
    cost = 0

    available = [True for x in range(N)]

    for i in range(x+1, N):
        minimum = INT_MAX
        min_index = -1

        for j in range(N):
            if (not assigned[j]) and (available[j]) and (cost_matrix[i][j] < minimum):
                min_index = j

                minimum = cost_matrix[i][j]

        
        cost += minimum
        available[min_index] = False

    
    return cost


def print_assignments(minimum):
    if minimum.parent == None:
        return

    print_assignments(minimum.parent)
    print(f"Assign worker {minimum.workerID} to job {minimum.jobID}\n")


def find_min_cost(cost_matrix):
    priority_queue = []
    
    assigned = [False for x in range(N)]
    root = Node(-1, -1, assigned, None)
    
    root.path_cost  =  0
    root.cost       =  0
    root.workerID   = -1

    priority_queue.append(root)
    
    while(len(priority_queue) > 0):
        minimum = priority_queue[0]

        priority_queue.pop(0)

        i = minimum.workerID+1

        if i == N:
            print_assignments(minimum)
            return minimum.cost


        for j in range(N):
            if not minimum.assigned[j]:
                child = Node(i, j, minimum.assigned, min)

                child.path_cost = minimum.path_cost + cost_matrix[i][j]

                child.cost = child.path_cost + calculate_cost(cost_matrix, i, j, child.assigned)

                priority_queue.append(child)

def main():
    cost_matrix = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ]

    print(find_min_cost(cost_matrix))

if __name__ == '__main__':
    main()