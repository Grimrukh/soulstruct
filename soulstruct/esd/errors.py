class EsdError(Exception):
    def __init__(self, lineno, msg):
        self.lineno = lineno
        super().__init__(f"LINE {lineno}: {msg}")


class EsdSyntaxError(EsdError):
    pass


class EsdValueError(EsdError):
    pass
