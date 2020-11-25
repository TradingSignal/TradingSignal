from enum import Enum


class ActionType(Enum):
    """
    Trade order actions
    """
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
