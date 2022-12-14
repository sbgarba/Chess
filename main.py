"""
Chess in python
"""


def main():
    """
    This project is meant to create a chess board that can move pieces around
    and give the user complete free rein.
    There are no actual rules to how the board has to function, as you simply
    move and replace pieces
    :return: nothing
    """

    __author__ = "Samuel Garbarino"

    daRules = "Welcome to Sam's Chess in python " \
              "\nFirst thing you need to know," \
              "is that the 'help' command shows you all possible actions\n" \
              "Now onto the actual chess part: instead of having black" \
              "and white, we have uppercase and lowercase.\n" \
              "All pieces are the character that starts with their name" \
              ", except for the kings, which are denoted with & and $ on" \
              "their respective sides.\n" \
              "if you dislike any symbol for a piece " \
              "you can swap it out with" \
              "'replace'.\n" \
              "There are no real rules, this is really only a step above" \
              "pencil and paper. You can start playing with 'move'"

    # The chessboard itself is simply a list that is manipulated, this is
    # easily seen through the way I've outlined it in the file itself
    chessBoard = ["r", "k", "b", "q", "&", "b", "k", "r",  # 1-8
                  "p", "p", "p", "p", "p", "p", "p", "p",  # 9-16
                  "_", "_", "_", "_", "_", "_", "_", "_",  # 17-24
                  "_", "_", "_", "_", "_", "_", "_", "_",  # 25-32
                  "_", "_", "_", "_", "_", "_", "_", "_",  # 33-40
                  "_", "_", "_", "_", "_", "_", "_", "_",  # 41-48
                  "P", "P", "P", "P", "P", "P", "P", "P",  # 49-56
                  "R", "K", "B", "Q", "$", "B", "K", "R"]  # 57-64
    # comments seen here ^ are to help myself

    def pieceSelector():
        """
        Players can select a piece to move or to analyze through this
        function
        :return: The pieces or coords selected through input
        """
        global selectedColumn, selectedRow
        selectedColumnInt = 0
        hasUserGivenValidResponse = False
        while not hasUserGivenValidResponse != False:
            hasUserGivenValidResponse = False
            try:
                selectedColumn = input("Please select a column: ")
                if selectedColumn == "A" or selectedColumn == "a":
                    selectedColumnInt = 1
                    hasUserGivenValidResponse = True
                elif selectedColumn == "B" or selectedColumn == "b":
                    selectedColumnInt = 2
                    hasUserGivenValidResponse = True
                elif selectedColumn == "C" or selectedColumn == "c":
                    selectedColumnInt = 3
                    hasUserGivenValidResponse = True
                elif selectedColumn == "D" or selectedColumn == "d":
                    selectedColumnInt = 4
                    hasUserGivenValidResponse = True
                elif selectedColumn == "E" or selectedColumn == "e":
                    selectedColumnInt = 5
                    hasUserGivenValidResponse = True
                elif selectedColumn == "F" or selectedColumn == "f":
                    selectedColumnInt = 6
                    hasUserGivenValidResponse = True
                elif selectedColumn == "G" or selectedColumn == "g":
                    selectedColumnInt = 7
                    hasUserGivenValidResponse = True
                elif selectedColumn == "H" or selectedColumn == "h":
                    selectedColumnInt = 8
                    hasUserGivenValidResponse = True
                else:
                    print("Invalid Response, please select a Column")
            except:
                print("Invalid Response, please select a Column")

        hasUserGivenValidResponse = False
        while not False != hasUserGivenValidResponse:
            try:
                selectedRow = int(input("Please select row: "))
                if not 0 >= selectedRow:
                    if selectedRow < 9:
                        hasUserGivenValidResponse = True
                    else:
                        print("Invalid Response,"
                              " please select a Row between 1 and 8")
                else:
                    print("Invalid Response,"
                          " please select a Row between 1 and 8")

            except:
                print("Invalid Response, please select a Row")
        # returning a coordinate
        coordSelected = (selectedColumnInt + ((8 - selectedRow) * 8)) - 1
        print("Currently selecting ", selectedColumn, selectedRow, " - ",
              chessBoard[coordSelected], sep="")
        return coordSelected

    def chessBoardVisualizer():
        """
        Displays the chess board for the players
        :return: none
        """

        rowNumber = 8
        print(rowNumber, "|", sep="", end=" ")

        for chessBoardRowCount in range(1, 9):

            for chessBoardRow in range(
                    (chessBoardRowCount * 8) - 8, chessBoardRowCount * 8):
                print(chessBoard[chessBoardRow], end=" ")

            rowNumber -= 1

            if rowNumber > 0:
                print("\n", rowNumber, "|", sep="", end=" ")
            else:
                print("\n", "  |~|~|~|~|~|~|~|", "\n",
                      "  A B C D E F G H")
                # the count of 8 and the 8 letters give instruction as to how
                # you should select a piece
        print()

    def boardChanger(selection1, newCharacter1, selection2):
        """
        allows changing of board state
        :param selection1: the first coord selection made by a player
        :param newCharacter1: the new character should one be replaced
        :param selection2: the second coord selection made by a player
        :return: none
        """
        if selection2 != -1:
            print("Moving", chessBoard[selection1], "to",
                  chessBoard[selection2])
            chessBoard[selection2] = chessBoard[selection1]
            chessBoard[selection1] = "_"
        else:
            print("Replacing", chessBoard[selection1], "with", newCharacter1)
            chessBoard[selection1] = newCharacter1

    def actionSelector():
        """
        The function allowing users to
        :return: can return False if the user wishes to end the program
        """
        hasUserGivenValidResponse = False

        while False == hasUserGivenValidResponse:

            print("Please select an action to make"
                  " (or say 'help' for help): ", end="")
            selectedAction = input()
            if selectedAction == "help":
                print("rules: Re-explains how the board works (but not the rules"
                      "of chess)",
                      "help: displays this message",
                      "move: begins moving a piece",
                      "replace: Replaces a piece on the board with a new one",
                      "end: Stops the program",
                      sep="\n")
                hasUserGivenValidResponse = True
            elif selectedAction == "rules":
                print(daRules)
                hasUserGivenValidResponse = True
            elif selectedAction == "move":
                boardChanger(pieceSelector(), "a", pieceSelector())
                hasUserGivenValidResponse = True
            elif selectedAction == "replace":
                newPiece = ""
                while newPiece == "":
                    newPiece = input("Please select replacement piece: ")
                selectedPiece = pieceSelector()
                boardChanger(selectedPiece, newPiece, -1)
                hasUserGivenValidResponse = True
            elif selectedAction == "end":
                return False
            else:
                print("Invalid action: type 'help' for help")
        return True

    print(daRules)
    runProgram = True
    while True == runProgram:
        chessBoardVisualizer()
        runProgram = actionSelector()


main()
