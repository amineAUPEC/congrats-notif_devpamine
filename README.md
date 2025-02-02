# congrats-notif_devpamine
The ultimate repo to get dopamine by a dev as a dev -  Aims to motivate and congrats dev - Xbox-achievements or Playstation like trophy
### Date : 01-02-2023
### Project Name : Devpamine => Congrats Notifs - Encouragement OR Music Notifs 🎉🎵

### Description : 
This code will send random notifications for support to give encouragement to the user. Developers, sysadmins, or other people might want to have some support or encouragement to keep going. It's like PlayStation trophies or Xbox achievement success. Some people like to have some support or encouragement to keep going. It will increase dopamine and motivation. 💪✨

#### Why this project? 🤔
This project is based on: ![Beat-5-Levels-Xbox-Achievements](https://www.kitguru.net/wp-content/uploads/2024/01/Beat-5-Levels-768x432.jpg)

A gif animation of Xbox achievement: 
![Achievements-Xbox](https://miro.medium.com/v2/resize:fit:640/format:webp/1*tF2NKWT2g3WB6qco60lKIg.gif)

Similar to PlayStation trophies or Xbox achievement success. 🏆🎮

---

#### Features :
- Send random notifications for support to give encouragement to the user.
    - Encouragement to keep going. 🚀
    - Encouragement to keep learning. 📚
    - Encouragement to keep coding. 💻
    - Encouragement to keep working. 🛠️
    - Encouragement to keep Infra working. 🌐
- Send random notifications for music to change music.
    - Music to keep going. 🎶
    - Music to keep learning. 🎧
    - Music to keep coding. 🎵
    - Music to keep working. 🎼

### Running
1. Git clone the project
1. Go to the app directory
1. Install from *requirements.txt*
```bash
pip install -r requirements.txt
```
1. Run the main.py file
```bash
python main.py
```
1. Ensure the JSON files are valid 
1. Ensure to set the **variable** `random_music=True` -> if you want to load music notifications. and False if you want to load encouragement notifications.
1. Set the **random** `time.sleep()`. 

1. Or **download** the exe and run it. 

---

### Pseudo-code :

1. I will import the JSON file *1-common/xbox-achievements.json* and *1-encouragement/encouragement.json*  
    1. And another version for music notifications to change music. 
1. Then I will iterate and print to debug each message/achievement.
1. I will iterate randomly and test notifications.
1. Every 2-5 minutes, a new notification will appear. ⏰
1. Start the script on `shell:startup` with the exe release.

---

### Structures : 
- README.md
- encouragement.json
- main.py <-- This code will send random notifications for support to give encouragement to the user.>
- requirements.txt

---

### Library : 
 - time
 - os
 - win10toast
 - random

---

### Building as exe : 
```powershell
pip install pyinstaller
pyinstaller --onefile main.py
 --hidden-import win10toast
 --add-data "1-encouragement/encouragement.json;."
 --add-data "1-common/xbox-achievements.json;."
 --add-data "1-music/1-music-supra.json;."
```

---

### Sources : 
[xboxachievements](https://www.xboxachievements.com/)
[tutorialspoint-win10toast](https://www.tutorialspoint.com/windows-10-toast-notifications-with-python)
[icons-icons-dev](https://icon-icons.com/fr/icone/dev/24012)
[learn-ms-adaptive-interative-toasts](https://learn.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts?tabs=xml)
[Windows10toast-Notifications-GeeksforGeeks](https://www.geeksforgeeks.org/windows-10-toast-notifications-with-python/)

### Feel free to contribute or give feedback. 💬
Any feedback is appreciated.
Any contribution is welcome.
If you make a Pull request to improve the code or share your JSON files for encouragement or music notifications, or if you add links or change the library, feel free to use it.

---

# FR Version 🇫🇷

### Date : 01-02-2023
### Nom du projet : Devpamine => Féliciter avec des Notifs - Notifications -> notif d'encouragement ou musicales 🎉🎵

### Description : 
Ce code enverra des notifications aléatoires pour soutenir et encourager l'utilisateur. Les développeurs, administrateurs système ou autres personnes peuvent vouloir recevoir du soutien ou des encouragements pour continuer. C'est similaire aux trophées PlayStation ou aux succès Xbox. Certaines personnes aiment recevoir du soutien ou des encouragements pour continuer. Cela augmentera la dopamine et la motivation. 💪✨

#### Pourquoi ce projet ? 🤔
Ce projet est basé sur : ![Beat-5-Levels-Xbox-Achievements](https://www.kitguru.net/wp-content/uploads/2024/01/Beat-5-Levels-768x432.jpg)

Une animation gif des succès Xbox : 
![Achievements-Xbox](https://miro.medium.com/v2/resize:fit:640/format:webp/1*tF2NKWT2g3WB6qco60lKIg.gif)

Similaire aux trophées PlayStation ou aux succès Xbox. 🏆🎮

---

#### Fonctionnalités :
- Envoyer des notifications aléatoires pour soutenir et encourager l'utilisateur.
    - Encouragement pour continuer. 🚀
    - Encouragement pour continuer à apprendre. 📚
    - Encouragement pour continuer à coder. 💻
    - Encouragement pour continuer à travailler. 🛠️
    - Encouragement pour maintenir l'infrastructure. 🌐
- Envoyer des notifications aléatoires pour changer de musique.
    - Musique pour continuer. 🎶
    - Musique pour continuer à apprendre. 🎧
    - Musique pour continuer à coder. 🎵
    - Musique pour continuer à travailler. 🎼

---

### Pseudo-code :

1. J'importerai le fichier json 1-common/xbox-achievements.json et 1-encouragement/encouragement.json  
    1. Et une autre version pour les notifications musicales pour changer de musique. 
1. Ensuite, j'itérerai et afficherai pour déboguer chaque message/succès.
1. J'itérerai de manière aléatoire et testerai les notifications.
1. Toutes les 2 à 5 minutes, une nouvelle notification apparaîtra. ⏰
1. Démarrer le script au démarrage du shell avec la version exe.

---

### Structures : 
- README.md
- encouragement.json
- main.py <-- Ce code enverra des notifications aléatoires pour soutenir et encourager l'utilisateur.>
- requirements.txt

---

### Bibliothèque : 
 - time
 - os
 - win10toast
 - random

---

### Construction en tant qu'exe : 
```powershell
pip install pyinstaller
pyinstaller --onefile main.py
 --hidden-import win10toast
 --add-data "1-encouragement/encouragement.json;."
 --add-data "1-common/xbox-achievements.json;."
```

