class HTMLBuilder:
    def __init__(self):
        self.__body = ""

    def __add_element(self, name: str, content: str = "", pair: bool = True, **params):
        element = "<" + name
        option = [f'{key}="{value}"' for key, value in params.items()]
        if option:
            element += " " + " ".join(option)
        if pair:
            element += f">{content}</{name}>"
        else:
            element += ">"
        return element

    def set_title(self, title: str):
        self.__title = title

    def add_paragraph(self, text: str):
        self.__body += self.__add_element("p", text, True)

    def add_link(self, href: str, text: str):
        self.__body += self.__add_element("a", text, True, href=href)

    def add_div(self, text: str):
        self.__body += self.__add_element("div", text, True)

    def add_h(self, number: int, text: str):
        self.__body += self.__add_element(f"h{number}", text, True)

    def add_img(self, URL: str):
        self.__body += self.__add_element("img", "", False, src=URL)

    def add_list(self, teg: str, array: list):
        self.__body += self.__add_element(teg, "", False)
        for i in range(len(array)):
            self.__body += self.__add_element("li", array[i], True)
        self.__body += f"</{teg}>"

    def change_text(self, teg: str, text: str):
        self.__body += self.__add_element(teg, text, True)

    def get_body(self) -> str:
        return self.__body

    def render(self):
        return f"""
    <html>
        <head>
            {self.__add_element("title",self.__title, True)}
        </head>
        <body>
            {self.__body}
            </body>
    </html>
    """


html = HTMLBuilder()
html.set_title("Test")
html.add_paragraph("First")
html.add_link("https://www.google.ru/", "Кликни")
html.add_div("fsdfd")
html.add_h(1, "Меня зовут Оксана")
html.add_img("https://www.tuninggeneration.it/wordpress/wp-content/uploads/2019/08/AC-Schnitzer-BMW-X5-G05-Tuning-01.jpg")
html.change_text("strong", "Я очень люблю")
html.add_list("ol", ["Играть в баскетбол", "777"])
print(html.render())

