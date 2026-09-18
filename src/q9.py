"""
Question 9 — GitHub: Git Workflow  [Short Answer]

This is the same workflow you used to SUBMIT this assessment, so you have
already done most of it. Write the exact git command for each step.

Scenario
--------
You have a local copy of a repo. You want to:
1. Create a new branch called `my-solutions`.
2. Switch to that branch.
3. After editing `q4.md`, stage that file for commit.
4. Commit the staged change with the message "Add Q4 answers".
5. Push the `my-solutions` branch to GitHub.

Write the exact git command for each step (one per line).
"""

# Step 1 — Create a new branch called `my-solutions`:
git branch my-solutions
# Step 2 — Switch to `my-solutions`:
git checkout my-solutions
# Step 3 — Stage q4.md:
git add q4.md
# Step 4 — Commit with message "Add Q4 answers":
git commit -m "Add Q4 answers"
# Step 5 — Push `my-solutions` to the remote:
git push origin my-solutions

"""
Step 6 (short answer). You run `git status` and it says
`Changes not staged for commit`. In one sentence, what does that tell you,
and which command moves a file from there into the next commit?

    Answer: It tells you that q4.md has been modified since the last commit but hasn't been added to the staging area yet; the command git add q4.md moves the file into the next commit.
"""
