from selenium import webdriver



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)

driver.get('http://img.sslibrary.com/n/slib/book/\
           slib/12985828/9067519fe8a64304b8c2495b9fff1342/c2cc71536ab68784452d023ec24f9544.shtml?\
           dxbaoku=true&deptid=7143&fav=http%3A%2F%2Fwww.sslibrary.com%2Freader%2Fpdg%2Fdxpdgrea\
           der%3Fd%3Df4fc2f98331b36f7f6cf84bfe44eb899%26enc%3Dc1548284b2655b3b0faf18ba2f65f012%2\
           6ssid%3D12985828%26did%3D7143%26username%3Dfyht_7143&fenlei=18170408&spage=1&t=5&user\
           name=fyht_7143&view=-1')
page_source = driver.page_source


