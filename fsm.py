from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'hello'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'who are you'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '你給我翻譯翻譯 什麼叫驚喜'
        return False

    def is_going_to_state3_2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '我叫你翻譯給我聽 什麼叫驚喜'
        return False

    def is_going_to_state3_3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '這就是驚喜阿'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return (text.lower() != 'hello' and text.lower() != 'who are you' and text.lower() != '你給我翻譯翻譯 什麼叫驚喜')
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "哈囉")
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "我是牆壁")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "這還要翻譯 就是驚喜阿")

    def on_exit_state3(self,event):
        print('Leaving state3')

    def on_enter_state3_2(self, event):
        print("I'm entering state3_2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "驚喜就是三天之後我給你一百八十萬兩銀子出城剿匪 接上我的腿 明白了嗎")

    def on_exit_state3_2(self, event):
        print('Leaving state3_2')

    def on_enter_state3_3(self, event):
        print("I'm entering state3_3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "...")
        self.go_back()

    def on_exit_state3_3(self):
        print('Leaving state3_3')   
        
    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "公三小")
        self.go_back()

    def on_exit_state4(self):
        print('Leaving state4')
