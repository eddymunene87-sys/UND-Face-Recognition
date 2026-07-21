from utils.register import FaceRegistrar

registrar = FaceRegistrar(max_images=20)

name = input("Enter person's name: ").strip()

if name:
    registrar.register_person(name)
else:
    print("Name cannot be empty.")