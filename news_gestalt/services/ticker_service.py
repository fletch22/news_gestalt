from typing import List

import pandas as pd

from news_gestalt.config import logger_factory, constants

logger = logger_factory.create(__name__)

COL_AFTER_HOURS = "f22_is_tweet_after_hours"
COL_PURCH_DATE = "purchase_date"


def get_ticker_searchable_tuples() -> List:
    df = pd.read_csv(constants.TICKER_NAME_SEARCHABLE_PATH)
    ticker_tuples = list(map(tuple, df[['ticker', 'name']].to_numpy()))
    return ticker_tuples
