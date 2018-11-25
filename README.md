# Title: Official public work with private tools

# Abstract

The Hillary Clinton email controversy arising from the use of private email server for official communications during her tenure as Secretary of State hit the headline of the media in 2015. However the content of the emails was not covered properly and reading relevant information related to it remains a difficult task. The goal of this project is to get some insight from the sensitive and sometimes confidential information publicly available on [Kaggle](https://www.kaggle.com/kaggle/hillary-clinton-emails). What was the Hillary's network? Did she use a private server in order to hide illegal actions? Is Hillary the only one responsible of the controversy? Questions are limitless, but we will focus more specifically on three points which we consider to be the base for any analysis. The first is related to the creation of the Hillary's network (integrating subjects importance, dates and world events) based on the metadata of the messages. The second step required is to classify messages in clusters. Finally, we decide to include geographical position to find out the most important subjects discuss in some regions and to understand if some regions appear to be more in the core of United States and if so for which context.

# Research questions

## General questions
- with whom does Hillary exchange emails? (network)
- what is the frequency exchanges in general? according to these people?
- which countries are most addressed? Are some ignored?
- what are the main subjects? according to countries? according to people?

## Technical questions
- How can we properly clean the data (handle with rawText)?
- How can we find the country that the mail is addressed?
- How can we define the main subjects (define the categories of interest)?
- Which visualization tools shall we use for countries lexicography fields? for network representation? for exchange frequency? for addressed countries? etc...


# Dataset

_List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant._

Kaggle provides the same data in two different format: four csv files VS one sqlite file. We quickly **over**read both and assume they are the same. The use of sqlite seems to be a better choice since we will manipulate textual combined in a relation entity fashion. The SQL commands to create the schema are provided below:

    -- 7945 returned by the command `COUNT(*)`
    CREATE TABLE Emails (
        Id INTEGER PRIMARY KEY,
        DocNumber TEXT,
        MetadataSubject TEXT,
        MetadataTo TEXT,
        MetadataFrom TEXT,
        SenderPersonId INTEGER,
        MetadataDateSent TEXT,
        MetadataDateReleased TEXT,
        MetadataPdfLink TEXT,
        MetadataCaseNumber TEXT,
        MetadataDocumentClass TEXT,
        ExtractedSubject TEXT,
        ExtractedTo TEXT,
        ExtractedFrom TEXT,
        ExtractedCc TEXT,
        ExtractedDateSent TEXT,
        ExtractedCaseNumber TEXT,
        ExtractedDocNumber TEXT,
        ExtractedDateReleased TEXT,
        ExtractedReleaseInPartOrFull TEXT,
        ExtractedBodyText TEXT,
        RawText TEXT);

    -- 513 returned by the command `COUNT(*)`
    CREATE TABLE Persons (
        Id INTEGER PRIMARY KEY,
        Name TEXT);

    -- 850 returned by the command `COUNT(*)`
    CREATE TABLE Aliases (
        Id INTEGER PRIMARY KEY,
        Alias TEXT,
        PersonId INTEGER);

    -- 9306 returned by the command `COUNT(*)`
    CREATE TABLE EmailReceivers (
        Id INTEGER PRIMARY KEY,
        EmailId INTEGER,
        PersonId INTEGER);

We got these results from this webapp: <https://kripken.github.io/sql.js/GUI/>. A lot of preprocessing is required before working with the data. It will be the main part in the first step of our analysis. We have to deal with the rawText data by removing common words, lowering, stemming, ... We will also likely map emails to countries using regex, create dictionaries for subject recognition. Moreover, in order to relate the emails to events, we will likely use information from online news.

The network graph will be made of 513 vertices. It seems reasonable.

# A list of internal milestones up until project milestone 2

First of all, we have to get a quick and general comprehension of the dataset. We will check the precision of the extraction provided in the sql file before cleaning and processing the textual data we have (e.g. lowercase...). It is worth to mention we will spend most of our time here and not only for this milestone. We estimate it to be 60-80% of the work because we expect the given extraction to be poor.

In parallel, one or two members will work on more elaborate functions:

- Create the Hillary's Network (including the frequency dimension in the edges)
- Mapping an email to countries automatically with the help of a lexicography field per country or region
- Defining a list of subjects appearing recurrently
- Create a time slider world map according to the frequency of country “apparition” in emails (including relative size per continent..?)
- Determining similarities between countries according to lexicography field. For example, we expect Ukraine and Russia to be close to each other
- Reflection on different visualization tools that we can add up to our analysis to make it clearer and enrich it

# Questions for TAa

Can we use libraries like Keras or NLTK?

# Update for milestone 2
## Cleaning
Since we had a first look on the dataset, we notice that the dataset is really dirty and the cleaning process might last longer as expected. We managed first to extract the sender, receivers, subjects but most of these features are missing, then we had to extract these features manually. We observed also that there many aliases to design a person for example 'h' or 'H' stand for 'Hillary' and some words are mispelled. New features were created to help us in our analysis, these features are the different regions where emails were exchanged, these features were created by a method to extract the words in the documents that reveal the region. For example, if Lybia were mentionned, then the email might come from Africa or Middle East. The new created region features are  boolean and indicate the emails origin. We have Africa, Europe, Middle East, Far East, Central Asia, North America, Latin America and Russia. The rawText feature containing the documents has been cleaned, all the characters were transformed in lowercase, the punctuation and redundant words were removed so that we get a feature content which is the cleaned rawText.

## Text analysis
After the first cleaning process, we proceeded on text analysis with observational studies and data visualization. Our first interests were focused on the mails origin and where most of the emails were exchanged. We have noticed that most of the emails came from North America, which seemed to be obvious, and a large part came from middle east which was quite intresting. A graphic according to the date were build and we observed a peak between 2010 and 2012 during the revolution period of the Maghreb. The word's frequency has been also analyzed, this is for the topics extraction of each emails. Wordclouds were also created to get an another visulization of the word's frequency and we used dendogram to visualize the group of emails.

# Expectation for milestone 3

Plan for milestone 3:

    - Create the Hillary's Network.
    - Carry on the text analysis.
    - Create a data story.
