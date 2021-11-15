import myCall


class myCalls:

    def __init__(self, calls_list: []):
        self.calls_list = calls_list

    def add_call(self, call: myCall):
        self.calls_list.append(myCall)

    def get_call_list(self) -> []:
        return self.calls_list
