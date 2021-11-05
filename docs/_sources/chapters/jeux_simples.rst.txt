Jeux d'arcade simples
=====================

Les collisions
--------------

Dans les jeux d'arcade, il est important de savoir quand un acteur sprite est entré en collision avec un autre acteur sprite. La majorité de ce code est copié de
:numref:`code-moving_boxes` et de
:numref:`code-keyboard_input`.

.. literalinclude:: programs/15_collisions.py
   :caption: Collisions
   :name: code-collisions
   :linenos:



.. topic:: Exercice

   Ajoutez du mouvement vertical (comme vous avez fait dans l'exercice :numref:`code-keyboard_input`).


.. topic:: Pour les plus avancés

   Créez une boite qui pourchasse l'extraterrestre.


.. topic:: Pour les plus avancés

    Affichez le nombre de fois que la boite entre en collision avec l'extraterrestre (par exemple le pointage).




Pourchasser
-----------

Au lieu de bouger constamment vers la droite, on peut rendre le mouvement conditionnel avec une déclaration ``if``. Ainsi, on peut faire en sorte que la boite pourchasse l'extraterrestre. La plupart du code a été copié de :numref:`code-collisions`. Les lignes qui ont été nouvellement ajoutées sont surlignées. Nous avons aussi modifié ce qui arrive lorsque la boite entre en contact avec l'extraterrestre: le programme termine et vous devez le relancer pour jouer à nouveau. Ceci n'est peut-être pas ce que vous voulez dans votre jeu, mais nous allons pouvoir modifier le programme plus tard.

.. literalinclude:: programs/15b_chase.py
   :emphasize-lines: 18-23
   :caption: Pourchasseur d'extraterrestres
   :name: code-chase
   :linenos:



.. topic:: Exercice

   Ajoutez du mouvement vertical (comme vous avez fait dans l'exercice précédent).


.. topic:: Pour les plus avancés

   Créez un nouvel acteur sprite. Enregistrez son image avec le nom `ennemi.png` dans votre fichier `code/images`. Chargez l'image avec `Actor('ennemi')` au lieu de `Rect()`.




Augmentation de puissance
-------------------------

Au lieu d'être un ennemi, la boite ici est une augmentation de puissance. Lorsque le joueur entre en contact avec la boite, elle disparait et réapparait dans un nouvel emplacement.

.. literalinclude:: programs/15c_powerup.py
   :caption: Collectionner les augmentations de puissance
   :name: code-powerup
   :linenos:



.. topic:: Exercice

   Ajoutez du mouvement vertical (comme vous avez fait dans l'exercice \ref{exercise:updown}).




.. topic:: Exercice

   Affichez une image pour représenter votre nouvelle augmentation de puissance. Enregistrez-le sous le nom de `powerup.png` dans votre fichier `code/images`. Chargez l'image avec `Actor('powerup')` au lieu de `Rect()`.


.. topic:: Pour les plus avancés

   Combinez ce programme avec l'ennemi du programme :numref:`code-chase` et l'arrière-plan de :numref:`code-background`. De plus, ajoutez n'importe quel autre élément qui vous intéresse afin de créer votre propre jeu.




Sons et animation
-----------------

Pygame Zero est livré avec une autre image ``alien_hurt.png`` et un son ``eep.wav``. Si vous voulez avoir plus de sons ou d'image, vous allez devoir les ajouter dans les fichiers ``sounds`` pour vos sons et ``images`` pour vos images.

La plupart de ce code a été copié de
:numref:`code-collisions`

.. literalinclude:: programs/16_collisions2_sound_animation.py
   :emphasize-lines: 19-24
   :caption: Sons et animation lorsqu'il y a collision
   :name: code-collisions2
   :linenos:



.. topic:: Exercice

   Enregistre ton propre effet sonore et ajoute-le au jeu.


.. topic:: Pour les plus avancés

   Ajoutez plus de boites ou de sprites qui se déplacent dans différentes directions. Faites en sorte que le joueur doit éviter ces objets.


.. topic:: Pour les plus avancés

   Ajoutez un second extraterrestre qui est contrôlé par des touches différentes ou par une manette afin de permettre à un autre joueur de jouer.




Les boutons de la souris
------------------------

Ceci utilise une fonction *call-back* pour capter des évènements. C'est similaire à :numref:`code-collisions2`, mais:

-  La boite a été retirée.
-  Il y a une fonction ``on_mouse_down()`` qui est appelée automatiquement lorsque le joueur appuie sur le bouton de la souris.
-  Le pointage est affiché.

Voir :numref:`code-functions` pour plus d'informations sur les fonctions.

.. literalinclude:: programs/17_mouse_input.py
   :caption: Capter les boutons de la souris
   :name: code-mouse_input
   :linenos:





Le déplacement de la souris
---------------------------

.. literalinclude:: programs/18_mouse_movement.py
   :caption: Capter les mouvements de la souris
   :name: code-mouse_movement
   :linenos:



.. topic:: Exercice

   Qu'est-ce qui arrive lorsqu'on remplace la ligne 8 par ceci::

        animate(alien, pos=pos, duration=1, tween='bounce_end')



.. topic:: Exercice

   Qu'est-ce qui arrive lorsqu'on change `on_mouse_move` avec `on_mouse_down`?


.. topic:: Pour les plus avancés

   Créez un jeu avec un premier extraterrestre qui est contrôlé par la souris et second extratérestre qui est contrôlé par les touches du clavier.
