##########
# Errors
##########

class Error:
    def __init__(self, errorName, details):
        self.errorName = errorName
        self.details = details

    def toString(self):
        return f'{self.errorName}: {self.details}'


class IllegalCharacterError(Error):
    def __init__(self, details):
        super().__init__("IllegalCharacterError", details)
