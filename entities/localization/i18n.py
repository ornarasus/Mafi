import json
import os
import re
from entities.localization.language import Language


class I18n:
    __langs: dict[str, Language]

    def __init__(self):
        self.__langs = {}
        for f in os.listdir("locale/"):
            if re.match(r"^[a-z]+_[A-Z]+\.json$", f) is not None:
                with open(f"locale/{f}", "r", encoding="UTF-8") as fp:
                    self.__langs[f.split(".")[0]] = Language(json.load(fp))

    def __get__(self, _, __):
        return self.__langs[os.environ["LANGUAGE"]]