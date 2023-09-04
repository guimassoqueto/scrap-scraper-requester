def is_magalu(url: str) -> bool:
  if "magazineluiza.com" in url: return True
  if "magazinevoce.com" in url: return True
  return False


def is_amazon(url: str) -> bool:
  if "amazon.com" in url: return True
  return False