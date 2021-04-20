import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import logging
import coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG", logger=logger)

stocks = [
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

response = yf.Tickers(" ".join(stocks))
tickers = response.tickers

for ticker, ticker_obj in tickers.items():
    # logger.info(json.dumps(ticker_obj.info, indent=2))
    try:
        df = ticker_obj.history(period="10y")
    except Exception:
        df = ticker_obj.history(period="ytd")

    df = df[["Close"]]
    df.reset_index(level=0, inplace=True)
    df.columns = ["ds", "y"]

    exp1 = df.y.ewm(span=12, adjust=False).mean()
    exp2 = df.y.ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    exp3 = macd.ewm(span=9, adjust=False).mean()

    plt.plot(df.ds, df.y, label=f"{ticker}", color="black")
    plt.plot(df.ds, macd, label=f"{ticker} MACD", color="green")
    plt.plot(df.ds, exp3, label="Signal Line", color="red")

    d = {"date": df.ds, "macd": macd, "signal": exp3}

    _df = pd.DataFrame(data=d)
    _df["buy/sell"] = _df.apply(lambda row: "buy" if row.macd > row.signal else "sell", axis=1)

    last_10_days = _df[-10:]
    logger.info(f"{ticker}: Mode of last 10 days: {last_10_days[['buy/sell']].mode()['buy/sell'].iloc[0]}")
    logger.info(f"{ticker}: Most recent suggestion: {last_10_days[-1:]['buy/sell'].iloc[0]}")
    # logger.info(f"Last 10 Days\n{last_10_days}")

    # Save files
    _df.to_csv(f"./files/csvs/{ticker}.csv")
    plt.legend(loc="upper left")
    plt.savefig(f"./files/plots/{ticker}.png")
    # plt.show()
    plt.clf()
