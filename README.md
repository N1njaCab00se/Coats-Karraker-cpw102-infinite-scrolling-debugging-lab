# CPW 102: Infinite Scroll Incident

## GitHub Setup

Create one repository per team from this assignment template.

1. One partner clicks **Use this template → Create a new repository** and chooses their own GitHub account as the owner.
2. Include both partners' last names in the repository name:

   ```text
   lastname-lastname-cpw102-infinite-scroll-debugging-lab
   ```

3. Set the visibility to **Public** and click **Create repository**.
4. Clone your team's repository using **Code → Open with GitHub Desktop**.
5. Before editing, one create a branch in GitHub Desktop using **Current branch → New branch**. Name it `development`, then click **Publish branch**. 
6. Open the project by clicking **Open in Visual Studio Code**.

Both partners work in the same team repository on `development`. Keep `main` as the starter. 

## Expected Program Behavior

Infinite scroll loads more content as you reach the bottom of a feed, keeping earlier posts visible. Try the [infinite-scroll demo](https://infinite-scroll.com/demo/full-page/) and watch new posts appear as you scroll. In this program, entering `y` simulates scrolling to load the next page.

The program should:

- Show the first three posts when the program starts, without asking the user to scroll first.
- When the user enters `y`, add the next three posts in order. If fewer than three remain, add those remaining posts.
- After loading posts, show all posts loaded so far and a count of how many there are. 
- After displaying the last posts, the next `y` should print `No more posts.` and end the session. 
- If there are no posts when the program starts, print that message and end without asking the user to scroll.
- When the user enters `n`, end the session without loading any more posts.
- Accept uppercase and lowercase answers, including answers with spaces before or after them. For example, `Y` and ` y ` should both work like `y`.
- For any other answer other than case-insensitive `y` or `n`, print `Please enter y or n.` and ask again. 
- Whenever the session ends through quitting or reaching the end of the feed, print `Session ended.` exactly once.

## User bug report

Users submitted the following tickets with reports of buggy behavior! 

> “Every time I scroll, I see the same three posts added again instead of new ones.”

> “I keep scrolling, but I never reach the end. The app never tells me there are no more posts.”

> “I typed ‘maybe’ instead of ‘y’ or ‘n’, and it loaded more posts anyway.”

## Your Task

Debug the program, logging your work as you go. Make code changes to fix the above bugs. 

## Debugging Log

Keep a chronological log of **every debugging step as you take it**, including unsuccessful attempts. Commit frequently. Choose your own investigation methods and evidence. Log enough to make your instructor confident that you have thoroughly investigated and fixed the users' bug(s).

## Submission

1. In GitHub Desktop, commit your changes, then click **Push origin**.
2. Create one PR for the team on GitHub
3. Leave the PR open. One partner submits the PR URL in Canvas on behalf of the team. Submit the PR link, not the repository homepage.
