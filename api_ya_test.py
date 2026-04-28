import requests

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = 'dict.1.1.20220928T183617Z.4449b33063fe4328.b93679d48620ed6f3c20da6bff0237bcbd0e8d6a'

def translate_word(word):
    params = {
        'key': token,
        'lang': 'ru-en',
        'text': word
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # Отладка - выводим весь ответ
    print(f"Word: {word}")
    print(f"Response: {data}")
    
    try:
        trans_word = data['result'][0]['tr'][0]
    except (KeyError, IndexError) as e:
        print(f"Error: {e}")
        trans_word = ''
    
    return trans_word
if __name__ == '__main__':
    word = 'машина'
    assert translate_word(word) == 'car'
