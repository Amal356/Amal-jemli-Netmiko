Mon Projet Netmiko

I. Initialiser un dépôt Git local
- `git init -b main`

II. Ajouter et commiter des fichiers
- `echo Mon Projet Netmiko > README.md`
- `git add README.md`
- `git commit -m "Ajout du fichier README"`
- `echo print("Hello, Git!") > main.py`
- `git add main.py`
- `git commit -m "Ajout du script Python principal"`

III. Créer et fusionner des branches
- `git checkout -b feature/netmiko`
- Modifier `main.py` pour ajouter `acces_netmiko` et `dire_bonjour`
- `git add main.py`
- `git commit -m "Ajout de la fonction acces_netmiko"`
- `git checkout main`
- `git merge feature/netmiko`
- `git log --oneline --decorate --graph --all`

IV. Travailler avec un dépôt distant sur GitHub
- Créer le dépôt GitHub `prenom-nom-netmiko`
- `git remote add origin https://github.com/<votre-utilisateur>/prenom-nom-netmiko.git`
- `git push -u origin main`
- Créer sur GitHub la branche `feature/salut`
- `git fetch origin`
- `git checkout -b feature/salut origin/feature/salut`
- Modifier `main.py` pour ajouter `dire_salut` et l'appeler
- `git add main.py`
- `git commit -m "Ajout de la fonction dire_salut"`
- `git push origin feature/salut`
- Créer la Pull Request sur GitHub et la fusionner vers `main`
- `git checkout main && git pull`