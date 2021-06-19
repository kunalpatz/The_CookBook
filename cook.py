def replace_text(string, char_to_replace):
    for key, value in char_to_replace.items():
        string = string.replace(key, value)
    return string


def process_list_sql(text):
    option_value_string = text.split(',')[0].split(' as ')[0].strip('select ')
    option_name_string = text.split(',')[1].split(' as ')[0].strip().replace("'", "")
    return {'%option_value%': option_value_string, '%option_name%': option_name_string}


class API:
    def __init__(self, recipes):
        self.dateContent = recipes['elements'][0]['content'][1]['content'][0]
        self.productContent = recipes['elements'][0]['content'][1]['content'][1]
        self.batchContent = recipes['elements'][0]['content'][1]['content'][2]
        self.numberContent = recipes['elements'][0]['content'][1]['content'][3]
        self.reasonContent = recipes['elements'][0]['content'][1]['content'][4]
        self.recipes = recipes

    def build_page(self, ingredients):
        with open('src/templates/home.html', 'w') as homepage:
            homepage.writelines(ingredients['root']['html']['before'])

            homepage.writelines(
                "<link rel = \"stylesheet\" type = \"text/css\" href = \"../static/css/common.css\"> </head>")

            intermediate = replace_text(ingredients['root']['html']['list'], {'<body>': '',
                                                                                   ' id="overlay" onclick="hidehelp()"': '',
                                                                                   ' id="help_modal"': '',
                                                                                   '<p>Help Text</p>': ''})

            homepage.writelines(
                '<body><fieldset class="black">' + intermediate + '</fieldset><fieldset> <div class="dataItem"><legend>' +
                ingredients['title']['html']['before'].replace('%display_name%',
                                                               self.recipes['name']) + '</legend></div>')

            homepage.writelines(ingredients['group']['html']['before'].replace('%display_name%',
                                                                               self.recipes['elements'][0]['content'][
                                                                                   1][
                                                                                   'display_name']))
            homepage.writelines(ingredients['form']['html']['before'].replace('%element_id%',
                                                                              self.recipes['elements'][0][
                                                                                  'element_id']))
            homepage.writelines(
                replace_text(ingredients['date']['html'], {'%element_id%': self.dateContent['element_id'],
                                                                '%display_name%': self.dateContent['display_name'],
                                                                '%element_name%': self.dateContent['element_name'],
                                                                '%help%': self.dateContent['help']}))

            homepage.writelines(replace_text(ingredients['select']['html']['before'],
                                             {'%element_id%': self.productContent['element_id'],
                                                   '%display_name%': self.productContent[
                                                       'display_name'],
                                                   '%element_name%': self.productContent[
                                                       'element_name']}))
            homepage.writelines(replace_text(ingredients['select']['html']['list'],
                                             process_list_sql(self.productContent['list_sql'])))
            homepage.writelines(ingredients['select']['html']['after'])
            homepage.writelines(
                replace_text(ingredients['text']['html']['before'],
                                  {'%element_id%': self.batchContent['element_id'],
                                   '%display_name%': self.batchContent['display_name'],
                                   '%element_name%': self.batchContent['element_name'],
                                   '%placeholder%': self.batchContent['placeholder']}))
            homepage.writelines(replace_text(ingredients['number']['html']['before'],
                                             {'%element_id%': self.numberContent['element_id'],
                                                   '%display_name%': self.numberContent['display_name'],
                                                   '%element_name%': self.numberContent['element_name'],
                                                   '%placeholder%': self.numberContent['placeholder'],
                                                   '%min_val%': self.numberContent['min_val'],
                                                   '%step_val%': self.numberContent['step_val']}))

            homepage.writelines(replace_text(ingredients['select']['html']['before'],
                                             {'%element_id%': self.reasonContent['element_id'],
                                                   '%display_name%': self.reasonContent['display_name'],
                                                   '%element_name%': self.reasonContent['element_name'],
                                                   }))
            homepage.writelines(
                replace_text(ingredients['select']['html']['list'],
                                  process_list_sql(self.reasonContent['list_sql'])))
            homepage.writelines(ingredients['select']['html']['after'])
            homepage.writelines(ingredients['form']['html']['after'])
            homepage.writelines(ingredients['group']['html']['after'])
            homepage.writelines("<script src = \"../static/js/common.js\"> </script>")

            homepage.writelines(
                replace_text(ingredients['root']['html']['after'], {'</body>': '</fieldset></body>'}))
        return 0

    def build_css(self, ingredients):
        with open('src/static/css/common.css', 'w') as css:
            css.writelines(ingredients['form']['css']['head'])
            css.writelines(ingredients['title']['css']['head'])
            css.writelines(ingredients['group']['css']['head'])
            css.writelines(ingredients['date']['css'])
            css.writelines(ingredients['text']['css']['head'])
            css.writelines(".online \n { \n color: green; \n text-align: right;\n }")
            css.writelines(".cache \n { \n color: grey; \n text-align: right;\n }")
            css.writelines(".topbar \n { \n margin-left: auto;\n }")
            css.writelines(".black\n { \n background-color: black;\nmargin-bottom:0px;\n }")
        return 0

    def build_js(self, ingredients):
        with open('src/static/js/common.js', 'w') as js:
            js.writelines(
                replace_text(ingredients['date']['js']['foot'], {'%element_id%': self.dateContent['element_id']}))
        return 0
