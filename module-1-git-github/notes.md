# Module 1 — Git & GitHub

**Student:** [Macky S. Maun]
**Date:** [September 27]

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

[So Git is for instance think about a camera that camera takes photo and then here is when Github comes in say that you wanna post that photo so you go to a social media to post that photo that's basically the nutshell of git and github, git is the tool github is the website.]

---

## Key vocabulary (in your own words)

- repository: [The one responsible to hold a link]
- commit: [When you wanna save things]
- branch: [A workspace to work individually and not mess up the main]
- push / pull: [We do push inorder to pull request while pull is for us to get the repo]
- pull request: [The one who has an authority whether to accept the pull request or not]
- merge conflict: [Basically collaborators have this common problem they try to change something in the same line but different branches]

---

## Walking through what I did

[After changing something I press Ctrl + S to save then do git add . after that git commit -m "Key vocabulary" then git push after that I go to my repo to get that pull request then add a description]

```
# PS C:\Users\Macky\Pictures\devnet-maunmacky> git add .
PS C:\Users\Macky\Pictures\devnet-maunmacky> git commit -m "Key vocabulary"
[lesson1 64c896c] Key vocabulary
 1 file changed, 6 insertions(+), 6 deletions(-)
PS C:\Users\Macky\Pictures\devnet-maunmacky> git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 629 bytes | 629.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/maunmacky08/devnet-maunmacky.git
   344efec..64c896c  lesson1 -> lesson1
```

---

## A mistake I made (or one I want to avoid)

[Absolutely make sure whatever branch your naming is the correct one if you did it wrong or accidently do git branch -m insertnamehere then just delete it from the github if you pushed it already]

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
