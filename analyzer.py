from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import logging
import coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG", logger=logger)

# make sure folders are set
Path("./files/plots").mkdir(parents=True, exist_ok=True)
Path("./files/csvs").mkdir(parents=True, exist_ok=True)

# **** START EDITING HERE ****
HOW_FAR_TO_LOOK_BACK = 5  # in years
HOW_MANY_DAYS_TO_CONSIDER = 14  # Changes the Mode of X days to look back when showing final decisions
STOCKS = [
    "NRZ",
    "RDS-B",
    "T",
    "KO",
    "AGNC",
    "XOM",
    "SPHD",
    "VYMI",
    "TSM",
    "ICLN",
    "THCX",
    "DVY",
    "VT",
    "VYM",
    "IJR",
    "SDY",
    "VTI",
    "VUG",
]
# **** END EDITING HERE ****

response = yf.Tickers(" ".join(STOCKS))
tickers = response.tickers

for ticker, ticker_obj in tickers.items():
    # TODO: lots of possibly useful info but not needed, maybe save to a file in the future?
    # logger.info(json.dumps(ticker_obj.info, indent=2))
    try:
        df = ticker_obj.history(period=f"{HOW_FAR_TO_LOOK_BACK}y")
    except Exception:
        df = ticker_obj.history(period="ytd")

    # Grab Closing stock prices and dates (already included in df as index)
    df = df[["Close"]]
    df.reset_index(level=0, inplace=True)
    df.columns = ["ds", "y"]

    # MACD Calculation
    exp1 = df.y.ewm(span=12, adjust=False).mean()
    exp2 = df.y.ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    exp3 = macd.ewm(span=9, adjust=False).mean()

    # Plot the stock, MACD and the Signal Line
    plt.plot(df.ds, df.y, label=f"{ticker}", color="black", linewidth=0.5)
    plt.plot(df.ds, macd, label=f"{ticker} MACD", color="green", linewidth=0.3)
    plt.plot(df.ds, exp3, label="Signal Line", color="red", linewidth=0.25)

    d = {"date": df.ds, "macd": macd, "signal": exp3}
    _df = pd.DataFrame(data=d)
    _df["buy/sell"] = _df.apply(lambda row: "buy" if row.macd > row.signal else "sell", axis=1)

    last_x_days = _df[-HOW_MANY_DAYS_TO_CONSIDER:]
    mode = last_x_days[["buy/sell"]].mode()["buy/sell"].iloc[0]

    # Print out info
    logger.info(f"{ticker}: Mode of last {HOW_MANY_DAYS_TO_CONSIDER} days: {mode}")
    logger.info(f"{ticker}: Most recent suggestion: {last_x_days[-1:]['buy/sell'].iloc[0]}")
    logger.info("--------------------------------------------------")

    # Save files
    _df.to_csv(f"./files/csvs/{ticker}.csv")
    plt.legend(loc="upper left")
    plt.savefig(f"./files/plots/{ticker}.png", dpi=1200, pad_inches=0.1)
    # plt.show()
    plt.clf()
