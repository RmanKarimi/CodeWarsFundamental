"""
 returns the time in a human-readable format (HH:MM:SS) from none-negative integer value
"""


def make_readable(sec):
    hours, rem = divmod(sec, 3600)
    minutes, seconds = divmod(rem, 60)

    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
    # return strftime("%I:%M:%S", gmtime(sec))
