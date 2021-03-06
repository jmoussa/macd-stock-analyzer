# MACD Stock Analyzer
> Analyze specific stocks' MACD and gain further insight into stock trends



## The Goal

The goal with this analyzer is to gain better insight and to identify strong and weak movements in a stock's price.
To do this we use the MACD and it's Signal Line to identify crossovers and classify them as bullish "buy" or bearish "sell" (more seen in the outputted csv files and plots).

## What is MACD?

Moving Average Convergence Divergence (MACD) is a trend following indicator.
MACD can be calculated very simply by subtracting the 26 period EMA (exponential moving average) from the 12 period EMA. 
The EMA is a type of moving average (MA) that places a greater weight and significance on the most recent data points.
MACD is commonly used by analyzing crossovers, divergences, and periods of steep slope (positive or negative). 
Along with the MACD line (from subtracting the 12 period EMA from the 16 period EMA) the chart commonly will include a signal line plotted on top of the MACD. 
This signal line is a 9 day EMA of the MACD.

## The analyzer

The analyzer script grabs the historical info for a select set of stocks by their tickers (the stocks are denoted in the `analyzer.py` script and can be edited to add any tickers).
Then runs analysis to graph out the MACD and mark the different buy/sell dates.

Final analysis that gets outputted shows a set number of days back (Default 5) and the consensus decision ("buy" or "sell") from those days as well as the latest decision.

The decisions come off of a few very simple principals:
- A bullish "buy" signal occurs when the MACD crosses above the signal line.
- A bearish "sell" signal occurs when MACD crosses below the signal line. 
**Useful info:** If a crossover occurs with a high sloping MACD, this can be a sign of an overbought or oversold condition, depending on if the crossover is bullish or bearish respectively. MACD is a great indicator for understanding if movement in the price is strong or weak. A weak movement is likely to correct and a strong movement is likely to continue.

## Setup

There are two ways to setup the environment:

- Using requirements.txt (pip with no environments)
- Using environment.yml (Anaconda/Conda Environments)

Both setup methods are shown below, you can choose either, or both. I'm not going to tell you how to live your life.

### Setup with Python Pip
First you'll need to have python (which I think comes with MacOS) and pip installed [install pip here](https://pip.pypa.io/en/stable/installing/).

Open up a terinal and follow the directions below:
```bash
# change directories to get into the folder of this project's directory
cd ~/<path_to_directory>/macd-stock-analyzer

# Install requirments
pip install -r requirements.txt
```

### Setup with Conda Python Virtual Environments

You'll need access to the conda command as this is packaged into an Anaconda python virtual environment
[Install Anaconda here](https://docs.anaconda.com/anaconda/install/).

Then open up a terminal and follow the instructions below:
```bash
# change directories to get into the folder of this project's directory
cd ~/<path_to_directory>/macd-stock-analyzer

# Initialize Conda
conda init bash

# Create the environment from the template supplied in the repository (this handles all pip installs too)
conda env create -f environment.yml

# Activate the environment
conda activate finance
```

## To Run

In the repo's directory:

```bash
python analyzer.py
```
You should see the logging output in the terminal as shown below, and you can check the `files/` folder for charts and csv's for further analysis.
![Terminal Screenshot](./screenshots/screenshot.jpg?raw=true)

Here is an example of what a chart and csv might look like (found in the `files/` folder after running `analyzer.py`). 
It should be noted that these are both for the stock of Coca Cola (KO), and that ticker is used as the filename for easy identification.
![Plot Screenshot](./screenshots/example_plot.jpg?raw=true)
![CSV Screenshot](./screenshots/example_csv.jpg?raw=true)

## Configuration Tweaks

In addition to modifying the `stocks` variable in `analyzer.py`, there are two other factors of the calculation that you can edit.

Below are the defaults:
```python
HOW_FAR_TO_LOOK_BACK = 5  # in years
HOW_MANY_DAYS_TO_CONSIDER = 14  # Changes the Mode of X days to look back when showing final decisions
```

**HOW_FAR_TO_LOOK_BACK**: Total number of years back, to fetch the stock data from. Default is set to 5 years back.
*Please note: the farther back you choose to look, the longer the script will take to finish.*

**HOW_MANY_DAYS_TO_CONSIDER**: When calculating the final decisions (those that are printed out in the terminal as the result), the script will take into consideration the most common decision (the mode) from a few days prior in order for the user to get a sense of what the previous inclinations (or declinations) toward this stock looked like. 
This variable adjusts the number of days to check back. Default is set to 14 days back.

## Credit where credit is due

I can't take credit for all of this amazing information, so here's the link to Luke Posey's article that I based this on.
https://towardsdatascience.com/implementing-macd-in-python-cc9b2280126a


## DISCLAIMER

The results presented here are not to be taken as financial advice with regards to how and when to pick your stocks. 
These are outputs based on an alogrithm, and any actions taken as a result of these outputs should not be done without conducting proper research and consulting professionals.
