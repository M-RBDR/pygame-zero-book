Jeux de devinettes basé sur du texte
====================================

Ces programmes peuvent être entré en utilisant un éditeur de texte. Je suggère d'utiliser l'éditeur
`Thonny <https://thonny.org>`__ puisqu'il est livré avec Python, Pygame Zero et d'autres bibliothèques toutes pré-installées dans un seul téléchargment.

Bonjour à tous
-------------

Traditionnellement, le premier programme utilisé pour s'assurer que Python soit bien installé et qu'on soit en mesure d'exécuter d'autres programmes est le programme *"Bonjour à tous"* ("Hello, world" en anglais).

Si vous utilisez l'éditeur Thonny:

1. Assurez-vous que sous ``Exécuter`` le mode Pygame Zero soit décoché.
2. Tapper le programme.
3. Cliquez sur ``Enregistrer`` et entrer le nom du programme.
4. Cliquez sur ``Exécuter le script courant``.



.. code-block:: python
   :caption: Bonjour à tous
   :name: code-hello
   :linenos:

   print("Bonjour à tous")

   # Cette ligne est un commentaire, vous n'avez pas besoin de tapper celles-ci!


Recevoir des entrés du clavier
------------------------------

Ce programme va faire une pause et attendre pour que vous entrer du texte avec le clavier et que vous tappez sur la touche d'entrée. Le texte que vous entrez est stocké dans une variable nommée ``x``.

.. literalinclude:: programs/02_input.py
   :caption: Recevoir des entrés du clavier
   :name: code-input
   :linenos:



.. topic:: Exercice

   Entrez les noms de vos amis et affichez leur des messages personalisés.


Faire des décisions: if, elif, else
-----------------------------------

Voici comment on ajoute un autre nom à :numref:`code-input`

.. literalinclude:: programs/03_input2.py
   :emphasize-lines: 6, 7, 8, 9
   :caption: Décisions: if, elif, else
   :name: code-input2
   :linenos:



:numref:`code-input2` est très simlaire à :numref:`code-input`. Les nouvelles lignes ont été surlignés. Vous pouvez soit modifier :numref:`code-input`, ou créer un nouveau ficher et utiliser les fonctions copier-coller pour copier le code de l'ancien programme vers le nouveau programme.

Une question de mathématique aléatoire
--------------------------------------

.. literalinclude:: programs/04_maths_question.py
   :caption: Une question de mathématique aléatoire
   :name: codemaths
   :linenos:


.. topic:: Exercice

   Ajoute plus de questions. Par exemple:

   * Au lieu de 7, utilisez un autre nombre aléatoire.
   * Utilisez un plus grand nombre aléatoire.
   * Multipliez (utilisez `*`), divisez (utilisez `/`) ou soustrayez (utilisez `-`) les nombres.



.. topic:: Exercice

   Affiche le nombre de questions que le joueur a réussi à la fin du programme.




Garder un pointage
------------------

On a créer une variable ``pointage`` afin d'enregistrer le nombre de questions que le joueur a réussi.


.. literalinclude:: programs/05_maths_question2.py
   :caption: Garder un pointage
   :name: code-maths2
   :linenos:


Jeux de devinettes avec une boucle
----------------------------------

Cette boucle ``while`` répète ses instructions pour toujours... ou jusqu'à ce que le joueur réussi à avoir une bonne réponse. Lorsque c'est le cas, la boucle ``break`` et on sort de la boucle. À noter que tous les éléments de la boucle sont en retrait.


.. literalinclude:: programs/06_loop.py
   :caption: Jeux de devinettes avec une boucle
   :name: codeloop
   :linenos:

.. topic:: Exercice

   Donnez un indice au joueur lorsqu'il n'a pas la bonne réponse. Est-ce que leur réponse était trop grande ou trop petite?


.. topic:: Exercice

   Affichez le nombre de tentatives qu'a fait le joueur avant de trouver la bonne réponse.




Jeux de devinettes amélioré
---------------------------

:numref:`codeloop` avec un indice qui révèle si la tentative est trop grande ou trop petite par rapport à la réponse.

.. literalinclude:: programs/07_loop2.py
   :caption: Jeux de devinettes amélioré
   :name: code-loop2
   :linenos:

