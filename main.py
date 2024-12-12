# currently no items and only LAN (offline) and two players and no AI
import random
from enum import Enum

class Bullet(Enum):
    BLANK = 0
    LIVE = 1

class Commands(Enum):
    PICKUP_GUN = "0"
    

class Player():
    def __init__(self, name):
        self.health = 5
        self.name = name

    def set_opponents_list(self, all_players_lst :list):
        self.opponents_list :list = []
        for player in all_players_lst:
            if player != self:
                self.opponents_list.append(player)

    def set_gun(self, gun):
        self.gun : Gun = gun

    def get_player_action(self):
        # TODO - replace with proper UI functions once implemented
        # TODO - prevent invalid commands
        cmd = input("Choose action: ")
        if cmd == "0":
            return Commands.PICKUP_GUN
        
    def choose_player_to_shoot(self):
        # TODO - replace with proper UI functions once implemented
        cmd = input("Choose person to shoot: ")
        if cmd == "me":
            return self
        else:
            return self.opponents_list[0]   # TODO - implement properly when 3/more players

    def play_turn(self):
        # use items # TODO - implement when items are added
        # pick up gun
        # choose who to shoot
        # fire

        action = self.get_player_action()
        if action == Commands.PICKUP_GUN:
            player_to_shoot = self.choose_player_to_shoot()
            self.gun.set_target(player_to_shoot)
            self.gun.fire()


    def lose_health(self, dmg):
        self.health -= dmg

    def is_alive(self):
        return self.health > 0
    
    def print_info(self):
        print(f"-------{self.name} Info--------")
        print(f"Health: {self.health}")
        print(f"opponents_list: {self.opponents_list}")
        print("---------------------------------------")


class Gun():
    def __init__(self):
        self.dmg = 1
        self.magazine :list = [] 

    def set_target(self, player :Player):
        self.target = player


    def fire(self):
        current_bullet = self.magazine.pop()
        if current_bullet == Bullet.BLANK:
            myoutput(f"Gun fired BLANK: No one is harmed")
        elif current_bullet == Bullet.LIVE:
            self.target.lose_health(self.dmg)
            myoutput(f"Gun fired LIVE: {self.target.name} got damaged by {self.dmg}!")


    def load_gun_in_random_order(self, num_blanks, num_lives):
        """
        PRE: magazine is empty
        """
        magazine :list = []

        for i in range(num_blanks):
            magazine.append(Bullet.BLANK)

        for i in range(num_lives):
            magazine.append(Bullet.LIVE)

        random.shuffle(magazine)
        self.magazine = magazine

        myoutput(f"Gun loaded: {self.magazine}")



    def is_empty(self):
        return len(self.magazine) == 0


def myoutput(str):
    print(str)

class Game():
    def __init__(self):
        self.gun = Gun()
        self.player1 = Player("Genshin")
        self.player2 = Player("ZZZ")

        all_players_list = [self.player1, self.player2]

        self.player1.set_gun(self.gun)
        self.player1.set_opponents_list(all_players_list)
        self.player1.print_info()

        self.player2.set_gun(self.gun)
        self.player2.set_opponents_list(all_players_list)
        self.player2.print_info()



    def generate_random_bullets(self):
        """
        PRE: magazine is empty
        """
        max_poss_bullets = 6
        total_num_bullets = random.randint(2, max_poss_bullets)
        num_blanks = random.randint(1, max_poss_bullets - 1)
        num_lives = total_num_bullets - num_blanks
        return num_blanks, num_lives


    def switch_turns(self):
        # TODO - implement properly if 3/more players
        if self.player_with_turn == self.player1:
            self.player_with_turn = self.player2
        else:
            self.player_with_turn = self.player1


    def run(self):
        myoutput("STARTING GAME")
        myoutput("------------------------------")

        self.player_with_turn = self.player1

        while self.player1.is_alive() and self.player2.is_alive():
            if self.gun.is_empty():
                myoutput("Loading bullets:")
                num_blanks, num_lives = self.generate_random_bullets()
                myoutput(f"Number of Blanks: {num_blanks}, Number of Lives: {num_lives}")
                self.gun.load_gun_in_random_order(num_blanks, num_lives)

            self.player_with_turn.play_turn()
            self.switch_turns()


        
            



        # while both players are alive

            # if gun is empty
                # generate random bullets
                # notify players
                # load gun

            # make player whos turn it is do their actions
            # end their turn
        

        # end game

game = Game()
game.run()