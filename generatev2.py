
author_template = '<nobr> <a href="javascript:void(0)">__name__</a></nobr> '

year_teamplate = '''

          <div class="container" style="max-width: 990px; margin-bottom:30px;">
            <p style="margin-left: -25px;">__year__</p>
            <ol>
             __li__
            </ol>
          </div>
'''

li_template = '''
        <li> __title__  __code__ </li>
'''



from yaml import parse


def parse_authors():
    authors = {}
    filename = '论文'
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            
            line = line.strip()
            first_dot_index = line.find('.')
            line = line[first_dot_index+1:]
            
            second_dot_index = line.find('.')
            author_end = second_dot_index
            
            big_boss_index = line.find('Shen')
            if big_boss_index != -1:
                author_end = big_boss_index + 4

            

            line = line[:author_end]
            words = line.split()
            if len(words) < 2:
                continue
            if line.startswith('Code'):
                break
            
            print(words)
            i = 0
            while i < len(words):
                print(i, len(words))
                if 'and' in words[i] :
                    i += 1
                    continue
                first_name = words[i]
                if first_name == 'Heng':
                    i += 3
                    full_name = 'Heng Tao Shen' 
                    authors[full_name] = 1
                    continue
                
                i += 1
                second_name = words[i]
                if not second_name[-1].isalpha():
                    second_name = second_name[:-1]
                full_name = first_name + ' ' + second_name
                print(full_name)
                authors[full_name] = 1
                i += 1

    print(authors)

# parse_authors()
# exit()
authors = {'Junchen Zhu': 1, 'Lianli Gao': 1, 'Jingkuan Song': 1, 'Yuan-Fang Li': 1, 'Feng Zheng': 1, 'Xuelong Li': 1, 'Heng Tao Shen': 1, 'Ye Liu': 1, 'Yaya Cheng': 1, 'Xianglong Liu': 1, 'Qilong Zhang': 1, 'Xinyu Lyu': 1, 'Yuyu Guo': 1, 'Zhou Zhao': 1, 'Hao Huang': 1, 'Hao Ni': 1, 'Xiaopeng Luo': 1, 'Wen Li': 1, 'Xiaosu Zhu': 1, 'Xiaodan Li': 1, 'Yuefeng Chen': 1, 'Yuan He': 1, 'Hui Xue': 1, 'Yu Lei': 1, 'Pengpeng Zeng': 1, 'Meng Wang': 1, 'Haonan Zhang': 1, 'Xuanhan Wang': 1, 'Yixuan Zhou': 1, 'Ji Zhang': 1, 'Hengtao Shen': 1, 'Jingqiu Zhang': 1, 'Xiangpeng Li': 1, 'Bo Wu': 1, 'Chuang Gan': 1, 'Yuxuan Hu': 1, 'Xing Xu': 1, 'Xu Lu': 1, 'Tao He': 1, 'Peng Wang': 1, 'Nicu Sebe': 1, 'Yan Dai': 1, 'Sitong Su': 1, 'Zijie Huang': 1, 'Yang yang': 1, 'Jie Shao': 1, 'Yazhou Yao': 1, 'Shuaiqi Jing': 1, 'Lei Zhao': 1, 'Daiyuan Chen': 1, 'Xinyu Lu': 1, 'Lianli gao': 1, 'Tangming Chen': 1, 'Sen Yang': 1, 'Yuanfeng Song': 1, 'Liyang Zhang': 1, 'Shuaicheng Liu': 1, 'Donghao Liu': 1, 'Tao Li': 1, 'Yiyue Zhang': 1, 'Fuhao Zou': 1, 'Junyu Lai': 1, 'Alan Hanjalic': 1, 'Dongxiang Zhang': 1, 'Kaixuan Fan': 1, 'Tao Mei': 1, 'Wenbing Huang': 1, 'Xiangnan He': 1, 'Wu Liu': 1, 'Liangfu Cao': 1, 'Xin-Shun Xu': 1, 'Zhao Guo': 1, 'Hanwang Zhang': 1, 'Jingdong Wang': 1, 'Ting Zhang': 1, 'jingkuan song': 1}




def write_files(html_code, li_html_codes, f):
    li_html_cdoe = '\n'.join(li_html_codes)
    html_code = html_code.replace('__li__', li_html_cdoe)
    f.write(html_code)

#读取论文这而文件
def main_generate():
    ret_file = open('ret.html', 'w', encoding='utf-8')
    filename = '论文'
    html_code = ''
    li_html_codes = []

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i]
            # line = line.replace("\"", '')
            # line = line.replace("“", '')
            # line = line.replace("*", '')
            # line = line.replace("”", '')
            # line = line.replace("Trans.", 'Trans')
            # line = line.replace("MM,", 'MM')
            # line = line.replace("IJCAI,", 'IJCAI')
            # line = line.replace("AAAI,", 'AAAI')
            # line = line.replace("PR,", 'PR')
            # line = line.replace("TPAMI,", 'TPAMI')
            # line = line.replace("Neurocomputing,", 'Neurocomputing')
            
            conf = ['Pattern Recognition'
                , 'TPAMI'
                , 'CVPR'
                , 'TPAMI'
                , 'ICLR'
                , 'TIP'
                , 'TCSVT'
                , 'ICCV'
                , 'AAAI'
                , 'IJCAI'
                , 'Neurocomputing'
                , 'TNNLS'
                , 'IJCV'
                , 'IJCAI'
                , 'PR'
                , 'IJCAI'
                , 'IJCAI'
                , 'TMM'
                , 'TMM'
                , 'ECCV'
                , 'TMM'
                , 'TMM'
                , 'TMM'
                , 'TMM'
                , 'ACM MM'
            ]
            for c in conf:
                if c in line:
                    line = line.replace(c, '<strong>' + c + '</strong>')
                    break



            if line.startswith('20'):    
                write_files(html_code, li_html_codes, ret_file)
                li_html_codes = []
                html_code = year_teamplate
                html_code = html_code.replace('__year__', line.strip())
                # if '2019' in line:
                #     break
                print('start parse year: ' + line)
                continue

            # 解析论文内容
            line = line.strip()
            if len(line) == 0 or line.startswith('Code'):
                continue


            first_dot_index = line.find('.')
            ord = int(line[:first_dot_index])
            print('ord', ord)
            # 去掉序号
            line = line[first_dot_index+1:].strip()
            print(line)

            if i+1<len(lines):
                next_line = lines[i+1].strip()
                code_href = ''
                if 'Code' in next_line:
                    code_href = next_line[next_line.find('http'):]
                    print('code_href', code_href)



        
            li_html_code = li_template
            
            # li_html_code = li_html_code.replace('__author__', author_code)
            li_html_code = li_html_code.replace('__title__', line)
            if code_href is not None:
                li_html_code = li_html_code.replace('__code__', '[<a href="{code_href}">code</a>]')
            else:
                li_html_code = li_html_code.replace('__code__', code_href)
    
        
            li_html_codes.append(li_html_code)

        #     print('*'*10)
        write_files(html_code, li_html_codes, ret_file)
main_generate()