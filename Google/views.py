from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

def home(request):
    return render(request, 'Google/index.html')


def error_500(request):
    return render(request, 'Google/error_page/chrome.html',{})

def error_400(request, exception):
    return render(request, 'Google/error_page/chrome.html',{})

def error_403(request, exception):
    return render(request, 'Google/error_page/chrome.html',{})

def error_404(request, exception):
    return render(request, 'Google/error_page/chrome.html',{})

# def search(request):
#     if request.method == 'POST':
#         search_query = request.POST['search']
#         url = 'https://in.search.yahoo.com/search?p=' + search_query
      
#         res = requests.get(url)
#         soup = bs(res.text, 'lxml')

#         result_listings = soup.find_all('div', {'class': 'algo-sr'})
#         final_result = []

#         for result in result_listings:
#             result_title = result.find('h3').text
#             result_url = result.find('a')['href']
#             result_desc = result.find('div', {'class': 'compText'}).text

#             final_result.append((result_title, result_url, result_desc))

#         context = {
#             'final_result': final_result
#         }

#         return render(request, 'Google/search.html', context)
#     else:    
#         return render(request, 'Google/search.html')


'''The below code is same as above but this code give more wed results'''
import requests
from bs4 import BeautifulSoup as bs

def search(request):
    if request.method == 'POST':
        search_query = request.POST['search']
        num_results = 30  # Number of results to retrieve
        results_per_page = 10  # Number of results per page

        final_result = []

        for page_num in range(num_results // results_per_page):
            start = page_num * results_per_page + 1
            url = f'https://in.search.yahoo.com/search?p={search_query}&b={start}'
            res = requests.get(url)
            soup = bs(res.text, 'lxml')

            result_listings = soup.find_all('div', {'class': 'algo-sr'})

            for result in result_listings:
                result_title = result.find('h3').text
                result_url = result.find('a')['href']
                result_desc = result.find('div', {'class': 'compText'}).text

                final_result.append((result_title, result_url, result_desc))

                if len(final_result) >= num_results:
                    break

            if len(final_result) >= num_results:
                break

        context = {
            'final_result': final_result
        }

        return render(request, 'Google/search.html', context)
    else:
        return render(request, 'Google/search.html')
    
