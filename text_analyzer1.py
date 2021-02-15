import glob
import datetime
import os

path = os.path


def text_counter():
    try:
        if not path.exists('result'):
            os.mkdir('result')
    except Exception as e:
        print(e)

    try:
        for file in glob.glob('raw_files/*.txt'):
            for i in range(0, len(glob.glob('raw_files/*.txt'))):
                news = [[] for _ in range(len(glob.glob('raw_files/*.txt')))]
                word_count = 0
                dict = {}
                sorted_dict = {}
                filename = path.basename(file)
                print('processing %s' % filename)
                with open(file, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        words = line.split(' ')
                        news[i].append(words)
                        print(news)
                for stuff in news[i]:
                    for st in stuff:
                        try:
                            dict[st] += 1
                        except KeyError as ke:
                            dict[st] = 1
                    word_count += len(stuff)

                sorted_keys = sorted(dict, key=dict.get, reverse=True)

                for w in sorted_keys:
                    sorted_dict[w] = dict[w]
                print('Counted words: %d' % word_count)
                write_down(sorted_dict, word_count, filename)
                print('Successfully written down in: ./result/%s' % filename)
    except Exception as e:
        print(e)


def write_down(dictionary, words_count, file_name):
    file_path = 'result/%s' % str(file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        date = datetime.datetime.now()
        f.write(str(date) + '\n')
        try:
            text = ('Number of words in %s = %d' % (file_name, words_count)) + '\n' + str(dictionary)
            f.write(text)
        except Exception as e:
            print(e)


text_counter()
