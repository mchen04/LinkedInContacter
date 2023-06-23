import requests
from bs4 import BeautifulSoup

def get_url(): 
    # Prompt the user to input a string
    LinkedIn_URL = input("Enter a string: ") 
    html_text = requests.get(LinkedIn_URL)
    soup 










#<a data-control-id="¨qAÙKg­5´´7QÑ" data-control-name="view_lead_panel_via_search_lead_name" 
#href="/sales/lead/ACwAAC7xS88B1uwTQmWgouHGluSQB6lzklAT-js,NAME_SEARCH,3F9T?_ntb=dxCjIYsdQSSbq63FYxYtJg%3D%3D" 
#id="ember5167" class="ember-view" data-lead-search-result="profile-link-st4331">
#<span data-anonymize="person-name">Eric Zhao</span>
