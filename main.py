#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-19 15:14
# Modified date : 2019-08-19 16:30
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from chatbot import ZhidaoChatbot

def test_user():
    handler = ZhidaoChatbot()
    while 1:
        question = input('你的问题:').strip()
        answers = handler.qa_main(question)
        print('回答:', answers)

def test_question(question, num=5):
    handler = ZhidaoChatbot()
    print("问题: %s" % question)
    answers = handler.qa_main(question, num)
    print('回答: %s\n' % answers)

def test_text():
    question = "天为什么下雪"
    test_question(question)
    question = "为什么下雪"
    test_question(question)
    question = "中国没有大航海"
    test_question(question)
    question = "为什么是西班牙发现新大陆"
    test_question(question)
    question = "新大陆"
    test_question(question)
    question = "为什么美洲文明消失了?"
    test_question(question)
    question = "草船借箭为什么不用火箭?"
    test_question(question)
    question = "为什么马能吃草?"
    test_question(question, 10)
    question = "为什么人会死?"
    test_question(question, 10)
    question = "为什么会得高血压?"
    test_question(question)
    question = "为什么会得痔疮?"
    test_question(question)
    question = "降准以后会怎样"
    test_question(question)
    question = "投资人投资意愿下降以后会怎样"
    test_question(question)
    question = "为什么要有女朋友"
    test_question(question)

def run():
    test_text()
    test_user()

run()

