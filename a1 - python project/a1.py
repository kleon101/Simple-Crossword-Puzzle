"""
Sliding Puzzle Game
Assignment 1
Semester 1, 2021
CSSE1001/CSSE7030
"""

from a1_support import *
from typing import Optional
from math import sqrt

__author__ = "Shanmukh Valluru, 46984434"
__email__ = "s4698443@uq.edu.au"


def shuffle_puzzle(solution: str) -> str:
    """
    Shuffle a puzzle solution to produce a solvable sliding puzzle.

    Parameters:
        solution (str): a solution to be converted into a shuffled puzzle.

    Returns:
        (str): a solvable shuffled game with an empty tile at the
               bottom right corner.

    References:
        - https://en.wikipedia.org/wiki/15_puzzle#Solvability
        - https://www.youtube.com/watch?v=YI1WqYKHi78&ab_channel=Numberphile

    Note: This function uses the swap_position function that you have to
          implement on your own. Use this function when the swap_position
          function is ready
    """
    shuffled_solution = solution[:-1]

    # Do more shuffling for bigger puzzles.
    swaps = len(solution) * 2
    for _ in range(swaps):
        # Pick two indices in the puzzle randomly.
        index1, index2 = random.sample(range(len(shuffled_solution)), k=2)
        shuffled_solution = swap_position(shuffled_solution, index1, index2)

    return shuffled_solution + EMPTY


# Write your functions here
def check_win(puzzle: str, solution: str) -> bool:
    """
    Returns True if game is won, otherwise will return false.

    Parameters:
        puzzle (str): string with a 'blank tile' at the end

        solution (str): a solution which is to be compared to the puzzle string


    Returns:

        check (bool): either true or false if puzzle == solution.

    """    
   

    check = True
    #If puzzle is equal to solution minus last character, then TRUE else FALSE.    
    if puzzle == solution[:-1] + " ":
        check = True
    else:
        check = False
    return check


def swap_position(puzzle: str, from_index: int, to_index: int) -> str:
    """
    Swaps the positions of characters at from_index and to_index
    and returns updated puzzle.

    Parameters:
        puzzle (str): string to which letters will be swapped.
        from_index (int): the index which will be swapped from.
        to_index (int): the index which will be swapped to.

    Returns:
        puzzle_list: which is the list of indexes after the swap has finished.

    """
    #Turns puzzle string into a list.
    puzzle_list = list(puzzle)

    #Swaps the from_index and to_index.
    puzzle_list[from_index], puzzle_list[to_index] = puzzle_list[to_index], puzzle_list[from_index]

    #Returns by joining the list into a string.
    return "".join(puzzle_list)
    
    
def move(puzzle: str, direction: str) -> Optional[str]:
    """
    Moves the empty tile in the given direction and returns the updated puzzle.
    """
    #To search for where (" ") is in the string. 
    from_index = puzzle.index(" ")


    #Length of puzzle (str)
    index_size = len(puzzle)

    #Gives the size of grid by Square Rooting the length of puzzle string.
    grid_size = sqrt(index_size)
    grid_size = int(grid_size)

    


    #If direction equals 'L' and isnt invalid then  move left.
    if direction == 'L':
        if from_index % grid_size == 0:
            puzzle = None
        else:
            puzzle = swap_position(puzzle, from_index, from_index - 1)


    #If direction equals 'R' and isnt invalid then move right.
    elif direction == 'R':
        if (from_index + 1) % grid_size == 0:
            puzzle = None
        else:
            puzzle = swap_position(puzzle, from_index, from_index + 1)

            
    #If direction equals 'U' and isnt valid then move up.
    elif direction == 'U':
        if from_index < grid_size:
            puzzle = None
        else:
            puzzle = swap_position(puzzle, from_index, from_index - 1 * grid_size)

    #If direction equals 'D' and isnt invalid then move down.
    elif direction == 'D':
        if from_index > index_size - grid_size:
            puzzle = None
        else:
            puzzle = swap_position(puzzle, from_index, from_index + 1 * grid_size)
        
        
    #Returns the updated string. 
    return puzzle
    
def print_grid(puzzle:str ) -> None:
    """ Displays the puzzle in a user-friendly format.
    """

    #Determines the length of the puzzle string. 
    index_size = len(puzzle)

    #Determines the size of the grid by square root length of string.
    grid_size = int(sqrt(index_size))


    
    for i in range(grid_size):
        #Print top border
        print("+---" * grid_size + "+")
        row = ""
        for j in range(grid_size):
            row += "| " + puzzle[j + i * grid_size] + " "

        #Print the rows for the grid.
        print(row + "|")
    #Print the bottom border.
    print("+---" * grid_size + "+")

       

  
    
