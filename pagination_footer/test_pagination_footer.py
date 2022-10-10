import pytest
from pagination_footer import pagination_footer


@pytest.mark.parametrize(
    ("current_page", "total_pages", "boundaries", "around", "expected_footer"),
    [
        pytest.param(
            *[1, 0, 2, 2, ""],
            id="no_total_pages",
        ),
        pytest.param(
            *[1, 1, 2, 2, "1"],
            id="current_page_is_the_only_page",
        ),
        pytest.param(
            *[1, 10, 0, 0, "1 ..."],
            id="current_page_is_first_page_no_bounderies_no_around",
        ),
        pytest.param(
            *[1, 10, 0, 3, "1 2 3 4 ..."],
            id="current_page_is_first_page_no_bounderies",
        ),
        pytest.param(
            *[1, 10, 3, 0, "1 ... 8 9 10"],
            id="current_page_is_first_page_no_around",
        ),
        pytest.param(
            *[10, 10, 0, 0, "... 10"],
            id="current_page_is_last_page_no_bounderies_no_around",
        ),
        pytest.param(
            *[10, 10, 0, 3, "... 7 8 9 10"],
            id="current_page_is_last_page_no_bounderies",
        ),
        pytest.param(
            *[10, 10, 3, 0, "1 2 3 ... 10"],
            id="current_page_is_last_page_no_around",
        ),
        pytest.param(
            *[5, 10, 0, 2, "... 3 4 5 6 7 ..."],
            id="no_bounderies",
        ),
        pytest.param(
            *[5, 10, 20, 2, "1 2 3 4 5 6 7 8 9 10"],
            id="bounderies_larger_than_total_pages_are_ignored",
        ),
        pytest.param(
            *[5, 10, -3, 2, "... 3 4 5 6 7 ..."],
            id="bounderies_lower_than_zero_is_ignored",
        ),
        pytest.param(
            *[5, 10, 2, 0, "1 2 ... 5 ... 9 10"],
            id="no_around",
        ),
        pytest.param(
            *[5, 10, 2, 20, "1 2 3 4 5 6 7 8 9 10"],
            id="around_larger_than_total_pages_is_ignored",
        ),
        pytest.param(
            *[5, 10, 2, -3, "1 2 ... 5 ... 9 10"],
            id="around_lower_than_zero_is_ignored",
        ),
        pytest.param(
            *[5, 10, 200, 200, "1 2 3 4 5 6 7 8 9 10"],
            id="bounderies_and_around_overlap",
        ),
        pytest.param(
            *[300, 10, 2, 2, "1 2 ... 8 9 10"],
            id="current_page_larger_than_total_pages_shows_last_page",
        ),
        pytest.param(
            *[-1, 10, 2, 2, "1 2 3 ... 9 10"],
            id="current_page_lower_than_one_shows_first_page",
        ),
        pytest.param(
            *[6, 11, 0, 0, "... 6 ..."],
            id="current_page_in_the_middle_no_bounderies_no_around",
        ),
        pytest.param(
            *[6, 11, 2, 2, "1 2 ... 4 5 6 7 8 ... 10 11"],
            id="current_page_in_the_middle_small",
        ),
        pytest.param(
            *[
                150_000_000,
                300_000_000,
                2,
                1,
                "1 2 ... 149999999 150000000 150000001 ... 299999999 300000000",
            ],
            id="current_page_in_the_middle_large_numbers",
        ),
    ],
)
def test_paginator_footer(
    current_page: int,
    total_pages: int,
    boundaries: int,
    around: int,
    expected_footer: str,
):
    result = pagination_footer(current_page, total_pages, boundaries, around)
    assert result == expected_footer
