#!/usr/bin/env python
# coding: utf-8

# (getting-started-with-python)=
# # Getting Started with Python

# >*Robots are nice to work with.*
# >
# >--Roger Zelazny [^note1]
# 
# [^note1]: Source: *Dismal Light* (1968).

# In this chapter I'll discuss how to get started in Python. I will have very little to say about how to [download and install Python](https://www.python.org/downloads/), because there are so many different ways to do this, with new advances coming out so often, that almost anything I say will be out of date as soon as I push the publish button on this chapter. Instead, most of the chapter will be focused on getting you started typing Python commands. Our goal in this chapter is not to learn any statistical concepts: we're just trying to learn the basics of how Python works and get comfortable interacting with the system. To do this, we'll spend a bit of time using Python as a simple calculator, since that's arguably the easiest thing to do with Python. In doing so, you'll get a bit of a feel for what it's like to work in Python. From there I'll introduce some very basic programming ideas: in particular, I'll talk about the idea of defining *variables* to store information, and a few things that you can do with these variables. 
# 
# However, before going into any of the specifics, it's worth talking a little about why you might want to use Python at all. Given that you're reading this, you've probably got your own reasons. However, if those reasons are "because that's what my stats class uses", it might be worth explaining a little why your lecturer has chosen to use Python for the class. Of course, I don't really know why *other* people choose Python, so I'm really talking about why I use it.
# 
# - It's sort of obvious, but worth saying anyway: doing your statistics on a computer is faster, easier and more powerful than doing statistics by hand. Computers excel at mindless repetitive tasks, and a lot of statistical calculations are both mindless and repetitive. For most people, the only reason to ever do statistical calculations with pencil and paper is for learning purposes. In my class I do occasionally suggest doing some calculations that way, but the only real value to it is pedagogical. It does help you to get a "feel" for statistics to do some calculations yourself, so it's worth doing it once. But only once!
# - Doing statistics in a spreadsheet (e.g., Microsoft Excel) is generally a bad idea in the long run. Although many people are likely to feel more familiar with them, spreadsheets are very limited in terms of what analyses they allow you do. Furthermore, because of "features" like auto-formatting, if you're not careful, [spreadsheet programs can really mess up your data](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-1044-7). If you get into the habit of trying to do your real life data analysis using spreadsheets, then you've dug yourself into a very deep hole.
# - Avoiding proprietary software is a very good idea. There are a lot of commercial packages out there that you can buy, some of which I like and some of which I don't. They're usually very glossy in their appearance, and generally very powerful (much more powerful than spreadsheets). However, they're also very expensive: usually, the company sells "student versions" (versions that are but shadowy husks of the real thing) very cheaply; they sell full powered "educational versions" at a price that makes me wince; and they sell commercial licences with a staggeringly high price tag. The business model here is to suck you in during your student days, and then leave you dependent on their tools when you go out into the real world. It's hard to blame them for trying, but personally I'm not in favour of shelling out thousands of dollars if I can avoid it. And you can avoid it: if you make use of tools like Python that are open source and free, you never get trapped having to pay exorbitant licensing fees. 
# - Something that you might not appreciate now, but will love later on if you do anything involving data analysis, is the fact that Python is highly extensible. When you download and install Python, you get all the basic "modules", and those are very powerful on their own. However, because Python is so open and so widely used, it's become something of a standard tool in statistics, and so lots of people write their own packages that extend the system. And these are freely available too. One of the consequences of this, I've noticed, is that if you look at people doing advanced work in statistical analysis, especially in the fields of machine learning and natural language processing, a *lot* of them use Python. In other words, if you learn how to do your basic statistics in Python, then you're a lot closer to being able to use the state of the art methods than you would be if you'd started out with a "simpler" system: so if you want to become a genuine expert in psychological data analysis, learning Python is a very good use of your time.
# - Related to the previous point: Python is a real programming language. As you get better at using Python for data analysis, you're also learning to program. To some people this might seem like a bad thing, but in truth, programming is a core research skill across a lot of the social and behavioural sciences. Think about how many surveys and experiments are done online, or presented on computers. Think about all those online social environments which you might be interested in studying; and maybe collecting data from in an automated fashion. Think about artificial intelligence systems, computer vision, "data science" and speech recognition. If any of these are things that you think you might want to be involved in -- as someone "doing research in psychology", that is -- you'll need to know a bit of programming. And if you don't already know how to program, then learning how to do statistics using Python is a nice way to start.
# 
# Those are the main reasons I use Python. It's not without its flaws: although it is relatively easy to learn, as programming languages go, it is a lot harder to learn than Excel, and it has a few very annoying quirks to it that we're all pretty much stuck with, but on the whole I think the strengths outweigh the weakness.
# 

