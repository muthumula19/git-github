class Device:
    def __init__(self,name,page):
        self.name=name
        self.page=page
    # def __repr__(self):
    #     return f'Name {self.name} and page {self.page}'
    def device(self):
        n=self.page+2
        return n
class printer(Device):
    def __init__(self,title,name,page):
        super().__init__(name,page)
        self.title=title
    def prin(self):
        return f'titel {self.title}'
# p=Device('naresh',124)
# print(p.device())
v=printer('Comady','hs',12)
print(v.prin())