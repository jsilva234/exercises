ELLIPSES = "..."
FIRST_PAGE = 1


def _calculate_arounds(
    current_page,
    around_len,
    last_page,
):
    reversed_left_side_values = []
    right_side_values = []

    for count in range(1, around_len + 1):
        current_left = current_page - count
        current_right = current_page + count

        is_left_valid = current_left >= FIRST_PAGE
        is_right_valid = current_right <= last_page

        if not is_left_valid and not is_right_valid:
            break

        if is_left_valid:
            reversed_left_side_values.append(current_left)

        if is_right_valid:
            right_side_values.append(current_right)

    reversed_left_side_values.reverse()
    return reversed_left_side_values, right_side_values


def _calculat_footer_center(current_page, total_pages, around_len):

    left_around, right_around = _calculate_arounds(
        current_page,
        around_len,
        last_page=total_pages,
    )

    footer_center = [*left_around, current_page, *right_around]

    return footer_center


def _calculate_left_boundery(
    boundery_len,
    first_page_footer_center,
):

    left_boundery = []
    for page_num in range(1, boundery_len + 1):
        if page_num >= first_page_footer_center:
            break

        left_boundery.append(page_num)

    if len(left_boundery):
        last_page_left_boundery = left_boundery[-1]

        if last_page_left_boundery + 1 != first_page_footer_center:
            left_boundery.append(ELLIPSES)

    elif FIRST_PAGE != first_page_footer_center:
        left_boundery.append(ELLIPSES)

    return left_boundery


def _calculate_right_boundery(
    boundery_len,
    last_page,
    last_page_footer_center,
):
    reversed_right_boundery = []

    for i in range(0, boundery_len):
        page_num = last_page - i
        if page_num <= last_page_footer_center:
            break

        reversed_right_boundery.append(page_num)

    if len(reversed_right_boundery):
        first_page_right_boundery = reversed_right_boundery[-1]

        if last_page_footer_center != first_page_right_boundery - 1:
            reversed_right_boundery.append(ELLIPSES)

    elif last_page_footer_center != last_page:
        reversed_right_boundery.append(ELLIPSES)

    reversed_right_boundery.reverse()
    return reversed_right_boundery


def pagination_footer(
    current_page,
    total_pages,
    boundery_len,
    around_len,
):
    if total_pages <= 0:
        return ""

    if current_page > total_pages:
        current_page = total_pages
    elif current_page < 1:
        current_page = 1

    current_and_arround_pages = _calculat_footer_center(
        current_page,
        total_pages,
        around_len,
    )

    left_boundery_pages = _calculate_left_boundery(
        boundery_len,
        first_page_footer_center=current_and_arround_pages[0],
    )
    right_boundery_pages = _calculate_right_boundery(
        boundery_len,
        last_page=total_pages,
        last_page_footer_center=current_and_arround_pages[-1],
    )

    footer_elements = [
        *left_boundery_pages,
        *current_and_arround_pages,
        *right_boundery_pages,
    ]

    printable_footer = [str(value) for value in footer_elements]
    return " ".join(printable_footer)


def print_pagination_footer(
    current_page,
    total_pages,
    boundaries,
    around,
):
    pagination_footer_str = pagination_footer(
        current_page, total_pages, boundery_len=boundaries, around_len=around
    )

    print(pagination_footer_str)
