class Language:
    __locale: dict[str, str]

    def __init__(self, locale: dict[str, dict]):
        self.__locale = {}
        for k, d in locale.items():
            self.__recurse(k, d)

    def __recurse(self, name: str, d: dict):
        for k, v in d.items():
            if isinstance(v, dict):
                self.__recurse(f"{name}.{k}", dict(v))
            elif isinstance(v, str):
                self.__locale[f"{name}.{k}"] = v
            elif isinstance(v, list):
                for i, text in enumerate(v):
                    self.__locale[f"{name}.{k}.{i}"] = text
            else:
                raise TypeError(type(v))


    def __getitem__(self, index):
        return self.__locale[index]
