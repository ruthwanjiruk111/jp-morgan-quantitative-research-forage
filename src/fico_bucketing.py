def bucket_log_likelihood(total_borrowers, defaults):
    """
    Calculate the log-likelihood for a single bucket.
    """

    # Avoid log(0)
    if defaults == 0 or defaults == total_borrowers:
        return 0

    pd = defaults / total_borrowers

    log_likelihood = (
        defaults * np.log(pd)
        + (total_borrowers - defaults) * np.log(1 - pd)
    )

    return log_likelihood



    def evaluate_bucket(start, end):
    """
    Calculate the log-likelihood for a bucket
    covering rows start through end (inclusive).
    """

    if start == 0:
        total = fico_summary.loc[end, "cum_total"]
        defaults = fico_summary.loc[end, "cum_defaults"]
    else:
        total = (
            fico_summary.loc[end, "cum_total"]
            - fico_summary.loc[start - 1, "cum_total"]
        )

        defaults = (
            fico_summary.loc[end, "cum_defaults"]
            - fico_summary.loc[start - 1, "cum_defaults"]
        )

    return bucket_log_likelihood(total, defaults)




def assign_rating(fico_score):
    """
    Assign a credit rating based on the optimized FICO score buckets.
    """

    for _, row in rating_df.iterrows():

        if row["Min FICO"] <= fico_score <= row["Max FICO"]:
            return int(row["Rating"])

    return None