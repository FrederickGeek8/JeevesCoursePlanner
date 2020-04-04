# JeevesCoursePlanner
The Jeeves Course Planner add-on for Albert!

TypeDoc documentation [here](http://skairunner.github.io/JeevesCoursePlanner/docs/.)


## Updating
You basically want to change
`NYU_CLS_WRK_NYU_SPRING` or `NYU_CLS_WRK_NYU_FALL` in `albertscaper.py` and 
`majorscraper.py` to either `NYU_CLS_WRK_NYU_SPRING`
or `NYU_CLS_WRK_NYU_FALL` depending on the target semester.

You also want to change `fall2019out` or `spring2020out` in `albertscraper.py` 
depending on your target semester. Depending on what you change here, you want
to make similar changes to `courseprocessor.py`.

After changing these values, you want to create the directories referenced in 
the code. For example if the target semester is Fall 2020, you would want to 
create `fall2020out`, `fall2020out/raw`, `fall2020out/permajor`.

## Scraping
For scraping data, you first want to go to the directory `scraper`. From there
run `python majorscraper.py`. This will create `possiblemajors.txt`, which if 
everything looks good (in line with the general structure of
`majors_shanghai.txt`) can be safely renamed to `majors_shanghai.txt` (you 
might want to make a backup of the old one).

In order to scrape the classes, you then want to run `python albertscraper.py`.
This will generate raw data from Albert. You can then convert this raw data
into the format consumed by Jeeves by running `python courseprocesser.py`.