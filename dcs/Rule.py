class Rule():
    def __init__(self,input_type, output_type):
        self.input_type = input_type
        self.output_type = output_type

    def check(self,input):
        if type(input) is not self.input_type or (type(input) == Rule and input.output_type == self.input_type):
            raise Exception("Rule must operate on a " + str(self.input_type) + " but a " + str(type(input)) + " was provided instead")

    def __emit__(self, input):
        pass


