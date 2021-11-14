Programmer des jeux vidéos avec Pygame Zero et Python
=====================================================

Cahier d'exercices de l'élève, 2e édition, révisée
--------------------------------------------------

`Lire le texte
ici <https://m-rbdr.github.io/pygame-zero-book/>`__

Soutenir l'auteur en achetant (en anglais) `le
livre <https://www.amazon.co.uk/dp/1071147706>`__.

La version (en anglais) `noire et blanc
<https://www.amazon.co.uk/Coding-Games-Pygame-Zero-Python/dp/1695028805>`__.

Il a aussi `un jeu <http://retrowar.net>`__.

Ce livre contient tous les exemples de logiciels utilisés dans ma 
classe CoderDojo pour enseigner le langage de programmation Python. Le 
but premier de cette classe est d'enseigner
la programmation en utilisant des jeux vidéos pour rendre 
l'apprentissage plus intéressant. Certains des exemples de cet ouvrage 
portent entièrement sur l'introduction de nouveaux concepts du langage 
Python ou sur l'usage de l'interface de programmation Pygame Zero. 
Toutefois, la plupart des exemples sont un mélange de ces deux 
tendances.

Générer le livre
================

Le livre utilise https://www.sphinx-doc.org:

::

   make clean
   make html
   cp -a _build/html/. docs/
   make latexpdf

Troisième édition?
==================

Regarde https://github.com/electronstudio/python_book
