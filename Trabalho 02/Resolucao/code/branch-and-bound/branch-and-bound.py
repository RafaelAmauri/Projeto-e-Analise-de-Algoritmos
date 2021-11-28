from knapsacker import Knapsacker
class Item:
  def __init__(self, value, cost):
    self.value = value
    self.cost = cost


<<<<<<< HEAD
items = [
 # test 1: capacity 20
  # Item(3, 7),
  # Item(5, 3),
  # Item(4, 8),
  # Item(9, 3),
  # Item(10, 9),
  # Item(6, 11)
 # test 2: capacity 60
  # Item(30, 5),
  # Item(20, 10),
  # Item(100, 20),
  # Item(90, 30),
  # Item(160, 40)
 # test 3: capacity 15
  Item(10, 2),
  Item(10, 4),
  Item(12, 6),
  Item(18, 9)
]
for i in Knapsacker(items, capacity=15).pack():
  print(str(i.value) + "-" + str(i.cost))
=======
    def __gt__(self, other):
        return self.cost > other.cost

    def __str__(self):
        return f'{self.cost}'


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
    
    while(len(priority_queue) != 0):

        print(priority_queue)
        minimum = priority_queue.pop(len(priority_queue) - 1)

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
                priority_queue.sort()

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
>>>>>>> b90a468cbeaaf1d7480b96c97345a8c9f7b36f39
