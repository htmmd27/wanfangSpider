# coding: utf-8

import csv
import os


def save_as_csv(result):
    """
    :param result:当前页列表
    :return: 无返回，直接将结果存到文件中
    """
    for i in result:
        # if not os.path.exists('./paperDetailed/{}.csv'.format(i[0])):
        #     os.mkdir('./paperDetailed/{}.csv'.format(i[0]))
        csvfile = open('./paperDetailed1/{}.csv'.format(i[0]), 'a', newline="", encoding='utf-8')
        writer = csv.writer(csvfile)
        writer.writerow(i)
        csvfile.close()


def getPeriodicalFromCSV(field):
    """
    :param: field: 领域名称，对应文件夹中六个csv文件
    :return: 返回期刊列表
    """
    csvfile = open('./periodicalName/{}.csv'.format(field), 'r', encoding='utf-8')
    reader = csv.reader(csvfile)

    periodical_list = []
    for row in reader:
        periodical_list.append(row[0])
    csvfile.close()
    return periodical_list
