
author_template = '<nobr> <a href="javascript:void(0)">__name__</a></nobr> '

year_teamplate = '''
    <div class="row m-0 p-0" style="border-top: 1px solid #ddd; flex-direction: row-reverse;">
            <div class="col-sm-1 mt-2 p-0 pr-1">
              <h3 class="bibliography-year">__year__</h3>
            </div>
            <div class="col-sm-11 p-0">
              <ol class="bibliography">
                __li__
            </ol>    
            </div>
          </div>
'''

li_template = '''
                <li><div class="row m-0 mt-3 p-0">
                     <div class="col-sm-1 p-0 abbr">
                <a class="badge_self font-weight-bold light-blue darken-1 align-middle" style="width: 65px;" href="javascript:void(0)" >
                    __conf__
                </a>
                <div style="margin: 10px 0;"></div>
                <a class="badge grey waves-effect font-weight-light mr-1" href="__code__" style="width: 65px;__nocode__" target="_blank">Code</a>
                    </div>
          <div class="col-sm-11 mt-2 mt-sm-0 p-0 pl-xs-0 pl-sm-4 pr-xs-0 pr-sm-2">
            
            <div id="bobu2022ICRA" class="col p-0">
              <h5 class="title mb-0">__title__</h5>
              <div class="author">
                    __author__
                        
              </div>
              <div>
                <p class="periodical font-italic">
                    __level__
                </p>
              </div>
            
              <div class="col p-0">
                
                  <a style='display:none' class="badge grey waves-effect font-weight-light mr-1" data-toggle="collapse" href="#bobu__ord__-abstract" role="button" aria-expanded="false" aria-controls="bobu2022ICRA-abstract">Abstract</a>
                
                  <!-- <a class="badge grey waves-effect font-weight-light mr-1" href="/assets/pdf/NVIDIA/bobu2022ICRA.pdf" target="_blank">PDF</a> -->
                  <!-- <a class="badge grey waves-effect font-weight-light mr-1" href="https://github.com/vikki-dai/RSGNet" target="_blank">Code</a> -->
                
              </div>
            
              <div class="col mt-2 p-0">
                <div id="bobu__ord__-abstract" class="collapse">
                  <div class="abstract card card-body font-weight-light mr-0 mr-sm-3 p-3">
                    This is an official pytorch implementation of " RSGNet: Relation based Skeleton Graph Network for Crowded Scenes Pose Estimation". In this work, we are committed to solving the problem of multi-person pose estimation under the condition of “crowded scenes”, where RGB images capture complex real-world scenes with highly-overlapped people, severe occlusions and diverse postures. In particular, we focus on two main problems: 1) how to design an effective pipeline for crowded scenes pose estimation; and 2) how to equip this pipeline with the ability of relation modeling for interference resolving. To tackle these problems, we propose a new pipeline named Relation based Skeleton Graph Network (RSGNet). 
            </div>
                </div>
              </div>
              
            </div>
          </div>
        </div>
        </li>
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
            line = line.replace("\"", '')
            line = line.replace("“", '')
            line = line.replace("*", '')
            line = line.replace("”", '')
            line = line.replace("Trans.", 'Trans')
            line = line.replace("MM,", 'MM')
            line = line.replace("IJCAI,", 'IJCAI')
            line = line.replace("AAAI,", 'AAAI')
            line = line.replace("PR,", 'PR')
            line = line.replace("TPAMI,", 'TPAMI')
            line = line.replace("Neurocomputing,", 'Neurocomputing')
            



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

            # 解析作者
            author_list = []
            while True:
                first_sign_index = line.find(',')
                
                if first_sign_index == -1 or first_sign_index > 20: # 人名字不太可能大于 10
                    first_sign_index = line.find('.')
                maybe_author = line[:first_sign_index]
                print(maybe_author)
                if maybe_author in authors:
                    author_list.append(maybe_author)
                    line = line[first_sign_index+1:].strip()
                else:
                    # if 'erarchical LSTM wi' in line:
                    #     print(maybe_author)
                    #     print('fuck')
                    #     exit()
                    break

            
            print('author_list', author_list)
            # print(line)

            # if 'erarchical LSTM wi' in line:
            #     exit()

            # 解析 JCR
            jcr_index = line.find('JCR')
            JCR_string = ''
            if jcr_index != -1:
                JCR_string = line[jcr_index:jcr_index+5]
                print('JCR_string', JCR_string)
                line = line.replace(JCR_string+'.', '').strip()
                line = line.replace(JCR_string, '').strip()

            # 解析 CCF
            CCF_index = line.find('CCF')
            CCF_string = ''
            if CCF_index != -1:
                CCF_string = line[CCF_index:CCF_index+5]
                print('CCF_string', CCF_string)
                line = line.replace(CCF_string+'.', '').strip()
                line = line.replace(CCF_string, '').strip()

            # 解析会议或者期刊
            if line[-1] == '.':
                line = line[:-1]
            conf_start_index_1 = line.rfind('.')
            conf_start_index_2 = line.rfind(',')
            conf_start_index = max(conf_start_index_1, conf_start_index_2)
            conf_string = line[conf_start_index+1:]
            
            print('conf_string', conf_string)
            line = line.replace(conf_string+'.', '').strip()
            line = line.replace(conf_string, '').strip()
            conf_list = [('ACM MM', 'ACM MM')
                , ('ACM Multimedia', 'ACM MM')
                , ('TNNLS', 'TNNLS')
                , ('TMM', 'TMM')
                , ('TPAMI', 'TPAMI')
                , ('CVPR', 'CVPR')
                , ('IEEE', 'IEEE')
                , ('AAAI', 'AAAI')
                , ('PR', 'PR')
                , ('IJCAI', 'IJCAI')
                , ('Pattern', 'PR')]
            for conf in conf_list:
                if conf[0] in conf_string:
                    conf_string = conf[1]
                    break

            # print(line)




            next_line = lines[i+1].strip()
            code_href = ''
            if 'Code' in next_line:
                code_href = next_line[next_line.find('http'):]
                print('code_href', code_href)


        
            li_html_code = li_template
            
            if len(CCF_string) > 0:
                li_html_code = li_html_code.replace('__level__', CCF_string)
            if len(JCR_string) > 0:
                li_html_code = li_html_code.replace('__level__', JCR_string)
            if len(CCF_string) == 0 and len(JCR_string) == 0:
                li_html_code = li_html_code.replace('__level__', '')
            if len(code_href) > 0:
                li_html_code = li_html_code.replace('__code__', code_href)
            else:
                li_html_code = li_html_code.replace('__nocode__', 'display: none;')
            author_code = ''
            for author in author_list:
                if author == author_list[-1]:
                    author = author + '.'
                else:
                    author = author + ','

                if 'Jingkuan' in author:
                    author = '<b>' + author + '</b>'
                    pass
                author_code += author_template.replace('__name__', author)
            
            li_html_code = li_html_code.replace('__author__', author_code)
            li_html_code = li_html_code.replace('__title__', line)
            li_html_code = li_html_code.replace('__conf__', conf_string)
            li_html_code = li_html_code.replace('__ord__', str(ord))
            # print(html_code)
            # ret_file.write(li_html_code)
            li_html_codes.append(li_html_code)

            print('*'*10)
        write_files(html_code, li_html_codes, ret_file)
main_generate()