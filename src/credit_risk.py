 def predict_default_probability(
    model,
    credit_lines_outstanding,
    loan_amt_outstanding,
    total_debt_outstanding,
    income,
    years_employed,
    fico_score
):
    """
    Predict the probability that a borrower will default.
    """

    borrower = pd.DataFrame({
        "credit_lines_outstanding": [credit_lines_outstanding],
        "loan_amt_outstanding": [loan_amt_outstanding],
        "total_debt_outstanding": [total_debt_outstanding],
        "income": [income],
        "years_employed": [years_employed],
        "fico_score": [fico_score]
    })

    probability = model.predict_proba(borrower)[0][1]

    return probability




def calculate_expected_loss(
    model,
    credit_lines_outstanding,
    loan_amt_outstanding,
    total_debt_outstanding,
    income,
    years_employed,
    fico_score,
    recovery_rate=0.10
):
    """
    Calculate the expected loss of a loan.
    """

    pd_probability = predict_default_probability(
        model,
        credit_lines_outstanding,
        loan_amt_outstanding,
        total_debt_outstanding,
        income,
        years_employed,
        fico_score
    )

    lgd = 1 - recovery_rate

    expected_loss = pd_probability * loan_amt_outstanding * lgd

    return (expected_loss)