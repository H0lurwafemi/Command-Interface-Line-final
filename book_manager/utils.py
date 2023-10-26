def validate_rating(rating):
    try:
        rating = float(rating)
        if 0.0 <= rating <= 5.0:
            return rating
        else:
            raise ValueError("Rating must be between 0.0 and 5.0.")
    except ValueError:
        raise ValueError(
            "Invalid rating. Please enter a numeric value between 0.0 and 5.0.")


def validate_input_length(input_str, max_length):
    if len(input_str) <= max_length:
        return input_str
    else:
        raise ValueError(
            f"Input exceeds the maximum length of {max_length} characters.")


def validate_not_empty(input_str):
    if input_str.strip():
        return input_str
    else:
        raise ValueError("Input should not be empty.")


def format_book_info(book):
    return f"Title: {book.title}\nAuthor: {book.author.name}\nGenre: {book.genre.name}\nRating: {book.rating}"


def format_book_list(books):
    if not books:
        return "No books found."
    book_list = [format_book_info(book) for book in books]
    return "\n\n".join(book_list)
