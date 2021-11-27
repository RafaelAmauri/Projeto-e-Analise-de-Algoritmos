import Celula
import Labirinto


ORDER_TO_CHECK = ["up", "left", "down", "right"]


def main(): 
    maze = Labirinto.Labirinto(6, 6, ORDER_TO_CHECK)

    '''
    Representacao do labirinto desenhado nesse exercicio

    0 1 2 3 4 5

0   1 0 0 0 1 0 
1   1 0 1 0 1 0 
2   1 0 1 1 1 0 
3   1 0 1 0 1 1 
4   1 0 1 0 0 0 
5   1 1 1 1 1 2
     '''
    
    maze.insert(1, 0, 0)
    maze.insert(1, 1, 0)
    maze.insert(1, 2, 0)
    maze.insert(1, 3, 0)
    maze.insert(1, 4, 0)
    maze.insert(1, 5, 0)
    maze.insert(1, 5, 1)
    maze.insert(1, 5, 2)
    maze.insert(1, 4, 2)
    maze.insert(1, 3, 2)
    maze.insert(1, 2, 2)
    maze.insert(1, 1, 2)
    maze.insert(1, 2, 3)
    maze.insert(1, 2, 4)
    maze.insert(1, 1, 4)
    maze.insert(1, 0, 4)
    maze.insert(1, 3, 4)
    maze.insert(1, 3, 5)
    maze.insert(1, 5, 3)
    maze.insert(1, 5, 4)
    maze.insert(2, 5, 5)

    print(f"Labirinto:\n\n{maze}")

    print("Procurando a saida do labirinto usando backtracking:\n")

    maze.find_path(0, 0)


if __name__ == '__main__':
    main()