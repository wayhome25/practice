import time
import random

class Player():
    def __init__(self, name, secret_num):
        self.name = name
        self.money = 0
        self.item = 0
        self.secret_number = secret_num

    @property
    def secret_number(self):
        return self.__secret_number

    @secret_number.setter
    def secret_number(self, secret_num):
        self.__secret_number = secret_num


    def turn_on(self):
        print("== start game ==")
        while True:
            print("What would you like to do? \n1: Go Shop \n2: Play Game\n3: get secret number\n4: set secret number\n0: Exit\n")
            answer = input("Input: ")
            if answer == "1":
                self.go_shop()

            elif answer == "2":
                self.play_game()

            elif answer == "3":
                print(self.secret_number)
           
            elif answer == "4":
                new_secret_number = input("새로운 secret number를 입력하세요: ")
                self.secret_number = new_secret_number
                print("변경완료")

            elif answer == "0":
                break

            else:
                print('입력값에 문제가 있습니다.')
        print("-------------------")
        print("== end game ==")

    def go_shop(self):
        if not self.money :
            print("돈이 없습니다 게임을 플레이하여 돈을 벌어오세요")
        else:
            self.money -= 10
            self.item += 1
            print("돈 10을 사용하고 아이템 1개를 얻었다! 남은 돈 :{}, 아이템 수: {}".format(self.money, self.item))


    def play_game(self):
        print("게임을 플레이중입니다...")
        time.sleep(1)
        get_money = random.choice([5, 10, 15, 20, 50])
        self.money += get_money
        print("게임완료 \n 획득한 돈 : {}\n 소유한 돈: {}".format(get_money, self.money))


if __name__ == "__main__":    
    p1 = Player('siwa', 1221)
    p1.turn_on()
     
