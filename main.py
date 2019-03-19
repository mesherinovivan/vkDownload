# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
import vk, os, time, math



def takeSecond(elem):
    return elem['height']

def get_sizes(sz):
    found = False
    for sizes in sorted(sz, key=takeSecond, reverse=True):
        if (sizes['type'] == 'w'):
            found = True
            break
        elif (sizes['type'] == 'z'):
            found = True
            break
        elif (sizes['type'] == 'y'):
            found = True
            break

    if not found:
        return 'not found'
    else:
        return  sizes['src']

def download():
    alboms = vkapi.photos.getAlbums(owner_id=owner_id,v=5.92,need_system=1)
    for item in alboms['items']:
        album_id = item['id']
        for photo in vkapi.photos.get(owner_id=owner_id,v=5.9,album_id=album_id, photo_sizes=1,count=1000)['items']:
            pass
            src = get_sizes(photo['sizes'])
            if src == 'not found':
                print(photo['sizes'][len(photo['sizes'])-1]['src'])
                print('=================NONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN=================')

            photo_folder = 'saved/album{0}_{1}'.format(owner_id, album_id)
            if not os.path.exists(photo_folder):
                os.mkdir(photo_folder)
            try:
                urlretrieve(src, photo_folder + "/" + os.path.split(src)[1])  # Загружаем и сохраняем файл
            except Exception:
                print('Произошла ошибка, файл пропущен.')
                continue



import sys
if __name__ == '__main__':
    # Авторизация
    if len(sys.argv) < 5:
        print(u'Передайте в первом параметре логин, во втором пароль а в 3-м app_id a в 4 owner_id ')
        exit(-1)


    login = sys.argv[1]
    password = sys.argv[2]
    vk_id = sys.argv[3]

    session = vk.AuthSession(app_id=vk_id, user_login=login, user_password=password, scope='photos')

    vkapi = vk.API(session)
    # Разбираем ссылку

    owner_id = sys.argv[4]  #'16214148' # url.split('/')[-1].split('_')[0].replace('album', '')

    if not os.path.exists('saved'):
        os.mkdir('saved')

    download()
