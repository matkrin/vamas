class FileExtensionError(Exception):
    def __init__(self) -> None:
        message = (
            "The file is not a vamas file, file extension needs to be '.vms'"
        )
        super().__init__(message)


class VmsIdentifierError(Exception):
    def __init__(self) -> None:
        message = "The file does not contain the correct vamas identifier"
        super().__init__(message)
