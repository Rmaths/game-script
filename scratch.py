fh = open('Timestamp.txt','w+')
title = input('Enter the channel name with date: ')
fh.write('<html> \n\n<head> \n\n<title> ' + title + '</title> \n\n</head>')
fh.write('<body> \n\n <h1>Time stamps</h1>\n')
yt_link = input('Copy & paste the link of the stream: ')
time = 0
while time != 'end':
    if time == 'end':
        print('Thank you....')
    else:
        time = int(input('enter timestamp in seconds: '))
        # time1 = int(input('Enter time in seconds'))
        sec = time % 60
        time = int(time / 60)
        mint = time % 60
        hr = int(time / 60)
        clickable_time_stamp = str(hr) + ':' + str(mint) + ':' + str(sec)
        label = input('Enter the label for it: ')
        fh.write('<a href=\"'+yt_link+'?t='+str(time)+'s\">'+clickable_time_stamp+'</a> '+label+'\n')
fh.close()
