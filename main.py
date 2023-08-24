import undetected_chromedriver as uc

if __name__ == '__main__':
    driver = uc.Chrome(headless=True,use_subprocess=False)
    driver.get('https://www.idealista.com/venta-viviendas/madrid/moncloa/con-precio-hasta_600000,metros-cuadrados-mas-de_100/')
    html_source = driver.page_source
    with open('test.html', 'w') as f_out:
        f_out.write(html_source)