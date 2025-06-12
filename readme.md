1. **Project Overview** A brief introduction to what your project does.
2. **Motivation** – Why you chose this project and what you aim to learn.
3. **Installation & Usage** – How to set up and run the project.
4. **Design Decisions & Thought Process** – *This is where you’d explain your reasoning.*
5. **Challenges & Solutions** – Document issues you encountered and how you resolved them.
6. **Key learnings** - Highlight the most valuable insights and skills gained during the project.
7. **Future Improvements** – Areas you plan to refine.


# Project Overview

# Motivation
After studying the module "Introduction to Python" at university, going through the book "Python crash course" by Eric Matthes, learnt through practical tutorials Virtual Studio Code and Git technology together with Gitlab, I want to put in practice concepts like:
-   Object-oriented programming: classes, inheritance, and subclasses  
-   Modular code organization using files, modules, and imports  
-   Persistent storage with `pathlib` and JSON files  
-   Exception handling  
-   Loops and user interaction through input prompts
-   Git configuration and basic usage like branches, merging, commiting and pushing.


# Installation & Usage



# Design Decisions & Thought Process
## The initial layout consists of:
This project simulates a basic library system. The initial layout includes the following components:

- Classes Book and User: Defined in their respective modules, these classes are responsible for creating instances of books and users. The created objects are then passed to the data module for storage.

- utils Module: Contains the core functionality and operations of the library, such as borrowing, returning, and managing books.

- data Module: Handles the persistence logic, saving and retrieving data from JSON files. These files act as a lightweight database.

- JSON Files: Two separate JSON files store books and users, respectively. The data is structured as dictionaries with keys being ISBN (for books) or user_number (for users), and values being dictionaries representing the object data.

- main Module: Serves as the entry point of the application.

There is a separate module called mock_data that can be run to populate the system with books, users, and transactions, simulating a typical library workflow.


# Challenges & Solutions
**Challenge:** Python objects cannot be directly stored in JSON format. 
    **Solution:** 
There are two primary approaches to address this:

Object Serialization: Convert Python objects into dictionaries using methods like . __dict__ before saving to JSON, and deserialize them back into objects upon loading. This method is more elaborate and can introduce unnecessary complexity.
Direct Dictionary Storage (Chosen Approach): Store data directly as dictionaries rather than objects. This approach is simpler and better aligned with the scope of the project.

# Key learnings
JSON and Python Objects: One of the main goals was to practice working with objects—modifying their attributes and persisting user input across sessions. However, JSON does not support direct serialization of Python class instances.
Initially, the intent was to save Book and User objects directly in JSON format. This proved unfeasible, leading to the decision to store the object data as dictionaries instead.
This experience reinforced the importance of understanding data serialization and the limitations of different storage formats.
 
The importance of try excepts blocks to avoid crashes.'


# Future Improvements