# ## Installing Python
# 
# Ok, I said I wasn't going to say much about [installing Python](https://www.python.org/downloads/), and I'm not. If you are reading this text for a course, then presumably your instructor has a particular way they would like you to access Python. If not, it is not difficult to find instructions for installing Python on your machine. A further complication is the installation of "modules" or "packages". Much of the power of Python comes not only from the language itself, but from the massive library of freely availabe code which others have written and made available for all of us to use. Although Python has an extremely rich ecosystem of packages available, it has not yet (as of this writing) really settled on a single way to distribute these packages. This can be frustrating, when you need to install some bit of code to do your analysis. Again, there are a variety of solutions available, such as [Anaconda](https://www.anaconda.com), and your instructor can likely help you with this. In this text, I have very consciously tried to limit the number of packages needed to a few of the very most common needed for data analysis: `numpy`, `scipy`, `pandas` and `seaborn`. These should all be relatively easy to access, and should be relatively stable.
# 
# Alternatively, you could use a cloud interface, like Google CoLab, although be aware that this requires you to upload any data that you may be analyzing to Google, so this should never be used for any sensitive data of any kind, especially if your data has any sort of information that could be used to identify your participants. If at all in doubt, it is always safer to keep your data safely enrypted on your own machine.
# 
# In addition to the various ways to install Python, there are also a variety of ways to send commands to Python. Although you may eventually want to simply write your Python code in a text file, and run it directly from the command line of your computer, a much easier way to interact with Python is either using a so-called IDE (Integrated Development Environment), which is a kind of software whose role in life is to make it easier for you to write Python code, or using an interactive web application like [Jupyter Notebooks](https://jupyter.org). Unless your instructor tells you otherwise, I strongly reccomend Jupyter Notebooks as the best way to get started writing Python code. This book was written in Jupyter Notebooks, and assembled using [Jupyter Book](https://jupyterbook.org/intro.html)

# ## Using the code in this book
# 
# Most of the code in this book should be usable no matter what environment you are using. I have tried to make the blocks of code in this book as self-sufficient as possible, so that you can simply copy/paste into your own Python interface. In practice, this means I have (as much as I remember to) imported the necessary modules into each block of code, even when this wasn't necessary for the code to run, although here and there I have deviated from this, when I though it was clear that I was showing a series of commands to be run right after each other.
# 
# Although most of the time you should be able to copy and paste the code from this book, there is one exception: in order to make figures with captions that I can link to elsewhere in the text, I have used a function called `glue`. Anywhere you see a line of code with `glue` in it, you can probably just ignore it: it's just there to make this book work right, and doesn't have anything to do with the code you will need for analysing data.

# (firstcommand)=
# 
# ## Typing commands at the Python console
# 
# One of the easiest things you can do with Python is use it as a simple calculator, so it's a good place to start. For instance, try typing `10 + 20`, and hitting enter.[^note2] When you do this, you've entered a ***command***, and Python will "execute" that command. If you are using Jupyter Notebooks, what you will see on screen will look something like this:
# 
# [^note2]: Seriously. If you're in a position to do so, open up Python and start typing. The simple act of typing it rather than "just reading" makes a big difference. It makes the concepts more concrete, and it ties the abstract ideas (programming and statistics) to the actual context in which you need to use them. Statistics is something you *do*, not just something you read about in a textbook.

# In[1]:


10 + 20


# Not a lot of surprises in this extract. But there's a few things worth talking about, even with such a simple example. Firstly, it's important that you understand how to read the extract. In this example, what *I* typed was the `10 + 20` part. Obviously, the correct answer to the sum `10 + 20` is `30`, and not surprisingly Python has printed that out as part of its response. But if you are using Jupyter Notebooks, you will probably also see something like `In [1]` and `Out [2]` part, which probably doesn't make a lot of sense to you right now. You're going to see that a lot. I'll talk about what this means in a bit more detail later on, but for now you can think of `Out [1]: 30` as if Python were saying "the answer to the 1st question you asked is 30". That's not quite the truth, but it's close enough for now. And in any case it's not really very interesting at the moment: we only asked Python to calculate one thing, so obviously there's only one answer printed on the screen. Later on this will change, and the `[1]` part will start to make a bit more sense. For now, I just don't want you to get confused or concerned by it. 

