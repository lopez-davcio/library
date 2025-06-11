1. **Project Overview** A brief introduction to what your project does.
2. **Motivation** – Why you chose this project and what you aim to learn.
3. **Installation & Usage** – How to set up and run the project.
4. **Design Decisions & Thought Process** – *This is where you’d explain your reasoning.*
5. **Challenges & Solutions** – Document issues you encountered and how you resolved them.
6. **Future Improvements** – Areas you plan to refine.


#Project Overview

#Motivation
After studying the module "Introduction to Python" at university, going through the book "Python crash course" by Eric Matthes, learnt through practical tutorials Virtual Studio Code and Git technology together with Gitlab, I want to put in practice concepts like:
-   Object-oriented programming: classes, inheritance, and subclasses  
-   Modular code organization using files, modules, and imports  
-   Persistent storage with `pathlib` and JSON files  
-   Exception handling  
-   Loops and user interaction through input prompts
-   Git configuration and basic usage like branches, merging, commiting and pushing.


#Installation & Usage



#Design Decisions & Thought Process
## The initial layout consists of:
- Classes Book and User, that will be held in their homonym modules, with the purpose of instantiating the object and send it to module data to be stored/saved.
- Module utils to represent the functions and logic of the library operations, such as lend/borrow book, return book, etc.
- Module data that will hold the logic to retrieve data from and save data to json files acting as database.
- Two json files to store books and users, as a dictionary with key=isbn (or key=user_number), and value=Book object (or user object).
- A main module as an access point for the program.   
The program will be preloaded with mock transactions, books and users to simulate a normal library workflow from the first interaction.


#Challenges & Solutions
**Issue:** Python objects (like instances of a class) can't be directly saved into JSON.  
    **Solution:** There are two main solutions, the first is to manually or through the special attribute __dict__ convert the object into a dictionary and save it, then retrieve it and convert it back into an object. More elaborated and subject to unnecessary conversions. 
    A simpler solution, more in line with the spirit and scope of the current project is to save the data as dictionaries directly instead of objects. 

#Future Improvements

