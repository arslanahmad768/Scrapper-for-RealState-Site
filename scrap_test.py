from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Setup Chrome options
options = Options()

# Add the custom headers
options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7")
options.add_argument("accept-encoding=gzip, deflate, br, zstd")
options.add_argument("accept-language=en-US,en;q=0.9,ar;q=0.8,ur;q=0.7")
options.add_argument("cache-control=no-cache")
options.add_argument("pragma=no-cache")
options.add_argument("sec-ch-ua=\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"")
options.add_argument("sec-ch-ua-mobile=?0")
options.add_argument("sec-ch-ua-platform=\"Windows\"")
options.add_argument("sec-fetch-dest=document")
options.add_argument("sec-fetch-mode=navigate")
options.add_argument("sec-fetch-site=none")
options.add_argument("sec-fetch-user=?1")
options.add_argument("upgrade-insecure-requests=1")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

# Initialize WebDriver
service = Service("C:/Users/Majid Ali/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Add cookies (as given in the headers)
cookies = {
    'reauid': '627e19b85a5a0d001019cc6696020000ae010000',
    'Country': 'PK',
    'split_audience': 'a',
    'AMCVS_341225BE55BBF7E17F000101%40AdobeOrg': '1',
    's_cc': 'true',
    'VT_LANG': 'language%3Den-US',
    'mid': '3572813873170068439',
    'topid': 'REAUID:627E19B85A5A0D001019CC6696020000AE010000',
    'KFC': 'nlosx3D+znCwDgjHY8uWhNOoZaUFTW53/vDNWvYGRHU=',
    'QSI_HistorySession': 'https%3A%2F%2Fwww.realestate.com.au%2F~1724745442046%7Chttps%3A%2F%2Fwww.realestate.com.au%2Ffind-agent~1724826760141%7Chttps%3A%2F%2Fwww.realestate.com.au%2Fagent%2Fmax-hui-1881998%3FcampaignType%3Dinternal%26campaignChannel%3Din_product%26campaignSource%3Drea%26campaignName%3Dsell_enq%26campaignPlacement%3Dagent_search_result_card%26campaignKeyword%3Dagency_marketplace%26sourcePage%3Dagent_srp%26sourceElement%3Dagent_search_result_card~1724835643015',
    'AMCV_341225BE55BBF7E17F000101%40AdobeOrg': '-330454231%7CMCIDTS%7C19964%7CMCMID%7C09213331464425107858267012453025087009%7CMCAID%7CNONE%7CMCOPTOUT-1724853030s%7CNONE%7CvVersion%7C3.1.2',
    '_lr_geo_location_state': 'PB',
    '_lr_geo_location': 'PK',
    'KP_UIDz-ssn': '032L9TEggWHeFQx349gcbghRvIsfX4e7jmmhzXSTdLmsMgGRFXxpIPKyrtjZVRWMOlyuI0TEshSBcB5yvfBLYE8f2rvzIP1jng0QPY6uMwo5r4QPIJacpPCpoiEOpghqk1ygdLVVevyytbsmwIkIXF15qEEb4tMcDx21sDkZtn',
    'KP_UIDz': '032L9TEggWHeFQx349gcbghRvIsfX4e7jmmhzXSTdLmsMgGRFXxpIPKyrtjZVRWMOlyuI0TEshSBcB5yvfBLYE8f2rvzIP1jng0QPY6uMwo5r4QPIJacpPCpoiEOpghqk1ygdLVVevyytbsmwIkIXF15qEEb4tMcDx21sDkZtn',
    's_sq': '%5B%5BB%5D%5D',
    'KP2_UIDz-ssn': '0F6aLpoV6bsjjejWrjIwWOygKbLd10yiFP3V6ozKRP6HFyNyecnmmOBu71x5lJrhsY8hT8u2Ca883qTt8vh9DzoSf9E3UPx3u4prHT2rhoKJ3ABLevZjzgb7aQb2xZfii4TsfaTff6lyTPGfhZ9WmV2huGA2ta15dkgI8bDY',
    'KP2_UIDz': '0F6aLpoV6bsjjejWrjIwWOygKbLd10yiFP3V6ozKRP6HFyNyecnmmOBu71x5lJrhsY8hT8u2Ca883qTt8vh9DzoSf9E3UPx3u4prHT2rhoKJ3ABLevZjzgb7aQb2xZfii4TsfaTff6lyTPGfhZ9WmV2huGA2ta15dkgI8bDY',
    'pageview_counter.srs': '15',
    's_nr30': '1724846661385-Repeat',
    'utag_main': 'v_id:01918d41fa1a00a9ad8f762bcf780506f001e06700bd0$_sn:7$_se:4$_ss:0$_st:1724848461265$vapi_domain:realestate.com.au$dc_visit:9$ses_id:1724845830218%3Bexp-session$_pn:4%3Bexp-session$_prevpage:rea%3Afind%20agent%3Aagent%3Asearch%20results%3Bexp-1724850261384$dc_event:4%3Bexp-session'
}

# Visit the specific URL
url = "https://www.realestate.com.au/agent/andrew-farnworth-3536844?campaignType=internal&campaignChannel=in_product&campaignSource=rea&campaignName=sell_enq&campaignPlacement=agent_search_result_card&campaignKeyword=agency_marketplace&sourcePage=agent_srp&sourceElement=agent_search_result_card"
driver.get(url)

# Add the cookies to the session
for name, value in cookies.items():
    driver.add_cookie({"name": name, "value": value})

# Refresh the page to apply cookies
driver.refresh()

# Wait for the page to load completely and print the title
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "title"))
    )
    print("Page title is:", driver.title)
except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()
