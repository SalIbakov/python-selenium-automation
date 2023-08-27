class Page:


    def click(self):
        print('Clicking...')

    def input_text(self):
        print('Inputting text...')

    def open(self, end_url=''):
        print(f'Openning https://www.amazon.com/{end_url}...')


class Signin(Page):

    def open_signin(self):
        self.open(end_url='signin')

class ProductDetails(Page):
    pass


signin_page = Signin()
signin_page.click()
signin_page.open_signin()

#product_details_page = ProductDetails()
#product_details_page.input_text()