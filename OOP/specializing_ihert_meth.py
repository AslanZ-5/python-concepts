class Super:
    context = {}

    def get_context_data(self, **kwargs):
        self.context = kwargs

    def delegate(self):
        self.action()


class Sub(Super):
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        self.context = kwargs


class Provider(Super):
    def action(self):
        print('in Provider.action')


class Fork:
    def delegate(self):
        self.action()
    def action(self):
        print('hello')
a = Fork()
a.delegate()

# a = Sub()
# a.get_context_data(name='aslan', age=35)
# print(a.context)
