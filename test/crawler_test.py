from modules.crawler import *

crawler = Crawler(use_driver=False)
notices = crawler.start_notice()
text = "🐤️로스트아크 점검 공지\n"
text += "═══════════\n"
for notice in notices:
    text += notice + '\n\n'
    text += '\n\n-----------------------\n'

print(text)