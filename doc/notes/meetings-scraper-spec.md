# /scrapers/meetings.py

For demo data, see /doc/notes/meetings-scraper-demo-data.html, which was taken from [june 30, 2021 archive.org snapshot][1] of 
<https://scstatehouse.gov/meetings.php>

## Meeting Format
- The element `<div id="contentsection">` contains the current week's agenda.


- The week's agenda is split into days:

    - Each day is defined in a child `<ul>` of the parent `<div>`

    - Each day contains zero, one, or multiple meetings.

    - The calendar day is defined by the text contents of
      `ul > span:first-of-type`, in the format "Monday, January 1"


- Each day is split into meetings:

    - Each meeting is defined by two child elements of the parent `<ul>`. 

    - The first child element, an `<a name="99999" />` tag, represents 
      the meeting's ID.

    - The second child element, an `<li> ... </li>` tag, contains information
      about the meeting's location and agenda.



[1]: <https://web.archive.org/web/20210630070143/https://www.scstatehouse.gov/meetings.php>