import operator
from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def counter(request):
    fulltext = request.GET['fulltext']

    word_list = fulltext.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # increment
            word_dictionary[word] += 1
        else:
            # add to dictiionary
            word_dictionary[word] = 1

    sorted_dict = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    print(fulltext)

    printed_dict = render(request, 'counter.html',{'fulltext':fulltext, 'count':len(word_list),
                                           'sorted_dict':sorted_dict})

    return printed_dict