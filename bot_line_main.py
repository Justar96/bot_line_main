import requests
import hashlib
import json

img_url = 'https://cdn.discordapp.com/attachments/1202220195184119829/1228651415161802803/IMG_7053.jpg?ex=662cd1cc&is=661a5ccc&hm=482b152b962aafb84780de2de0d01c8ec89c930646680e2d71679d98e743c400&'
img_url_slip = 'https://imagedelivery.net/X2Gapb0ZkIiqSMuUxTsn5g/a50b77e8-7a6e-4186-2f69-1a3cf810d200/public'


# Method: Post
url = 'https://checkimg.jinda789.co.th:2096/get_slip_data'

header =  {'token':'private-ongphra-api','Content-Type':'application/json'}

# data
data={'image_url':img_url_slip}

r = requests.post(url,data=json.dumps(data),headers=header)

print(r.content)
# file_name = 'download.jpeg'

# with open(file_name,'rb') as f:
#     file_img = f.read()
# # print(r.content)
# hash_str = 'private-ongphra-api-' + str(file_name)
# hash_obj = hashlib.md5(hash_str.encode())
# hash_val = hash_obj.hexdigest()

# print(hash_str)
# print(hash_val)

# url = 'https://checkimg.jinda789.co.th:2096/get_ai_percent'
# header =  {'HashValue':hash_val,'origin':'1'}


# img_data = file_img

# # data
# files = {"image": (file_name, img_data)}

# r = requests.post(url,headers=header,files=files)
# # Example Output:
# # Response: {"ai_generated":true,"score":99}
# print(r.content)