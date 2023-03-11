import requests
TOKEN = 'y0_AgAAAAAKqp3uAADLWwAAAADdE8MH5IvZg_JETn-tiWBhlS3pOPeHv4w'

def create_new_folder(token, folder_name):
    url = f"https://cloud-api.yandex.net/v1/disk/resources?path={folder_name}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    response = requests.put(url, headers=headers)
    if response.status_code == 201:
        print('Папка успешно создана')
    if response.status_code == 409:
        print('Такая папка уже есть')

    return response.status_code

# print(create_new_folder(TOKEN, 'New folder'))
