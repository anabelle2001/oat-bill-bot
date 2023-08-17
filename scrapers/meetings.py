#!/usr/bin/python3
import requests
import json 
import bs4
import re
from dataclasses import dataclass
from itertools import islice
import dateparser

@dataclass
class Meeting:
    MID: int
    canceled: bool = False
    starts: str = "???"
    room: str = "???"
    agendaURL: str = "https://null.invalid/agenda.pdf"
    revisions: [str] = None

    #Used to split the scraping code into two parts.
    #We break off MID and startDate because they
    
    @staticmethod
    def fromHTML(
        MID:       str,
        startDate: str,
        sourceLI:  bs4.Tag
    ) -> 'Meeting': #Can't reference meeting before completed definition,
                    #This fixes that.

        firstChild: bs4.Tag = list(sourceLI.children)[0]
        
        assert \
            firstChild.name == "span", \
            ("Expected first child of <li> tag to be a <span> containing the "
            f"time. got a <'{firstChild.name}'> instead")
        
        givenTimeSTR = firstChild.text
        
        timeMatch: re.Match = re.match(
            r"(\d{1,2}):(\d{2}) ([ap]m)",
            firstChild.text
        )

        if timeMatch is None:
            print("Warning:\nExpected 12-hour time formatted like '9:15 am';"
                 f"got <span>'{firstChild.text}'</span> instead.")
            starts = f"{startDate} '{}'"
        else:
            isPM = timeMatch.group(3) == "pm"
            hr = int(timeMatch.group(1)) + (12 if isPM else 0)
            starts = f"{startDate} {hr:02}:{timeMatch.group(2)}"

        agendaURLTag = sourceLI.select_one("div > a")

        assert agendaURLTag is not None, \
            "Could not find `> div > a` (containing agenda url) in meeting <li>"
        
        agendaURL = f"https://scstatehouse.gov{agendaURLTag.attrs['href']}"

        return Meeting(
            MID,
            starts, #TODO: add date in addition to time
            agendaURL
        )

def scrape(responseText) -> [Meeting]:
    soup = bs4.BeautifulSoup(responseText,'html.parser')
    contentSection = soup.find(id="contentsection")
    ul_days = contentSection.findChildren("ul")

    meetings = []

    for ul_day in ul_days:
        startDate = ul_day.span
        MID = None #Meeting ID

        for child in ul_day.children:
            if child.name == "a":
                #Ensure we don't have duplicate anchor elements
                if MID is not None: raise RuntimeError (
                    "Didn't find <li> after <a> tag containing meeting id"
                )

                #Save the Meeting ID
                MID = child.attrs["name"]

            elif child.name == "li":
                #Ensure we have a meeting ID
                if MID is None: raise RuntimeError (
                    "Didn't find <a> tag containing meeting id before <li> tag"
                    "containing meeting details."
                )
                
                #create the meeting object
                meetings.append(Meeting.fromHTML(
                    MID,
                    startDate,
                    sourceLI=child
                ))

                #re-null meeting ID
                MID = None
    #after parsing the whole page, return the array of meetings
    return meetings
        

    meetings = []
    for meetingID,meetingLI,meetingDate in zip(anchors,listItems,dates):
        meetings