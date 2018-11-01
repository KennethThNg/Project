# Title

# Abstract
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?

The goal of this project is to analyze the mailing exchange of Hillary Clinton. We considere the emails provided by the Kaggle platform. Firstly, we will focus on the Hillary's network to get the information with whom she exchanges and how much. We will then focus more on the principal exchangers and try to understand the main subjects that she abords with them and to present the time frequency of these exchanges. Thanks to precious visualization tools, we will focus deeper on the countries that are the main interest of these exchanges with timeline consideration. Which will be done particularly to find out if some countries are totally ignored. We will finally stretch out a lexicography field for the main countries aborded to understand the core subjects of these.

 

# Research questions
A list of research questions you would like to address during the project. 

## General questions
- with who Hillary exchanges emails ? (network)
- what is the frequency exchanges in general or according to these people ?
- which countries are most addressed ? Are some ignored ?
- what are the main subjects ? according to countries ? according to people ?

## Technical questions
- How can we properly clean the data (handle with rawText) ?
- How can we find the country that the mail is addressed ?
- How can we define the main subjects (define the categories of interest) ? 
- Which visualization tools shall we use for countries lexicography fields ? for network representation ? for exchange frequency ? for addressed countries ? etc


# Dataset

We will mostly use the datasets provided by the Kaggle platform, which are as follows:
-
-
-

The most important one is ... It contains the main informations about the mails: 
- Sender
- From
- rawText
- ...

The size of these datasets is not an issue since it is 51mb. They are essentially on a .csv format. The rawText are totally included in one cell. The main difficulty will be to structure the rawText and to fill the missing value or wrong values related to the following features: 
- Sender
- Receiver
- Date
- Subject (Start-End of the mail)
- Title
- ...
These features are for the main part provided but we have remarked that they are absolutely not accurate, we have to handle them.
After that, one difficulty will be to catch the main informations per mail (remove common words, text processing (lowcast, stem words, ...), creation of dictionary related to subject (war, ...)). Data cleaning will be a main part in this project.

We may include external datasets or knowledge: governemantal position of people, sex, world events in timeline,...



List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

# A list of internal milestones up until project milestone 2

First we will have to do cleaning data, particularly n the rawText features. We will have to extract with precision all the above features (sender, receiver, subject, contain, etc). Once this made we have to clean the contain of mails as described above (remove common words, text processing, etc). With this in our possession we will be able to start a deeper analysis. 
- Create the Hillary's network 
- Create a function that maps mails with countries
- Time series of mailing count, country frequency
- Countries subjects correlation (or even in a graph (connecting two countries containing same subjects), in a spider format, countries are settled according to main subjects)
- Construct the world map with time slider related to mails content
- Find the main subjects (word2vec, categorized mailing (unsupervised analysis), ...)
- Spider map related to categories and frequency of these categories
- Heuristic schema for the X main destinaters (Hillary in the middle, Y components and the X main destinaters are fix in the graph related to their mails exchange content
- Create lexical field related to countries 


Add here a sketch of your planning for the next project milestone.

# Questions for TAa
Add here some questions you have for us, in general or project-specific.
