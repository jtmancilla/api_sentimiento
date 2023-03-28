import datetime


def prepare_text(text):
    text = str(text)
    text = text.strip()
    text = text.lower()

    return text


def get_current_datetime():
    return f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC"