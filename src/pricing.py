def create_daily_history(df):
    """
    Convert monthly prices to daily prices using linear interpolation.
    """
    daily_index = pd.date_range(
        start=df.index.min(),
        end=df.index.max(),
        freq="D"
    )

    df_daily = df.reindex(daily_index)
    df_daily["Prices"] = df_daily["Prices"].interpolate(method="linear")

    return df_daily


   

def forecast_prices(df, months=12):
    """
    Forecast monthly prices using the average monthly trend
    and historical seasonal effects.
    """

    monthly_change = df["Prices"].diff().mean()

    monthly_average = df.groupby(df.index.month)["Prices"].mean()
    overall_average = df["Prices"].mean()
    seasonal_effect = monthly_average - overall_average

    forecast_dates = pd.date_range(
        start=df.index.max() + pd.offsets.MonthEnd(),
        periods=months,
        freq="ME"
    )

    forecast_values = []

    last_price = df["Prices"].iloc[-1]

    for date in forecast_dates:
        seasonality = seasonal_effect.loc[date.month]
        next_price = last_price + monthly_change + seasonality

        forecast_values.append(round(next_price, 2))
        last_price = next_price

    forecast_df = pd.DataFrame(
        {"Prices": forecast_values},
        index=forecast_dates
    )

    return forecast_df



    
def build_full_price_table():
    """
    Combine historical daily prices with forecasted daily prices.
    """

    df = load_data()

    historical_daily = create_daily_history(df)

    forecast_df = forecast_prices(df)

    forecast_daily_index = pd.date_range(
        start=forecast_df.index.min(),
        end=forecast_df.index.max(),
        freq="D"
    )

    forecast_daily = forecast_df.reindex(forecast_daily_index)

    forecast_daily["Prices"] = forecast_daily["Prices"].interpolate(
        method="linear"
    )

    full_prices = pd.concat([historical_daily, forecast_daily])

    return full_prices


FULL_PRICES = build_full_price_table()




def estimate_price(date):
    """
    Estimate the natural gas price for any supported date.
    """

    date = pd.to_datetime(date)

    if date < FULL_PRICES.index.min() or date > FULL_PRICES.index.max():
        raise ValueError(
            f"Date must be between "
            f"{FULL_PRICES.index.min().date()} and "
            f"{FULL_PRICES.index.max().date()}."
        )

    return round(FULL_PRICES.loc[date, "Prices"], 2)


    

def price_contract(
    injection_date,
    withdrawal_date,
    volume,
    storage_cost_per_month,
    injection_cost,
    withdrawal_cost,
    max_storage,
):
    """
    Calculate the value of a natural gas storage contract.
    """

    if volume > max_storage:
        raise ValueError("Volume exceeds maximum storage capacity.")

    buy_price = estimate_price(injection_date)
    sell_price = estimate_price(withdrawal_date)

    purchase_cost = buy_price * volume
    sales_revenue = sell_price * volume

    injection_date = pd.to_datetime(injection_date)
    withdrawal_date = pd.to_datetime(withdrawal_date)

    storage_months = (
        (withdrawal_date.year - injection_date.year) * 12
        + withdrawal_date.month
        - injection_date.month
    )

    total_storage_cost = storage_months * storage_cost_per_month
    total_operating_cost = injection_cost + withdrawal_cost

    contract_value = (
        sales_revenue
        - purchase_cost
        - total_storage_cost
        - total_operating_cost
    )

    return round(contract_value, 2)