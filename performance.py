from selenium import webdriver
import time
import json
import requests

# Documentation: https://developers.google.com/speed/docs/insights/v5/get-started

# JSON paths: https://developers.google.com/speed/docs/insights/v4/reference/pagespeedapi/runpagespeed


def get_performance(url):

    if not url.startswith('http://'):
        url = 'http://' + url

    # This is the google pagespeed api url structure, using for loop to insert each url in .txt file
    # If no "strategy" parameter is included, the query by default returns desktop data.
    x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile'
    print(f'Requesting {x}...')
    r = requests.get(x)
    final = r.json()

    #print(json.dumps(final, indent=4, sort_keys=True))

    performance = {"FCI": [], "FCP": [], "FMP": [], "FI": [], "items": []}

    try:
        # Tested Site Url
        urlid = final['id']
        split = urlid.split('?')  # This splits the absolute url from the api key parameter
        urlid = split[0]  # This reassigns urlid to the absolute url
        ID2 = str(urlid)
        #performance["url"] = ID2

        FCI = f" First CPU Idle  ~ {str(final['lighthouseResult']['audits']['first-cpu-idle']['displayValue'])} "
        FCI_score = f" First CPU Idle Score ~ {str(final['lighthouseResult']['audits']['first-cpu-idle']['score'])} "
        performance["FCI"].append(FCI)
        performance["FCI"].append(FCI_score)

        FCP = f" First Contentful Paint  ~ {str(final['lighthouseResult']['audits']['first-contentful-paint']['displayValue'])} "
        FCP_score = f" First Contentful Paint Score ~ {str(final['lighthouseResult']['audits']['first-contentful-paint']['score'])} "
        performance["FCP"].append(FCP)
        performance["FCP"].append(FCP_score)

        FMP = f" First Meaningful Paint  ~ {str(final['lighthouseResult']['audits']['first-meaningful-paint']['displayValue'])} "
        FMP_score = f" First Meaningful Paint Score ~ {str(final['lighthouseResult']['audits']['first-meaningful-paint']['score'])} "
        performance["FMP"].append(FMP)
        performance["FMP"].append(FMP_score)

        FI = f" Time to Interactive ~ {str(final['lighthouseResult']['audits']['interactive']['displayValue'])} "
        FI_score = f" Time to Interactive Score ~ {str(final['lighthouseResult']['audits']['interactive']['score'])} "
        performance["FI"].append(FI)
        performance["FI"].append(FI_score)

        item_data = final['lighthouseResult']['audits']['diagnostics']['details']['items'][0]

        for key in item_data:
            item = f" {key} ~ {item_data[key]}"
            performance["items"].append(item)

        print(performance)

        '''
        for i in performance:
            for j in performance[i]:
                print(j)
        '''

        return performance

    except KeyError:
        print(f'<KeyError> One or more keys not found {url}.')

