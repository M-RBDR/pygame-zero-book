Aperçu du langage Python
========================

Commentaires
------------

Un programme informatique est destiné à être compris à la fois par les humains et les ordinateurs. Pour faciliter la tâche des humains, le code peut contenir des commentaires.

.. code:: python

   # Un commentaire ressemble à ceci.

Python ignore les commentaires puisqu'ils fournissent seulement des explications seulement pour les lecteurs humains et non pour l'ordinateur. Il est utile d'utiliser des commentaires pour se souvenir de ce qu'on a écrit précédemment ou pour expliquer à un autre programmeur ce que le code fait ou devrait faire.

Les littéraux
-------------

Un littéral est un nombre ou du texte dans le code qui représente littéralement le numéro ou le texte écrit par le programmeur. Un programme Python peut contenir n'importe quel nombre et n'importe quelle *chaîne* de caractères entourée de guillemets anglais (singulier ou double).

Exemples:

= ==== ========= =========
5 1.23 “Bonjour” ‘Antoine’
= ==== ========= =========

Mots-clés
---------

Chaque langage informatique a un certain nombre de *mots-clés* que vous devrez apprendre. Ils ressemblent à des mots anglais et, heureusement, il n'y en a que quelques-uns en Python. Vous pourriez les cocher au fur et à mesure que vous les rencontrez.

======= ======== ======== ====== ==== ====== ====== ======
False   None     True     and    as   assert async  await
break   class    continue def    del  elif   else   except
finally for      from     global if   import in     is
lambda  nonlocal not      or     pass raise  return try
while   with     yield                              
======= ======== ======== ====== ==== ====== ====== ======

Fonctions natives
-----------------

Python est également livré avec un grand nombre de *fonctions*. Les plus courantes sont intégrées au langage et toujours disponibles (comme les mots-clés). Voici une liste d'entre eux, juste par souci d'exhaustivité. *Vous ne les utiliserez probablement jamais tous*, et, quand vous en utiliserez un, vous le chercherez probablement dans la documentation du langage. Donc vous n'avez *pas besoin de vous en souvenir*.

========== ========== ========== ========= ========== ============
abs        all        any        ascii     bin        bool
breakpoint bytearray  bytes      callable  chr        classmethod
compile    complex    copyright  credits   delattr    dict
dir        divmod     enumerate  eval      exec       exit
filter     float      format     frozenset getattr    globals
hasattr    hash       help       hex       id         input
int        isinstance issubclass iter      len        license
list       locals     map        max       memoryview min
next       object     oct        open      ord        pow
print      property   quit       range     repr       reversed
round      set        setattr    slice     sorted     staticmethod
str        sum        super      tuple     type       vars
zip                                                   
========== ========== ========== ========= ========== ============

À la fin de ce livre, vous connaîtrez au moins 20 mots-clés/fonctions, ce qui est suffisant pour créer une grande variété de programmes.

Bibliothèques
-------------

Il existe de nombreuses autres fonctions (trop nombreuses pour présenter ici), mais tout le monde n'en a pas toujours besoin. Ces fonctions sont donc conservées dans des bibliothèques. Une bibliothèque est un répertoire de fonctions déjà écrites pour nous et qu'on peut ajouter à notre programme. Pour pouvoir utiliser les fonctions d'une bibliothèque, vous devez *importer* le module de la bibliothèque. Par exemple, si vous souhaitez un nombre aléatoire, il vous suffit d'importer la bibliothèque aléatoire:

.. code:: python

   from random import randint
   print(randint(0,10))

Certaines bibliothèques sont livrées avec Python alors que d'autres doivent être téléchargés. C'est le cas des bibliothèques Minecraft, Pygame, Numpy et Richlib.

Noms et variables
-----------------

Vous verrez de nombreux mots dans un programme qui ne sont pas des littéraux, des mots-clés ou des fonctions de bibliothèques. Ce sont des noms de variables choisis par le programmeur. Une variable est comme une boite dans laquelle on peut mettre un nombre ou une *chaîne* de caractères. On déclare et initialise une variable grâce au symbole *=*. Par exemple, si le programme doit enregistrer un score et le stocker dans une variable, le programmeur peut choisir de donner le nom ``pointage`` à cette variable :

.. code:: python

   pointage = 1

Puis, on peut utiliser cette variable dans une fonction en l'invoquant ou l'appelant avec son nom. Par exemple, on répète le mot ``pointage`` dans la fonction print pour que Python insère la valeur de la variable pointage, ici *1*, à cet endroit.

.. code:: python

   print("Pointage: ", pointage)

Python ne comprend pas ce que signifie le nom ``pointage``. Il ne fait que se soucier que le même mot est utilisé à chaque fois pour représenter la valeur de ``pointage``. Donc un programmeur différent pourrait décider d'écrire le programme comme celui-ci:

.. code:: python

   points = 1
   print("Pointage: ", points)

Un programmeur qui n'aime pas frapper sur un clavier pourrait utiliser un nom plus court et moins descriptif:

.. code:: python

   p = 1
   print("Score: ", p)

Cependant, le programmeur doit être cohérent. Ce prochain code **ne fonctionnerait pas** puisqu'on n'informe pas Python de l'existence de la variable pointage:

.. code:: python

   points = 1
   print("Pointage: ", pointage)

L'espace blanc
--------------

Python est particulier en ce qu'il se soucie de *l'espace blanc*, c'est-à-dire ce que vous obtenez lorsque vous appuyez sur la touche de *tabulation* ou sur la barre *espace* sur votre clavier.

Les programmes Python sont organisés en blocs de lignes. Chaque ligne d'un bloc doit avoir la même quantité d'espace qui l'a précédé - *l'indentation*.  Voir :numref:`code-blocks` pour un exemple.
