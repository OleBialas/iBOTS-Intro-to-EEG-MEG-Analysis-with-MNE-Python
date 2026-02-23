# Instructions
When you find new information about the content or structure of this project that would be useful for future sessions, append them it to this document.

# Repository structure
This repository contains materials for a hands-on workshop on EEG and MEG analysis in Python using the MNE package.
The worshop spans three days and each day contains 4 sessions.
Each session is in a separate folder and the session number is encoded in the folder name (01_ to 12_).
Each folder contains an `index.ipynb` file with the course notebook and possibly a `slides.ipynb` file with a short introductory lecture

# Course goals
The course is directed to neuroscience researchers (PhDs and postdocs) and the goal is to teach them neuroscientific theory and application as well as best practices for coding. The course should be accessible for beginners but also allow more advanced participants to expand their knowledge.

# Session structure
Each session usually consists of four sections.
Each section starts with a short description of the background and a table that contains code snippets for solving the exercises.
The code table should be complete so that it contains all the examples required to solve the exercises.
The first two sessions contain the core learings and the later sections contain more advanced applications of the same techniques.
The later sections should not be required to understand later sections.
Each exercise should have a solution and the code cell should be tagged as "solution".

# Quality requirements
- There should be no typos or grammatical errors
- The language used in the notebooks should be consistent, if there are multiple terms used for a gven technique, the same name should be used across all notebooks consistently.
- Sessions and sections should be as self-contained as possible. Failing at a specific exercise should not prevent the participant from solving subsequent exercises.
- All the descriptions should be scientifically and mathematically correct.
- There shouldn't be any unnecessary outputs (e.g. duplicated plots or matplotlib text outputs)
- IMPORTANT: when being asked to proofread always do an additional pass without considering your previous edits and repeat until you manage to do a pass were you can't find anything

# Technology
The project uses pixi to manage the environment so whenever running any Python commands, it should be executed via `pixi run`.