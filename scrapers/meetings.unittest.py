import unittest
import meetings

class testMeetings(unittest.TestCase):
    def testOnSnapshot20210630070143(self):
        url = "./test/testcases/meetings-snapshot-20210630070143.html"
        webpage = open(url,"r")
        results = meetings.scrape(webpage)

        expectedResult0 = meetings.Meeting(
            MID=11457,
            canceled=False,
            starts="2021-06-28 11:00",
            room="Gressette Room 207",
            agendaURL="https://web.archive.org/web/20210630070143/https://www.scstatehouse.gov/agendas/124j11457.pdf",
            revisions=[
                "Meeting added with agenda in PDF format on 06/15/2021 at 03:11 pm",
                "Agenda (in PDF format) revised on 06/25/2021 at 03:00 pm"
            ]
        )
   
        assert(
            "Test meeting 1",
            expectedResult0 == results[0]
        )
        
if __name__ == '__main__':
    unittest.main()