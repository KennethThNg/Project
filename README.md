# Title

# Abstract
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?

The goal of this project is to analyze the mailing exchange of Hillary Clinton. We considere the emails provided by the Kaggle platform (https://www.kaggle.com/kaggle/hillary-clinton-emails). We will focus at first on the Hillary's network to get an understanding with whom she exchanges emails and at which frequency. Afterthat we want to catch the main subjects that she abords with the principal addressers in order to retrieve the kind of relation that she has with them. An analysis of the countries of interest will be provided firstly to see if some are ignored and secondly to catch the major world discussion that she has. We will finally focus on the most frequent countries in building up a lexicography field around them in order to catch the main subject in countries or region. One goal will be to cluster countries based on these lexicographies fields. A large and diversify panel of visualization tools will be provided along all the project in order to illustrate and explain at most the analysis. Thanks to a deep analysis we may have a better understanding of this mailing scandal. One of the goals will be to determine if this scandal was really one according to the subject that we will highlight and if so, in which context.

VVVVVVVVVVV: **REHAN VERSION**

The Hillary Clinton email controversy arising from the use of private email server for official communications during her tenure as Secretary of State hit the headline of the media in 2015. However the content of the emails was not covered properly and reading relevant information related to it remains a difficult task. The goal of this project is to get some insight from the sensitive and sometimes confidential information publicly available on [Kaggle](https://www.kaggle.com/kaggle/hillary-clinton-emails). What was the Hillary's network? Did she use a private server in order to hide illegal actions? Is Hillary the only one responsible of the controversy, who could have report it and did not? Questions are limitless, but we will focus more specifically on two points which we consider to be the base for any analysis: The first step is to create a network based on the metadata of the messages. Besides the (normal) graph which can easily be generated, the dates need to be integrated somehow to relate the emails to world events. The second step required is to classify messages in clusters. We decide to group them by their position on the map: Afghanistan and Pakistan; Europe; Middle East; Africa; East Asia and Pacific.

AAAAAAAAAAA **END REHAN VERSION**

# Research questions
A list of research questions you would like to address during the project.

## General questions
- with who Hillary exchanges emails ? (network)
- what is the frequency exchanges in general ? according to these people ?
- which countries are most addressed ? Are some ignored ?
- what are the main subjects ? according to countries ? according to people ?

## Technical questions
- How can we properly clean the data (handle with rawText) ?
- How can we find the country that the mail is addressed ?
- How can we define the main subjects (define the categories of interest) ?
- Which visualization tools shall we use for countries lexicography fields ? for network representation ? for exchange frequency ? for addressed countries ? etc


# Dataset

We will mostly use the datasets provided by the Kaggle platform, which are as follows:
- Emails.csv: contains raw mails (sender, receiver, date, etc)
- EmailReceivers.csv: contains id of receiver
- Aliases.csv: contains PersonId for aliases
- Persons.csv: contains persons names related to PersonId

The three last datasets will be used principaly to ensure identification of senders, receivers and to group them on an unique key.

The Emails.csv is which of main interest since it contains all informations about the emails:
- Sender
- From
- rawText
- Date
- Cc
- Attachement
- etc

The size of these datasets is not an issue since it is a total of only 51mb. They are all in a .csv format. The rawText are totally included in one cell. The main difficulty will be to understand the structure of the rawText and to extract information to fill missing value or wrong values related to the following features:
- Sender
- Receiver
- Date
- Subject (Start-End of the mail)
- Title
- etc

These features are for the main part provided but we have remarked that they are absolutely not accurate, we have to handle them.
Once this extraction made, one difficulty will be to catch the main information per email (remove common words, text processing (lowcast, stem words, ...), creation of dictionaries related to subject (war, finance, etc)). Data cleaning will be for sure at the core of this project.

We may include external datasets or knowledge: governemantal position of people, sex, world events in timeline, etc. However it is not decided yet if we will include them or not. We have first to deal with the current datasets.



List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

# A list of internal milestones up until project milestone 2

First of all, we have to get a quick and general comprehension of the dataset. We have to understand how rawText in the Emails is structured to catch and extract the major informations of it, namely: Sender, Receiver, Date, Subject, Email (Start-End). Once this made we will be able to start our first steps of our analysis, i.e. data cleaning, text processing, etc.

At this stage, we expect to have cleaning our datasets, it means that all the information (as said before Senders, Receivers, etc) are correct and that the content of each email is processed (lowcast, remove common words, may include words transformation, etc). If all of these is made until the end of project 2, it would be a great start since data cleaning takes generally around 60-80% of the work.

If everything is done before the deadline, we may start to create the necessary functions to get the results according to the list of tasks that we have given in the abstract:

- Create the Hillary's Network (illustrated in a clear point of view including frequency)
- Create a function that maps emails with countries
- Elaborate a list of subjects that are common in emails
- Create a time slider world map according to the frequency of country "apparition" in emails (including relative size per continent..?)
- Elaborate a lexicography field per country or region
- Elaborate relative similarities between countries according to lexicography field
- Reflection on different visualization tools that we can add up to our analysis to make it clearer and enrich it


Add here a sketch of your planning for the next project milestone.

# Questions for TAa

Add here some questions you have for us, in general or project-specific.
