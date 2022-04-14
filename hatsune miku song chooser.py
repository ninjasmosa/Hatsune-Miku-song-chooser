import random
import time

songList = ["World is Mine", "Senbonzakura", "Freely Tomorrow", "Ievan Polkka", "Magical Girl and Chocolate", "Nyanyanyanyanyanyanya", "MikuMiku Ni Shiteageru", "Viva Happy", "From Y to Y", "Love Trial", "Miracle Paint", "Summer Idol", "HIBANA", "Worlds's End Dancehall", "Hibikase", "The Disappearence of Hatsune Miku", "Tell Your World", "Brand New Day", "Ohedo Julianight", "Assassin Princess", "Melt", "Nee Nee Nee", "Ai Dee", "Newly Edgy Idols", "Maison Hatsune"]
print("Hello. You have arrived at the Hatsune Miku song chooser.")
time.sleep(1)
print(" ")
randomSong = random.choice(songList)
print("The song I think you should listen to is " + randomSong)
time.sleep(1)
print("Have a nice day!")
