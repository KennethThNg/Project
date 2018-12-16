# Title: Official public work with private tools

# Abstract

The Hillary Clinton email controversy arising from the use of private email server for official communications during her tenure as Secretary of State hit the headline of the media in 2015. However the content of the emails was not covered properly and reading relevant information related to it remains a difficult task. The goal of this project is to get some insight from the sensitive and sometimes confidential information publicly available on [Kaggle](https://www.kaggle.com/kaggle/hillary-clinton-emails). What was the Hillary's network? Did she use a private server in order to hide illegal actions? Is Hillary the only one responsible of the controversy? Questions are limitless, but we will focus more specifically on three points which we consider to be the base for any analysis. The first one is to extract topics covered in the messages. The second one is related to the creation of the Hillary's network based on the metadata of the messages.

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

The network graph will be made of roughly 500 vertices. It seems reasonable.

# Questions for TAa

Can we use libraries like Keras or NLTK? (The answer is yes)

# Contribution of group members

Rehan: RawContent cleaning, recover missing or dirty fields, implementation topics detection, report.

Brice: recover missing or dirty field, fixing duplicated persons, readme for milestone 1, most of the textual description in the notebook, report structure.

Kenneth: plot emails per regions, word cloud, readme for milestone 2, presentation.
