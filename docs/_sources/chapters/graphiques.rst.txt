Afficher des graphiques
=======================

Pour créer des graphiques pour nos jeux, nous allons utiliser la bibliothèque `Pygame Zero
<https://pygame-zero.readthedocs.io>`__. Pour comprendre quelles nouvelles fonctions vous sont disponibles, vous pouvez vous référer à la documentation disponible sur son site internet!

Le plus petit carré pouvant être affiché sur un moniteur s'appelle un *pixel*. Ce diagramme montre une vue rapprochée d'une fenêtre de 40 pixels de large et de 40 pixels de haut. À la taille normale, vous ne verrez pas les lignes de la grille.

.. figure:: images/figures/pixelgrid.png
   :alt: La disposition des pixels de votre écran

   La disposition des pixels de votre écran

On peut référer à n'importe quel pixel en donnant deux coordonnés: *(x,y)*. La coordonnée *x* est la position horizontale du pixel et la coordonnée *y* est la position verticale du pixel. Une particularité importante à prendre en compte est que l'origine de notre système de coordonnées se trouve en haut à droite de la fenêtre. Si *x* est positif, notre *pixel* se trouvera un peu plus vers la droite. Si *y* est positif, notre *pixel* se trouvera un peu plus vers le bas. Assurez-vous de bien comprendre ce que sont des coordonnés avant de continuer puisque tout ce qu'on va faire avec Pygame Zero va utiliser des coordonnés. En mathématique, on appelle ce système de coordonnés le 'système de coordonnées cartésiennes'.

Des lignes et des cercles
-------------------------

Si vous utilisez l'éditeur Thonny, Pygame Zero est déjà inclus, mais **tu dois te souvenir de sélectionner le 'Mode Pygame Zero' sous l'onglet 'Exécuter' avant de lancer ton programme**!

Si tu utilises un autre éditeur de texte, `des instructions générales se trouvent ici <https://pygame-zero.readthedocs.io/en/stable/ide-mode.html>`__.

.. literalinclude:: programs/10_lines_circles.py
   :caption: Des lignes et des cercles
   :name: code-lines_circles
   :linenos:



.. topic:: Exercice

   Complète cette image.


.. topic:: Exercice
   
   Crée ta propre image.



Bouger des rectangles
---------------------

Pour faire bouger les éléments qu'on affiche, on doit ajouter une fonction spéciale qui s'appelle ``update()``.
On n'a pas besoin d'écrire notre propre boucle puisque *Pygame Zero appelle cette fonction pour nous dans sa propre boucle*.

.. literalinclude:: programs/11_moving_boxes.py
   :caption: Bouger des rectangles
   :name: code-moving_boxes
   :linenos:



.. topic:: Exercice

   Faites bouger la boite plus rapidement.


.. topic:: Exercice

   Faites bouger la boite dans une autre direction.


.. topic:: Exercice

   Crée deux boites de différente couleur.




Les acteurs sprites
-------------------

Un ``acteur`` est tout personnage ou objet qu'on veut insérer dans notre jeu. Un ``sprite`` est l'image qu'on veut utiliser pour représenter l'acteur. Les acteurs sprites sont très similaires aux boites! Ils peuvent être déplacés tout comme une boite puisqu'ils ont aussi des coordonnées. Il est important de mentionner qu'``acteur`` doit s'écrire en anglais (``Actor``) lorsque vous l'utilisez dans votre code.
Dans votre système de fichier, trouvez le fichier où se trouve votre code, cliquez sur le dossier ``Images`` pour voir les divers fichiers d'images disponibles.
``extraterrestre.png`` devrait s'y trouver. Si vous voulez ajouter d'autres images à votre jeu, il faut les insérer dans le dossier ``Images``.

Vous pouvez utiliser plusieurs logiciels pour faire des sprites comme
`Krita <https://krita.org>`__ ou `Libresprite <https://libresprite.github.io/#!/>`__.

.. literalinclude:: programs/12_sprites.py
   :caption: Les acteurs sprites
   :name: code-sprites
   :linenos:



.. topic:: Exercice

   Dessinez ou téléchargez vos propres images (attention aux droits d'auteurs!) pour remplacer l'image ``extraterrestre.png``. Ensuite, utilisez cette nouvelle image dans votre code.




L'image d'arrière-plan
----------------------

Nous allons ajouter une image d'arrière-plan à
:numref:`code-sprites`

Clique sur le dossier ``Images`` pour voir les fichiers d'images disponibles.

**Tu dois créer ou télécharger (attention aux droits d'auteurs!) une image afin de l'afficher en arrière-plan.**
Sauvegarde l'image sous le nom ``arriereplan.png`` dans le dossier ``mu_code/images``. L'image devrait être la même largeur et longueur que la fenêtre de jeu, soit 500×500 pixels et doit être en format ``.png``.

.. literalinclude:: programs/12b_background.py
   :caption: Arrière-plan
   :name: code-background
   :linenos:



.. topic:: Exercice

    Crée une image afin de l'utiliser comme image d'arrière-plan. Enregistre l'image sous le nom `arriereplan.png`. Exécute le programme.




Saisie du clavier
-----------------

L'extraterrestre se déplace quand tu frappes sur les flèches de ton clavier.

.. literalinclude:: programs/13_keyboard_input.py
   :caption: Saisie du clavier
   :name: code-keyboard_input
   :linenos:



.. topic:: Exercice

   Faites en sorte qu'on puisse déplacer l'extraterrestre de haut en bas et de droite en gauche.


.. topic:: Exercice

   Utilisez l'opérateur += qui est plus concis pour modifier la valeur `extraterrestre.x` (voir :numref:`code-shortcuts`).


.. topic:: Exercice

    Utilise l'opérateur `or` pour permettre de déplacer l'extraterrestre avec les touches WASD ainsi qu'avec les flèches du clavier (voir :numref:`code-logic`).