def main():
    """Entry point to gameplay"""


    
    print(WELCOME_MESSAGE)

    #Asks what difficulty size of the grid.
    board_size = int(input(BOARD_SIZE_PROMPT))

    #Checks for validity of the size of grid (2-14)
    if board_size >= 2 and board_size <= 14:
         solution = get_game_solution("words.txt", board_size)


    #Puzzle shuffles the words from solution variable.
    puzzle = shuffle_puzzle(solution)

    print('Solution:')

    print_grid(solution)

    print('\nCurrent position:')

    print_grid(puzzle)

    
    #Starts the while loop for the game.
    while True:

        #If the puzzle is equal to the solution, then game won.
        if check_win(puzzle, solution) == True:

            print("\n" + WIN_MESSAGE)


            #Asks user if they want to play again.
            play_again = input(PLAY_AGAIN_PROMPT)

            #If the user wants to play again ('Y') or if not ('N')
            if play_again == 'Y' or play_again == "y":

                board_size = int(input(BOARD_SIZE_PROMPT))

                if board_size >= 2 and board_size <= 14:
                    solution = get_game_solution("words.txt", board_size)

                    puzzle = shuffle_puzzle(solution)

                    print('Solution:')

                    print_grid(solution)

                    print('\nCurrent position:')

                    print_grid(puzzle)

             


               
            #If the user press 'N' then break loop and returns None.
            elif play_again == 'N' or play_again == 'n':

                print(BYE)

                break

        
        
        prompt_command = input("\n" + DIRECTION_PROMPT)

        

            

        

         #The different options for user.

        #If 'H' entered.
        if prompt_command == HELP:
            print(HELP_MESSAGE)

            print('Solution:')
            print_grid(solution)
            print('\nCurrent position:')
            print_grid(puzzle)

        #If 'GU' is entered
        elif prompt_command == 'GU':
            print(GIVE_UP_MESSAGE)
            play_again = input(PLAY_AGAIN_PROMPT)

            #Asks if they want to play again. 
            #If 'Y' is selected then prompts difficulty
            if play_again == 'Y' or play_again == "y":
                board_size = int(input(BOARD_SIZE_PROMPT))

                #Determines the size of the grid and uses print_grid to return grids.
                if board_size >= 2 and board_size <= 14:
                    solution = get_game_solution("words.txt", board_size)

                    puzzle = shuffle_puzzle(solution)

                    print('Solution:')

                    print_grid(solution)

                    print('\nCurrent position:')

                    print_grid(puzzle)
               

                continue

            #If 'N' is selected then loop breaks and returns None.
            elif play_again == 'N' or play_again == 'n':

                print(BYE)

                break

        #If 'U' is entered moves up in the grid and returns updated grid.
        elif prompt_command == 'U':

            #Uses the move function to update the puzzle string.
            new_puzzle = move(puzzle, 'U')

            #Declares the new_puzzle to puzzle.
            if  new_puzzle:
                puzzle = new_puzzle

            #If the move is invalid then prints the invalid move message.
            else:
                print(INVALID_MOVE_FORMAT.format('U'))
                print('Solution:')
                print_grid(solution)
                print('\nCurrent position:')
                print_grid(puzzle)
                continue

            #If the move valid then prints the Solution and Current grid.
            print('Solution:')
            print_grid(solution)
            print('\nCurrent position:')
            print_grid(puzzle)

        #If 'D' is entered moves down the grid and returns the updated grid.
        elif prompt_command == 'D':

           
            new_puzzle = move(puzzle, 'D')

            #Declares new_puzzle as puzzle.
            if  new_puzzle:
                puzzle = new_puzzle

            #If the move is invalid then prints the Invalid message.
            else:
                print(INVALID_MOVE_FORMAT.format('D'))
                print('Solution:')
                print_grid(solution)
                print('\nCurrent position:')
                print_grid(puzzle)
                continue

            #If move valid then prints the Solution and Current grid.
            print('Solution:')
            print_grid(solution)
            print('\nCurrent position:')
            print_grid(puzzle)

            
        #If 'L' is entered moves left and returns the updated grid.
        elif prompt_command == 'L':
            new_puzzle = move(puzzle, 'L')
            if  new_puzzle:
                puzzle = new_puzzle

            #If invalid move then prints Invalid message.
            else:
                print(INVALID_MOVE_FORMAT.format('L'))
                print('Solution:')
                print_grid(solution)
                print('\nCurrent position:')
                print_grid(puzzle)
                continue

            #If move is valid then prints Solution and Current grid.
            print('Solution:')
            print_grid(solution)
            print('\nCurrent position:')
            print_grid(puzzle)
            

        #If 'R' is entered moves right and returns the updated grid.
        elif prompt_command == 'R':
            new_puzzle = move(puzzle, 'R')
            if  new_puzzle:
                puzzle = new_puzzle

            #If move is invalid prints the Invalid message.
            else:
                print(INVALID_MOVE_FORMAT.format('R'))
                print('Solution:')
                print_grid(solution)
                print('\nCurrent position:')
                print_grid(puzzle)
                continue

            #If move valid then prints the Solution and Current grids.
            print('Solution:')
            print_grid(solution)
            print('\nCurrent position:')
            print_grid(puzzle)

        #If the nothing valid is entered then prints the INVALID message.
        else:
            print(INVALID_MESSAGE)

            #Prints the solution and current grids and continues with the loop. 
            print('Solution:')
            print_grid(solution)
            print('\nCurrent position:')
            print_grid(puzzle)
            continue

        
            
            

   

    


        

       
            
           

        

        
                
                

        

         

            

            

        



        
            
                        
        
    

if __name__ == "__main__":
    random.seed(1001.2021)
    main()
