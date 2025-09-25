# visualiseur d'images
## Description
Un visualiseur d'images en python, permettant de comparer le contenu de deux images, exprimées par un tableaux numpy (H,W,1), en niveau de gris.
On peut zoomer et se déplacer de façon synchronisée dans les images afin de comparer des détails.
Les coordonnées dans les images du pixel en haut à gauche sont affichées.
## Installation
## Installation

Assurez-vous d’avoir [Poetry](https://python-poetry.org/) installé sur votre machine.

Clonez le dépôt, puis installez les dépendances :

```bash
git clone <url-du-repo>
cd my-viewer
poetry install
```

Pour lancer le projet dans un environnement virtuel Poetry :

```bash
poetry run python <nom_du_script_principal>.py
```