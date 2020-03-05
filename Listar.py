import glob

def write_locations(folder, textFile):
    print('')
    file = open(textFile, 'w')
    for contents in glob.glob('{}/*'.format(folder)):
        try:
            fileName = contents.split("\\")[-1]
            file.write('\n./{0}/{1}'.format(folder, fileName))
            print('./{0}/{1}'.format(folder, fileName))
        except:
            pass

write_locations('Positive', 'positives.txt')
write_locations('Negative', 'negatives.txt')

print(" Arquivo Criado ")





