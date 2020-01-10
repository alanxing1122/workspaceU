import random
def jdstb_game():
	computer = random.randint(1,3)

	player = input("1.剪刀、2.石头、3.布\t请输入对应的数字：")
	player = int(player)

	if(player not in [1,2,3]):
		print("请输入1、2、3")
	elif(computer == player):
		
		print("平局")
	elif((computer == 1 and player == 3)or(computer == 2 and player == 1)or(computer==3 and player==2)):
		print("电脑胜")
	else:
		print("玩家胜")


while(1):

	jdstb_game()
	
