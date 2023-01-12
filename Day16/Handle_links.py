driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()
# Find Total no. Links
#links=driver.find_elements(By.TAG_NAME,'a')
# links=driver.find_elements(By.XPATH,'//a')
# print("Total no. of links",len(links))
# #PRint all the links name
#
# for link in links:
#     print(link.text)