class Game():
    

    def game(self,player1_choice,player2_choice):
        if player1_choice == player2_choice:
            return "Draw"
        elif player1_choice == "rock" and player2_choice == "paper":
            return "Paper wins over rock"
        elif player2_choice == "rock" and player1_choice == "paper":
            return "Paper wins over rock"
        elif player1_choice == "rock" and player2_choice == "scissors":
            return "Rock wins over scissors"
        elif player2_choice == "rock" and player1_choice == "scissors":
            return "Rock wins over scissors"
        else:
            return "Scissors wins over paper"