# README for project datasets

The datasets for this project are stored on Google Drive:  

<https://drive.google.com/drive/folders/1Ag39uw9kKCKqlEOUkCxcezAutJI6mWyC?usp=sharing>

## How to manage datasets locally

***The .csv extension has been added to .gitignore so that csv datasets can be stored in local repositories and won't be pushed so we don't hit Github's file limit.***

1. Go to the Google Drive above and download the dataset files you are missing to your local repo in the corresponding datasets/ folders.

2. Access them normally in your analysis.

3. When you go to "git push" the .csv files *will not* be pushed to GitHub. See the note above about .gitignore.

## Original sources of these datasets

### Politcal TV Ads Archive - 2016 Elections

See <http://politicaladarchive.org/data/>

### Information used to identify the intended beneficiary of an ad

We reviewed the list of ad sponsors to determine which candidate each supported and, in some cases,
to identify sponsors that did not support either candidate.  In limited circumstances we reviewed
ads themselves to identify whether the ad was likely to benefit one candidate or the other.  We also
identified one as sponsor "Internet Archive" that sponsored two ads that were aired, in total, over
500 times.  One of these ads was likely to benefit Clinton and one Trump.  Our working data set
reflects that dichotomy.  The results of this exercise are reflected in the beneficiary column of the
advertising dataset.

### MIT Election Lab County Presidential Election Returns 2000-2020

See <https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/VOQCHQ>

### Information used to build mapping from counties to television markets

See <https://en.wikipedia.org/wiki/List_of_United_States_television_markets>
