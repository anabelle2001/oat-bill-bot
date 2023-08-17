#!/usr/bin/python3

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

    - helps keep explainMeetingEquality() [D.R.Y.] - used to compare a property
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
        
    if meetingExpected.__dict__[prop] != meetingActual.__dict__[prop]:
        return(
            False,
            f"meetings don't have the same {naturalPropName}"
            f" - expected '{meetingExpected.__dict__[prop]}', got "
            f"'{meetingActual.__dict__[prop]}'"
        )
    return True,""
    # End of helper method testProp(...)

def explainMeetingEquality( actual: meetings.Meeting,
                            expected: meetings.Meeting ) -> str:
    """
    Used to compare two `class Meeting():` objects
    - if they are unequal, returns a string explaining why
    """

    ## Suggestion to improve readibility:
    # This function should probably be split in two - one to get the list of 
    # differeing props, another to assemple the error str.

    issues = []
    for (prop,naturalPropName) in [
        ("MID","Meeting ID"),
        ("title","Title"),
        ("canceled","Canceled Status"),
        ("starts","Start Time"),
        ("room","Room"),
        ("agendaURL","Agenda URL"),
    ]:
        testPassed, errorMessage = testMeetingProp(
            actual,
            expected,
            prop,
            naturalPropName
        )
        if not testPassed: issues.append(errorMessage)

    numIssues = len(issues)
    if numIssues == 0: return None
    errorStr = (
        f"`class Meeting()` Equality Test Failure - Encountered {numIssues} non-matching fields:\n"+
        "\n".join( [
            f"{issueNumber}: {issue}"
            for issueNumber,issue in enumerate(issues)
        ] )
    )

    return errorStr
            
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
   
        assert len(results) == len(expectedResults),\
            (f"Expected to parse {len(expectedResults)} meetings, "
             f"got back {len(results)} instead")

        for i,result,expectedResult in zip(
            range(len(results)),
            results,
            expectedResults
        ):
            equalByBuiltinMethod = result == expectedResult
            testerResults = explainMeetingEquality(result,expectedResult)

            # Case 1, both the bultin __eq__ and explainMeetingEquality pass this 
            # meeting, so we continue
            if equalByBuiltinMethod and testerResults == "": continue

            # Case 2: tME errors - meaning we have an error str to print for
            # debugging
            if testerResults != "":
                raise AssertionError(f"Error in results[{i}] - {testerResults}")

            # Case 3: __eq__ errors, but tME passes - we need to serve the user 
            # a generic error in this case
            raise AssertionError(
                f"\nError in test #{i}:\n"
                "Expected meeting differed from actual meeting.\n"
                "Furthermore, tester function explainMeetingEquality() failed "
                "to catch that the meetings were different. This means that "
                "there is not only an error with the code parsing the meetings"
                ", but also with the function that tests that code."
            )
        
if __name__ == '__main__':
    unittest.main()