def round_ans(val):
    """
    Rounds to 2 decimal places
    """
    return "{:.2f}".format(val)


def nzd_to_usd(amount):
    """
    Converts NZD to USD
    """
    answer = amount * 0.59
    return round_ans(answer)


def usd_to_nzd(amount):
    """
    Converts USD to NZD
    """
    answer = amount / 0.59
    return round_ans(answer)