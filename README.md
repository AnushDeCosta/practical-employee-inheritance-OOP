# Employee Inheritance – OOP Project

![Image](https://github.com/user-attachments/assets/b2d680ec-a83b-4a3e-b410-d33a0ae727e8)

## Summary
**Employee Inheritance** is a Python-based object-oriented system that models various employee types in a workplace. It demonstrates key OOP principles including inheritance, encapsulation, method overriding, and polymorphism.

The system includes a generic `Employee` class, and two specialised subclasses: `SoftwareDeveloper` and `DigitalArtist`, each with unique attributes and behaviors.

## Introduction
This project was developed to reinforce object-oriented programming fundamentals as part of the **Week 6 Practical** for the Bachelor of Data Analytics (XBDA) at the **University of South Australia (UniSA)**. It focuses on:

- Subclassing and inheritance of shared behavior
- Overriding base methods for contextual output
- Encapsulation of class attributes using name mangling
- Safe handling of optional lists and default values

> **Note**: This project was tested using both method interaction and internal `__dict__` validation for private attributes.

## Project Features
The system supports:

- **Base `Employee` behavior**:
  - Work on a project
  - Assign new projects to a backlog
  - Swap current project with one from the backlog
- **SoftwareDeveloper extensions**:
  - Override `work()` to show current programming language
  - Learn and store additional programming languages
- **DigitalArtist extensions**:
  - Override `work()` to show current digital software
  - Learn and store new software tools

### Core Mechanics
- All employee types inherit from the `Employee` base class
- Subclasses override the `work()` method using `super()` design
- Attributes are kept private using double underscores (`__`) and verified via `__dict__`

## Tools
- Python 3.10+
- PyCharm or VSCode
- GitHub for version control

## Files
```
├── employee.py     # Contains all class definitions (Employee, SoftwareDeveloper, DigitalArtist)
├── main.py         # Testing script for behavior and attribute verification
├── README.md       # Project documentation
```

## Usage
To use the system and verify output:

```python
from employee import SoftwareDeveloper, DigitalArtist

dev = SoftwareDeveloper(1, "Ash", "Trainer", "Beat Elite Four", "Python")
dev.work()
dev.learn_language("C++")
dev.assign_project("Master ReactJS")
dev.swap_project(1)
dev.work()

artist = DigitalArtist(2, "Oak", "Professor", "Draw Mew", "Photoshop")
artist.work()
artist.learn_software("Procreate")
artist.assign_project("Sketch Charizard")
artist.swap_project(1)
artist.work()
```

## Sample Output
```
Working on Beat Elite Four in Python.
Master ReactJS added to project backlog
Switched to project 'Master ReactJS'. Moved 'Beat Elite Four' to backlog.
Working on Master ReactJS in Python.

Working on Draw Mew using Photoshop.
Sketch Charizard added to project backlog
Switched to project 'Sketch Charizard'. Moved 'Draw Mew' to backlog.
Working on Sketch Charizard using Photoshop.
```

## Attribute Verification (using __dict__)
```python
expected = [
  '_Employee__id', '_Employee__name', '_Employee__current_project',
  '_Employee__profession', '_Employee__project_backlog',
  '_SoftwareDeveloper__language', '_SoftwareDeveloper__programming_languages'
]

dev = SoftwareDeveloper(...)
for attr in expected:
    assert attr in dev.__dict__
```

## Future Enhancements
- Add getter and setter properties for controlled access
- Introduce department or manager relationships using aggregation
- Use abstract base classes to enforce work behavior

## License
This project is intended for educational purposes only as part of coursework for the **University of South Australia (UniSA)** Bachelor of Data Analytics (XBDA) degree.  
© 2025 Anush De Costa.

## Acknowledgements
Special thanks to the UniSA teaching team for their guidance on modular class design, attribute encapsulation, and testing with `__dict__` introspection.
