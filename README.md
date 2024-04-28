# Générateur de Combinaisons de Numéros

<img width="382" alt="2024-04-28_18-02-11" src="https://github.com/BreakingTechFr/Generateur_de_Combinaisons_de_numeros/assets/128238555/d4e6158a-ee8a-418b-a789-764adfc251a8">

Ce script Python permet de générer toutes les combinaisons possibles à partir d'un numéro initial contenant des chiffres inconnus représentés par des 'X'. Les combinaisons peuvent être générées dans différents formats de sortie tels que le texte brut, le CSV ou le JSON.

## Prérequis
Avant d'exécuter ce script, assurez-vous d'avoir Python 3.11.9 installé sur votre système. De plus, les bibliothèques suivantes doivent être installées :

tkinter
PIL (Python Imaging Library)
itertools
csv
json
threading
multiprocessing
Installation

## Utilisation
1. Assurez-vous d'avoir installé les dépendances requises en exécutant :
```shell
pip install -r requirements.txt
```
2. Exécutez le script en exécutant la commande :
```shell
python numero.py
```
3. Entrer le numéro initial : Saisissez le numéro initial dans le champ prévu à cet effet. Utilisez 'X' pour représenter les chiffres inconnus.
4. Choisir le format de sortie : Sélectionnez le format de sortie souhaité parmi les options disponibles (texte, CSV ou JSON).
5. Générer les combinaisons : Cliquez sur le bouton "Générer" pour démarrer le processus de génération des combinaisons.
Consulter le résultat : Une fois le processus terminé, un message de succès s'affichera, et le fichier de sortie sera créé dans le répertoire du script.

### Remarques
Liste de confidentialité des numéros de téléphone (Accord. Sites Web)
J'ai décidé de créer une liste de sites Web bien connus sur lesquels les gens s'inscrivent souvent et j'ai examiné de plus près leurs processus de réinitialisation de mot de passe. Mon objectif était de découvrir quels sites Web nécessitaient uniquement votre adresse e-mail pour démarrer le processus, lesquels prenaient en charge la réinitialisation du mot de passe sur mobile et combien de chiffres de votre numéro de téléphone avaient été révélés au cours du processus. Voici une partie de la liste que j'ai trouvée :

eBay (trois premiers et deux derniers chiffres)
Amazon (trois premiers et deux derniers chiffres)
Airbnb (trois premiers et deux derniers chiffres)
LinkedIn (trois premiers et deux derniers chiffres)
Airbnb (trois premiers et deux derniers chiffres)
Walmart (trois premiers et deux derniers chiffres) deux derniers chiffres)
Dropbox (trois premiers et deux derniers chiffres)
Vimeo (trois premiers et deux derniers chiffres)
Pinterest (trois premiers et deux derniers chiffres)
Evernote (trois premiers et deux derniers chiffres)
Quora (trois premiers et deux derniers chiffres)
TripAdvisor (trois premiers et deux derniers chiffres)
GoDaddy (trois premiers et deux derniers chiffres)
Slack (trois premiers et deux derniers chiffres)
Vimeo (trois premiers et deux derniers chiffres)
Zillow (trois premiers et deux derniers chiffres)
Pandora (trois premiers et deux derniers chiffres) deux chiffres)
Etsy (trois premiers et deux derniers chiffres)
Hulu (trois premiers et deux derniers chiffres)
Salesforce (trois premiers et deux derniers chiffres)
SoundCloud (trois premiers et deux derniers chiffres)
Uber (trois premiers et deux derniers chiffres)
Salesforce ( trois premiers et deux derniers chiffres)

PayPal ( premier et quatre derniers chiffres )
Microsoft ( premier et quatre derniers chiffres )
Apple ( premier et quatre derniers chiffres )
Netflix ( premier et quatre derniers chiffres )
Adobe ( premier et quatre derniers chiffres )
Spotify ( premier et quatre derniers chiffres )
Snapchat ( premier et quatre derniers chiffres )
Reddit ( premier et quatre derniers chiffres )

Yahoo ( premier et deux derniers chiffres )
Instagram ( premier et deux derniers chiffres )
Dropbox ( premier et deux derniers chiffres )
Tumblr ( premier et deux derniers chiffres )
Reddit ( premier et deux derniers chiffres )

LastPass ( quatre derniers chiffres )
GitHub ( quatre derniers chiffres )
Bitbucket ( quatre derniers chiffres )
Trello ( quatre derniers chiffres )
Evernote ( quatre derniers chiffres )

Google ( deux derniers chiffres )
Facebook ( deux derniers chiffres )
Twitter ( deux derniers chiffres )
Hotmail ( deux derniers chiffres )
Steam ( deux derniers chiffres )

Par exemple, si vous avez des comptes à la fois sur eBay et LastPass, un attaquant pourrait potentiellement découvrir sept des dix chiffres de votre numéro de téléphone, simplement en connaissant votre adresse e-mail. En termes plus simples, votre adresse e-mail peut aider un attaquant à réduire les possibilités de deviner votre numéro de téléphone d'un milliard d'options à seulement mille.

## Suivez-nous

- [@breakingtechfr](https://twitter.com/BreakingTechFR) sur Twitter.
- [Facebook](https://www.facebook.com/BreakingTechFr/) likez notre page.
- [Instagram](https://www.instagram.com/breakingtechfr/) taguez nous sur vos publications !
- [Discord](https://discord.gg/VYNVBhk) pour parler avec nous !
