# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file 
* renaming a file
* listing hidden files
* copying a file from one directory to another 


Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 
show current working directory path - **pwd**

creating a directory - **mkdir**

deleting a directory - **rmdir**

creating a file using `touch` command - **touch**

deleting a file - **rm**

renaming a file - **rename**

listing hidden files - **ls -a**

copying a file from one directory to another - **cp**

changing a directory - **cd**

moving a file to another folder or directory - **mv**

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` - **list directory contents of files and directories**

`ls -a` - **list contents including hidden files starting with '."**

`ls -l` - **list contents using the long listing format**

`ls -lh` - **list contents using the long listing format with human readable file size**

`ls -lah` - **list contents using the long format, include hidden files with human readable file size**

`ls -t` - **list contents sorted by time and date**

`ls -Glp` - **list contents in long format including owner info, with long listing format, append '/' indicator for directories** 

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -d - **list contents displaying only directories** 

ls -p - **list contents displaying directories with '/'** 

ls -1 - **list contents displaying each entry on a line** 

ls -u - **lists contents displaying files by the file access time** 

ls -R - **list contents displaying subdirectories as well** 
---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` builds and executes command lines from stanard input.  For exampple, if you have a program that outputs filesnames on standard out and you need to use them as individual arguements for a command, you'd use xargs.

    ie: find /etc -name ".conf" | xargs ls -l

