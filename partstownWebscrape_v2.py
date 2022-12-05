from bs4 import BeautifulSoup
import requests
import pandas as pd

url_list_html = 'https://www.partstown.com/true/gdm-72/parts'
#url_list_html_page_0 = 'https://www.partstown.com/true/gdm-72/parts?page=0'

output_file = '/Users/yrout/internship/partstownOutput.csv'


def get_data(url):
   try:
      req =  requests.get(url, timeout=60)
      soup = BeautifulSoup(req.text, 'html.parser')
      #print(req.text)
      return soup
   except requests.exceptions.RequestException as e:
      print (e) 


def get_url_list(url_list_html):
  url_list = []
  print(url_list_html)
  url_list_section = get_data(url_list_html)
  #print(url_list_section)
  parts = url_list_section.find_all('a',{'class': 'js-link-paging'})
  #for part in parts:
     #print(part)
     #url_list.append(part['data-base-url'])
     #print(part['data-base-url'])
  #return url_list


def parse(soup):
   partsList = []

   aList = soup.find_all('div', {'class' : 'details'})

   for a in aList:
      
      item_name = a.find('div',{'class' : 'name'}).text

      #print(item_name)

      item_name_str = item_name

      item_name_str = item_name_str.replace("&nbsp", " ") 

      #print("Name is :" + item_name_str)

      serial_num = item_name_str[7:13]

      #print("Serial number is: " + serial_num)

      product = {
         'Category': 'Resturant',
         'Asset': 'Refigerator',
         'Manufacturer': 'True',
         'Model': 'GDM-72',
         'Product Name': item_name_str,
         'Serial Number': serial_num
         
      }

      # Create an array with part phrases
      # Read each phrase from array
      # Compare each phrase to the product name
      # Add to the output file if part's phrase is present in product name

      parts_phrase_list = ["gasket", "compressor", "door", "hinge", "screw"]

      found = False
      for single_parts_phrase in parts_phrase_list:
         if single_parts_phrase.lower() in item_name_str.lower():
            found = True
      if found == True:
         partsList.append(product)

   return partsList

def output(partslist):
   partsdf = pd.DataFrame(partslist)
   partsdf.to_csv(output_file, index=False)
   print('Saved to CSV')
   return


#url_list = get_url_list(url_list_html) 
#for url in url_list:
soup = get_data(url_list_html)
parts_list = parse(soup)

output(parts_list)




