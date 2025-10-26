# Class Schedule Using a Greedy Algorithm

## Description

This program assigns teachers to subjects using a **greedy set cover algorithm**.  
The goal is to minimize the number of teachers while ensuring that all subjects are covered.

## How the Algorithm Works

1. There is a set of subjects that must be covered.
2. At each step, the algorithm selects the teacher who can teach the **largest number of uncovered subjects**.
3. If multiple teachers cover the same number of subjects, the **youngest** teacher is chosen.
4. The subjects taught by that teacher are marked as covered.
5. The process repeats until all subjects are covered or no suitable teachers remain.

## Output

The program prints a list of selected teachers and the subjects they are assigned to.  
If it is impossible to cover all subjects, a message is displayed indicating that.
