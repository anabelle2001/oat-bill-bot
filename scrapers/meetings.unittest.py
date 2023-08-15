import unittest
import meetings

def testMeetingProp(
    meetingActual:   meetings.Meeting,
    meetingExpected: meetings.Meeting,
    prop:            str,
    naturalPropName: str = None        
) -> (bool,str):
    """
    Helper method used to test if two meetings share the same property `prop`

    - helps keep testMeetingEquals() [D.R.Y.] - used to compare a property
      and return an explanatory string if the props aren't equal.
      [D.R.Y]: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
    
    TLDR:
    If Meeting()s are equal:
        return (True,"").
    else:
        return (False,explanation:string).
    """

    if naturalPropName == None:
        naturalPropName = prop
        
    if expected[prop] != actual[prop]:
        issues.append(
            f"meetings don't have the same {naturalPropName}"
            f" - expected {expected[prop]}, got {actual[prop]}"
        )
    # End of helper method testProp(...)

def testMeetingEquals( actual: meetings.Meeting,
                       expected: meetings.Meeting ):
    """
    - Used to compare two `class Meeting():` objects

    - Calls unittest.TestCase.assertFalse(True, details) if they are unequal
    
    - `details` Provides details on which fields differ between actual and  
      expected meeting objects
    
    - Suggestion to improve readibility:
      This function should probably be split in two - one to get the list of 
      differeing props, another to assemple the error str.
    """
    
    issues = []
    for (prop,naturalPropName) in [
        ("MID","Meeting ID"),
        ("title","Title"),
        ("canceled","Canceled Status"),
        ("starts","Start Time"),
        ("room","Room"),
        ("agendaURL","Agenda URL"),
    ]:
        testPassed, errorMessage = testProp(
            actual,
            expected,
            prop,
            naturalPropName
        )
        if not testPassed: issues.append(errorMessage)

    numIssues = len(issues)
    if numIssues is 0: return
    errorStr = (
        f"`class Meeting()` Equality Test Failure - Encountered {numIssues} non-matching fields:\n\n"
        "\n".join(
            [f"{issueNumber}: {issue}" for issueNumber,issue in issues
        ])
    )

    #Pass the error to unittest
    #TODO: this next line feels clumsy. is there a better way?
    unittest.TestCase.assertTrue(False,errorStr)
            
class testMeetings(unittest.TestCase):
    def testOnSnapshot20210630070143(self):
        url = "./test/testcases/meetings-snapshot-20210630070143.html"
        webpage = open(url,"r")
        results = meetings.scrape(webpage)

        expectedResults = [
            meetings.Meeting(
                title="State Regulation of Public Utilities Review Committee",
                MID=11457,
                canceled=False,
                starts="2021-06-28 11:00",
                room="Gressette Room 207",
                agendaURL="https://web.archive.org/web/20210630070143/https://www.scstatehouse.gov/agendas/124j11457.pdf",
                revisions=[
                    "Meeting added with agenda in PDF format on 06/15/2021 at 03:11 pm",
                    "Agenda (in PDF format) revised on 06/25/2021 at 03:00 pm"
                ]
            ),
            meetings.Meeting(
                MID=11477,
                title="Greenville County Legislative Delegation Committee on Municipal Affairs, Medical Affairs and Special Service Districts",
                canceled=True,
                starts="2021-06-28 ??:??",
                room="Blatt Room 433",
                agendaURL="",
                revisions = [
                    "Meeting added on 06/28/2021 at 10:19 am",
                    "Time changed and agenda revised on 06/28/2021 at 02:22 pm",
                ],
            ),
            meetings.Meeting(
                MID=11474,
                title="Santee Cooper Oversight Committee",
                canceled=True,
                starts="2021-06-28 16:00",
                room="Gressette Room 105",
                agendaURL="",
                revisions = [
                    "Meeting added on 06/25/2021 at 10:28 am",
                    "Meeting canceled on 06/29/2021 at 04:23 pm",
                ],
            ),
            meetings.Meeting(
                MID=11476,
                title="Agency Head Salary Commission",
                canceled=False,
                starts="2021-06-28 16:30",
                room="Gressette Room 408",
                agendaURL="",
                revisions = [
                    "Meeting added on 06/28/2021 at 10:03 am"
                ],
            ),
        ]
   
        for r,e in zip(results,expectedResults):
            testMeetingEquals(r,e)
        
if __name__ == '__main__':
    unittest.main()