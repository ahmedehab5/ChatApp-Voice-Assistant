from  pos import POS
from NER.tagger import NER
from classification.classification import classify


def getNERInput(tokStems, stemsTag):
    posTarget = ''
    i = 0
    while i < len(tokStems):
        if stemsTag[i] == 'SUFF_F_S':
            posTarget += tokStems[i]
        elif stemsTag[i] == 'IV2' or stemsTag[i] == 'IV3' or stemsTag[i] == 'IV1':
            posTarget += tokStems[i] + tokStems[i+1]
            i += 1
        elif tokStems[i] == 'علي':
            posTarget += ' ' + tokStems[i]
        elif stemsTag[i] != 'PREP' and stemsTag[i] != 'INTERROGATE':
            posTarget += ' ' + tokStems[i]
        i += 1
    posTarget = posTarget.strip()

    return posTarget

def getClassificationInput(entities, tags, text):
    name = entities[0] + ' ' 
    order = ''
    for i in range(1, len(entities)):
        if tags[i] == 'I-PERSON':
            name += entities[i] + ' '
        else:
            break
    name = name.strip()

    position = text.find(name)

    if position != -1:  # If the specific sentence is found
        # Slice the string up to the position of the specific sentence
        order = text[:position + len(name)].strip()
        
    order = order.replace(name, '').strip()

    return name , order


if __name__ == '__main__':
    text = 'ابدأ الاتصال بمجدي حسن'
    tokStems , stemsTag = POS(text)
    print('tokStems: ')
    print(tokStems)
    print('\n')
    print('stemsTags: ')
    print(stemsTag)

    NERInput = getNERInput(tokStems, stemsTag)
    print('NERInput: ' + NERInput)

    entities, tags = NER(NERInput)
    print('entities: ')
    print(entities)
    print('\n')
    print('tags: ')
    print(tags)
    print('\n')

    if len(entities) > 0:
        name, order = getClassificationInput(entities, tags, NERInput)
    
    else:
        name = ''
        order = NERInput
    command = classify(order)

    print('name: ' + name)
    print('order: ' + order)
    print('command: ' + command)