# ### Be very careful to avoid typos
# 
# Before we go on to talk about other types of calculations that we can do with R, there's a few other things I want to point out. The first thing is that, while Python is good software, it's still software. It's pretty stupid, and because it's stupid it can't handle typos. It takes it on faith that you meant to type *exactly* what you did type. For example, suppose that you hit the wrong key when trying to type `+`, and as a result your command ended up being `10 = 20` rather than `10 + 20`. Here's what happens:

# In[2]:


10 = 20


# What's happened here is that Python has attempted to interpret `10 = 20` as a command, and spits out an error message because the command doesn't make any sense to it. When a *human* looks at this, and then looks down at their keyboard and sees that `+` and `=` are on the same key (depending on what country your keyboard is from, of course), it's pretty obvious that the command was a typo. But Python doesn't know this, so it gets upset. And, if you look at it from its perspective, this makes sense. All that Python "knows" is that `10` is a legitimate number, `20` is a legitimate number, and `=` is a legitimate part of the language too. In other words, from its perspective this really does look like the user meant to type `10 = 20`, since all the individual parts of that statement are legitimate and it's too stupid to realise that this is probably a typo. Therefore, Python takes it on faith that this is exactly what you meant... it only "discovers" that the command is nonsense when it tries to follow your instructions, typo and all. And then it whinges, and spits out an error.

# Even more subtle is the fact that some typos won't produce errors at all, because they happen to correspond to "well-formed" Python commands. For instance, suppose that not only did I forget to hit the shift key when trying to type `10 + 20`, I also managed to press the key next to one I meant do. The resulting typo would produce the command `10 - 20`. Clearly, Python has no way of knowing that you meant to *add* 20 to 10, not *subtract* 20 from 10, so what happens this time is this:

# In[3]:


10 - 20


# In this case, Python produces the right answer, but to the the wrong question. 
# 
# To some extent, I'm stating the obvious here, but it's important. The people who wrote Python are smart. You, the user, are smart. But Python itself is dumb. And because it's dumb, it has to be mindlessly obedient. It does *exactly* what you ask it to do. There is  no equivalent to "autocorrect" in Python, and for good reason. When doing advanced stuff -- and even the simplest of statistics is pretty advanced in a lot of ways -- it's dangerous to let a mindless automaton like Python try to overrule the human user. But because of this, it's your responsibility to be careful. Always make sure you type *exactly what you mean*. When dealing with computers, it's not enough to type "approximately" the right thing. In general, you absolutely *must* be precise in what you say to Python ... like all machines it is too stupid to be anything other than absurdly literal in its interpretation.

# ### Python is (a teeny bit) flexible with spacing
# 
# Of course, now that I've been so uptight about the importance of always being precise, I should point out that there are some exceptions. Or, more accurately, there are some situations in which Python does show a bit more flexibility than my previous description suggests. One thing Python is smart enough to do is ignore redundant spacing. What I mean by this is that, when I typed `10 + 20` before, I could equally have done this

# In[4]:


10+                            20


# or this

# In[5]:


10+20


# and I would get exactly the same answer. However, by now the people reading this who are already familiar with Python are howling in anger at my characterization of Python as flexible with spacing, because there are other ways in which Python is *notoriously* inflexible when it comes to spaces. In certain (ok, in very many) situations, Python cares a *lot* about where there are and are not spaces, and how many spaces there are. We will get to these situations later, but for now just be aware that although Python is fairly liberal when it comes to spaces within a line of code, it is zealously conservative when it comes to indenting lines of code. There are strict rules for when and how lines of code are to be indented in Python, and Python will enforce these rules with an iron fist.

# Whether you use `10+20` or `10 + 20` is a matter of preference. Personally, I prefer to put the spaces in, because I like the way it looks better, but I will probably write it both ways in this book. Sometimes I get lazy and leave the spaces out.

# (arithmetic)=
# 
# ## Doing simple calculations with Python
# 
# Okay, now that we've discussed some of the tedious details associated with typing Python commands, let's get back to learning how to use some of the most powerful piece of statistical software in the world as a \$2 calculator. So far, all we know how to do is addition. Clearly, a calculator that only did addition would be a bit stupid, so I should tell you about how to perform other simple calculations using Python. But first, some more terminology. Addition is an example of an "operation" that you can perform (specifically, an arithmetic operation), and the ***operator*** that performs it is `+`. To people with a programming or mathematics background, this terminology probably feels pretty natural, but to other people it might feel like I'm trying to make something very simple (addition) sound more complicated than it is (by calling it an arithmetic operation). To some extent, that's true: if addition was the only operation that we were interested in, it'd be a bit silly to introduce all this extra terminology. However, as we go along, we'll start using more and more different kinds of operations, so it's probably a good idea to get the language straight now, while we're still talking about very familiar concepts like addition! 

