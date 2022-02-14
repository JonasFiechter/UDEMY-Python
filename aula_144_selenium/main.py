from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class EdgeAuto:
    def __init__(self):
        self.driver_path = 'msedgedriver'
        self.options = webdriver.EdgeOptions()
        # self.options.add_argument('user-data-dir=Perfil')
        self.edge = webdriver.Edge(
            self.driver_path,
            options=self.options
        )

    def sign_in(self):
        try:
            btn_sign_in = self.edge.find_element(By.NAME, 'csi')
            btn_sign_in.send_keys('QUALQUER COISA')
        except Exception as e:
            print(f'Erro {e}, ao clicar em sign in.')

    def acessa(self, site):
        self.edge.get(site)

    def quit(self):
        self.edge.quit()


if __name__ == '__main__':
    edge = EdgeAuto()
    sleep(4)
    edge.acessa('https://google.com')
    sleep(2)
    edge.sign_in()