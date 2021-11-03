for x in range(0, 10):
    print("Boucle", x)

# loop with step 2
for x in range(0, 10, 2):
    print("Boucle encore", x)

# loop inside another loop
for a in range(0, 6):
    for b in range(0, 6):
        print(a, "fois", b, "est", a * b)