# ### Adding, subtracting, multiplying and dividing
# 
# So, now that we have the terminology, let's learn how to perform some arithmetic operations in R. To that end, the table below lists the operators that correspond to the basic arithmetic we learned in primary school: addition, subtraction, multiplication and division.

# |  operation  | operator | example input | example output |
# | :---------: | :------: | :-----------: | :------------: |
# |  addition   |    +     |    10 + 2     |       12       |
# | subtraction |    -     |     9 - 3     |       6        |
# | multiplication |  *    |     5 * 5     |       25       |
# |  division   |    /     |    10 / 3     |       3.333    |
# |    power    |    **    |     5 ** 2    |       25       |
# 

# As you can see, Python uses fairly standard symbols to denote each of the different operations you might want to perform: addition is done using the `+` operator, subtraction is performed by the `-` operator, and so on. So if I wanted to find out what 57 times 61 is (and who wouldn't?), I can use Python instead of a calculator, like so:

# In[6]:


57 * 61


# So that's handy.
# 
# ### Taking powers
# 
# 
# The first four operations listed above are things we all learned in primary school, but they aren't the only arithmetic operations built into Python. There are three other arithmetic operations that I should probably mention: taking powers, doing integer division, and calculating a modulus. Of the three, the only one that is of any real importance for the purposes of this book is taking powers, so I'll discuss that one here.
# 
# For those of you who can still remember your high school maths, this should be familiar. But for some people high school maths was a long time ago, and others of us didn't listen very hard in high school. It's not complicated. As I'm sure everyone will probably remember the moment they read this, the act of multiplying a number $x$ by itself $n$ times is called "raising $x$ to the $n$-th power". Mathematically, this is written as $x^n$. Some values of $n$ have special names: in particular $x^2$ is called $x$-squared, and $x^3$ is called $x$-cubed. So, the 4th power of 5 is calculated like this:
# 
# $$
# 5^4 = 5 \times 5 \times 5 \times 5 
# $$

# One way that we could calculate $5^4$ in Python would be to type in the complete multiplication as it is shown in the equation above. That is, we could do this

# In[7]:


5 * 5 * 5 * 5


# but it does seem a bit tedious. It would be very annoying indeed if you wanted to calculate $5^{15}$, since the command would end up being quite long. Therefore, to make our lives easier, we use the power operator instead. When we do that, our command to calculate $5^4$ goes like this:

# In[8]:


5 ** 4


# Much easier.[^note3]
# 
# [^note3]: In fact, Python has two other ways to calculate powers. We could also have written `pow(5,4)`, or imported the `math` module and then written `math.pow(5,4)`. If you try this, you will see that a key difference is that `math.pow` will always return a number with a decimal place. In computer speak, `math.pow()` converts the numbers you enter into it into "floating-point values". Just FYI.

# (bedmas)=
# 
# ### Doing calculations in the right order
# 
# Okay. At this point, you know how to take one of the most powerful pieces of statistical software in the world, and use it as a \$2 calculator. And as a bonus, you've learned a few very basic programming concepts. That's not nothing (you could argue that you've just saved yourself \$2) but on the other hand, it's not very much either. In order to use Python more effectively, we need to introduce more programming concepts.
# 
# In most situations where you would want to use a calculator, you might want to do multiple calculations. Python lets you do this, just by typing in longer commands. [^note4] In fact, we've already seen an example of this earlier, when I typed in `5 * 5 * 5 * 5`. However, let's try a slightly different example:
# 
# [^note4]: If you're reading this with Python open, a good learning trick is to try typing in a few different variations on what I've done here. If you experiment with your commands, you'll quickly learn what works and what doesn't.

# In[9]:


1 + 2 * 4


# Clearly, this isn't a problem for Python either. However, it's worth stopping for a second, and thinking about what Python just did. Clearly, since it gave us an answer of `9` it must have multiplied `2 * 4` (to get an interim answer of 8) and then added 1 to that. But, suppose it had decided to just go from left to right: if Python had decided instead to add `1+2` (to get an interim answer of 3) and then multiplied by 4, it would have come up with an answer of `12`. 
# 
# To answer this, you need to know the **_order of operations_** that Python uses. If you remember back to your high school maths classes, it's actually the same order that you got taught when you were at school: the "**_BEDMAS_**" order. That is, first calculate things inside **B**rackets `()`, then calculate **E**xponents `**`, then **D**ivision `/` and **M**ultiplication `*`, then **A**ddition `+` and **S**ubtraction `-`. So, to continue the example above, if we want to force Python to calculate the `1+2` part before the multiplication, all we would have to do is enclose it in brackets:

