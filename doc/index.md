# [Balmorel GitHub Tutorial](https://github.com/tgraulich/Balmorel_GitHub_Tutorial)

This tutorial will show, how to work with **Balmorel** on **GitHub**. It will cover the basic steps of:
- **Forking** the **Balmorel** and **Balmorel_data** repository.
- **Cloning** the repository to your **local PC** or **HPC** and setting up the folder structure
- **Commiting** changes and pushing them upstream to your **remote repository**
- Creating your own **branch**
- Making a **pull request** to merge into the **master branch**

## GitHub, VS Code, or command line

We offer **three different paths** for this exercise:
- **GitHub** (this is the one we will demonstrate)
- **VS Code** (if you prefer to follow along using an editor)
- **Command line** (for people comfortable with the command line)


## Creating a copy of the repository by "forking" and/or "cloning"

A **repository** is a collection of files in one directory tracked by Git.  A
GitHub repository is GitHub's copy, which adds things like access control,
issue tracking, and discussions.  Each GitHub repository is owned by a user or
organization, who controls access.

For Balmorel we have mainly to of these repositories:
- <https://github.com/balmorelcommunity/Balmorel>, which contains the model formulation and addons
- <https://github.com/balmorelcommunity/Balmorel_data>, which contains all the data needed to run the model

To start, we need to make **our own copy** of these repositories and transfer them to our **own Computer** or the **HPC**.

:::{figure} forking_cloning.png
:alt: Illustration of the concepts of **forking** and **cloning** and the recommended workflow for Balmorel: **forking** then **cloning**.
:width: 100%

Illustration of the concepts of **forking** and **cloning** and the recommended workflow for Balmorel: **forking** then **cloning**.
:::

At all times you should be aware of if you are looking at **your repository**
or the **upstream repository** (original repository):
- Your repository: https://github.com/**USER**/Balmorel
- Upstream repository: https://github.com/**balmorelcommunity**/Balmorel

:::{admonition} How to create a fork
1. Go to the repository view on GitHub: <https://github.com/balmorelcommunity/Balmorel>
1. First, on GitHub, click the button that says "Fork". It is towards
   the top-right of the screen.
1. You should shortly be redirected to your copy of the repository
   **USER/Balmorel**.
1. Repeat the same step for the <https://github.com/balmorelcommunity/Balmorel_data> repository.
:::


## Exercise: Copy (clone) the repositories and setup the correct folder structure

Work on this by yourself or in pairs.

::::::{admonition} Exercise preparation
:::::{tabs}
::::{group-tab} GitHub
In this case you will download the repositories as a **.zip** file from GitHub:

1. Go to the Balmorel GitHub repository.
1. **Make sure the URL says `https://github.com/USER/Balmorel`, where `USER` is your username.**
1. Download the repository:
:::{figure} GitHub_clone.png
:width: 100%
:::
4. Extract the folder to a location of your choice.
5. Download the `https://github.com/USER/Balmorel_data` repository the same way (**Make sure you are cloning your forked repository**).
6. Extract the files into the local copy of the **Balmorel** repository, into the **base** folder.
7. Rename the `Balmorel_data` folder to `data`.
::::

::::{group-tab} VS Code
You need to have forked the repository as described above.

We need to start by making a clone of this repository so that you can work
locally.

1. Start VS Code.
1. If you don't have the default view (you already have a project
open), go to File → New Window.
1. Under "Start" on the screen, select "Clone Git Repository...". Alternatively
   navigate to the "Source Control" tab on the left sidebar and click on the "Clone Repository" button.
1. Paste in this URL: `https://github.com/USER/Balmorel`, where
   `USER` is your username.  You can copy this from the browser.
1. Browse and select the folder in which you want to clone the
   repository.
1. Say yes, you want to open this repository.
1. Select "Yes, I trust the authors" (the other option works too).
1. Repeat the same process for `https://github.com/USER/Balmorel_data` until you have to choose the location.
1. Select the `.../Balmorel/` and clone the data to this location.
1. Rename the `Balmorel_data` folder to `data`.
::::

::::{group-tab} Command line
**This path is advanced and we do not include all command line
information: you need to be somewhat
comfortable with the command line already.**

You need to have forked the repository as described above.

We need to start by making a clone of this repository so that you can work
locally.

1. Start the terminal in which you use Git (terminal application, or
   Git Bash).
1. Change to the directory where you would want the repository to be
   (`cd ~/code` for example, if the `~/code` directory is where you
   store your files).
1. Run the following command: `git clone https://github.com/USER/Balmorel`, where `USER` is your username.  You might need to use a SSH clone command instead of HTTPS, depending on your setup.
1. Change to that directory: `cd Balmorel`
1. Run the following command: `git clone https://github.com/USER/Balmorel_data`, where `USER` is your username.
1. Rename the `Balmorel_data` folder to `data` by typing the following command: `mv Balmorel_data data`.
::::
:::::
::::::


:::{admonition} Exercise: Browsing and editing the repositories (10 min)

Browse the [Balmorel repository](https://github.com/balmorelcommunity/Balmorel) either on GitHub or your local PC and explore commits and branches. Take notes and
prepare questions. The hints are for the GitHub path in the browser.

1. Browse the **commit history**: Are commit messages understandable?
   (Hint: "Commit history", the timeline symbol, above the file list)
1. Try to find the **history of commits for a single file**, e.g. `base/output/OUTPUT_SUMMARY.inc`.
   (Hint: "History" button in the file view)
1. **Which files creates the MainResults.gdx file**?
   (Hint: the GitHub search on top of the repository view, look for execute_unload `"MainResults.gdx"`)
1. In the `base/output/OUTPUT_SUMMARY.inc` file,
   find out when the parameter `STORAGE_LEVEL` was added and **in which commit**.
   (Hint: "Blame" view in the file view)
:::
<!---
The solution below goes over most of the answers, and you are
encouraged to use it when the hints aren't enough - this is by
design.


## Solution and walk-through now

### (1) Basic browsing

The most basic thing to look at is the history of commits.

* This is visible from a button in the repository view.  We see every
  change, when, and who has committed.
* Every change has a unique identifier, such as `244c993`.  This can
  be used to identify both this change, and the whole project's
  version as of that change.
* Clicking on a change in the view shows more.

:::::{tabs}

::::{group-tab} GitHub
Click on the timeline symbol in the repository view:
  :::{figure} img/browsing/history.png
  :alt: Screenshot on GitHub of where to find the commit history
  :width: 100%
  :class: with-border
  :::
::::

::::{group-tab} VS Code
This can be done from "Timeline", in the bottom of explorer, but only
for a single file.
::::

::::{group-tab} Command line
Run:
```console
$ git log
```

Try also:
```console
$ git log --oneline
```
::::

:::::


### (2) Compare commit history with network graph

The commit history we saw above looks linear: one commit after
another.  But if we look at the network view, we see some branching and merging points.
We'll see how to do these later.  This is another one of the
basic Git views.

:::::{tabs}
::::{group-tab} GitHub
In a new browser tab, open the "Insights" tab, and click on "Network".
You can hover over the commit dots to see the person who committed and
how they correspond with the commits in the other view:
  :::{figure} img/browsing/network.png
  :alt: Screenshot on GitHub of the network graph
  :width: 100%
  :class: with-border
  :::
::::

::::{group-tab} VS Code
We don't know how to do this without an extension. Try starting a terminal and using the
"Command line" option.
::::

::::{group-tab} Command line
This is a useful command to browse the network of commits locally:
```console
$ git log --graph --oneline --decorate --all
```

To avoid having to type this long command every time, you can define an alias (shortcut):
```console
$ git config --global alias.graph "log --graph --oneline --decorate --all"
```

From then on, you can use `git graph` to see the network graph.
::::

:::::


### (3) How can you browse the history of a single file?

We see the history for the whole repository, but we can also see it
for a single file.

:::::{tabs}

::::{group-tab} GitHub
Navigate to the file view: Main page → simulate.py.
Click the "History" button near the top right.
::::

::::{group-tab} VS Code
Open simulate.py file in the editor.  Under the file browser,
we see a "Timeline" view there.
::::

::::{group-tab} Command line
The `git log` command can take a filename and provide the log of only
a single file:

```
$ git log simulate.py
```
::::

:::::


### (4) Which files include the word "position"?

Version control makes it very easy to find all occurrences of a
word or pattern. This is useful for things like finding where functions or
variables are defined or used.

:::::{tabs}
::::{group-tab} GitHub
We go to the main file view.  We click the Search magnifying
class at the very top, type "position", and click enter. We see every
instance, including the context.

:::{admonition} Searching in a forked repository will not work instantaneously!

It usually takes a few minutes before one can search for keywords in a forked repository
since it first needs to build the search index the very first time we search.
Start it, continue with other steps, then come back to this.
:::
::::

::::{group-tab} VS Code
If you use the "Search" magnifying class on the left sidebar, and
search for "position" it shows the occurrences in every file. You can
click to see the usage in context.
::::

::::{group-tab} Command line
`grep` is the command line tool that searches for lines matching a term
```console
$ git grep position          # only the lines
$ git grep -C 3 position     # three lines of context
$ git grep -i position       # case insensitive
```
::::

:::::


### (5) Who modified a particular line last and when?

This is called the "annotate" or "blame" view. The name "blame"
is very unfortunate, but it is the standard term for historical reasons
for this functionality and it is not meant to blame anyone.

:::::{tabs}

::::{group-tab} GitHub
From a file view, change preview to "Blame" towards the top-left.
To get the actual commit, click on the commit message next
to the code line that you are interested in.
::::

::::{group-tab} VS Code
This requires an extension.  We recommend for now you use the command
line version, after opening a terminal.
::::

::::{group-tab} Command line
These two commands are similar but have slightly different output.
```console
$ git annotate simulate.py
$ git blame simulate.py
```
::::

:::::--->
## Creating branches and commits

The first and most basic task to do in Git is **record changes** using
commits. In this part, we will record changes in two
ways: on a **new branch** (which supports multiple lines of work at once), and directly
on the "main" branch (which happens to be the default branch here).

The goal is to:
- Record new changes to our own copy of Balmorel.
- Understand adding changes in two separate branches.
- See how to compare different versions or branches.


## Background

- Each **commit** is a snapshot of the entire project at a certain
  point in time and has a unique identifier (**hash**) .
- A **branch** is a line of development, and the `main` branch or `master` branch
  are often the default branch in Git.
- A branch in Git is like a **sticky note that is attached to a commit**. When we add
  new commits to a branch, the sticky note moves to the new commit.
- **Tags** are a way to mark a specific commit as important, for example a release
  version. They are also like a sticky note, but they don't move when new
  commits are added.

## Exercise: Creating branches and commits

:::{admonition} Exercise: Practice creating commits and branches (20 min)
1. First create a new branch and then modify an
   existing file and commit the change.  Make sure that you now work **on your
   copy** of the repository. You can for example change the years in the simulation by editing the `YYY.inc` file.
1. In a new commit, modify the file again.
1. Switch to the `main` branch and create a commit there.
1. Browse the network and locate the commits that you just created ("Insights" -> "Network").
1. Compare the branch that you created with the `main` branch. Can you find an easy way to see the differences?
:::
<!---
The solution below goes over most of the answers, and you are
encouraged to use it when the hints aren't enough - this is by
design.


## Solution and walk-through


### (1) Create a new branch and a new commit

:::::{tabs}
::::{group-tab} GitHub
1. Where it says "main" at the top left, click, enter a new branch
   name (e.g. `new-tutorial`), then click on
   "Create branch ... from main".
1. Make sure you are still on the `new-tutorial` branch (it should say
   it at the top), and click "Add file" → "Create new file" from the
   upper right.
1. Enter a filename where it says "Name your file...".
1. Share some Git or programming trick you like.
1. Click "Commit changes"
1. Enter a commit message. Then click "Commit
   changes".

You should appear back at the file browser view, and see your
modification there.
::::

::::{group-tab} VS Code
1. Make sure that you are on the main branch.
1. Version control button on left sidebar → Three dots in upper right of source control → Branch → Create branch.
1. VS Code automatically switches to the new branch.
4. Create a new file.
4. In the version control sidebar, click the `+` sign to add the file for the next commit.
4. Enter a brief message and click "Commit".
::::

::::{group-tab} Command line
Create a new branch called `new-tutorial` from `main` and switch to it:
```console
$ git switch --create new-tutorial main
```

Then create the new file. Finally add and commit the file:
```console
$ git add tutorial.md  # or a different file name
$ git commit -m "sharing a programming trick"
```
::::
:::::


### (2) Modify the file again with a new commit

:::::{tabs}
::::{group-tab} GitHub
This is similar to before, but we click on the existing file to
modify.

1. Click on the file you added or modified previously.
2. Click the edit button, the pencil icon at top-right.
3. Follow the "Commit changes" instructions as in the previous step.
::::

::::{group-tab} VS Code
Repeat as in the previous step.
::::

::::{group-tab} Command line
Modify the file. Then commit the new change:
```console
$ git add tutorial.md
$ git commit -m "short summary of the change"
```

Make sure to replace "short summary of the change" with a meaningful commit
message.
::::
:::::


### (3) Switch to the main branch and create a commit there

:::::{tabs}
::::{group-tab} GitHub
1. Go back to the main repository page (your user's page).
1. In the branch switch view (top left above the file view), switch to
   `main`.
1. Modify another file that already exists, following the pattern
   from above.
::::

::::{group-tab} VS Code
Use the branch selector at the bottom to switch back to the main branch.  Repeat the same steps as above,
but this time modify a different file.
::::

::::{group-tab} Command line
First switch to the `main` branch:
```console
$ git switch main
```

Then modify a file. Finally `git add` and then commit the change:
```console
$ git commit -m "short summary of the change"
```
::::
:::::


### (4) Browse the commits you just made

Let's look at what we did.  Now, the `main` and the new branches
have diverged: both have some modifications. Try to find the commits
you created.

:::::{tabs}
::::{group-tab} GitHub
Insights tab → Network view (just like we have done before).
::::

::::{group-tab} VS Code
This requires an extension.  Opening the VS Code terminal lets you use the
command line method (View → Terminal will open a terminal at bottom).  This is
a normal command line interface and very useful for work.
::::

::::{group-tab} Command line
```console
$ git graph
$ git log --graph --oneline --decorate --all  # if you didn't define git graph yet.
```
::::
:::::


### (5) Compare the branches

Comparing changes is an important thing we need to do.  When using the
GitHub view only, this may not be so common, but we'll show it so that
it makes sense later on.

:::::{tabs}

::::{group-tab} GitHub
A nice way to compare branches is to add `/compare` to the URL of the repository,
for example (replace USER):
https://github.com/**USER**/planets/compare
::::

::::{group-tab} VS Code
This seems to require an extension.  We recommend you use the command line method.
::::

::::{group-tab} Command line
```console
$ git diff main new-tutorial
```

Try also the other way around:
```console
$ git diff new-tutorial main
```

Try also this if you only want to see the file names that are different:
```console
$ git diff --name-only main new-tutorial
```
::::
:::::


### (6) Compare two arbitrary commits

This is similar to above, but not only between branches.

:::::{tabs}
::::{group-tab} GitHub
Following the `/compare`-trick above, one can compare commits on GitHub by
adjusting the following URL:
https://github.com/**USER**/planets/compare/**VERSION1**..**VERSION2**

Replace `USER` with your username and `VERSION1` and `VERSION2` with a commit hash or branch name.
Please try it out.
::::

::::{group-tab} VS Code
Again, we recommend using the Command Line method.
::::

::::{group-tab} Command line
First try this to get a short overview of the commits:
```console
$ git log --oneline
```

Then try to compare any two commit identifiers with `git diff`.
::::
:::::


### (7) Renaming a branch

:::::{tabs}
::::{group-tab} GitHub

Branch button → View all branches → three dots at right side → Rename branch.

::::
::::{group-tab} VS Code
Version control sidebar → Three dots (same as in step 2) → Branch → Rename branch.  Make sure you are on the right branch before you start.
::::

::::{group-tab} Command line
Renaming the current branch:
```console
$ git branch -m new-branch-name
```

Renaming a different branch:
```console
$ git branch -m different-branch new-branch-name
```
::::
:::::


### (8) Creating a tag

Tags are a way to mark a specific commit as important, for example a release
version. They are also like a sticky note, but they don't move when new
commits are added.

:::::{tabs}
::::{group-tab} GitHub
On the right side, below "Releases", click on "Create a new release".

What GitHub calls releases are actually tags in Git with additional metadata.
For the purpose of this exercise we can use them interchangeably.
::::

::::{group-tab} VS Code
Version control sidebar → Three dots (same as in step 2) → Tags → Create tag.  Make sure you are on the expected commit before you do this.
::::

::::{group-tab} Command line
Creating a tag:
```console
$ git tag -a v1.0 -m "New manuscript version for the pre-print"
```
::::
:::::


## Summary

In this part, we saw how we can make changes to our files.  With branches, we
can track several lines of work at once, and can compare their differences.

- You could commit directly to `main` if there is only one single line
  of work and it's only you.
- You could commit to branches if there are multiple lines of work at
  once, and you don't want them to interfere with each other.
- Tags are useful to mark a specific commit as important, for example a
  release version.
- In Git, commits form a so-called "graph". Branches are tags in Git function
  like sticky notes that stick to specific commits. What this means for us is
  that it does not cost any significant disk space to create new branches.
- Not all files should be added to Git. For example, temporary files or
  files with sensitive information or files which are generated as part of
  the build process should not be added to Git. For this we use
  `.gitignore` (more about this later: {ref}`practical-advice`).
- Unsure on which branch you are or what state the repository is in?
  On the command line, use `git status` frequently to get a quick overview.
--->

(merging)=

## Merging changes and contributing to the project

Git allows us to have different development lines where we can try things out.
It also allows different people to work on the same project at the same.  This
means that we have to somehow combine the changes later. In this part we will
practice this: **merging**.

Goals for this section:
- Understand that on GitHub merging is done through a **pull request** (on GitLab: "merge request"). Think
  of it as a **change proposal**.
- Create and merge a pull request within your own repository.
- Understand (and optionally) do the same across repositories, to contribute to
  the upstream public repository.


## Exercise


::::::{admonition} Exercise: Merging branches
:::::{tabs}
::::{group-tab} GitHub

First, we make something called a pull request, which allows
review and commenting before the actual merge.

We assume that in the previous exercise you have created a new branch with one
or few new commits.  We provide basic hints. You should refer to the solution
as needed.

1. Navigate to your branch from the previous exercise
   (hint: the same branch view we used last time).

1. Begin the pull request process
   (hint: There is a "Contribute" button in the branch view).

1. Add or modify the pull request title and description, and verify the other data.
   In the pull request verify the target repository and the target
   branch. Make sure that you are merging within your own repository.
   **GitHub: By default, it will offer to make the change to the
   upstream repository, `balmorelcommunity`.  You should change this**, you
   shouldn't contribute your commit(s) upstream yet.  Where it says
   `base repository`, select your own repository.

1. Create the pull request by clicking "Create pull request". Browse
   the network view to see if anything has changed yet.

1. Merge the pull request, or if you are not on GitHub you can merge
   the branch locally. Browse the network again. What has changed?

1. Find out which branches are merged and thus safe to delete. Then remove them
   and verify that the commits are still there, only the branch labels are
   gone (hint: you can delete branches that have been merged into `main`).

1. Optional: Try to create a new branch with a new change, then open a pull
   request but towards the original (upstream) repository. We will later merge few of
   those.
::::

::::{group-tab} Local (VS Code, Command line)

When working locally, it's easier to merge branches: we can just do
the merge, without making a pull request.  But we don't have that step
of review and commenting and possibly adjusting.

1. Switch to the `main` branch that you want to merge the *other*
   branch into. (Note that this is the other way around from the
   GitHub path).

Then:

5. Merge the other branch into `main` (which is then your current branch).

6. Find out which branches are merged and thus safe to delete. Then remove them
   and verify that the commits are still there, only the branch labels are
   gone. (Hint: you can delete branches that have been merged into `main`).

7. Optional: Try to create a new branch, and make a
   GitHub pull request with your change, and contribute it to our
   upstream repository.
::::
:::::
::::::
<!---
The solution below goes over most of the answers, and you are
encouraged to use it when the hints aren't enough - this is by design.


## Solution and walk-through

### (1) Navigate to your branch

Before making the pull request, or doing a merge, it's important to
make sure that you are on the right branch.  Many people have been
frustrated because they forgot this!

:::::{tabs}
::::{group-tab} GitHub
GitHub will notice a recently changed branch and offer to make a pull request (clicking there will bring you to step 3):
   :::{figure} img/merging/github-compare-and-pr.png
   :alt: Screenshot on GitHub suggesting to compare and make a pull request.
   :width: 80%
   :class: with-border
   :::

If the yellow box is not there, make sure you are on the branch you want to
merge **from**:
   :::{figure} img/merging/github-navigate-to-branch.png
   :alt: Screenshot on GitHub where we navigate to the branch we wish to merge.
   :width: 80%
   :class: with-border
   :::
::::

::::{group-tab} VS Code
Remember, you need to switch to the `main` branch, the branch we want to merge **to**.
This is different from the GitHub path.
::::

::::{group-tab} Command line
Remember, you need to switch to the `main` branch, the branch we want to merge **to**.
This is different from the GitHub path:
```console
$ git switch main
```
::::
:::::


(create-pull-request)=

### (2) Begin the pull request process

In GitHub, the pull request is the way we propose to merge two
branches together.  We start the process of making one.

:::::{tabs}
::::{group-tab} GitHub
   :::{figure} img/merging/github-contribute.png
   :alt: Screenshot on GitHub where we get to the pull request process.
   :width: 80%
   :class: with-border
   :::
::::

::::{group-tab} VS Code
It is possible to open pull requests from the editor, but
we don't cover that here.

If you are working locally, continue to step 5.
::::

::::{group-tab} Command line
It is possible to open pull requests from the command line, but
we don't cover that here.

If you are working locally, continue to step 5.
::::
:::::


### (3) Fill out and verify the pull request

Check that the pull request is directed to the right repository and branch
and that it contains the changes that you meant to merge.

:::::{tabs}
::::{group-tab} GitHub
Things to check:
- Base repository: this should be your own
- Title: make it descriptive
- Description: make it informative
- Scroll down to see commits: are these the ones you want to merge?
- Scroll down to see the changes: are these the ones you want to merge?
   :::{figure} img/merging/github-comparing-changes.png
   :alt: Screenshot on GitHub where we verify the changes we want to merge.
   :width: 80%
   :class: with-border

   This screenshot only shows the top part. If you scroll down, you
   can see the commits and the changes. We recommend to do this before
   clicking on "Create pull request".
   :::
::::

::::{group-tab} VS Code
If you are working locally, continue to step 5.
::::

::::{group-tab} Command line
If you are working locally, continue to step 5.
::::
:::::


### (4) Create the pullhfbjhsbf request

We actually create the pull request.  Don't forget to navigate to the Network
view after opening the pull request.  Note that the changes proposed in the
pull request are not yet merged.

:::::{tabs}
::::{group-tab} GitHub
Click on the green button "Create pull request".

If you click on the little arrow next to "Create pull request", you can also
see the option to "Create draft pull request". This will be interesting later
when collaborating with others. It allows you to open a pull request that is
not ready to be merged yet, but you want to show it to others and get feedback.
::::

::::{group-tab} VS Code
It is possible to create pull requests from the editor, but
we don't cover that here.

If you are working locally, continue to step 5.
::::

::::{group-tab} Command line
It is possible to create pull requests from the command line, but
we don't cover that here.

If you are working locally, continue to step 5.
::::
:::::


### (5) Merge the pull request

Now, we do the actual merging. We see some effects now.

:::::{tabs}
::::{group-tab} GitHub
Review it again (commits and changes), and then click "Merge pull request".

After merging, verify the network view. Also navigate then to your "main"
branch and check that your change is there.
::::

::::{group-tab} VS Code
Just like with the command line, when we merge we modify our *current* branch.  Verify you are on the `main` branch.

1. Verify current branch at the bottom.
1. From the version control sidebar → Three dots → Branch → Merge.
1. In the selector that comes up, choose the branch you want to merge *from*.
   The commits on that branch will be added to the current branch.
::::

::::{group-tab} Command line
On the command line, when we merge, we always modify our *current* branch.

If you are not sure anymore what your current branch is, type:
```console
$ git branch
```
... or equally useful to see where we are right now:
```console
$ git status
```

In this case we merge the `new-tutorial` branch into our current branch:
```console
$ git merge new-tutorial
```
::::
:::::


### (6) Delete merged branches

Before deleting branches, first check whether they are merged.

If you delete an un-merged branch, it will be difficult to find the commits
that were on that branch. If you delete a merged branch, the commits are now
also part of the branch where we have merged to.

:::::{tabs}
::::{group-tab} GitHub
One way to delete the branch is to click on the "Delete branch" button after the pull
request is merged:
   :::{figure} img/merging/github-merged.png
   :alt: Screenshot on GitHub suggesting us to delete a branch after it has been merged.
   :width: 80%
   :class: with-border
   :::

But what if we forgot? Then navigate to the branch view:
   :::{figure} img/merging/github-branches.png
   :alt: Screenshot on GitHub where we navigate to the branches view.
   :width: 80%
   :class: with-border
   :::

In the overview we can see that it has been merged and we can delete it.
::::

::::{group-tab} VS Code
From the Source Control sidebar → the three dots (as before) → Branch → Delete Branch.  Select the branch name to delete.
::::

::::{group-tab} Command line
Verify which branches are merged to the current branch:
```console
$ git branch --merged

* main
  new-tutorial
```

This means that it is safe to delete the `new-tutorial` branch:
```console
$ git branch -d new-tutorial
```

Verify then that the branch is gone but that the commits are still there:
```console
$ git branch
$ git log --oneline
```
::::
:::::


### (7) Contribute to the original repository with a pull request

This is an advanced step. We will practice this tomorrow and
it is OK to skip this at this stage.

:::::{tabs}
::::{group-tab} GitHub
Now that you know how to create branches and opening a pull request, try to
open a new pull request with a new change but this time the base repository
should be the upstream one.

In other words, you now send a pull request **across repositories**: from your fork
to the original repository.

Another thing that is different now is that you might not have permissions to
merge the pull request.  We can then together review and browse the pull
request.
::::

::::{group-tab} VS Code
Not described. We will return to this when we discuss collaboration using GitHub.

You would create a new branch locally like above, push it to GitHub to your own
user's repository, and from there open a pull request towards the upstream
repository.
::::

::::{group-tab} Command line
Not described. We will return to this when we discuss collaboration using GitHub.

You would create a new branch locally like above, push it to GitHub to your own
user's repository, and from there open a pull request towards the upstream
repository.
::::
:::::


## Summary

- We learned how to merge two branches together.
- When is this useful? This is not only useful to combine development lines in
  your own work. Being able to merge branches also **forms the basis for collaboration**.
- Branches which are merged to other branches are safe to delete, since we only
  delete the "sticky note" next to a commit, not the commits themselves.
  --->
