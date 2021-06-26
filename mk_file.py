import os
path_w = './py_icre/user.ics'
f = open(path_w, 'w')

print("============================================= \n")
print("ICS FILE　自動生成ツール\n")
print("\n")
print("Create day:2021/06/21  NAME: Baramatsu\n")
print("=============================================\n")


input("Enterにて操作してください")
input("入力を開始します。")
input_year = input('イベント開始年を入力してください:')
input_month = input('次に、開催する月を入力してください:')
input_date = input('次に、日付を入力してください:')
input_time = input('次に、開始時間(h)を入力してください:')
input_mimutes = input('最後に、開始時刻(m)を入力してください:')
input_begindata = input_year+input_month+input_date+'T'+input_time+input_mimutes+'00'
dtstart_str = 'DTSTART:'+input_begindata +'\n'
dtstamp_str = 'DTSTAMP:'+input_begindata +'\n'
dtstart_tzid = 'DTSTART;TZID=Asia/Tokyo:'+input_begindata +'\n'
print("出力は右のようにされました --> " + input_begindata)

input("続いて、終了時刻の入力を開始します。")
output_year = input('イベント終了年を入力してください:')
output_month = input('次に、終了する月を入力してください:')
output_date = input('次に、終了する日付を入力してください:')
output_time = input('次に、終了時間(h)を入力してください:')
output_mimutes = input('最後に、終了時刻(m)を入力してください')
input_finishdata=output_year+output_month+output_date+'T'+output_time+output_mimutes+'00'
dtend_tzid ='DTEND;TZID=Asia/Tokyo:'+input_finishdata + '\n'
print("出力は右のようにされました --> " + input_finishdata)
input_sammary = input("SAMMARY:")
enter_sammary = 'SUMMARY:' + input_sammary +'\n'
input_description = input("DISCRIPTION:")
enter_description = 'DESCRIPTION:' + input_description + '\n'
input ("それでは、入力を開始します。Enterを押してください。")


with open(path_w, mode='a') as f:
    f.write('BEGIN:VCALENDAR\n')
    print("BEGIN:VCALENDAR is written")
    f.write('VERSION:2.0\n')
    print("VERSION:2.0 is written")
    f.write('CALSCALE:GREGORIAN\n')
    f.write('BEGIN:VTIMEZONE\n')
    f.write('TZID:Asia/Tokyo\n')
    f.write('X-LIC-LOCATION:Asia/Tokyo\n')
    f.write('BEGIN:STANDARD\n')
    f.write('TZOFFSETFROM:+0900\n')
    f.write('TZOFFSETTO:+0900\n')
    f.write('TZNAME:JST\n')
    f.write(dtstart_str)
    f.write('END:STANDARD\n')
    f.write('END:VTIMEZONE\n')
    f.write('BEGIN:VEVENT\n')
    f.write(dtstamp_str)
    f.write(dtstart_tzid)
    f.write(dtend_tzid)
    f.write(enter_sammary)
    f.write(enter_description)
    f.write('LOCATION:\n')
    f.write('TRANSP:OPAQUE\n')
    f.write('X-MICROSOFT-CDO-BUSYSTATUS:BUSY\n')
    f.write('BEGIN:VALARM\n')
    f.write('ACTION:DISPLAY\n')
    f.write('DESCRIPTION:hello\n')
    f.write('TRIGGER:-PT15M\n')
    f.write('END:VALARM\n')
    f.write('END:VEVENT\n')
    f.write('END:VCALENDAR\n')
    

f.close()