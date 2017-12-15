from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('https://testapi.fadada.com:8443/api/gotoSign.action?v=2.0&app_id=400563&send_app_id=&transaction_id=00848171ca00431d9eafbf896960f9ef&extSignId=2c928381605453700160546c7394373d&client_id=15A35E723AF4827EA5BE34A3C0ADB16A&contractTargetId=47924257&accountId=151306255615148&proxyId=&return_url=http%3A%2F%2F116.62.207.57%2Fcontract%2FsignSuccess%3FcustomerId%3Dc2a9329632d642d9861ac8478c0fc1f6&accountEmail=ceshiyouxiang%40qq.com&fddTcid=408783cd6b2145a88f70bb67b5b56eae&sign_keyword=&keyword_strategy=&isScale=1&ext_data=&signature_positions=')
driver.find_element_by_xpath('//*[@id="signpanel"]/div/img')
