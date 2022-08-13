from bs4 import BeautifulSoup
import requests, re

url = 'https://mcf.knust.edu.gh/index.php/staff'

res = requests.get(url)
print(res.status_code)

soup = BeautifulSoup(res.content, 'html.parser')

res = soup.find_all("div", class_="col-sm-2")
print(res[0].get('div'))

# https://mcf.knust.edu.gh/sites/mcf.knust.edu.gh/files/2021-06/Ms%20Afia%20Ampomah%20Awuah.jpg

# <div class="col-sm-2">
# <div class="staff-img"> <img alt="" height="2170" src="/sites/mcf.knust.edu.gh/files/2021-06/Ms%20Afia%20Ampomah%20Awuah.jpg" title="Ms Afia Ampomah Awuah" typeof="Image" width="1800"/>
# </div>
# <div class="staff-name">
# <a href="/index.php/staff/afia-ampomah-awuah"><h4><span>Ms</span> <span>Afia Ampomah Awuah</span></h4></a>
# <h5>Program Manager</h5>
# </div>
# </div>