def belt_degree(dictionary):
    for key, val in dictionary.items():
        print(f"I'm {key} and I'm a {val} belt")

def belt_count(dictionary):
    ninja_belts = list(dictionary.values())
    for ninja_belt in set(ninja_belts):
        num = ninja_belts.count(ninja_belt)
        print(f"There are {num} {ninja_belt} belts")

belts = {}

while True:
    name = input("Name of the student: ")
    belt = input("Belt color: ")
    belts[name] = belt

    another_student = input("another student? (Enter yes or no): ")
    if another_student == 'yes':
        continue
    elif another_student == 'y':
        continue
    elif another_student == 'YES':
        continue
    else:
        break

belt_degree(belts)
belt_count(belts)
