# filters out quirks of the way the articles get sent to us such as "==" and "==="


class QuirkFilter():
    BLACKLIST={"==", "==="}
    def __call__(self, words):
        return [word for word in words if not word in QuirkFilter.BLACKLIST]