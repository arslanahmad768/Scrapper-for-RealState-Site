from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# # Setup options to add custom headers
options = Options()

# Disable automation flag
options.add_argument("--disable-blink-features=AutomationControlled")

# Add the custom headers as arguments
options.add_argument(
    "accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7")
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
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

service = Service("C:/Users/Arslan Ahmad/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Set cookies
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
# Visit the website
driver.get("https://www.realestate.com.au/find-agent")

# Add cookies
for name, value in cookies.items():
    driver.add_cookie({"name": name, "value": value})

# Refresh to ensure cookies are applied
driver.refresh()

# Wait for the search bar to be visible


regions = ["ABBEYARD", "ABBOTSFORD"]
for area in regions:
    search_bar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "hero-search-bar"))
    )
    print("Main page tiyle", driver.title)
    search_bar.send_keys(area)

    # Wait for recommendations to load (adjust time as needed)
    time.sleep(3)

    # Fetch all the recommendation elements
    recommendations = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "hero-search-bar-menu"))
    )

    for recommendation in recommendations:
        print("ecommendation found", recommendation)
        print("text of recommendation", recommendation.text)
        recommendation.click()
        # driver.refresh()
        # Wait for the new page to fully load
        try:
            WebDriverWait(driver, 20).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            print("Page ready state complete.")

        except:
            print("Page did not load properly, timeout occurred.")
            continue

        agents = driver.find_elements(By.CLASS_NAME, "ResultsHeader__no-result__header")
        if agents:
            print("No agents Found")
            # driver.back()
            continue
        result_section = driver.find_elements(By.CLASS_NAME, "results-section")

        time.sleep(10)
        if result_section:
            child_divs = result_section[0].find_elements(By.TAG_NAME, "div")
            for child_div in child_divs:
                # Extract data from the child div as needed
                div_text = child_div.find_element(By.CLASS_NAME, "agent-card__profile").find_element(By.TAG_NAME, 'a').get_attribute("href")
                print("Agents Found", div_text)
        print("Checking data......", agents)
        print("page tiyle", driver.title)
    driver.back()
    time.sleep(5)

# Print the title of the page


# Close the browser
# driver.quit()
