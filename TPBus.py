# 延平中學高一6班張詠青
# 自主學習期末報告
# 台北市公車即時資訊
# 練習從 JSON 與 HTML 擷取資料
#   處理資料、合併列印結果

import urllib.request as request
from bs4 import BeautifulSoup
import json
import os

IDMap = {'1' : '10723', '2' : '10262', '5' : '11861', '8' : '16406', '9' : '10882', '12' : '10864', '14' : '10891', '18' : '10726', '20' : '10873', '21' : '10253', '22' : '10832', '26' : '11203', '28' : '15141', '32' : '11066', '33' : '11821', '37' : '11091', '38' : '10862', '39' : '11243', '41' : '11871', '42' : '15142', '46' : '10872', '49' : '11831', '51' : '16467', '52' : '10792', '53' : '10767', '57' : '16468', '62' : '11244', '63' : '10847', '66' : '17944', '68' : '11204', '72' : '15362', '88' : '10971', '99' : '17517', '108' : '10822', '109' : '11813', '111' : '10472', '128' : '15724', '129' : '15726', '201' : '10171', '202' : '15111', '203' : '15314', '204' : '11212', '205' : '10181', '206' : '15372', '207' : '15572', '208' : '15112', '211' : '11232', '212' : '10912', '214' : '15561', '215' : '15322', '218' : '11156', '221' : '10415', '222' : '10842', '223' : '11124', '224' : '15375', '225' : '10443', '226' : '11245', '227' : '15521', '230' : '11151', '231' : '10161', '232' : '10416', '234' : '10132', '235' : '10283', '237' : '10745', '241' : '10173', '242' : '10116', '243' : '10172', '245' : '10162', '246' : '15381', '247' : '15353', '248' : '15181', '249' : '10772', '250' : '15333', '251' : '10712', '252' : '10746', '253' : '10735', '254' : '10783', '255' : '11252', '256' : '15143', '257' : '10942', '260' : '10823', '261' : '10414', '262' : '10961', '264' : '16588', '267' : '15332', '268' : '15352', '270' : '11841', '274' : '10893', '275' : '16581', '276' : '11851', '277' : '10874', '278' : '10752', '279' : '15391', '280' : '15546', '281' : '10856', '282' : '15162', '284' : '11221', '286' : '10845', '288' : '11165', '292' : '11246', '294' : '10747', '295' : '10748', '297' : '11041', '298' : '11023', '299' : '11411', '300' : '15532', '302' : '11125', '303' : '10272', '306' : '10473', '307' : '16111', '308' : '15151', '310' : '16112', '311' : '15563', '505' : '10848', '508' : '10441', '513' : '11421', '520' : '10424', '521' : '15313', '529' : '11161', '530' : '15164', '531' : '10764', '536' : '10263', '539' : '11242', '542' : '10277', '550' : '11123', '551' : '11114', '552' : '11056', '553' : '15356', '556' : '15172', '557' : '17333', '559' : '17805', '568' : '10725', '570' : '16897', '571' : '16898', '572' : '16899', '573' : '16900', '574' : '16901', '575' : '16902', '576' : '18041', '577' : '17672', '578' : '16845', '579' : '16847', '580' : '16849', '581' : '16851', '582' : '16855', '583' : '17513', '585' : '17683', '586' : '16997', '587' : '17001', '589' : '17009', '590' : '17016', '591' : '17017', '592' : '16930', '593' : '16772', '594' : '16767', '595' : '16768', '600' : '15571', '602' : '15735', '604' : '16121', '605' : '15514', '606' : '11815', '611' : '11742', '612' : '11093', '615' : '10471', '616' : '15581', '617' : '10422', '618' : '10221', '620' : '15334', '621' : '11231', '622' : '10423', '624' : '17300', '629' : '5415', '630' : '10861', '631' : '15224', '635' : '10475', '636' : '10474', '637' : '10491', '638' : '10492', '639' : '10511', '640' : '10453', '641' : '10452', '643' : '10328', '644' : '10333', '645' : '10461', '646' : '10765', '647' : '10331', '648' : '10326', '651' : '16122', '652' : '10844', '656' : '10163', '657' : '10164', '658' : '16113', '660' : '15191', '662' : '11241', '663' : '10282', '667' : '16123', '668' : '15515', '669' : '10278', '670' : '10771', '671' : '10736', '672' : '10785', '673' : '10782', '675' : '15512', '676' : '15161', '677' : '15638', '678' : '5416', '679' : '16127', '680' : '16184', '681' : '15359', '682' : '15221', '683' : '15335', '685' : '10811', '688' : '11834', '701' : '10151', '702' : '10148', '704' : '16517', '705' : '10195', '706' : '10196', '707' : '16461', '711' : '15513', '712' : '17945', '756' : '16504', '757' : '16707', '758' : '16706', '760' : '18738', '778' : '17515', '779' : '16511', '780' : '16637', '781' : '16644', '782' : '16643', '783' : '16692', '785' : '16693', '786' : '16694', '787' : '16642', '788' : '16641', '789' : '16739', '790' : '16740', '791' : '16682', '793' : '16689', '796' : '16691', '797' : '16571', '799' : '16576', '800' : '16573', '801' : '16594', '802' : '16608', '803' : '16595', '805' : '17524', '806' : '17523', '807' : '16223', '808' : '16547', '810' : '16670', '811' : '16425', '812' : '16189', '813' : '17526', '815' : '16500', '816' : '16499', '817' : '16731', '818' : '16623', '819' : '16258', '820' : '16584', '821' : '16695', '822' : '16730', '823' : '17525', '824' : '17889', '825' : '16551', '826' : '16554', '827' : '16548', '835' : '16485', '836' : '16269', '837' : '16497', '838' : '16270', '839' : '16427', '842' : '16609', '843' : '16474', '845' : '17518', '846' : '16734', '847' : '16429', '848' : '16215', '849' : '16393', '851' : '16665', '852' : '16666', '854' : '17802', '857' : '16591', '858' : '16515', '859' : '16518', '860' : '16528', '861' : '16529', '862' : '17528', '863' : '16675', '864' : '16651', '865' : '16530', '866' : '16531', '867' : '16532', '868' : '16630', '869' : '16526', '870' : '16626', '871' : '16628', '872' : '16627', '873' : '16629', '874' : '16535', '875' : '16536', '876' : '16564', '877' : '16538', '878' : '16527', '879' : '16542', '880' : '16659', '881' : '16522', '882' : '16543', '883' : '16660', '885' : '16513', '886' : '16565', '887' : '16557', '888' : '16556', '889' : '16607', '890' : '16733', '891' : '16580', '894' : '17838', '895' : '16717', '896' : '5413', '897' : '17557', '898' : '17625', '899' : '17806', '902' : '15171', '903' : '10763', '905' : '15183', '906' : '10329', '907' : '10724', '908' : '16585', '909' : '10325', '910' : '16462', '912' : '15173', '913' : '15717', '915' : '10754', '916' : '17519', '917' : '16210', '918' : '17532', '919' : '16633', '920' : '16603', '921' : '16664', '922' : '16224', '923' : '16422', '925' : '16604', '927' : '17536', '928' : '17537', '930' : '16423', '932' : '16560', '933' : '17534', '935' : '16562', '936' : '16583', '937' : '16655', '938' : '16672', '939' : '16635', '940' : '16728', '941' : '16726', '943' : '16759', '945' : '17292', '946' : '17293', '947' : '17570', '948' : '16662', '949' : '17363', '950' : '17390', '951' : '17548', '952' : '17576', '953' : '17575', '955' : '17709', '957' : '17740', '958' : '17790', '959' : '17791', '960' : '17789', '963' : '17916', '965' : '17937', '966' : '18118', '967' : '18119', '981' : '16606', '982' : '17668', '983' : '16688', '1717' : '16746', '0東' : '10841', '0南' : '11811', '108區' : '16168', '202區' : '15185', '208直' : '16157', '208區' : '15113', '212夜' : '16132', '212直' : '10911', '214直' : '15562', '216區' : '11141', '218直' : '11157', '218區' : '11158', '225區' : '16128', '227區' : '15522', '232快' : '10419', '236區' : '11763', '240直' : '15355', '247區' : '15358', '251區' : '11764', '254區' : '16709', '255區' : '11253', '260區' : '10824', '262區' : '10962', '265夜' : '16131', '265區' : '10482', '265經中央路' : '10481', '265經明德路' : '11171', '278區' : '16439', '280直' : '15657', '286副' : '10846', '287區' : '10853', '290副' : '10784', '290副萬和' : '17479', '292副' : '16158', '295副' : '18057', '303區' : '10273', '304承德' : '15553', '304重慶' : '15554', '306區' : '11853', '311區' : '17512', '38區' : '10863', '39夜' : '15664', '42區' : '16559', '508區' : '10442', '542預' : '18348', '582經工業區' : '18148', '605快' : '15516', '605副' : '15517', '605新台五' : '15518', '617副' : '17952', '622預' : '18788', '624綠野香坡' : '10149', '638副' : '17868', '645副' : '10462', '657延' : '16685', '660區' : '17825', '666皇帝殿' : '17482', '666烏塗窟' : '17483', '666華梵大學' : '10753', '672區' : '16169', '677副' : '17015', '704區' : '16521', '712副' : '18258', '716(臺灣好行-皇冠北海岸線)' : '17530', '786區' : '17719', '787經瑞芳工業區' : '16681', '788海科館' : '17501', '788區' : '18098', '789區' : '17865', '790漁港' : '17500', '791經貢寮區衛生' : '17718', '791繞貢寮' : '17692', '795往十分寮' : '16757', '795往木柵' : '16719', '795往平溪' : '16758', '802區' : '16479', '813區' : '17527', '819副' : '17923', '837副' : '17971', '837區' : '17972', '839耕莘' : '16656', '847區' : '16697', '849屈尺社區' : '17696', '856(台灣好行-黃金福隆線)' : '16552', '867區' : '16710', '871經中山北路' : '16577', '872經正德國中、直行中山北路' : '16578', '873經正德國中' : '16579', '878區' : '18558', '886區' : '17824', '88區' : '17869', '897區' : '17706', '905副' : '15184', '907通勤' : '17928', '908延' : '17775', '918區' : '18318', '920副' : '18729', '927經台北港' : '17545', '930延' : '16614', '932繞國家教育研究院' : '17717', '937副' : '18728', '939副' : '17942', '939跳蛙' : '17720', '939繞國家教育研究所' : '17716', '946副' : '17294', '953區' : '17845', '966副' : '18730', '967直' : '18128', '967副' : '18731', '982直達' : '17680', '982直達新埔線' : '17687', '982區' : '17679'}
TTEMap = {'0':'　進站中','':'　未發車','-1':'　未發車','-2':'交管不停','-3':'末班已過','-4':'今日未營運'}

