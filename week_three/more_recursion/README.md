## Instructions:

1. A few chess players have made it to the finals fighting for 1st - 4th place.

```py
finalists = ['Sherman', 'Rosemary', 'Lucero', 'Yareli']
```

Using the `finalists` array, write a function that will return all the ways the players can get placed.

Example:

- possible placement 1: `['Sherman', 'Rosemary', 'Lucero', 'Yareli']`
- possible placement 2: `['Sherman', 'Rosemary', 'Yareli', 'Lucero']`
- possible placement 3: `['Sherman', 'Lucero', 'Rosemary', 'Yareli']`

2. The `all_students` array, is a list of all the chess students before the finals.

```py
all_students = ['Raven', 'Dorian', 'Santiago', 'Marisol', 'Stephanie', 'Roland', 'Sherman', 'Rosemary', 'Lucero', 'Yareli']
```

Write a function that finds all the combinations of last 4 finalists that could have ocurred.

Example:

- `['Raven', 'Dorian', 'Santiago', 'Marisol']`
- `['Raven', 'Dorian', 'Santiago', 'Stephanie']`

_NOTE: order doesn't matter here!_

Example: `['Raven', 'Dorian', 'Santiago', 'Marisol']` making it to the finals is the same as, `['Marisol', 'Raven', 'Santiago', 'Dorian']` (_It's the same 4 people!_).

3. Raven has caught wind of a pop quiz coming up and wants to let everyone in the class know about it. She only has the number of her 2 best friends: Stephanie and Rosemary. They have some other people's phone numbers, and so on.

If each student can only text one other person, what would be the chain of communication that get's everyone the information?

Here's a dictionary of the lines of communication:

```py
communications = {
    'Raven': ['Stephanie', 'Rosemary'],
    'Dorian': ['Santiago', 'Yareli'],
    'Santiago': ['Dorian', 'Roland'],
    'Marisol': ['Roland', 'Sherman', 'Yareli'],
    'Stephanie': ['Raven', 'Rosemary'],
    'Roland': ['Santiago','Marisol', 'Lucero'],
    'Sherman': ['Marisol'],
    'Rosemary': ['Raven', 'Stephanie', 'Lucero'],
    'Lucero': ['Roland', 'Rosemary'],
    'Yareli': ['Dorian', 'Marisol']
}
```
