class MyNode:
    def __init__(self, value, link=None):
        self.value = value
        self.link = link

    def __str__(self):
        return f"node with val {self.value}"

a = MyNode(0)
a.link = MyNode(1)
print(a)
print(a.link)