def printReport(arr):
    for ss in arr:
        if ss[0] == "0":
            print("\033[91m%5s %s\033[m" % (TTEMap[str(ss[0])], ss[1]))
        elif ss[0] < "0":
            print("%5s %s" % (TTEMap[str(ss[0])], ss[1]))
        else:
            print("%8s %s" % (str(int(ss[0]) // 60) + "分", ss[1]))

os.system("chcp 437")
print("\033[H\033[J")
for ss, vv in IDMap.items():
    print("%4s" % ss, end=" ")
num = input("\n\n請輸入要查詢的公車：")
try:
    routeid = IDMap[num]
except:
    print("\033[91m找不到這輛公車\033[m")
    input("按 ENTER 結束")
    exit()
else:
    stopsrc = "https://pda.5284.gov.taipei/MQS/RouteDyna?routeid=" + routeid
    routesrc = "https://pda.5284.gov.taipei/MQS/route.jsp?rid=" + routeid

stopdata = json.load(request.urlopen(stopsrc))
clist = stopdata["Stop"]

stopArr = {}
for ss in clist:
    stopArr[ss["n1"].split(",")[1]] = ss["n1"].split(",")[7]

with request.urlopen(routesrc) as response:
    data = response.read().decode("utf-8")
soup = BeautifulSoup(data, 'html.parser')
try:
    strGo = soup.find(class_='ttegotitle').string
    strBack = soup.find(class_='ttebacktitle').string
except:
    strGo = soup.find(class_='title3').string
    strBack = ""

tables = soup.find_all("table")
# 去程
tabGo = tables[3]
arrGo = []
a_tags = tabGo.find_all('a')
for tag in a_tags:
    arrGo.append([stopArr[tag.get('href').split("=")[1]], tag.string])

# Print report
print("\033[H\033[J")
print("****** \033[6m" + num + " 號公車\033[m ******\n")
if (strBack != ""):
    print("\033[93m" + strGo + "\033[0m")
printReport(arrGo)

# 回程
if (strBack != ""):
    tabBack = tables[4]
    arrBack = []
    a_tags = tabBack.find_all('a')
    for tag in a_tags:
        arrBack.append([stopArr[tag.get('href').split("=")[1]], tag.string])
# Print report
    print()
    print("\033[93m" + strBack + "\033[0m")
    printReport(arrBack)

input("\n按 ENTER 結束")
