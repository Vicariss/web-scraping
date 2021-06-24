import urllib.parse as urlparse
import requests


def check_url(url):

    response = requests.get(url)  # send request
    status_code = response.status_code  # get status code

    #  check if connection is valid
    if status_code == 200:
        print(f'* HTTP Status code: {status_code}, request successful *\n')
    else:
        print(f'* HTTP Status code: {status_code}, request failed *\n')

    print('---Headers---')

    headers_dict = response.headers  # retrieve headers

    for key in headers_dict:
        print(f'{key}: {headers_dict[key]}')

    parsed_url = urlparse.urlparse(url)  # parsing url
    parsed_query = urlparse.parse_qs(parsed_url.query)  # parsing query string
    params_dict = dict.copy(parsed_query)

    if len(params_dict) == 0:
        print('No parameters in URL.')
    else:
        print('\n---Parameters---')
        for key in params_dict:
            for item in params_dict[key]:
                print(f'{key}: {item}')
             