# Project Flow & Integration Overview

This document outlines how individual components of the project
connect to form a unified regime-aware portfolio framework.

---

## 1. Market Regime Detection

**Input:**
- S&P 500 daily price data

**Process:**
- Compute daily returns
- Calculate rolling volatility
- Define volatility threshold
- Label each period as High-Vol or Low-Vol regime

**Output:**
- Time series of regime labels
- Summary statistics by regime

This regime classification is used across all subsequent analyses.

---

## 2. Regime Validation

**Objective:**
Ensure that identified regimes are statistically and economically distinct.

**Methods:**
- Compare mean volatility across regimes
- Conduct basic statistical tests (e.g., difference in means)
- Verify alignment with known market stress periods

---

## 3. Regression & Factor Stability Analysis

**Input:**
- Asset returns
- Regime labels

**Process:**
- Run regression models separately within each regime
- Compare factor sensitivities across regimes

**Output:**
- Coefficient estimates by regime
- Interpretation of changes in economic meaning

---

## 4. Correlation Networks & Diversification

**Input:**
- Asset returns
- Regime labels

**Process:**
- Compute correlation matrices by regime
- Construct network graphs
- Analyze clustering and centrality shifts

**Output:**
- Regime-specific correlation structures
- Diversification insights

---

## 5. Portfolio Risk & Integration

**Input:**
- Asset returns
- Regime labels
- Portfolio weights

**Process:**
- Apply weights conditionally on regime
- Evaluate portfolio-level risk metrics
- Compare performance against S&P 500 benchmark

**Output:**
- Risk and performance metrics by regime
- Unified narrative linking regimes, correlations, and portfolio behavior

---

## Notes
- All teams use the same asset universe and time period.
- Components are modular and can be extended independently.
- The framework is designed to generalize beyond the selected assets.
