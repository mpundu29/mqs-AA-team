"""
Correlation Analysis by Market Regime
------------------------------------
Computes asset correlation matrices separately for
low-volatility and high-volatility market regimes.
"""

import pandas as pd


def align_returns_and_regime(
    returns: pd.DataFrame,
    regime: pd.Series
) -> pd.DataFrame:
    """
    Align asset returns with regime labels by date.
    """
    data = returns.copy()
    data["Regime"] = regime
    data = data.dropna()
    return data


def split_by_regime(
    data: pd.DataFrame,
    regime_label: str
) -> pd.DataFrame:
    """
    Filter return data for a specific regime.
    """
    return data[data["Regime"] == regime_label].drop(columns="Regime")


def compute_correlation_matrix(
    returns: pd.DataFrame
) -> pd.DataFrame:
    """
    Compute correlation matrix from returns.
    """
    return returns.corr()


def correlation_by_regime(
    returns: pd.DataFrame,
    regime: pd.Series
):
    """
    Main pipeline: returns correlation matrices for
    low- and high-volatility regimes.
    """
    aligned = align_returns_and_regime(returns, regime)

    low_vol_returns = split_by_regime(aligned, "Low Vol")
    high_vol_returns = split_by_regime(aligned, "High Vol")

    corr_low = compute_correlation_matrix(low_vol_returns)
    corr_high = compute_correlation_matrix(high_vol_returns)

    return corr_low, corr_high
