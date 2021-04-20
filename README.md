# MACD Stock Analyzer

## What is MACD?

Moving Average Convergence Divergence (MACD) is a trend following indicator.
MACD can be calculated very simply by subtracting the 26 period EMA from the 12 period EMA.
MACD is commonly used by analyzing crossovers, divergences, and periods of steep slope (positive or negative). 
Along with the MACD line (from subtracting the 12 period EMA from the 16 period EMA) the chart commonly will include a signal line plotted on top of the MACD. 
This signal line is a 9 day EMA of the MACD.

## The analyzer

The analyzer script grabs the historical info for a select set of stocks by their tickers (the stocks are denoted in the `analyzer.py` script and can be edited to add any tickers).
Then runs analysis to graph out the MACD and mark the different buy/sell dates.

Final analysis that gets outputted shows that 10 day consensus decision ("buy" or "sell") and the latest decision.


## Setup

You'll need access to the conda command as this is packaged into an Anaconda python virtual environment.

[Quick Install Anaconda](https://docs.anaconda.com/anaconda/install/)
Then open up a terminal on your computer and navigate to the place you installed this repository
```bash
# change directories to get into the folder of this directory
cd ~/<path_to_directory>/macd-stock-analyzer

# Initialize Conda
conda init bash

# Create the environment from the template supplied in the repository
conda env create -f environment.yml

# Activate the environment
conda activate finance
```

## To Run
In the repo's directory:

```bash
python analyzer.py
```
You will see the logging output in the terminal and you can check the `files/` folder for charts and csv's for further analysis.
