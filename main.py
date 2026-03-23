
# import pygame, sys, random, time
# from pygame.locals import *
# from operator import truediv
# from zoneinfo import available_timezones
#
# # comment
#
#
# # print("Hello World!")
# #
# # door_open = True
# # name = "Alfie"
# # print(name)
# #
# #
# # price = 20
# # price *= 1.2
# # print(price)
#
# # name = "Alfie"
# # age = 80
# # height = 1.89
# # sentence = "Hello World" + "I am: %s "
# # print("Hello World" + "I am: %s, my age is %d, and I am %f cm tall." %(name, age, height))
# #
# # print("My name is {}, My age is {}, and I am {} cm tall".format(name, age, height))
# #
# # print(name[0])
# # print(name[0:1])
# # print(name[0:2])
# # print(name[0:3])
# # print(name[0:4])
# #
# # print(len(sentence))
#
#
# # name = input("What is your name?")
# # print("Hello, " + name)
# # age = input("How old are you? ")
#
#
# # number = int(input("Give me a big number"))
# # final_number = 5+number
# # if final_number <= 100:
# #     print("That's a small number!")
# # elif final_number <= 1000:
# #     print("That's not a big number yet!")
#
# # Session 3
#
# # Session 3 Task One
# # usr_input = input("Give me a few numbers / using spaces between them:")
# # new_list = []
# #
# # list_from_inp = usr_input.split()
# # for j in list_from_inp:
# #     if int(j) % 2 == 1:
# #         new_list.append(j)
# #     print(new_list)
#
# # Session 3 Tuple Task (remove empty from tuple list)
# # tupleList = [(), (), (''), ('a','b'), ('a', 'b', 'c'), ('d')]
# # for i in tupleList[:]:
# #     if not i:
# #         tupleList.remove(i)
# #
# #     print(tupleList)
#                                 # DICTIONARIES
#     # weaponsList = {"Axe": 45, "Sword": 120, "Dagger": 35}
#     #
#     # print(weaponsList["Sword"])
#     # weaponsList["Sword"] = 200
#     # print(weaponsList)
#
# # myDict = ({"Name": "A", "Age": "150"})
# # print(myDict)
# #
# # spellList= ({"Fireball": "50", "Thunder": "60", "Fissure": "100"})
# #
# # print(spellList["Fireball"])
# # spellList["Fireball"] = 200
# # print(spellList)
# # removedItem = spellList.pop("Fireball")
#
# # available_items = {"health potion": 10, "cake": 5, "green elixir": 20, "lombas bread": 25, "bogweed": 15, "rabbit stew":30}
# # health_points = 20
# #
# # print(available_items)
# # health_points += available_items.pop("health potion", 10)
# # print(health_points)
# #
# # for key, value in available_items.items():
# #     print(key, value)
# #
# #     for key in sorted(available_items.keys()):
# #         print(key, available_items[key])
#
# # tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Heirophant", 6: "The Lovers", 7: "The Chariot", 8:"Strength", 9: "The Hermit", 10: "Wheel of Fotune", 11: "Justice", 12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star", 18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}
# #
# # fortune = {}
# # fortune["past"] = "Tower"
# # print(fortune)
# #
# # fortune["Past"] = tarot.pop(13)
# # fortune["Present"] = tarot.pop(22)
# # fortune["Future"] = tarot.pop(10)
# #
# # for key in fortune:
# #     print(fortune[key])
#
# pygame.init()
# pygame.display.set_caption("My first Pygame program")
# screen = pygame.display.set_mode((1080, 700))
# screen_w, screen_h = pygame.display.get_surface().get_size()
#
#
#
#
# def move(self):
#     if pressed_key[K_RIGHT]:
#         self.x += 4
#         if self.x > screen_w - 120:
#             self.x = screen_w -120
#             if pressed_key[K_LEFT]:
#                 self.x += 4
#                 if self.x <= 0:
#                     self.x = 0
#
# class Raindrops:
#     def __init__(self, x, y):
#
#
#
#
#
#
# def rain(self):
#     rain.append(Raindrops(random.randint(self.x+100, self.x + 500), self.y+200))

