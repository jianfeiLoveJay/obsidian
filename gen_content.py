# Python script to generate content
text = '''TEST CONTENT
line 2
line 3
'''
path = 'D:\\obsidian_project\\research\\信念传播算法\\论文研读\\temp_insert.txt'
with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print('done')
