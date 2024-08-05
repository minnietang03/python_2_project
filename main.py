import random

moves = ["rock", "paper", "scissors"]


class Player:
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass

class AllRockPlayer(Player):
    def move(self):
        return "rock"

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move (rock, paper, scissors): ").lower()
            if move in moves:
                return move
            else:
                print("Invalid input! Please try again.")


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = random.choice(moves)

    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)

    def move(self):
        next_move_index = (moves.index(self.my_move) + 1) % len(moves)
        self.my_move = moves[next_move_index]
        return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return two in {
        'rock':['scissors'],
        'scissors':['paper'],
        'paper':['rock']
    }.get(one,[])


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("Player 1 wins this round!")
            self.p1_score += 1
        elif beats(move2, move1):
            print("Player 2 wins this round!")
            self.p2_score += 1
        else:
            print("This round is a tie!")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Score: Player 1 - {self.p1_score}, Player 2 - {self.p2_score}")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")
        print(f"Final Score: Player 1 - {self.p1_score},"
              f"Player 2 - {self.p2_score}")
        if self.p1_score > self.p2_score:
            print("Player 1 wins the game!")
        elif self.p2_score > self.p1_score:
            print("Player 2 wins the game!")
        else:
            print("The game is a tie!")


if __name__ == "__main__":
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
