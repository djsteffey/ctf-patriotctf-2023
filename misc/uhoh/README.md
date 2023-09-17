# Uh Oh!
![](images/problem.PNG)

## Files
- provided
    - rockyou.zip
- created
    - None

## Solution
We have a password list file, "rockyou.txt" (inside the provided zip file), and we need to find the phone number that was added.

Let's start by unzipping the provided zip file.
![](images/ss_00.PNG)

Before we just open up the file and start looking for the phone number, let's find out how many lines are in the file.
![](images/ss_01.PNG)

I don't know about you, but I am not manually looking through 14,344,395 lines of a file until I find a phone number!  Is there a way to automate this?  Yes!  We just need to know what a phone number *looks like*.  Fortunately the problem gave us a link to a webpage that shows us what a phone number looks like *and* it even gives us an example.  We can look at the page or follow the example.  Let's just do the latter.
![](images/ss_02.PNG)

Now that we know what a phone number generally looks like, let's use a built-in Kali command to search text for a *pattern*.  In this case it will be a *regular expression* (re) pattern.  The Kail command is `grep` and it will take text input and will search that text for what you tell it to find.  In Kali we can use a pipe to send the contents of the file to `grep` so that we can search the contents of the file.  Now we just need to create the re pattern to match on a phone number.  This is not a tutorial on regular expression syntaxes so you will just have to take my word for this, but the pattern we want to search is `\([0-9]{3}\) [0-9]{3}-[0-9]{4}` which equates to a search for `(xxx) xxx-xxxx` where the `x` is any single digit.
![](images/ss_03.PNG)

We now have the line number and the phone number.

Challenge Complete!
