from employee import Employee
from employee import SoftwareDeveloper
from employee import DigitalArtist

# ---- TEST 1: EMPLOYEE BEHAVIOUR ----
print("=== EMPLOYEE TEST ===")
emp = Employee(101, "Alex Mercer", "Agent", "Find the Prototype")
emp.work()
emp.assign_project("Stop the virus")
emp.swap_project(1)
emp.work()
print()

# ---- TEST 2: SOFTWARE DEVELOPER BEHAVIOUR ----
print("=== SOFTWARE DEVELOPER TEST ===")
dev = SoftwareDeveloper(102, "Ash Ketchum", "Pokemon Trainer", "Beat the Elite Four", "Python")
dev.work()
dev.learn_language("C++")
dev.assign_project("Be the very best")
dev.swap_project(1)
dev.work()
print()

# ---- TEST 3: DIGITAL ARTIST BEHAVIOUR ----
print("=== DIGITAL ARTIST TEST ===")
artist = DigitalArtist(103, "Professor Oak", "Researcher", "Let children do his research", "Blender")
artist.work()
artist.learn_software("Procreate")
artist.assign_project("Draw Mewtwo")
artist.swap_project(1)
artist.work()
print()

# ---- TEST 4: ATTRIBUTE PRESENCE TESTS ----
print("=== ATTRIBUTE INSPECTION TESTS ===")

# SoftwareDeveloper __dict__ test
dev_dict = SoftwareDeveloper(1, "Ash Ketchum", "Trainer", "Catch 'em all", "Python").__dict__
expected_dev_attrs = [
    '_Employee__id', '_Employee__name', '_Employee__profession',
    '_Employee__current_project', '_Employee__project_backlog',
    '_SoftwareDeveloper__language', '_SoftwareDeveloper__programming_languages'
]
for attr in expected_dev_attrs:
    if attr not in dev_dict:
        print(f"Missing SoftwareDeveloper attribute: {attr}")

# DigitalArtist __dict__ test
artist_dict = DigitalArtist(2, "Professor Oak", "Professor", "Let kids do research", "Blender").__dict__
expected_artist_attrs = [
    '_Employee__id', '_Employee__name', '_Employee__profession',
    '_Employee__current_project', '_Employee__project_backlog',
    '_DigitalArtist__software', '_DigitalArtist__suite'
]
for attr in expected_artist_attrs:
    if attr not in artist_dict:
        print(f"Missing DigitalArtist attribute: {attr}")
