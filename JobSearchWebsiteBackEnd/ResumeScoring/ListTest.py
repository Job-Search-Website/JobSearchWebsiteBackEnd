import Matcher

class ListTester:
    def __init__(self, text):
        self.Score = 0
        GraduateDiploma = ['研究生', '硕士生', '博士生']
        diploma211 = ['中国农业大学', '东华大学', '西南财经大学', '苏州大学', '华南师范大学', '四川大学', '北京航空航天大学', '中国药科大学', '浙江大学',
                      '西安交通大学', '西北大学', '中南大学', '北京化工大学', '华东理工大学', '华北电力大学', '东北农业大学', '北京中医药大学',
                      '太原理工大学', '北京体育大学', '宁夏大学', '第四军医大学', '延边大学', '东北林业大学', '江南大学', '北京交通大学 ', '内蒙古大学',
                      '中央财经大学', '东南大学', '大连理工大学', '西南交通大学', '河北工业大学', '四川农业大学', '清华大学', '上海财经大学',
                      '中国地质大学', '武汉大学', '南京师范大学', '云南大学', '国防科学技术大学', '郑州大学', '北京大学', '第二军医大学',
                      '西北农林科技大学', '南开大学', '北京林业大学', '华中师范大学', '中央民族大学', '天津医科大学', '上海大学', '电子科技大学',
                      '山东大学', '武汉理工大学', '西南大学', '南昌大学', '新疆大学', '哈尔滨工程大学', '陕西师范大学', '吉林大学', '南京大学',
                      '南京理工大学', '中国政法大学', '重庆大学', '西安电子科技大学', '北京外国语大学', '华中科技大学', '北京工业大学', '中国人民大学',
                      '湖南大学', '贵州大学', '中国科学技术大学', '长安大学', '天津大学', '上海交通大学', '中山大学', '中国石油大学', '河海大学',
                      '上海外国语大学', '暨南大学', '华南理工大学', '辽宁大学', '中国传媒大学', '大连海事大学', '青海大学', '北京理工大学', '中南财经政法大学',
                      '东北大学', '复旦大学', '西藏大学', '东北师范大学', '广西大学', '石河子大学', '同济大学', '南京农业大学  ', '北京邮电大学',
                      '哈尔滨工业大学', '中国海洋大学', '兰州大学', '海南大学', '华中农业大学', '西北工业大学', '中国矿业大学', '对外经济贸易大学',
                      '中央音乐学院', '福州大学', '安徽大学', '北京科技大学', '华东师范大学', '湖南师范大学', '北京师范大学', '南京航空航天大学',
                      '合肥工业大学', '厦门大学']
        diploma985 = ['北京大学', '中国人民大学', '清华大学', '北京航空航天大学', '北京理工大学', '中国农业大学', '北京师范大学', '中央民族大学', '南开大学',
                      '天津大学', '大连理工大学', '东北大学', '吉林大学', '哈尔滨工业大学', '复旦大学', '同济大学', '上海交通大学', '华东师范大学',
                      '南京大学', '东南大学', '浙江大学', '中国科学技术大学', '厦门大学', '山东大学', '中国海洋大学', '武汉大学', '华中科技大学',
                      '湖南大学', '中南大学', '国防科学技术大学', '中山大学', '华南理工大学', '四川大学', '电子科技大学', '重庆大学', '西安交通大学',
                      '西北工业大学', '西北农林科技大学', '兰州大学']
        diplomaTop = ['北京大学', '清华大学']
        diplomaNormal = True
        matcher = Matcher.Matcher(GraduateDiploma, text)
        if (matcher.getResult()):
            self.Score += 10
            diplomaNormal = False
        matcher = Matcher.Matcher(diploma211, text)
        if (matcher.getResult()):
            self.Score += 10
            diplomaNormal = False
        matcher = Matcher.Matcher(diploma985, text)
        if (matcher.getResult()):
            self.Score += 10
            diplomaNormal = False
        matcher = Matcher.Matcher(diplomaTop, text)
        if (matcher.getResult()):
            self.Score += 10
            diplomaNormal = False
        if (diplomaNormal):
            self.Score -= 10
        top500 = ['沃尔玛', '中国石油化工集团公司', '国家电网公司', '中国石油天然气集团公司', '荷兰皇家壳牌石油公司', '沙特阿美公司', '大众公司',
                  '英国石油公司', '亚马逊', '丰田汽车公司', '埃克森美孚', '苹果公司', 'CVS Health公司', '伯克希尔-哈撒韦公司', '联合健康集团',
                  '麦克森公司', '嘉能可', '中国建筑集团有限公司', '三星电子', '戴姆勒股份公司', '中国平安保险', '美国电话电报公司', '美源伯根公司',
                  '中国工商银行', '道达尔公司', '鸿海精密工业股份有限公司', '托克集团', 'EXOR集团', 'Alphabet公司', '中国建设银行',
                  '福特汽车公司', '信诺', '开市客', '安盛', '中国农业银行', '雪佛龙', '嘉德诺', '摩根大通公司', '本田汽车', '通用汽车公司',
                  '沃博联', '三菱商事株式会社', '中国银行', '威瑞森电信', '中国人寿保险', '安联保险集团', '微软', '马拉松原油公司',
                  '华为投资控股有限公司', '中国铁路工程集团有限公司', '克罗格', '上海汽车集团股份有限公司', '房利美', '中国铁道建筑集团有限公司',
                  '俄罗斯天然气工业股份公司', '宝马集团', '卢克石油公司', '美国银行', '家得宝', '日本邮政控股公司', 'Phillips66 公司',
                  '日本电报电话公司', '美国康卡斯特电信公司', '中国海洋石油总公司', '中国移动通信集团公司', '意大利忠利保险公司',
                  '法国农业信贷银行', 'Anthem公司', '美国富国银行', '花旗集团', '瓦莱罗能源公司', '日本伊藤忠商事株式会社', '汇丰银行控股公司',
                  '西门子', '太平洋建设集团', '俄罗斯石油公司', '通用电气公司', '中国交通建设集团有限公司', '中国华润有限公司', '英国保诚集团',
                  '戴尔科技公司', '雀巢公司', '日产汽车', '现代汽车', '英国法通保险公司', '德国电信', '意大利国家电力公司', '英杰华集团',
                  '中国第一汽车集团公司', '中国邮政集团公司', '正威国际集团', '中国五矿集团有限公司', '西班牙国家银行', '软银集团', '博世集团',
                  '信实工业公司', 'SK集团', '家乐福', '法国巴黎银行', '东风汽车公司', '标致', '京东集团', '乐购', '强生', '中国南方电网有限责任公司',
                  '日立', '恒力集团', '国家能源投资集团', '中国中化集团公司', '法国电力公司', '中国宝武钢铁集团', '中国人民保险集团股份有限公司',
                  '埃尼石油公司', '州立农业保险公司', '日本永旺集团', '空中客车公司', '塔吉特公司', '国际商业机器公司', '雷神技术公司',
                  '巴西国家石油公司', '波音', '索尼', '引能仕控股株式会社', '荷兰全球保险集团', '房地美', '中国中信集团有限公司', 'Centene公司',
                  '皇家阿霍德德尔海兹集团', '联合包裹速递服务公司', '日本生命保险公司', 'Uniper公司', '阿里巴巴集团', '墨西哥石油公司',
                  '北京汽车集团', '慕尼黑再保险集团', '中粮集团有限公司', '美国劳氏公司', '英特尔公司', '苏黎世保险集团', '泰国国家石油有限公司',
                  '美国邮政', '德国邮政敦豪集团', '巴斯夫公司', 'Facebook公司', '中国医药集团', '安赛乐米塔尔', '碧桂园控股有限公司',
                  '联邦快递', '大都会人寿', '华特迪士尼公司', '印度石油公司', '中国恒大集团', '松下', '中国兵器工业集团公司',
                  '布鲁克菲尔德资产管理公司', '宝洁公司', '中国电力建设集团有限公司', '中国电信集团公司', 'Engie集团', '百事公司',
                  '三菱日联金融集团', '交通银行', '中国航空工业集团公司', '中国化工集团公司', '第一生命控股有限公司', '哈门那公司', '保德信金融集团',
                  'ADM公司', 'Equinor公司', '英国劳埃德银行集团', '瑞士罗氏公司', '三井物产株式会社', '丸红株式会社', '艾伯森公司', '雷诺',
                  '绿地控股集团有限公司', '丰田通商公司', 'Seven & I 控股公司', '西斯科公司', '迪奥公司', '宏利金融', '洛克希德-马丁',
                  'Alimentation Couche-Tard公司', '惠普公司', '联合利华', '马来西亚国家石油公司', '中国建材集团', '东京电力公司',
                  '招商银行', '印度石油天然气公司', '中国保利集团', '法国兴业银行', '中国太平洋保险', '韩国浦项制铁公司', '万喜集团',
                  '欧尚集团', '腾讯控股有限公司', '日本制铁集团公司', '法国国家人寿保险公司', 'Energy Transfer公司', '西班牙电话公司', '高盛',
                  '摩根士丹利', '卡特彼勒', '百威英博', '广州汽车工业集团', 'LG电子', '万科企业股份有限公司', '美洲电信', '物产中大集团',
                  '思科公司', '山东能源集团有限公司', '巴西JBS公司', '拜耳集团', '辉瑞制药有限公司', '伊塔乌联合银行控股公司', '中国铝业公司',
                  '河钢集团', 'HCA 医疗保健公司', '上海浦东发展银行', '印度国家银行', '兴业银行', '加拿大皇家银行', '联想集团', '诺华公司',
                  '东京海上日动火灾保险公司', '韩国电力公司', '沃达丰集团', '起亚汽车', '德国大陆集团', '美国国际集团', '德国联邦铁路公司',
                  '瑞士再保险股份有限公司', '厦门建发集团有限公司', '招商局集团', '日本出光兴产株式会社', '日本三井住友金融集团', '住友商事',
                  '中国民生银行', '俄罗斯联邦储蓄银行', '日本KDDI电信公司', '法国BPCE银行集团', '浙江吉利控股集团', '圣戈班集团', '雷普索尔公司',
                  'MS&AD保险集团控股有限公司', '电装公司', '蒂森克虏伯', 'Orange公司', '友邦保险集团', '', '美国运通公司', '达美航空',
                  '中国光大集团', '西班牙对外银行', '意昂集团', '默沙东', '美国航空集团', '特许通讯公司', '沃尔沃集团', '伍尔沃斯集团',
                  '必和必拓集团', 'Finatis公司', '好事达', '中国远洋海运集团有限公司', '陕西延长石油', '中国华能集团公司', '多伦多道明银行',
                  '巴西布拉德斯科银行', '和硕', '美国纽约人寿保险公司', 'Talanx公司', '美国全国保险公司', '陕西煤业化工集团', '西班牙ACS集团',
                  '百思买', '联合航空控股公司', '韩华集团', '美国利宝互助保险集团', '埃森哲', '力拓集团', '中国机械工业集团有限公司', '英国葛兰素史克公司',
                  '陶氏公司', '厦门国贸控股集团有限公司', '丰益国际', '法国布伊格集团', '泰森食品', '巴西银行', '赛诺菲', '中国联合网络通信股份有限公司',
                  '德意志银行', 'TJX公司', '瑞银集团', '麦德龙', '兖矿集团', '雪松控股集团', '邦吉公司', '象屿集团', 'M&G公司',
                  '三菱电机股份有限公司', '怡和集团', '采埃孚', 'Iberdrola公司', '汉莎集团', '中国航空油料集团公司', '美国教师退休基金会',
                  '美的集团股份有限公司', '山东魏桥创业集团', '巴拉特石油公司', '意大利联合圣保罗银行', '大和房建', '德国艾德卡公司', '费森尤斯集团',
                  '甲骨文公司', '麦格纳国际', '国家电力投资集团公司', '通用动力', '法国国营铁路集团', '迪尔公司', '马士基集团', '德国中央合作银行',
                  '耐克公司', '前进保险公司', '苏宁易购集团', '大众超级市场公司', '巴西联邦储蓄银行', '巴克莱', '长江和记实业有限公司',
                  '青山控股集团', '乔治威斯顿公司', 'Enbridge公司', '中国航天科工集团公司', '巴西淡水河谷公司', '日本明治安田生命保险公司',
                  '可口可乐公司', '万通互惠理财公司', '印度塔塔汽车公司', '菲尼克斯集团控股公司', '日本三菱重工业股份有限公司', '瑞士ABB集团',
                  'Tech Data公司', '荷兰国际集团', '江西铜业集团公司', '森宝利公司', '全球燃料服务公司', '加拿大鲍尔集团', '霍尼韦尔国际公司',
                  '康菲石油公司', '日本瑞穗金融集团', '意大利邮政集团', '江苏沙钢集团', '中国航天科技集团公司', '中国能源建设集团', '阳光龙净集团有限公司',
                  '联合服务汽车协会', '富士通', '瑞士信贷', '加拿大丰业银行', '爱信精机', '利安德巴塞尔工业公司', '中国中车集团', '台积公司',
                  '损保控股有限公司', 'Exelon公司', '日本钢铁工程控股公司', '安达保险公司', '安徽海螺集团', '美国诺斯洛普格拉曼公司', '金川集团',
                  '中国华电集团公司', '路易达孚集团', '第一资本金融公司', 'Plains GP Holdings公司', '国泰金融控股股份有限公司', '欧莱雅', '三菱化学控股',
                  '广达电脑公司', '艾伯维', '英美烟草集团', '佳能', '中国电子科技集团公司', '斯伦贝谢公司', 'StoneX集团',
                  'Enterprise Products Partners公司', '现代摩比斯公司', '中国电子信息产业集团有限公司', '普利司通', '西北互助人寿保险公司',
                  '3M公司', '铃木汽车', '住友生命保险公司', '中国太平保险集团有限责任公司', '雅培公司', 'CHS公司', '康帕斯集团', '仁宝电脑',
                  'CRH公司', 'Inditex公司', 'Travelers公司', '马自达汽车株式会社', '鞍钢集团公司', '东芝', '富邦金融控股股份有限公司', 'SAP公司',
                  '斯巴鲁公司', '冀中能源集团', 'Coles集团', '美敦力公司', '台湾中油股份有限公司', '菲尼克斯医药公司', '法国航空-荷兰皇家航空集团',
                  '法国威立雅环境集团', '施耐德电气', '武田药品公司', '法国达飞海运集团', '澳洲联邦银行', 'Medipal控股公司', '加拿大永明金融集团',
                  '英美资源集团', 'CFE公司', '菲利普-莫里斯国际公司', '小米集团', '上海建工集团股份有限公司', '泰康保险集团', 'Coop集团',
                  'KB金融集团', '森科能源公司', '关西电力', '首钢集团', '蒙特利尔银行', '慧与公司', '英国电信集团', '法国邮政',
                  '中国兵器装备集团公司', '海尔智家股份有限公司', '珠海格力电器股份有限公司', 'CJ集团', '波兰国营石油公司', '江森自控国际公司',
                  '英国森特理克集团', '艾睿电子', '深圳市投资控股有限公司', '新疆广汇实业投资', '林德集团', '住友电工', '国际航空集团',
                  'GS加德士', 'Migros集团', '华夏保险公司', '日本电气公司', '赛峰集团', '纬创集团', '达能', '日本中部电力',
                  '盛虹控股集团有限公司', '铜陵有色金属集团', '维亚康姆CBS公司', "Financière de l'Odet公司", '山东钢铁集团有限公司',
                  'Dollar General公司', 'Achmea公司', 'Rajesh Exports公司', '大同煤矿集团有限责任公司', '曼福集团', '中国大唐集团公司',
                  '美国合众银行', '三星人寿保险', '海亮集团有限公司', '联合信贷集团', '东日本旅客铁道株式会社', 'KOC集团', '米其林公司',
                  '上海医药集团股份有限公司', '喜力控股公司', 'X5 零售集团', '拉法基豪瑞集团', '中国通用技术', '星巴克公司', '任仕达公司',
                  '阿迪达斯集团', '三星C&T公司', 'Fomento Económico Mexicano公司', '奥地利石油天然气集团', '德科集团', '山西焦煤集团有限责任公司',
                  '河南能源化工集团', '百时美施贵宝公司', '诺基亚', '潞安集团', '广西投资集团有限公司', '西太平洋银行', '西班牙能源集团',
                  '中国核工业集团有限公司', 'US Foods Holding公司', '亿滋国际', '中国中煤能源集团有限公司', '帕卡公司', '赛默飞世尔科技公司',
                  '山西阳泉煤业', '山西晋城无烟煤矿业集团']
        topEng = ['walmart', 'sinopec group', 'state grid', 'china national petroleum', 'royal dutch shell',
                  'saudi aramco',
                  'volkswagen', 'bp', 'amazon.com', 'toyota motor', 'exxon mobil', 'apple', 'cvs health',
                  'berkshire hathaway',
                  'unitedhealth group', 'mckesson', 'glencore', 'china state construction engineering',
                  'samsung electronics',
                  'daimler', '集团', 'at&t', 'amerisourcebergen', 'industrial & commercial bank of china', 'total',
                  'hon hai precision industry', 'trafigura group', 'exor group', 'alphabet', 'china construction bank',
                  'ford motor', 'cigna', 'costco wholesale', 'axa', 'agricultural bank of china', 'chevron',
                  'cardinal health',
                  'jpmorgan chase', 'honda motor', 'general motors', 'walgreens boots alliance', 'mitsubishi',
                  'bank of china',
                  'verizon communications', '集团', 'allianz', 'microsoft', 'marathon petroleum',
                  'huawei investment & holding',
                  'china railway engineering group', 'kroger', 'saic motor', 'fannie mae', 'china railway construction',
                  'gazprom', 'bmw group', 'lukoil', 'bank of america', 'home depot', 'japan post holdings',
                  'phillips 66',
                  'nippon telegraph and telephone', 'comcast', 'china national offshore oil',
                  'china mobile communications',
                  'assicurazioni generali', 'crédit agricole', 'anthem', 'wells fargo', 'citigroup', 'valero energy',
                  'itochu', 'hsbc holdings', 'siemens', 'pacific construction group', 'rosneft oil', 'general electric',
                  'china communications construction', 'china resources', 'prudential', 'dell technologies', 'nestlé',
                  'nissan motor', 'hyundai motor', 'legal & general group', 'deutsche telekom', 'enel', 'aviva',
                  'china faw group', 'china post group', 'amer international group', 'china minmetals',
                  'banco santander',
                  'softbank group', 'bosch group', 'reliance industries', 'sk holdings', 'carrefour', 'bnp paribas',
                  'dongfeng motor', 'peugeot', 'jd.com', 'tesco', 'johnson & johnson', 'china southern power grid',
                  'hitachi', 'hengli group', 'china energy investment', 'sinochem group', 'electricité de france',
                  'china baowu steel group', "people's insurance co. of china", 'eni', 'state farm insurance', 'aeon',
                  'airbus', 'target', 'international business machines', 'raytheon technologies', 'petrobras', 'boeing',
                  'sony', 'eneos holdings', 'aegon', 'freddie mac', 'citic group', 'centene', 'royal ahold delhaize',
                  'united parcel service', 'nippon life insurance', 'uniper', 'alibaba group holding', 'pemex',
                  'beijing automotive group', 'munich re group', 'cofco', "lowe's", 'intel', 'zurich insurance group',
                  'ptt', 'u.s. postal service', 'deutsche post dhl group', 'basf', 'facebook', 'sinopharm',
                  'arcelormittal',
                  'country garden holdings', 'fedex', 'metlife', 'walt disney', 'indian oil', 'china evergrande group',
                  'panasonic', 'china north industries group', 'brookfield asset management', 'procter & gamble',
                  'powerchina',
                  'china telecommunications', 'engie', 'pepsico', 'mitsubishi ufj financial group',
                  'bank of communications',
                  'aviation industry corp. of china', 'chemchina', 'dai-ichi life holdings', 'humana',
                  'prudential financial',
                  'archer daniels midland', 'equinor', 'lloyds banking group', 'roche group', 'mitsui', 'marubeni',
                  'albertsons', 'renault', 'greenland holding group', 'toyota tsusho', 'seven & i holdings', 'sysco',
                  'christian dior', 'manulife financial', 'lockheed martin', 'alimentation couche-tard', 'hp',
                  'unilever',
                  'petronas', 'china national building material group', 'tokyo electric power', 'china merchants bank',
                  'oil & natural gas', 'china poly group', 'société générale', '集团', 'posco', 'vinci', 'auchan holding',
                  'tencent holdings', 'nippon steel corporation', 'cnp assurances', 'energy transfer', 'telefónica',
                  'goldman sachs group', 'morgan stanley', 'caterpillar', 'anheuser-busch inbev',
                  'guangzhou automobile industry group', 'lg electronics', 'china vanke', 'américa móvil',
                  'wuchan zhongda group',
                  'cisco systems', 'shandong energy group', 'jbs', 'bayer', 'pfizer', 'itaú unibanco holding',
                  'aluminum corp. of china', 'hbis group', 'hca healthcare', 'shanghai pudong development bank',
                  'state bank of india', 'industrial bank', 'royal bank of canada', 'lenovo group', 'novartis',
                  'tokio marine holdings', 'korea electric power', 'vodafone group', 'kia motors', 'continental',
                  'american international group', 'deutsche bahn', 'swiss re', 'xiamen c&d', 'china merchants group',
                  'idemitsu kosan', 'sumitomo mitsui financial group', 'sumitomo', 'china minsheng banking', 'sberbank',
                  'kddi', 'groupe bpce', 'zhejiang geely holding group', 'saint-gobain', 'repsol',
                  'ms&ad insurance group holdings',
                  'denso', 'thyssenkrupp', 'orange', 'aia group', '', 'american express',
                  'delta air lines', 'china everbright group', 'banco bilbao vizcaya argentaria', 'e.on', 'merck',
                  'american airlines group', 'charter communications', 'volvo', 'woolworths group', 'bhp group',
                  'finatis',
                  'allstate', 'china cosco shipping', '集团', 'china huaneng group', 'toronto-dominion bank',
                  'banco bradesco',
                  'pegatron', 'new york life insurance', 'talanx', 'nationwide', 'shaanxi coal & chemical industry',
                  'acs',
                  'best buy', 'united airlines holdings', 'hanwha', 'liberty mutual insurance group', 'accenture',
                  'rio tinto group', 'sinomach', 'glaxosmithkline', 'dow', 'xiamen itg holding group',
                  'wilmar international',
                  'bouygues', 'tyson foods', 'banco do brasil', 'sanofi', 'china united network communications',
                  'deutsche bank',
                  'tjx', 'ubs group', 'metro', 'yankuang group', 'cedar holdings group', 'bunge', 'xmxyg', 'm&g',
                  'mitsubishi electric', 'jardine matheson', 'zf friedrichshafen', 'iberdrola', 'lufthansa group',
                  'china national aviation fuel group', 'tiaa', 'midea group', 'shandong weiqiao pioneering group',
                  'bharat petroleum', 'intesa sanpaolo', 'daiwa house industry', 'edeka zentrale', 'fresenius',
                  'oracle',
                  'magna international', 'state power investment', 'general dynamics', 'sncf group', 'deere',
                  'maersk group',
                  'dz bank', 'nike', 'progressive', 'suning.com group', 'publix super markets',
                  'caixa econ?mica federal',
                  'barclays', 'ck hutchison holdings', 'tsingshan holding group', 'george weston', 'enbridge',
                  'china aerospace science & industry', 'vale', 'meiji yasuda life insurance', 'coca-cola',
                  'massachusetts mutual life insurance', 'tata motors', 'phoenix group holdings',
                  'mitsubishi heavy industries',
                  'abb', 'tech data', 'ing group', 'jiangxi copper', 'j. sainsbury', 'world fuel services',
                  'power corp. of canada', 'honeywell international', 'conocophillips', 'mizuho financial group',
                  'poste italiane', 'jiangsu shagang group', 'china aerospace science & technology',
                  'china energy engineering group', 'yango longking group', 'united services automobile assn.',
                  'fujitsu', 'credit suisse group', 'bank of nova scotia', 'aisin seiki',
                  'lyondellbasell industries', 'crrc group', 'taiwan semiconductor manufacturing',
                  'sompo holdings', 'exelon', 'jfe holdings', 'chubb', 'anhui conch group', 'northrop grumman',
                  'jinchuan group', 'china huadian', 'louis dreyfus', 'capital one financial', 'plains gp holdings',
                  'cathay financial holding', "l'oréal", 'mitsubishi chemical holdings', 'quanta computer', 'abbvie',
                  'british american tobacco', 'canon', 'china electronics technology group', 'schlumberger',
                  'stonex group',
                  'enterprise products partners', 'hyundai mobis', 'china electronics', 'bridgestone',
                  'northwestern mutual',
                  '3m', 'suzuki motor', 'sumitomo life insurance', 'china taiping insurance group',
                  'abbott laboratories',
                  'chs', 'compass group', 'compal electronics', 'crh', 'inditex', 'travelers', 'mazda motor',
                  'ansteel group', 'toshiba', 'fubon financial holding', 'sap', 'subaru', 'jizhong energy group',
                  'coles group', 'medtronic', 'cpc', 'phoenix pharma', 'air france-klm group', 'veolia environnement',
                  'schneider electric', 'takeda pharmaceutical', 'cma cgm', 'commonwealth bank of australia',
                  'medipal holdings', 'sun life financial', 'anglo american', 'cfe', 'philip morris international',
                  'xiaomi', 'shanghai construction group', 'taikang insurance group', 'coop group',
                  'kb financial group',
                  'suncor energy', 'kansai electric power', 'shougang group', 'bank of montreal',
                  'hewlett packard enterprise',
                  'bt group', 'la poste', 'china south industries group', 'haier smart home',
                  'gree electric appliances',
                  'cj corp.', 'pkn orlen group', 'johnson controls international', 'centrica', 'arrow electronics',
                  'shenzhen investment holdings', '集团', 'linde', 'sumitomo electric industries',
                  'international airlines group',
                  'gs caltex', 'migros group', 'huaxia life insurance', 'nec', 'safran', 'wistron', 'danone',
                  'chubu electric power', 'shenghong holding group', 'tongling nonferrous metals group', 'viacomcbs',
                  "financière de l'odet", 'shandong iron & steel group', 'dollar general', 'achmea', 'rajesh exports',
                  'datong coal mine group', 'mapfre group', 'china datang', 'u.s. bancorp', 'samsung life insurance',
                  'hailiang group', 'unicredit group', 'east japan railway', 'ko? holding', 'michelin',
                  'shanghai pharmaceuticals holding', 'heineken holding', 'x5 retail group', 'lafargeholcim',
                  'starbucks', 'randstad', 'adidas', 'samsung c&t', 'fomento económico mexicano', 'omv group',
                  'adecco group', 'shanxi coking coal group', 'henan energy & chemical', 'bristol-myers squibb',
                  'nokia', 'shanxi luan mining group', 'guangxi investment group', 'westpac banking',
                  'naturgy energy group',
                  'china national nuclear', 'us foods holding', 'mondelez international', 'china national coal group',
                  'paccar', 'thermo fisher scientific', '集团', 'shanxi jincheng anthracite coal mining group']
        experienceNormal = False
        matcher = Matcher.Matcher(top500, text)
        if matcher.getResult():
            self.Score += 10
            experienceNormal = False
        if experienceNormal:
            matcher = Matcher.Matcher(topEng, text)
            if matcher.getResult():
                self.Score += 10
                experienceNormal = False
        sex = ['女', '未婚', '未孕', '生子意愿']
        matcher = Matcher.Matcher(sex, text)
        self.Score -= matcher.getNum() * 10

    def getListTest(self):
        return self.Score
