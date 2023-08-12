#!/usr/bin/python3
import requests
import json 
from bs4 import BeautifulSoup as bs
from dataclasses import dataclass

@dataclass
class Meeting:
    MID: int
    canceled: bool
    starts: str
    room: str
    revisions: [str]

    #Used to split the scraping code into two parts.
    #We break off MID and startDate because they
    
    def __init__(self, MID, startDate, sourceUL):
        pass

def scrape(response) -> [Meeting]:
    soup = bs(response.text,'html.parser')
    contentSection = soup.find(id="contentsection")
    ul_days = contentSection.findChildren("ul")

    def expectedItem():
        """
        Keeps track of whether or not an anchor <a> tag or a list item <li>
        tag is expected to occour next

        returns "a" if the next tag is expected to be an anchor tag
        returns "li" if the next tag is expected to be a list item tag

        throws error if it's unclear which should come next.
        
        """
        
        if len(anchors) == len(listItems):
            return "a"
        if len(anchors) == len(listItems) + 1:
            return "li"
        raise Exception(f"Couldn't parse HTML - too many <{'a'if len(anchors) > len(listItems) else 'li'}> tags")

    meetings = []

    for ul_day in ul_days:
        startDate = ul_days.span
        MID = None #Meeting ID

        for child in ul_day.children:
            if child.name == "a":
                #Ensure we don't have duplicate anchor elements
                if MID is not None: raise RuntimeError (
                    "Didn't find <ul> after <a> tag containing meeting id"
                )

                #Save the Meeting ID
                MID = child.attrs.name

            elif child.name == "ul":
                #Ensure we have a meeting ID
                if MID is None: raise RuntimeError (
                    "Didn't find <a> tag containing meeting id before <ul> tag"
                    "containing meeting details."
                )
                
                #create the meeting object
                meetings.append(Meeting(
                    MID,
                    startDate,
                    sourceUL=child
                ))

                #re-null meeting ID
                MID = None
    
    return meetings
        

    meetings = []
    for meetingID,meetingLI,meetingDate in zip(anchors,listItems,dates):
        meetings