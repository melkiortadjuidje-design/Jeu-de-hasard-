import random

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bet = 0
        self.lottery_number = None
        self.color = None


class GameEngine:
    def __init__(self):
        self.player = Player("Player1", 100)

    def get_bet(self):
        """Asks for a stake and validates it."""
        while True:
            try:
                bet = int(input(f"How much do you want to bet? (Balance: {self.player.money}$) "))
                if bet <= 0:
                    print("Please enter a positive amount.")
                elif bet > self.player.money:
                    print("You cannot bet more than your current balance.")
                else:
                    self.player.bet = bet
                    break
            except ValueError:
                print("Invalid input — please enter a whole number.")

    def get_choices(self):
        """Collects the player's color and number choices."""
        while True:
            color = input("Choose a color (blanc / noir): ").strip().lower()
            if color in ["blanc", "noir"]:
                self.player.color = color
                break
            print("Invalid color. Please type 'blanc' or 'noir'.")

        while True:
            try:
                number = int(input("Choose a number (0–49): "))
                if 0 <= number <= 49:
                    self.player.lottery_number = number
                    break
                print("Number must be between 0 and 49.")
            except ValueError:
                print("Invalid input — please enter a whole number.")

    def spin(self):
        """Generates the round's winning color and number."""
        return random.choice(["blanc", "noir"]), random.randint(0, 49)

    def resolve(self, win_color, win_number):
        """Applies the outcome and updates the player's balance."""
        print(f"\n  → Result: {win_color} / {win_number}")

        if self.player.color == win_color and self.player.lottery_number == win_number:
            gain = self.player.bet * 5
            self.player.money += gain
            print(f"  🎉 Jackpot! You won {gain}$. Balance: {self.player.money}$")

        elif self.player.color == win_color:
            gain = self.player.bet * 2
            self.player.money += gain
            print(f"  ✅ Good guess! You won {gain}$. Balance: {self.player.money}$")

        else:
            loss = self.player.bet // 2   # player recovers 50% of stake
            self.player.money -= loss
            print(f"  ❌ Wrong. You lost {loss}$ (50% of your stake). Balance: {self.player.money}$")


class UI:
    def __init__(self):
        self.engine = GameEngine()

    def _build_ui(self):
        self.engine.player.name = input( "Entre ton nom avant de commencer  :  ")
        print(f"\nWelcome, {self.engine.player.name}! Starting balance: {self.engine.player.money}$\n")

        while self.engine.player.money > 0:
            print("─" * 40)
            action = input("Press Enter to play or type 'q' to quit: ").strip().lower()

            if action == "q":
                print(f"\nThanks for playing! Final balance: {self.engine.player.money}$")
                break

            self.engine.get_bet()
            self.engine.get_choices()
            win_color, win_number = self.engine.spin()
            self.engine.resolve(win_color, win_number)

        else:
            print("\nGame over — you have no money left.")


if __name__ == "__main__":
    ui = UI()
    ui._build_ui()
