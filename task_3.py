a = int(input())
if a // 4 == 0 or a // 100 == 0 or a % 400 == 0:
    print('Год високостный')
else:
    print('Год уже был високостный')
