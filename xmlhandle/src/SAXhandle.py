#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import xml.sax

os.chdir("file/")
way = os.getcwd()
print(way)


class MovieHandler(xml.sax.ContentHandler):
  def __init__(self):
    self.CurrentData = ""
    self.type = ""
    self.format = ""
    self.year = ""
    self.rating = ""
    self.stars = ""
    self.description = ""

  # 元素开始事件处理
  # 遇到XML开始标签时调用，tag是标签的名字，attributes是标签的属性值字典。
  def startElement(self, tag, attributes):
    self.CurrentData = tag
    if tag == "movie":
      print("*****Movie*****")
      title = attributes["title"]
      print("Title:", title)

  # 元素结束事件处理
  # 遇到XML结束标签时调用。
  def endElement(self, tag):
    self.CurrentData = ""
    # if self.CurrentData == "type":
    #   print("Type:", self.type)
    # elif self.CurrentData == "format":
    #   print("Format:", self.format)
    # elif self.CurrentData == "year":
    #   print("Year:", self.year)
    # elif self.CurrentData == "rating":
    #   print("Rating:", self.rating)
    # elif self.CurrentData == "stars":
    #   print("Stars:", self.stars)
    # elif self.CurrentData == "description":
    #   print("Description:", self.description)
    # self.CurrentData = ""

  # 内容事件处理
  # 调用时机：
  # 从行开始，遇到标签之前，存在字符，content的值为这些字符串。
  # 从一个标签，遇到下一个标签之前， 存在字符，content的值为这些字符串。
  # 从一个标签，遇到行结束符之前，存在字符，content的值为这些字符串。
  # 标签可以是开始标签，也可以是结束标签。
  def characters(self, content):
    if self.CurrentData == "type":
      self.type = content
    elif self.CurrentData == "format":
      self.format = content
    elif self.CurrentData == "year":
      self.year = content
    elif self.CurrentData == "rating":
      self.rating = content
    elif self.CurrentData == "stars":
      self.stars = content
    elif self.CurrentData == "description":
      self.description = content

if (__name__ == "__main__"):
  # 创建一个 XMLReader
  parser = xml.sax.make_parser()
  # turn off namepsaces
  parser.setFeature(xml.sax.handler.feature_namespaces, 0)

  # 重写 ContextHandler
  Handler = MovieHandler()
  parser.setContentHandler(Handler)

  parser.parse("test.xml")
