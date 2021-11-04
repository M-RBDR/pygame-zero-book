Jeux d'arcade
=============

Les collisions
--------------

Dans les jeux d'arcade, il est important de savoir quand un acteur sprite a entré en collision avec un autre acteur sprite. La plupart de ce code est copié de
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

Au lieu de bouger constament vers la droite, on peut rendre le mouvement conditionnel avec une déclaration ``if``. Ainsi, on peut faire en sorte que la boite pourchasse l'extraterrestre. La plupart du code a été copié de :numref:`code-collisions`. Les lignes qui ont été nouvellement ajoutés sont surlignés. Nous avons aussi modifié ce qui arrive lorsque la boite entre en contacte avec l'extraterrestre: le programme termine et vous devez le relancer pour jouer à nouveau. Ceci n'est peut-être pas ce que vous voulez dans votre jeu, mais nous allons pouvoir modifier le programme plus tard.

.. literalinclude:: programs/15b_chase.py
   :emphasize-lines: 18-23
   :caption: Pourchasseur d'extraterrestre
   :name: code-chase
   :linenos:



.. topic:: Exercice

   Ajoutez du mouvement vertical (comme vous avez fait dans l'exercice précédent).


.. topic:: Pour les plus avancés

   Créez un nouvel acteur sprite ennemie. Enregistrez son image avec le nom `ennemie.png` dans votre fichier `code/images`. Chargez l'image grâce à `Actor('ennemie')` au lieu de `Rect()`.




Powerup
-------

Instead of an enemy the box here is a powerup that the player must
collect. When he does it disappears and moves to a new location.

.. literalinclude:: programs/15c_powerup.py
   :caption: Collect the powerups
   :name: code-powerup
   :linenos:



.. topic:: Exercise

   Add vertical movement (as you did in Exercise \ref{exercise:updown}).




.. topic:: Exercise

   Draw a new powerup image.  Save it as `powerup.png` in your `mu_code/images` folder. Load it as an `Actor('powerup')` instead of the `Rect()`.


.. topic:: Advanced

   Combine this program with the enemy from  Program :numref:`code-chase` and the background from :numref:`code-background` and whatever else you want to make your own game.




Sound and animation
-------------------

Pygame Zero comes with one other image ``alien_hurt.png`` and one sound
``eep.wav``. If you want more you will have to add them to the
``sounds`` and ``images`` folders.

Most of this code is copied from
:numref:`code-collisions`

.. literalinclude:: programs/16_collisions2_sound_animation.py
   :emphasize-lines: 19-24
   :caption: Sound and animation upon collision
   :name: code-collisions2
   :linenos:



.. topic:: Exercise

   Record your own sound effect and add it to the game.


.. topic:: Advanced

   Add more boxes or sprites that move in different ways for the player to avoid.


.. topic:: Advanced

   Add a second alien controlled by different keys or gamepad for player 2.




Mouse clicks
------------

This uses a *function call-back* for event-based input. It is similar
to :numref:`code-collisions2` but:

-  The box has been removed.
-  There is an ``on_mouse_down()`` special function that is called
   automatically when the player click the mouse.
-  The score is displayed.

See :numref:`code-functions` for more about functions.

.. literalinclude:: programs/17_mouse_input.py
   :caption: Getting input from mouse clicks
   :name: code-mouse_input
   :linenos:





Mouse movement
--------------

.. literalinclude:: programs/18_mouse_movement.py
   :caption: Getting input from mouse movement
   :name: code-mouse_movement
   :linenos:



.. topic:: Exercise

   What happens if you delete line 8 and replace it with this::

        animate(alien, pos=pos, duration=1, tween='bounce_end')



.. topic:: Exercise

   What happens if you change `on_mouse_move` to `on_mouse_down`?


.. topic:: Advanced

   Make a game with one alien controlled by mouse and another controlled by keyboard

