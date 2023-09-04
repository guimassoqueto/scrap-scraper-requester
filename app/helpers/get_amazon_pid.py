from re import search

def get_amazon_pid(url: str) -> str | None:
    try:
        pid =  search(r"/dp/([A-Z0-9]+)", url).groups()[0]
        return pid
    except Exception as e:
        return None