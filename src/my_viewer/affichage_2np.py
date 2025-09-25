import sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets

def affiche_deux_images(img1: np.ndarray, img2: np.ndarray, titre: str = "Affichage de deux images numpy"):
    """
    Affiche côte à côte deux images numpy (mêmes dimensions, niveaux de gris 8 bits) dans une fenêtre pyqtgraph.
    img1, img2 : np.ndarray 2D (uint8)
    titre : titre de la fenêtre
    """
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    win = QtWidgets.QWidget()
    main_layout = QtWidgets.QVBoxLayout(win)
    images_layout = QtWidgets.QHBoxLayout()
    main_layout.addLayout(images_layout)

    # Création de deux ImageView sans histogramme, ROI ni boutons
    view1 = pg.ImageView(view=pg.PlotItem())
    view2 = pg.ImageView(view=pg.PlotItem())

    # Suppression de l'histogramme, du ROI et des boutons
    for view in (view1, view2):
        view.ui.histogram.hide()
        view.ui.roiBtn.hide()
        view.ui.menuBtn.hide()

    # Synchronisation des vues (zoom/déplacement)
    vb1 = view1.getView()
    vb2 = view2.getView()
    vb1.setXLink(vb2)
    vb1.setYLink(vb2)

    view1.setImage(img1)
    view2.setImage(img2)

    images_layout.addWidget(view1)
    images_layout.addWidget(view2)

    # Label pour afficher les coordonnées du pixel en haut à gauche
    coord_label = QtWidgets.QLabel()
    main_layout.addWidget(coord_label)

    def update_label():
        # On prend la vue de view1 (elles sont synchronisées)
        vb = view1.getView()
        # Limites de la vue (rect visible)
        rect = vb.viewRect()
        if rect is not None:
            x = int(rect.left())
            y = int(rect.top())
            # On s'assure que les coordonnées sont dans l'image
            x = max(0, min(x, img1.shape[1]-1))
            y = max(0, min(y, img1.shape[0]-1))
            coord_label.setText(f"Pixel en haut à gauche affiché : (x={x}, y={y})")
        else:
            coord_label.setText("")

    # Connecte le signal de changement de vue
    view1.getView().sigRangeChanged.connect(lambda *args: update_label())
    update_label()

    win.setWindowTitle(titre)
    win.resize(900, 400)
    win.show()

    # Si on est dans un script principal, on lance la boucle Qt
    if not QtWidgets.QApplication.instance().startingUp():
        sys.exit(app.exec_())

# Exemple d'utilisation (à supprimer ou commenter si importé comme module)
if __name__ == "__main__":
    img1 = np.random.randint(0, 256, (300, 400), dtype=np.uint8)
    img2 = np.random.randint(0, 256, (300, 400), dtype=np.uint8)
    affiche_deux_images(img1, img2)
