# Group Project
*Bronte Baer, Jean-Luc Jackson, Christian Montecillo, Richard Robbins*
The work included within was a team collaboration between the authors, all contributing in equal parts through each project phase.

## Repo Description

Working group notes can be found here:

<https://docs.google.com/document/d/1-F4i9-C3O2mMvCOjjr535WKAWVze1KHxKGtjeL70zfs/edit?usp=sharing>

Original raw source data sets that we are working from can be found here (see /datasets/README.md for more information):

<https://drive.google.com/drive/u/2/folders/1Ag39uw9kKCKqlEOUkCxcezAutJI6mWyC>

The web site describing our primary dataset (Political TV Ads) can be found here:

<http://politicaladarchive.org/data/>

The web page describing our supplemental data set with county level election returns can be found here:
<https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/VOQCHQ>

Information used to build mapping from counties to television markets can be found here:
<https://en.wikipedia.org/wiki/List_of_United_States_television_markets>

## Repo Organization

### code

#### Jupyter Notebooks

- ```filter_country_returns.ipynb``` and ```filter_to_presidential_ads.ipynb``` contain the code used to generate the various working datasets.  You are unlikely to need to use them but they are there if of interest.  

- ```load_presidential_ads.ipynb``` and ```load_enriched_county_results.ipynb``` include code to load the working datasets and cells to highlight some of the data in those datasets.  They could serve as useful reference points for how to begin to interact with the data.  By default, these notebooks use the `awesome_puppies` module described below.  For best results, you should define your `PYTHONPATH` environment variable as described below.

#### Python Scripts and any other coding files

- ```awesome_puppies.py``` is a module that can be used to load our primary dataframes into a Python environment (including a Jupyter Notebook).

- ```from awesome_puppies import ads_df, vote_df``` will bring the two primary working datasets into your environment.

- In order for the module to be found regardless of your then current working directory, it is useful to have the ```PYTHONPATH``` environment variable point to the directory containing ```awesome_puppies.py``` which can be accomplished with a line in ```.bashrc``` (or whatever equivalent script gets run when your shell command line environment is invoked), such as ```export PYTHONPATH=$PYTHONPATH:REPLACE_WITH_REFERENCE_TO_ROOT_DIRECTORY_OF_REPO/code/Python```

- Additional detail that might help with above: https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html

### datasets

Our working datasets come from two sources, the MIT Election Lab and the Political TV Ad Archive.  Each source has a separate subdirectory.

#### Political TV Ad Archive

This directory contains our primary working dataset, ```political_ad_pres_airing_from_june.gz``` as well as two related datasets which are not currently being used, namely ```political_ad_pres_airing.gz``` and ```political_ad_pres_unique.gz```.

Our project focuses on advertising from June 1, 2016 through November 8, 2016 so we derive the `airing_from_june` dataset by removing information about earlier and later broadcasts from the larger `political_ad_pres_airing` dataset.

The `ad_pres_unique` dataset does not have information about when or where ads were aired.  It contains information about unique ads that may have been aired multiples times in a single market or across markets.  As our project focuses on exposure of people to advertising, we need the information about when an ad was aired and the market information for the broadcast that is excluded from this dataset.

We collected these datasets and keep them in case they prove to be helpful, but for now, our focus is clearly on the `airing_from_june` dataset.

#### MIT Election Lab

This folder contains ```enriched_county_pres_2016.gz``` which has information about presidential election returns, by county, across the United States for the 2016 presidential election.  We have taken the source data and enriched it with a datafield that maps each county in regional markets of interest to us to those markets.  This enables us to compare election returns in a market with the advertising insight we derive from our analysis, which will be done on a market by market basis.

### output

This folder contains output files from analysis:

- Visualizations
- Tables
- and any other useful outputs

### report

Reports for this project are found here.
