import vk_api
import vk_api.bot_longpoll
import random
from _token import token

group_id = 224796843


class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            print("Получено событие")
            try:
                self.on_event(event)
            except Exception as err:
                print(err)

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_EVENT:
            print(event.object.text)
            self.api.message.send(
                messages=event.object.text,
                random_id=random.randint(0, 2 ** 20),
                peer_id=event.object.peer_id
            )
        else:
            print('Мы пока не умеем обрабатывать события такого типа', event.type)


if __name__ == '__main__':
    bot = Bot(group_id, token)
    bot.run()
