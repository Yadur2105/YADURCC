# Lab 4 notes: Git & GitHub

Draft answers. Questions 2, 3, 7 and 8 depend on the output on your own machine, so check them against your terminal before submitting.

1. `--global` saves the setting to `~/.gitconfig`, so every repository on this computer uses that name and email. Without it, `git config` only writes to the current repository's `.git/config`, and the commits in that repository use that value.
2. `ls -a` shows `.git`, a hidden directory that holds the repository itself: the object database, branch references, `HEAD`, the index and config files. Do not edit it by hand.
3. Git lists every file and folder that is not ignored. Check the count in your terminal. Anything under `.venv/` was not written by you.
4. After `.gitignore` was created, the `.venv/` entries disappeared from `git status`, so Git no longer offers that third-party code for tracking.
5. `.gitignore` should be committed. Anyone who clones the repository then gets the same ignore rules without setting them up again.
6. `README.md` moved from "Untracked files" to "Changes to be committed". It went from the working directory into the staging area (index). `git commit` then moves it into the repository history.
7. Check the output in your terminal. It prints the branch, the short hash, the message, and the number of files changed.
8. The first seven characters are the short form of the commit hash. Git uses that unique ID to identify the commit, and you can type the short form in commands instead of the full 40 characters.
9. The loop is: edit a file, stage it with `git add`, commit it with `git commit`, then check the result with `git status` or `git log`.
10. `README.md` is a convention. GitHub shows it on the repository's front page, rendered from Markdown, which is why it sits in the top-level folder.
11. `gh auth login` stores a GitHub credential, so `git push` over HTTPS authenticates without asking for a password.
12. The README is shown on the front page. GitHub renders the top-level README automatically, so visitors see it first.
13. `git push` copies your commits to GitHub. Local commits keep the same hashes, and your local history is unchanged.
14. A private repository exists on GitHub, with its own URL, but only you and the people you invite can see it. A repository that does not exist has no URL and no content on GitHub at all.
