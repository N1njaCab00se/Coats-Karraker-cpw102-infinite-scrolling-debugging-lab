# Incident Note — INC-204

**Responders:Coats-Karraker**

## Investigation log

Record **every debugging step in chronological order as you work**, including unsuccessful attempts and changes you undo. Commit your work as you go. 

For each step, briefly note what you tried and why, what you observed, and what you concluded or decided to try next.

Include relevant inputs, code changes, or output so someone else can follow your investigation. 

Use numbered entries or timestamps. Use Markdown formatting to make it easy to read.

## Resolution

Explain the causes, your repairs, and the evidence that verifies them. Identify
anything still uncertain or unresolved. Make code changes in `feed.py`.

## NOTES
Initial run attempts: 
Tried input that went with either "y" or "n". Only input being registers is a lowercase "n". Any other input loads more lines. Even a word like "loops" will load more lines. No code changes as of yet.

First Commit: Added in .strip().lower() to make the case non-sensitive and to cut white spaces out.
Second Commit: Added in an "elif" and "else" statement to provide fixes for "y" and "n" input. Partially works.
Third Commit: Moved code to a different location. First posts no longer load on start, but "y" and "n" work as it should. Invalid inputs don't load new posts and go back to input for valid prompts, however, program does not end once all posts are shown.
Fourth Commit: Duplicated some code to load posts on open. Posts now load on start, load in as normal on "y", program ends on "n", and acts as expected with invalid input. Only thing that seems to be needed is to end program on all posts being loaded.