import re
import unicodedata as ud

from bs4 import BeautifulSoup
from nltk import FreqDist
from urllib.request import urlopen

from include import functions
from include.posTagGeneration.importURL import ImportURL
from include.posTagGeneration.importQuran import ImportQuran

def POS(textIn):
    modelCorpus = '/media/ahmed/College/grad project/Models/POS Models/POS/model/corpus/'
    modelSources = '/media/ahmed/College/grad project/Models/POS Models/POS/model/sources/'
    modelResults = '/media/ahmed/College/grad project/Models/POS Models/POS/model/results/'
    

    input = textIn

    tokStems = functions.tok_stem(input)
    normTokStems = functions.normalization(tokStems, modelSources)
    
    numberStems = len(normTokStems)
    numberUNK = 0

    #print('tokStems: ', tokStems)
    text = ''
    counter = 0
    while counter < len(tokStems):
        text += tokStems[counter] + ' '
        if normTokStems[counter] == 'مجه':
            numberUNK += 1
        counter += 1



    stemsTags = functions.viterbi(normTokStems, modelSources)
    #print('stemsTags: ', stemsTags)

    return tokStems, stemsTags
    #affix = text
    #print('affix: ', affix)

    '''text = ''
    tagsText = ''
    counter = 0
    while counter < len(stemsTags):
        tag = stemsTags[counter]
        token = tokStems[counter]

        tagsText += tag + ' '
        text += token + '/' + '<span style="background-color: yellow; font: bold 11px;">' + tag + '</span>' + ' '

        counter += 1


    print('tagsText: ', tagsText)
    
    return affix, tagsText
    file = open(self.mainWindow.modelResults+'Out.txt', 'w', encoding='utf-8')
    file.write(self.parentWindow.posTagTab.taggedTextEdit.toPlainText())
    file.close()'''

