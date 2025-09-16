# visualiseur d'images
## Description
Un visualiseur d'images en python, permettant de comparer le contenu de deux images, exprimées en tableaux numpy (H,W,1), en niveau de gris.
On doit pouvoir zoomer et se déplacer simultanément dans les images afin de comparer des détails.
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