from typing import List


def get_user_urls() -> List[str]:
  raw_input = input("Insert URLs, separated by commas: ")
  
  while not raw_input:
    raw_input = input("Insert URLs, separated by commas: ")
  
  crude_urls = raw_input.replace(" ", "").split(",")
  
  urls = []
  if crude_urls:
    for url in crude_urls:
      if not url.startswith("https://"): continue
      if "magazineluiza.com" in url: urls.append(url)
      if "magazinevoce.com" in url: urls.append(url)
      if "amazon.com" in url: urls.append(url)
      
  return urls