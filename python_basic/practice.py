# user_input_score = input("점수를 쉼표로 구분하여 입력하세요: ")
# score_list = user_input_score.split(",")

# print(score_list)

# total=0

# for score in score_list:
#     total += int(score)

# avg = total/len(score_list)
# print("입력한 점수들의 평균은: ", avg)

# fruits = ["apple", "banana", "cherry"]
# uppercase_fruit = []

# for fruit in fruits:
#     uppercase_fruit.append(fruit.upper())

# print(uppercase_fruit)

# fruits = ["apple", "banana", "cherry"]
# uppercase_fruits = [fruit.upper() for fruit in fruits]
# print(uppercase_fruits)

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [n**3 for n in numbers]
# print(squared_numbers)

# numbers = [10, 15, 20, 25, 30]
# filtered_numbers = [n for n in numbers if n > 20]
# print(filtered_numbers)

# fruits = ["banana", "apple", "cherry", "date"]
# fruits_with_a = [fruit for fruit in fruits if "a" in fruit]
# print(fruits_with_a)

# 중첩리스트

# people = [
#     ["철수", 20],
#     ["영희", 22],
#     ["민수", 19]
# ]

# print(people[0])
# print(people[1][0])

# numbers = [1, 2, 3]
# num2 = [4, 5, 6]
# num = numbers *3
# print(num)

# player_health = 10

# while player_health > 0:
#     print("플레이어 공격 받음!. 체력: ", player_health)
#     player_health -= 2
# print("Game Over! 플레이어의 체력이 모두 소진되었습니다.")

# turn = 0
# player_health = 10

# while player_health > 0:
#     turn += 1
#     if turn % 2 == 1:
#         continue
#     print("플레이어가 공격 받습니다! 턴: ", turn)
#     player_health -= 1

# print("플레이어 체력 소진, 게임 오버!")
