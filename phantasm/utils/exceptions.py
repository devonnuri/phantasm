class WASMError(BaseException):
    pass


def wasm_assert(condition: bool, message: str):
    if not condition:
        raise WASMError(message)
