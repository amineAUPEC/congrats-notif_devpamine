from win10toast import ToastNotifier
import json
import random
import time

notifier = ToastNotifier()


# Load and print achievements
def achievement():
    global achievements
    with open('1-common/xbox-achievements.json', encoding='utf-8') as json_file:
        achievements = json.load(json_file)
        for achievement in achievements:
            print(achievement['achievements'])

# Load and print encouragements
def encouragement():
    global encouragements
    with open('1-encouragement/encouragement.json', encoding='utf-8') as json_file:
        encouragements = json.load(json_file)
        for encouragement in encouragements:
            print(encouragement['msg'])

# Load and print musics for supra Sukriti and Prakriti KAKAR twins
def music_supra():
    global musics
    with open('1-music/1-music-supra.json', encoding='utf-8') as json_file:
        musics = json.load(json_file)
        for music in musics:
            print(music['track'])

# Randomly select and print an achievement and an encouragement
def notif():
    while True:
        random_achievement = random.choice(achievements)['achievements']
        random_encouragement = random.choice(encouragements)['msg']
        random_music=False 
        if random_music:
            random_music = random.choice(musics)['track']
            print(f"Random Achievement: {random_achievement}")
            print(f"Random Music: {random_music}")
            notifier.show_toast(f"{random_achievement}", f"{random_music}", duration=25, icon_path="assets/ico/dev_24012.ico")
            # time.sleep(random.randint(1, 10))  # Sleep for a random time between 30s and 5 minutes
            time.sleep(random.randint(30, 300))  # Sleep for a random time between 30 sec and 5 minutes
        else:
            print(f"Random Achievement: {random_achievement}")
            print(f"Random Encouragement: {random_encouragement}")
            notifier.show_toast(f"{random_achievement}", f"{random_encouragement}", duration=25, icon_path="assets/ico/dev_24012.ico")
            # time.sleep(random.randint(1, 10))  # Sleep for a random time between 30s and 5 minutes
            time.sleep(random.randint(30, 300))  # Sleep for a random time between 30s and 5 minutes

def main():
    achievement()
    encouragement()
    music_supra()
    notif()

if __name__ == "__main__":
    main()
