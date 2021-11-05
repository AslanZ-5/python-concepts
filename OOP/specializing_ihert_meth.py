class Super:
    context = {}
    def get_context_data(self,**kwargs):
        self.context = kwargs



class Sub(Super):
    def get_context_data(self,**kwargs):
        super().get_context_data(**kwargs)
        self.context = kwargs

a = Sub()
a.get_context_data(name='aslan',age=35)
print(a.context)
