"""The awesome_puppies module supplies project dataframes and functions.

Dataframes: ads_df and votes_df
Region functions: regions, region_fips, region_string
Vote functions: votes_by_region, votes_by_party
Ad functions: ad_counts_by_region_and_beneficiary
Other functions: groupby_agg"""

import os.path
import re
import pandas as pd


module_directory = os.path.dirname(__file__)
data_root_directory = re.sub("code/Python$", "datasets", module_directory)

ads_directory = data_root_directory + "/Political_TV_Ad_Archive/"
returns_directory = data_root_directory + "/MIT_Election_Lab/"

ads_df = pd.read_csv(
    ads_directory + "political_ad_pres_airing_from_june.gz",
    compression="gzip",
    parse_dates=["start_time", "end_time", "start_utc", "end_utc"],
)
ads_df.duration = ads_df.end_time - ads_df.start_time

votes_df = pd.read_csv(
    returns_directory + "enriched_county_pres_2016.gz",
    compression="gzip",
    dtype={"county_fips": str, "candidatevotes": int, "totalvotes": int},
)


def regions():
    """Returns a list of all regions"""
    return sorted(votes_df.region_id.unique().tolist())


def region_fips():
    """Returns a series of fips (as a numpy array) by region."""
    return votes_df.groupby("region_id")["county_fips"].apply(pd.unique)


def region_string(region_id):
    """Return the display string for a region_id string."""
    if region_id not in regions():
        raise ValueError("invalid region_id")
    return region_id.replace("_", " ").title().replace("Dc", "DC")


def votes_by_region():
    """Returns votes by region dataframe.
    The columns are the votes, by party, for each region."""
    return votes_df.groupby(["region_id"]).sum()


def votes_by_party():
    """Returns votes by party dataframe.
    The columns are regions."""
    return votes_df.groupby(["region_id"]).sum().T


def ad_counts_by_region_and_beneficiary():
    """Returns a DataFrame with ad counts by beneficiary. The result has
    region_ids as its indices and [Clinton, Trump] as its columns.
    Access a region's ad counts by df.loc["<region_id>"]
    Access a beneficiary's ad counts by df.loc[<region>].Clinton or .Trump"""
    return ads_df.groupby(["region_id", "beneficiary"]).size().unstack(level=1)


def groupby_agg(df, groupby_list=[], func="size", fill_value=None):
    """This function generalizes the application of groupby() and aggregate()
    functions to the passed DataFrame "df". If multiple labels are provided in
    the "groupby_list", this function unstacks the resulting MultiIndex DF by
    the number of labels - 1.  Aggregate functions are passed as strings to the
    "func" argument (such as "size", "sum", "mean", etc.) and "size" is applied
    by default.

    df.groupby(<groupby_list>).agg(<func>).unstack(<unstack_level>)"""

    # If grouping by multiple labels, unstack the resulting MultiIndex DF
    if len(groupby_list) > 1:
        return (
            df.groupby(groupby_list)
            .agg(func)
            .unstack(level=(len(groupby_list) - 1), fill_value=fill_value)
        )

    # If grouping by only one label, resulting DF will have single Index
    # and no unstack is needed
    else:
        return df.groupby(groupby_list).agg(func)
