class MockRequest:
    def __init__(self, user):
        self.user = user
        self.GET = {}
        self.POST = {}
