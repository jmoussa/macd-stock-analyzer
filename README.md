# MACD Stock Analyzer

## What is MACD?

Moving Average Convergence Divergence (MACD) is a trend following indicator.
MACD can be calculated very simply by subtracting the 26 period EMA from the 12 period EMA.
MACD is commonly used by analyzing crossovers, divergences, and periods of steep slope (positive or negative). 
Along with the MACD line (from subtracting the 12 period EMA from the 16 period EMA) the chart commonly will include a signal line plotted on top of the MACD. 
This signal line is a 9 day EMA of the MACD.

## The analyzer

The analyzer script grabs the historical info for a select set of stocks by their tickers.
Then runs analysis to graph out the MACD and mark the different buy/sell dates.

Final analysis that gets outputted shows that 10 day consensus decision ("buy" or "sell") and the latest decision.

## To Run

```bash
conda env create -f environment.yml
conda activate finance
python analyzer.py
```

Check `files/` folder for figures and csv's for further analysis
