import json
import os
import re
from entities.localization.language import Language


class I18n:
    __langs: dict[str, Language]

    def __init__(self):
        self.__langs = {}
        for f in os.listdir("locale/"):                                         # Search file in directory %ProjectDir%/locale/
            if re.match(r"^[a-z]+_[A-Z]+\.json$", f) is not None:               # Filter of files: xx_XX.json
                with open(f"locale/{f}", "r", encoding="UTF-8") as fp:          # Open file (read-only)
                    self.__langs[f.split(".")[0]] = Language(json.load(fp))     # Add object of Language class with parsed data

    def __get__(self, _, __):
        return self.__langs[os.environ["LANGUAGE"]]
    