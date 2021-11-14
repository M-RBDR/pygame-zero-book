Boink!
======

Mettons en pratique ce que nous avons appris jusqu'à présent en créant un jeu classique. Nous allons programmer le jeu Boink! qui s'inspire fortement du jeu d'Atari intitulé Pong. Ce jeu est très simple. Il y a deux palettes qui sont aux deux extrémités de l'écran et une balle qui débute au centre de l'écran. L'objectif du jeu est d'utiliser une palette pour faire rebondir la balle dans le but de l'adversaire et, ainsi, gagner des points.

.. literalinclude:: programs/15_collisions.py
   :caption: Collisions
   :name: code-collisions
   :linenos:



.. topic:: Exercice

   Ajoutez du mouvement vertical (comme vous avez fait dans l'exercice :numref:`code-keyboard_input`).


.. topic:: Pour les plus avancés

   Créez une boite qui pourchasse l'extraterrestre.


Initializer Pygame Zero
-----------------------

Cette étape est seulement nécessaire si vous n'utilisez pas l'éditeur Thonny. Pour que votre code fonctionne, vous devez y ajouter une ligne d'importation au début et une fonction à la fin.

.. code:: python

   import pgzrun

   # insérez votre code de jeux entre ces deux lignes

   pgzrun.go()

Afficher les éléments du jeu à l'écran
--------------------------------------

Afin d'avoir une fenêtre de jeu, nous devons assigner des valeurs aux variables ``WIDTH`` et ``HEIGHT``. De plus, nous allons donner un titre à notre fenêtre par le biais de la variable ``TITLE``.

.. code:: python

   import pgzrun # Ne sera plus affiché dans les prochains exemples

   WIDTH = 800
   HEIGHT = 600
   TITLE = "Boink!"

   pgzrun.go() # Ne sera plus affiché dans les prochains exemples

Pour Boink!, nous allons seulement utiliser des ``Rect`` pour créer les éléments du jeu. Les Rect sont comme les éléments fondamentaux des sprites acteurs. Ils servent à encadrer les images des acteurs sur l'écran et, surtout, de gérer les colisions qu'il peut y avoir entre les acteurs.

Pour créer un Rect, nous avons besoin de deux points: le point en haut à gauche du rectangle et le point en bas à droite du rectangle. Ici, nous prenons la moitié des dimensions de l'écran et soustrayons la grandeur désirée du rectangle pour les premiers points. Pour les deuxièmes points, nous spécifions où ils vont se situer en fonction du premier point. Si nous prenons l'exemple de la balle, son deuxième point sera 20 unités en x et y du premier point.

.. code:: python

   WIDTH = 800
   HEIGHT = 600
   TITLE = "Boink!"

   balle = Rect((WIDTH / 2 - 10, HEIGHT / 2 - 10), (20, 20))
   joueur = Rect((WIDTH - 20, HEIGHT / 2 - 50), (10, 100))
   adversaire = Rect((10, HEIGHT / 2 - 50), (10, 100))


Affichons maintenant quelque chose à l'écran pour avoir une idée du jeu. Pour ce faire, nous devons utiliser la fonction ``draw()``. Cette fonction affiche à la surface d'affichage (le display surface en anglais). Cette surface est créée et gérée pour nous au travers de Pygame Zero. Pourtant, lorsqu'il est question des rectangles et de certaines autres formes géométriques, il est tout de même nécessaire de spécifier qu'on veut afficher à cette surface. Pour ce faire, nous utilisons les méthodes ou les fonctions de l'objet ``screen`` (écran en français).

.. code:: python

   def draw():
    screen.fill((20, 20, 20))
    screen.draw.filled_rect(balle, (200, 200, 200))
    screen.draw.filled_rect(joueur, (200, 200, 200))
    screen.draw.filled_rect(adversaire, (200, 200, 200))
    screen.draw.line((WIDTH / 2, 0),(WIDTH / 2, HEIGHT), (200, 200, 200))


Souvenez-vous qu'il est important de mettre ces fonctions dans un ordre qui ne fera pas cacher des éléments du jeu. C'est pourquoi nous avons débuté avec screen.fill() qui agit comme notre arrière-plan. Cette fonction prend trois arguments en tuple (dans une autre parenthèse). Ils représentent le montant de rouge, de vert et de bleu de la couleur que nous voulons afficher. La valeur minimale de ces arguments est de 0, ce qui représente l'absence d'une de ces couleurs, et la valeur maximale est de 255, ce qui représente la présence complète d'une de ces couleurs. Les prochaines fonctions, screen.draw.filled_rect(), servent à afficher des rectangles remplis à l'écran. Ces fonctions prennent comme argument un Rect (ceux que nous avons déjà créés) et une couleur dans un Tuple. La dernière fonction que nous appelons est la fonction screen.draw.line() qui nous permet d'afficher une ligne au milieu de l'écran. Cette fonction prend en argument les deux points de la ligne ainsi que la couleur du trait.

Avec ces lignes de code, nous avons un programme qui affiche les éléments de base de notre jeu. Il ne reste qu'à rendre notre programme interactif.

Mettre à jour les éléments du jeu
---------------------------------

Par où commencer lorsque nous voulons ajouter des éléments qui se déplacent dans notre jeu? Une bonne façon de répondre à ce genre de question est de réduire le problème en plus petits problèmes. Commençons par la balle de notre jeu.

Comme pour les autres projets de ce livre, nous devons mettre les éléments interactifs du programme dans la fonction ``update()``. Il serait donc utile de créer cette fonction et d'y ajouter les fonctionnalités de base de notre balle. La balle doit pouvoir rebondir des côtés de l'écran et des palettes de jeu. Si vous essayez de changer directement les valeurs de x ou y (la position), vous allez remarquer qu'il sera très difficile d'accomplir l'effet désiré. Nous devons donc créer deux nouvelles variables qui représentent le déplacement ou la vitesse en x et en y de la balle. Ainsi, si la balle entre en contact avec les marges de l'écran ou avec un autre élément du jeu, il sera possible, avec ces nouvelles variables, de renverser la valeur de la position de la balle pour créer l'effet de rebond. Ajoutons donc ces variables en dessous de la création de nos rectangles.

.. code:: python

   balle = Rect((WIDTH / 2 - 10, HEIGHT / 2 - 10), (20, 20))
   joueur = Rect((WIDTH - 20, HEIGHT / 2 - 50), (10, 100))
   adversaire = Rect((10, HEIGHT / 2 - 50), (10, 100))

   # Variables du jeu
   balle_dx = 5
   balle_dy = 5

Nous nommons ces variables avec le suffixe dx et dy afin de rendre plus évident que ces variables gèrent le déplacement de la balle sur l'axe des x et sur l'axe des y. Une fois ces variables créées, nous pouvons les utiliser dans la fonction update() pour gérer le mouvement de la balle. Il suffit d'ajouter la valeur des variables dx et dy à la position de la balle.

.. code:: python

   # Ce code ne fonctionne pas
   def update():
          balle.x += balle_dx
          balle.y += balle_dy

Comme souligner dans le commentaire, ce code nous donne une erreur. La raison de cette erreur est que nous assignons de nouvelles valeurs à balle_dx et à balle_dy dans update() et Python ne comprend pas que ces variables existent déjà (même si nous avons défini nos variables à l'extérieur des fonctions). Ceci est dû au fait que les variables définies dans les fonctions sont spécifiques à ces fonctions. Il faut dire à Python qu'on parle des variables globales qui sont à l'extérieur des fonctions. En somme, Python croit que ces variables sont spécifiques à la fonction update() et ne comprend pas pourquoi nous n'avons pas initialisé ces variables en écrivant balle_dx = 5 et balle_dy = 5. Pour indiquer à Python qu'on veut utiliser les variables qui sont à l'extérieur des fonctions, il faut ajouter le terme ``global``.

.. code:: python

   # Ce code fonctionne
   def update():
          global balle_dx, balle_dy
          balle.x += balle_dx
          balle.y += balle_dy

Avec ce code, notre balle se déplace. Toutefois, elle ne rebondit pas. Il nous faut donc vérifier lorsque la balle fait une collision avec les marges de l'écran avec des fonctions if. Nous pouvons utiliser les valeurs top, bottom, left et right du rectangle de la balle pour faire la comparaison avec la grandeur (WIDTH) et la hauteur de l'écran (HEIGHT). Lorsqu'il y a collision, il nous suffit d'inverser la variable dx ou dy afin de faire le rebond. Ceci est fait en multipliant la valeur de ces variables par -1.

.. code:: python

   def update():
          global balle_dx, balle_dy
          balle.x += balle_dx
          balle.y += balle_dy

          if balle.top <= 0 or balle.bottom >= HEIGHT:
               balle_dy *= -1 # équivalent à balle_dy = balle_dy * -1
          if balle.left <= 0 or balle.right >= WIDTH:
               balle_dx *= -1

Nous allons ajouter une dernière vérification afin de savoir si la balle fait une collision avec le joueur ou l'adversaire. Pygame Zero nous facilite un peu le travail lorsqu'il est question de savoir si un Rect entre en collision avec un autre Rect. En effet, on peut utiliser la méthode (une fonction d'un objet) colliderect() afin de savoir s'il y a collision entre deux Rect.

.. code:: python

   def update():
          global balle_dx, balle_dy
          balle.x += balle_dx
          balle.y += balle_dy

          if balle.top <= 0 or balle.bottom >= HEIGHT:
               balle_dy *= -1 # équivalent à balle_dy = balle_dy * -1
          if balle.left <= 0 or balle.right >= WIDTH:
               balle_dx *= -1

          if balle.colliderect(joueur) or balle.colliderect(adversaire):
               balle_dx *= -1

Si vous lancez le programme, vous allez voir une balle qui rebondit partout. Félicitation, vous avez réussi à résoudre un des petits problèmes de notre code.

Maintenant, si on regarde notre fonction update(), on y voit beaucoup de code qui est spécifique à la gestion de notre balle. Notre code est fonctionnel, mais peu structuré. La structure est importante en programmation pour faciliter la compréhension de votre code à d'autres programeurs. Elle sert aussi à faciliter la gestion de votre programme. Pour organiser notre code, mettons tout le code de la balle dans sa propre fonction et appelons cette fonction dans update().

.. code:: python

   def mouvement_balle():
          global balle_dx, balle_dy
          balle.x += balle_dx
          balle.y += balle_dy

          if balle.top <= 0 or balle.bottom >= HEIGHT:
               balle_dy *= -1 # équivalent à balle_dy = balle_dy * -1
          if balle.left <= 0 or balle.right >= WIDTH:
               balle_dx *= -1

          if balle.colliderect(joueur) or balle.colliderect(adversaire):
               balle_dx *= -1

   def update():
          mouvement_balle()


Saisie du clavier
-----------------

Tout comme pour la fonction mouvement_balle(), mettons le code pour gérer le joueur dans sa propre fonction.

.. code:: python

   def mouvement_joueur():


   def update():
          mouvement_balle()
          mouvement_joueur()

Afin de déplacer le joueur, nous pouvons utiliser les variables de déplacement déjà définies par Pygame Zero.

.. code:: python

   def mouvement_joueur():
          if keyboard.up:
               joueur.y -= joueur_vitesse
          if keyboard.down:
               joueur.y += joueur_vitesse

   def update():
          mouvement_balle()
          mouvement_joueur()

En utilisant ``keyboard``, on peut saisir la touche du clavier qui a été appuyé par l'utilisateur du programme. Lorsque la touche haut est appuyée (la flèche du haut sur le clavier), nous déplaçons le joueur vers le haut de l'écran en fonction de sa vitesse grâce à ``joueur.y -= joueur_vitesse``. On fait de même pour la touche bas avec ``joueur.y += joueur_vitesse``. Nous ne devons pas utiliser le mot-clé ``global`` puisque nous n'assignons pas une  nouvelle valeur à joueur_vitesse. Python détecte automatiquement qu'on veut utiliser la valeur globale.

Nous avons un nouveau problème. Le joueur peut quitter l'écran. Pour le limiter à l'espace de jeu, nous pouvons utiliser la même technique que nous avons utilisée avec la balle.

.. code:: python

   def mouvement_joueur():
          if keyboard.up:
               joueur.y -= joueur_vitesse
          if keyboard.down:
               joueur.y += joueur_vitesse

          if joueur.top <= 0:
               joueur.top <= 0
          if joueur.bottom >= HEIGHT:
               joueur.bottom = HEIGHT

   def update():
          mouvement_balle()
          mouvement_joueur()

En utilisant le Rect du joueur, nous pouvons faciliter la détection de la sortie de ce dernier grâce aux variables de l'objet ``top`` et ``bottom``. Si nous dépassons les marges de l'écran, nous donnons la valeur de ``0`` (le haut de l'écran) ou de ``HEIGHT`` (le bas de l'écran) à top (le haut du rectangle du joueur) ou bottom (le bas du rectangle du joueur) respectivement.

Nous avons maintenant une balle qui rebondit et un joueur qui peut se déplacer. Ajoutons un adversaire.

Ajouter un adversaire
---------------------

Créons d'abord la fonction pour gérer l'adversaire.

.. code:: python

   def mouvement_adversaire():


   def update():
          mouvement_balle()
          mouvement_joueur()
          mouvement_adversaire()

Faisons en sorte que l'adversaire suit simplement la balle en fonction de sa vitesse.

.. code:: python

   def mouvement_adversaire():
          if adversaire.top < balle.y:
               adversaire.top += adversaire_vitesse
          if adversaire.bottom > balle.y:
               adversaire.bottom -= adversaire_vitesse

   def update():
          mouvement_balle()
          mouvement_joueur()
          mouvement_adversaire()

Ce code, qui est très similaire au code pour maintenir les éléments du jeu dans l'espace de jeu, fait en sorte que l'adversaire suit la balle. Si on veut un adversaire plus difficile, on peut augmenter la valeur de la vitesse de l'adversaire. Inversement, si on veut un adversaire plus facile, on peut diminuer cette même valeur.

Règles du jeu
-------------

Pour simuler un but, nous pouvons simplement changer le code de la fonction mouvement_balle() pour que la balle se fasse replacer au centre de l'écran.

.. code:: python

   def mouvement_balle():
          global balle_dx, balle_dy
          balle.x += balle_dx
          balle.y += balle_dy

          if balle.top <= 0 or balle.bottom >= HEIGHT:
               balle_dy *= -1 # équivalent à balle_dy = balle_dy * -1
          if balle.left <= 0 or balle.right >= WIDTH:
               balle.center = (WIDTH / 2, HEIGHT / 2)

          if balle.colliderect(joueur) or balle.colliderect(adversaire):
               balle_dx *= -1

   def update():
          mouvement_balle()

Généralement, il est préférable de mettre ce genre de déplacement d'object dans sa propre fonction puisque souvent nous voulons ajouter d'autres étapes après le déplacement. Aussi, il est plus simple de retrouver cette règle du jeu si elle se trouve dans sa propre fonction.

.. code:: python

   def replacer_balle():
          balle.center = (WIDTH / 2, HEIGHT / 2)

   def mouvement_balle():
          global balle_dx, balle_dy
          balle.x += balle_dx
          balle.y += balle_dy

          if balle.top <= 0 or balle.bottom >= HEIGHT:
               balle_dy *= -1 # équivalent à balle_dy = balle_dy * -1
          if balle.left <= 0 or balle.right >= WIDTH:
               replacer_balle()

          if balle.colliderect(joueur) or balle.colliderect(adversaire):
               balle_dx *= -1

   def update():
          mouvement_balle()


Régler une bogue
----------------

Si vous jouez assez longtemps, vous allez remarquer que votre balle peut rester prise dans une des raquettes du jeu. Ceci est causé par notre code qui, lorsque la balle entre en collision avec un autre élément du jeu, ne positionne pas la balle à sa position originale. On ne fait qu'inverser sa valeur de vitesse en x. Ainsi, si la position de la balle est déjà à l'intérieur d'une des raquettes, la balle restera prise. Pour corriger ceci, nous devons replacer la balle à une position à l'extérieur des raquettes.


.. code:: python

   def replacer_balle():
          balle.center = (WIDTH / 2, HEIGHT / 2)

   def mouvement_balle():
          global balle_dx, balle_dy

          ancien_x = balle.x

          balle.x += balle_dx
          balle.y += balle_dy

          if balle.top <= 0 or balle.bottom >= HEIGHT:
               balle_dy *= -1 # équivalent à balle_dy = balle_dy * -1
          if balle.left <= 0 or balle.right >= WIDTH:
               replacer_balle()

          if balle.colliderect(joueur) or balle.colliderect(adversaire):
               balle.x = ancien_x
               balle_dx *= -1

En nous souvenant de notre ancienne position avec la variable ``ancien_x`` et en utilisant cette variable pour remettre la position du Rect de la balle lorsqu'on entre en collision avec le joueur ou l'adversaire, nous réglons notre bogue.

Avec cette modification, nous avons un jeu qui est techniquement complet. Toutefois, il y a de nombreuses améliorations qu'on pourrait faire. Selon vous, quelles améliorations pourrait-on faire pour améliorer notre programme?

Voici le code complet du jeu jusqu'à présent:

.. code:: python

   import pgzrun

   WIDTH = 800
   HEIGHT = 600
   TITLE = "Boink!"

   balle = Rect((WIDTH / 2 - 10, HEIGHT / 2 - 10), (20, 20))
   joueur = Rect((WIDTH - 20, HEIGHT / 2 - 50), (10, 100))
   adversaire = Rect((10, HEIGHT / 2 - 50), (10, 100))

   balle_dx = 5
   balle_dy = 5

   joueur_vitesse = 6

   adversaire_vitesse = 6

   def replacer_balle():
          balle.center = (WIDTH / 2, HEIGHT / 2)

   def mouvement_balle():
          global balle_dx, balle_dy

          ancien_x = balle.x

          balle.x += balle_dx
          balle.y += balle_dy

          if balle.top <= 0 or balle.bottom >= HEIGHT:
               balle_dy *= -1
          if balle.left <= 0 or balle.right >= WIDTH:
               replacer_balle()

          if balle.colliderect(joueur) or balle.colliderect(adversaire):
               balle.x = ancien_x
               balle_dx *= -1

   def mouvement_joueur():
          if keyboard.up:
               joueur.y -= joueur_vitesse
          if keyboard.down:
               joueur.y += joueur_vitesse

          if joueur.top <= 0:
               joueur.top = 0
          if joueur.bottom >= HEIGHT:
               joueur.bottom = HEIGHT

   def mouvement_adversaire():
          if adversaire.top < balle.y:
               adversaire.top += adversaire_vitesse
          if adversaire.bottom > balle.y:
               adversaire.bottom -= adversaire_vitesse

   def update():
          mouvement_balle()
          mouvement_joueur()
          mouvement_adversaire()

   def draw():
         screen.fill((20, 20, 20))
         screen.draw.filled_rect(balle, (200, 200, 200))
         screen.draw.filled_rect(joueur, (200, 200, 200))
         screen.draw.filled_rect(adversaire, (200, 200, 200))
         screen.draw.line((WIDTH / 2, 0),(WIDTH / 2, HEIGHT), (200, 200, 200))

   pgzrun.go()


.. topic:: Pour les plus avancés

   Ajoutez un pointage au milieu de l'espace de jeu et faites en sorte qu'après un certain nombre de points, la partie se termine.

.. topic:: Pour les plus avancés

   Ajoutez un chronomètre au début du jeu de 3 secondes afin de donner du temps au joueur pour se préparer à la prochaine manche.

.. topic:: Pour les plus avancés

   Ajoutez des images pour représenter la balle et les palettes.

.. topic:: Pour les plus avancés

   Ajoutez des sons et de la musique au jeu.
