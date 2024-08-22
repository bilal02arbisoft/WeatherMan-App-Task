import os
import re as regex
from typing import Tuple


def extract_year_month(date: str) -> Tuple[int, int]:
    year, month, *_ = map(int, date.split('-'))

    return year, month


def extract_year(date: str) -> int:
    year = int(date.split('-')[0])

    return year


def extract_month(date: str):
    month = int(date.split('-')[1])

    return month


def remove_whitespaces_from_start_end(text: str) -> str:

    return text.strip()


def is_valid_path(directory_path: str) -> bool:

    return os.path.exists(directory_path)


def is_valid_year(date_year: str) -> bool:

    return bool(regex.match(r'^\d{4}$', date_year))


def is_valid_year_month(date_year_month: str) -> bool:
    MIN_MONTH = 1
    MAX_MONTH = 12

    return (bool(regex.match(r'^\d{4}-\d{2}$', date_year_month))
            and (MIN_MONTH <= extract_month(date_year_month) <= MAX_MONTH))
