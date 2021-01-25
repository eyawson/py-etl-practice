# What is it?

An Extract, Transform, Load or ETL for short is a process designed to take data from a source, process it, and insert it to a new destination. This is a very common task that you will may face in career and each one presents it's own individual challenges.

## Extract

Extraction refers to the gathering of data from one or many sources. The source of the data could be one of many things including:

- Database
- API
- File Store
- Documents(ex. CSV)

The data being ingested from your source is likely to not be in a format that is usable or efficient for your use case. This takes us to the next step in the process

## Transform

The transform step of this process is where the magic happens. In the transform step, we will process the data that has been extracted, in preparation of loading into our destination system or data store.

- Cleansing of Data
- Data Verification
- Filtering
- Splitting and Merging

## Load

Loading data is the last step of the process. This is where we move our transformed data to it's final resting place.

- Database
- File Store
- Documents(ex. CSV

## Scenario

You are the newest member of a tabloid media company who specializes in news involving Space and Extra Terrestrials! This company is called "Three Toes and a Spike" and they have enlisted your help in creating a way for them to gather data from SpaceX Launches to provide to their readers. Space X makes their launch data public, and they want to be able to pull specific data and make it usable for their systems to help their analyst to help write stories for the tabloid.

## Requirements

- Get Launch Data from SpaceX([https://api.spacexdata.com/v3/launches](https://api.spacexdata.com/v3/launches))
  - We only need the following data:
  - mission name
  - mission patch image
  - launch year
  - launch success
        - Launch failure details if launch was unsucessful
    - Payload Type
  - Load Data into CSV
