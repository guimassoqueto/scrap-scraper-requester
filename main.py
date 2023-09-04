from app.helpers.user_input import get_user_urls
from app.helpers.check_url import is_amazon, is_magalu
from app.helpers.get_amazon_pid import get_amazon_pid
from app.infra.rabbitmq import RabbitMQ
from app.settings import AMAZON_QUEUE, MAGALU_QUEUE

magalu_message = {
  MAGALU_QUEUE: []
}

amazon_message = {
  AMAZON_QUEUE: []
}


if __name__ == "__main__":
  urls = get_user_urls()
  
  for url in urls:
    if is_amazon(url):
      pid = get_amazon_pid(url)
      if isinstance(pid, str): amazon_message[AMAZON_QUEUE].append(pid)
    if is_magalu(url): magalu_message[MAGALU_QUEUE].append(url)

  if magalu_message[MAGALU_QUEUE]:
    rabbitmq = RabbitMQ(MAGALU_QUEUE)
    rabbitmq.send_message(magalu_message)
    print(f"{len(magalu_message[MAGALU_QUEUE])} to {MAGALU_QUEUE}")

  if amazon_message[AMAZON_QUEUE]:
    rabbitmq = RabbitMQ(AMAZON_QUEUE)
    rabbitmq.send_message(amazon_message)
    print(f"{len(amazon_message[AMAZON_QUEUE])} to {AMAZON_QUEUE}")

  