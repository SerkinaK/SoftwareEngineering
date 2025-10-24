with open('Lab7.txt', 'a+', encoding='utf-8') as f:
    f.write( '\nСтрока стихотворного текста, организованная по определённому ритмическому образцу')

with open(r'Lab7.txt', encoding='utf-8') as f:
    result = f.readlines()
    print(result)