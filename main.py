from game_manager import GameManager
import sys

def main():
    arg = sys.argv
    search_type = 'bd_bfs'
     
    if len(arg) > 1:
        if arg[1] in ['ids', 'a_star', 'bd_bfs', 'ucs']:
            search_type = arg[1]
        else:
            print('\n\nUse "ids" or "a_star" or "bd_bfs" as an argument.')
            return

    print(f'{search_type} :')
    game_manager = GameManager()

    # Finding way
    result, depth, cost = game_manager.start_search(search_type)

    # Printing outputs
    directions = {(1, 0): 'D', (-1, 0): 'U', (0, 1): 'R', (0, -1): 'L'}
    p1 = game_manager.init_state.santa
    for i in range(len(result)):
        p2 = result[i].santa
        print(directions[(p2[0] - p1[0], p2[1] - p1[1])], end='')
        p1 = result[i].santa

    print('\nTotal moves:', depth)
    print('Total cost:', cost)
    game_manager.display_states(result)

if __name__ == "__main__":
    main()
