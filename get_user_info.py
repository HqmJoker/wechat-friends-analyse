import itchat
import json
import codecs

sex_dict = {}
sex_dict['0'] = "其他"
sex_dict['1'] = "男"
sex_dict['2'] = "女"

#下载好友头像
def download_images(frined_list):
    image_dir = "./images/"
    num = 1
    for friend in frined_list:
        image_name = str(num)+'.jpg'
        num+=1
        img = itchat.get_head_img(userName=friend["UserName"])
        with open(image_dir+image_name, 'wb') as file:
            file.write(img)

def save_data(frined_list):
    out_file_name = "./data/friends.json"
    with codecs.open(out_file_name, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(frined_list,ensure_ascii=False))

if __name__ == '__main__':
    itchat.auto_login()
    
    friends = itchat.get_friends(update=True)[0:]#获取好友信息
    friends_list = []
    # with open('./data/wechat-friends.json') as f:
    #     friends = json.load(f)
    #     friends_list = []

    for friend in friends:
        item = {}
        item['NickName'] = friend['NickName']
        item['HeadImgUrl'] = friend['HeadImgUrl']
        item['Sex'] = sex_dict[str(friend['Sex'])]
        item['Province'] = friend['Province']
        item['Signature'] = friend['Signature']
        item['UserName'] = friend['UserName']

        friends_list.append(item)

    save_data(friends_list)
    download_images(friends_list)
