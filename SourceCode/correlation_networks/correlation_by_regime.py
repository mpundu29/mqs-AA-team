import pandas as pd


def split_returns_by_regime(
    returns: pd.DataFrame,
    regime: pd.Series
):
    low_vol = returns[regime == "Low Vol"]
    high_vol = returns[regime == "High Vol"]
    return low_vol, high_vol


def compute_correlation_matrix(
    returns: pd.DataFrame
) -> pd.DataFrame:
    return returns.corr()


def correlation_by_regime(
    returns: pd.DataFrame,
    regime: pd.Series
):
    low, high = split_returns_by_regime(returns, regime)
    corr_low = compute_correlation_matrix(low)
    corr_high = compute_correlation_matrix(high)
    return corr_low, corr_high

