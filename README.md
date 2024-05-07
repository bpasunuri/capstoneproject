

Configuration:
=====================
git config --global user.name "Your Name": Set your username globally.
git config --global user.email "youremail@example.com": Set your email globally.

Creating Repositories:
=====================
git init: Initialize a new Git repository in the current directory.
git clone <repository_url>: Clone a repository from a remote server to your local machine.

Basic Snapshotting:
=====================
git add <file>: Add a file to the staging area.
git add .: Add all changes in the current directory to the staging area.
git commit -m "Commit message": Commit changes with a descriptive message.

Branching & Merging:
=====================
git branch: List all branches in the repository.
git branch <branch_name>: Create a new branch.
git checkout <branch_name>: Switch to a different branch.
git merge <branch_name>: Merge changes from another branch into the current branch.

Inspecting & Comparing:
======================
git status: Check the status of the working directory and staging area.
git log: View commit history.
git diff: Show changes between commits, branches, etc.

Undoing Changes:
=======================
git reset <file>: Unstage changes for a file.
git checkout -- <file>: Discard changes in the working directory for a file.
git revert <commit>: Revert changes from a specific commit.

Working with Remotes:
========================
git remote add <name> <url>: Add a remote repository.
git push <remote> <branch>: Push changes to a remote repository.
git pull <remote> <branch>: Fetch changes from a remote repository and merge them into the current branch.
git fetch <remote>: Fetch changes from a remote repository.

Miscellaneous:
=======================
git stash: Temporarily store changes that are not ready to be committed.
git tag <tag_name>: Create a lightweight tag for the current commit.





Searching:
=======================
git grep <pattern>: Search the working directory for a specified pattern.
git log --grep=<pattern>: Search commit messages for a specified pattern.

Rewriting History:
==========================
git rebase <branch_name>: Reapply commits from one branch onto another.
git cherry-pick <commit>: Apply changes introduced by a specific commit to the current branch.
git commit --amend: Modify the last commit with new changes or an updated commit message.

Submodules:
====================
git submodule add <repository_url>: Add a submodule to the repository.
git submodule update --init: Initialize and update submodules.

Aliases:
=====================
git config --global alias.<shortcut> <git_command>: Create a shortcut (alias) for a Git command.
Interactive Rebase
git rebase -i <commit>: Perform an interactive rebase, allowing you to reorder, squash, edit, or drop commits.

Ignore Files:
=====================
.gitignore: Create or edit a .gitignore file to specify files or directories to ignore.

Show Information:
=====================
git show <commit>: Show the details of a specific commit.

Cleaning:
=====================
git clean -n: Preview which untracked files will be removed.
git clean -f: Remove untracked files from the working directory.

Remote Operations:
======================
git remote -v: List all remote repositories and their URLs.
git remote show <remote_name>: Show information about a specific remote.

Git Help:
======================
git help <command>: Display help information for a specific Git command.
git <command> --help: Display help information for a specific Git command.

Git Configuration:
===================
git config --list: List all Git configurations.
git config --global --edit: Edit the global Git configuration file.



Reflogs:
====================
git reflog: Show a log of changes to the Git reference (HEAD) over time.
git reflog <branch_name>: Show a log of changes to a specific branch over time.

Bisecting:
=========================
git bisect start: Start the binary search to find the commit that introduced a bug.
git bisect good <commit>: Mark a commit as good (bug-free) during the bisect process.
git bisect bad <commit>: Mark a commit as bad (buggy) during the bisect process.
git bisect reset: Finish the bisect process and return to the original branch state.

Workflows:
==================
git flow init: Initialize a GitFlow repository.
git flow feature start <feature_name>: Start a new feature branch.
git flow release start <release_version>: Start a new release branch.
git flow hotfix start <hotfix_name>: Start a new hotfix branch.

Hooks:
===================
Git hooks allow you to run custom scripts in response to Git events. Common hooks include pre-commit, post-commit, pre-push, etc.

Subversion (SVN) Commands:
=========================
git svn clone <svn_repository_url>: Clone an SVN repository into a Git repository.
git svn fetch: Fetch changes from the SVN repository into the Git repository.
git svn rebase: Rebase local changes on top of changes fetched from the SVN repository.
git svn dcommit: Commit changes from the Git repository to the SVN repository.

Worktrees:
==========================
git worktree add <path> <branch>: Add a linked working directory (worktree) for a branch.
git worktree list: List all linked working directories.







