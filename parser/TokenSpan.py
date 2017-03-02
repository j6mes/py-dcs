class TokenSpan():
    def __init__(self,tokens,start_token,end_token):
        self.start_token = start_token
        self.end_token = end_token
        self.tokens = tokens[start_token:end_token]


if __name__ == "__main__":
    ts = TokenSpan("the cat sat on the mat".split(),1,2)