# In[10]:


(1 + 2) * 4 


# This is a fairly useful thing to be able to do. The only other thing I should point out about order of operations is what to expect when you have two operations that have the same priority: that is, how does Python resolve ties? For instance, multiplication and division are actually the same priority, but what should we expect when we give Python a problem like `4 / 2 * 3` to solve? If it evaluates the multiplication first and then the division, it would calculate a value of two-thirds. But if it evaluates the division first it calculates a value of 6. The answer, in this case, is that Python goes from *left to right*, so in this case the division step would come first:

# In[11]:


4 / 2 * 3


# All of the above being said, it's helpful to remember that *brackets always come first*. So, if you're ever unsure about what order Python will do things in, an easy solution is to enclose the thing *you* want it to do first in brackets.  There's nothing stopping you from typing `(4 / 2) * 3`. By enclosing the division in brackets we make it clear which thing is supposed to happen first. In this instance you wouldn't have needed to, since Python would have done the division first anyway, but when you're first starting out it's better to make sure Python does what you want!

# (assign)=
# 
# ## Storing a number as a variable
# 
# One of the most important things to be able to do in Python (or any programming language, for that matter) is to store information in **_variables_**. Variables in Python aren't exactly the same thing as the variables we talked about in the last chapter on research methods, but they are similar. At a conceptual level you can think of a variable as *label* for a certain piece of information, or even several different pieces of information. When doing statistical analysis in Python, all of your data (the variables you measured in your study) will be stored as variables in Python, but as well see later in the book you'll find that you end up creating variables for other things too. However, before we delve into all the messy details of data sets and statistical analysis, let's look at the very basics for how we create variables and work with them. 

# Since we've been working with numbers so far, let's start by creating variables to store our numbers. And since most people like concrete examples, let's invent one. Suppose I'm trying to calculate how much money I'm going to make from this book. There's several different numbers I might want to store. Firstly, I need to figure out how many copies I'll sell. This isn't exactly *Harry Potter*, so let's assume I'm only going to sell one copy per student in my class. That's 350 sales, so let's create a variable called `sales`. What I want to do is assign a **_value_** to my variable `sales`, and that value should be `350`. We do this by using the **_assignment operator_**, which is `=`. Here's how we do it:

# In[12]:


sales = 350


# 
# When you hit enter, Python doesn't print out any output. But behind the scenes, Python has created a new variable, with a range of properties. One of these is that it contains the value `350`. The simplest way to see what is currently stored in a variable is to just write the name of the variable, and hit enter:

# In[13]:


sales


# It might seem obvious, but it is probably worth mentioning anyway, that direction matters here. Whatever is to the right of the `=` sign is assigned to the variable to the left of the `=` sign.

# ### Doing calculations using variables
# 
# Okay, let's get back to my original story. In my quest to become rich, I've written this textbook. To figure out how good a strategy is, I've started creating some variables in Python. In addition to defining a `sales` variable that counts the number of copies I'm going to sell, I can also create a variable called `royalty`, indicating how much money I get per copy. Let's say that my royalties are about \$7 per book:

# In[14]:


sales = 350
royalty = 7


# The nice thing about variables (in fact, the whole point of having variables) is that we can do anything with a variable that we ought to be able to do with the information that it stores. That is, since Python allows me to multiply `350` by `7`

# In[15]:


350 * 7


# it also allows me to multiply `sales` by `royalty`

# In[16]:


sales * royalty


# As far as Python is concerned, the `sales * royalty` command is the same as the `350 * 7` command. Not surprisingly, I can assign the output of this calculation to a new variable, which I'll call `revenue`. And when we do this, the new variable `revenue` gets the value `2450`. So let's do that, and then get Python to print out the value of `revenue` so that we can verify that it's done what we asked:

# In[17]:


revenue = sales * royalty
revenue


# That's fairly straightforward. A slightly more subtle thing we can do is reassign the value of my variable, based on its current value. For instance, suppose that one of my students (no doubt under the influence of psychotropic drugs) loves the book so much that he or she donates me an extra \$550. The simplest way to capture this is by a command like this:

# In[18]:


revenue = revenue + 550
revenue


# In this calculation, Python has taken the old value of `revenue` (i.e., 2450) and added 550 to that value, producing a value of 3000. This new value is assigned to the `revenue` variable, overwriting its previous value. In any case, we now know that I'm expecting to make \$3000 off this. Pretty sweet, I thinks to myself. Or at least, that's what I thinks until I do a few more calculations and work out what the implied hourly wage I'm making off this looks like. 

# In[34]:





# In[ ]:





# In[ ]:




