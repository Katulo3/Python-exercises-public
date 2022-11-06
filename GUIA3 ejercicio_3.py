usuarios: list = [
    "Brahms",
    "Schubert",
    "Vivaldi",
    "Verdi",
    "Tchaikovsky",
]
administradores: list = []

data = {"Admins": administradores}

# news admins
administradores.append("Verdi")
administradores.append("Brahms")
# chau admin
administradores.remove("Brahms")
# new admin
administradores.append("Tchaikovsky")

# segunda manera de hacerlo
# if administradores[0] in usuarios:
#     print(f"Hay {len(administradores)} usarios que son administradores")
#     print(f"Los admins son: {str(administradores)}"

if data["Admins"][0] in usuarios:
    print(f"Hay {len(administradores)} usarios que son administradores")
    print(f"Los admins son: {str(administradores)}")
else:
    print("no hay usuarios que sean admins")

print(f"Hay {len(usuarios)} usuarios y son: {str(usuarios)}")
