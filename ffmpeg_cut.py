'''

用ffmpeg切割视频
先将ffmpeg程序路径添加到系统环境变量

'''

import os
import time
import datetime

# 主程序，切割视频
def cut(start_time, lasting_time, origin_filename, out_filename):
    count_start_time = time.time()
    cmdline = 'ffmpeg -ss ' + start_time + ' -i '+ origin_filename + ' -c copy -t '+ lasting_time + ' ' + out_filename
    os.system(cmdline)
    count_end_time = time.time()
    cost_time = count_end_time - count_start_time
    print('Done! \nSpend time: %d seconds.' % cost_time)

# 获取要分割视频文件的列表
def get_origin_filename():
    file = []
    file_path = os.getcwd()
    for filenames in os.walk(file_path):
            file.append(filenames)
    filename = file[0]
    filename = filename[2]
    return filename

# 选择文件
def choose_a_file(filename):
    for i in range(0,len(filename)):
        print(str(i) + '.' + ' '+ filename[i])
    chosen_num = input('choose a file: ')
    try:
        chosen_file = filename[int(chosen_num)]   
    except:
        chosen_file = ''
    return chosen_file

# 文件名预处理，将文件名含有的空格替换为下划线
def replace_filename_spaces():
    file = []
    file_path= os.getcwd()
    for filenames in os.walk(file_path):
            file.append(filenames)
    filename = file[0]
    filename = filename[2]
    for files in filename:
        print('replacing spaces(in file names) into underline...')
        os.rename(files, files.replace(' ','_'))
    print('done!')

# 将时间字符串转化为秒数
def t2s(t):
    h,m,s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

replace_filename_spaces()
fn = get_origin_filename()
origin_filename = choose_a_file(fn)

start_time = input('input start time: ')
end_time = input('input end time: ')
start_time_s = t2s(start_time)
end_time_s = t2s(end_time)
deltatime = end_time_s - start_time_s
lasting_time = str(datetime.timedelta(seconds=deltatime))

out_filename0 = input('input out_filename(without extension): ')
origin_filename_split = origin_filename.split('.')
out_filename1 = origin_filename_split[len(origin_filename_split)-1]
out_filename = out_filename0 + '.' + out_filename1

cut(start_time, lasting_time, origin_filename, out_filename)
