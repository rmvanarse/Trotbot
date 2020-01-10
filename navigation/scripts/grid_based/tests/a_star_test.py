#! /usr/bin/env python

import time
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../mapping')))
try:
    from a_star import AStar
    from lidar_to_grid import Mapper
except:
    raise ImportError("AStar Could'nt be imported")


def test1():
    inf = np.inf
    scan =[inf, inf, inf, inf, inf, inf, inf, 3.056861639022827, 3.0252268314361572, 3.0203325748443604, 2.0132949352264404, 1.9735280275344849, 1.953012466430664, 1.9486260414123535, 1.9373271465301514, 1.9421530961990356, 1.9569212198257446, 2.002772331237793, inf, inf, inf, 0.9855800271034241, 0.9726546406745911, 0.9509224891662598, 0.9256065487861633, 0.9257093071937561, 0.922886073589325, 0.9183664917945862, 0.906120240688324, 0.8961981534957886, 0.9056581854820251, 0.9420517683029175, 0.9265859723091125, 0.9183934330940247, 0.9498110413551331, 0.9667358994483948, 1.0045623779296875, 2.442192792892456, 2.4326982498168945, 2.4553067684173584, 2.4645442962646484, 2.506408214569092, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 1.7533923387527466, 1.71872878074646, 1.70149827003479, 1.6858848333358765, 1.6909033060073853, 1.7164965867996216, 1.7079846858978271, 1.7376644611358643, 1.785688877105713, 3.3595521450042725, 3.3191449642181396, 3.29377818107605, 3.2705166339874268, 3.2538671493530273, 3.2152647972106934, 3.2159855365753174, 3.19524884223938, 3.0854270458221436, 2.8649425506591797, 2.6712183952331543, 2.554349184036255, 2.556751251220703, 2.5452141761779785, 2.5436341762542725, 2.5213427543640137, 2.5272300243377686, 2.5183942317962646, 2.509161949157715, 2.5124869346618652, 2.4297120571136475, 2.3386430740356445, 2.2512683868408203, 2.1818249225616455, 2.103046417236328, 2.0564870834350586, 1.9878475666046143, 1.9268088340759277, 1.885642170906067, 1.8311305046081543, 1.7829922437667847, 1.7410887479782104, 1.7179292440414429, 1.65846848487854, 1.6332777738571167, 1.5900510549545288, 1.5677014589309692, 1.5201916694641113, 1.4969840049743652, 1.4841266870498657, 1.4385578632354736, 1.4428545236587524, 1.4075186252593994, 1.3866387605667114, 1.3508318662643433, 1.3370169401168823, 1.3260891437530518, 1.3067781925201416, 1.2939659357070923, 1.2805120944976807, 1.2707873582839966, 1.2281290292739868, 1.2153609991073608, 1.2014520168304443, 1.2100038528442383, 1.1812770366668701, 1.1618354320526123, 1.1519147157669067, 1.1456130743026733, 1.1571439504623413, 1.1326026916503906, 1.1386666297912598, 1.0997953414916992, 1.091562271118164, 1.1005403995513916, 1.1073905229568481, 1.075814962387085, 1.0699113607406616, 1.078955054283142, 1.0810444355010986, 1.0660544633865356, 1.0604965686798096, 1.0380046367645264, 1.0327768325805664, 1.078073501586914, 1.0491496324539185, 1.0314854383468628, 1.0256805419921875, 1.0399309396743774, 1.039351224899292, 1.0458898544311523, 1.0328317880630493, 1.0365073680877686, 1.0345937013626099, 1.0336904525756836, 1.045121431350708, 1.019679069519043, 0.9782207012176514, 0.9893175959587097, 0.9512673616409302, 0.9016335606575012, 0.8861187696456909, 0.8714970350265503, 0.8524404168128967, 0.8410521745681763, 0.8306225538253784, 0.806861162185669, 0.7750387787818909, 0.772260308265686, 0.7613915205001831, 0.7231266498565674, 0.7228431701660156, 0.7109572291374207, 0.7123162746429443, 0.6959463357925415, 0.6842755079269409, 0.6778551936149597, 0.672926127910614, 0.6455686688423157, 0.6492228507995605, 0.650477945804596, 0.6205228567123413, 0.63560950756073, 0.6331012845039368, 0.6159425973892212, 0.6135613918304443, 0.5959789752960205, 0.610405445098877, 0.5870363712310791, 0.5804761052131653, 0.6007770299911499, 0.5676383972167969, 0.5660935640335083, 0.5781680345535278, 0.5915207862854004, 0.5583205819129944, 0.5651285648345947, 0.5652458071708679, 0.5596476197242737, 0.545867919921875, 0.5507373809814453, 0.5318761467933655, 0.542111337184906, 0.540361225605011, 0.5328619480133057, 0.5332945585250854, 0.5352373123168945, 0.5453101992607117, 0.5408035516738892, 0.5488573908805847, 0.5210607647895813, 0.5293474793434143, 0.5348880290985107, 0.5456039905548096, 0.5199136734008789, 0.5178253650665283, 0.5266040563583374, 0.5523934364318848, 0.5342961549758911, 0.5384075045585632, 0.5334569215774536, 0.5281636714935303, 0.5111650228500366, 0.5428661704063416, 0.5401403903961182, 0.5570170879364014, 0.5265321731567383, 0.5520188212394714, 0.5388387441635132, 0.5361006855964661, 0.5432685613632202, 0.5588036775588989, 0.5637043118476868, 0.5593273043632507, 0.5618724226951599, 0.5681909918785095, 0.580647349357605, 0.5878729224205017, 0.567261815071106, 0.5693681240081787, 0.5898579955101013, 0.6078497171401978, 0.6051531434059143, 0.6091262102127075, 0.5822492837905884, 0.6195617318153381, 0.6141515374183655, 0.617192804813385, 0.6386907696723938, 0.6485453248023987, 0.6483967900276184, 0.6659299731254578, 0.6548660397529602, 0.6864899396896362, 0.6838104128837585, 0.6932967901229858, 0.7090590596199036, 0.7026281356811523, 0.7346917986869812, 0.7633113861083984, 0.7599661350250244, 0.7832435369491577, 0.779472291469574, 0.8087064623832703, 0.8164687752723694, 0.8538014888763428, 0.8430877923965454, 0.8757237195968628, 0.8956906199455261, 0.9206846356391907, 0.9354161024093628, 0.9733413457870483, 0.9885174036026001, 1.0486935377120972, 1.049687385559082, 1.1021144390106201, 1.1006282567977905, 1.1586135625839233, 1.2052730321884155, 1.2459439039230347, 1.302675485610962, 1.3653827905654907, 1.4164248704910278, 1.4472814798355103, 1.535380244255066, 1.532191514968872, 1.5412589311599731, 1.5219082832336426, 1.5472310781478882, 1.5644363164901733, 1.55789053440094, 1.5711780786514282, 1.5786079168319702, 1.5898356437683105, 1.600523829460144, 1.6128002405166626, 1.6159331798553467, 1.626638412475586, 1.8782384395599365, 2.235314130783081, 2.2563958168029785, 2.2954134941101074, 2.307398557662964, 2.3106799125671387, 2.351066827774048, 2.391575813293457, 2.3959853649139404, 2.430370569229126, 2.449401378631592, 2.478189468383789, 2.516754150390625, 2.5472171306610107, 2.59478759765625, 2.6314077377319336, 2.6275601387023926, 2.682375907897949, 2.7329845428466797, 2.7940165996551514, 2.8262627124786377, 2.891613245010376, 2.943937301635742, 2.9711005687713623, 3.0209319591522217, 3.1053292751312256, 1.0324296951293945, 1.0091277360916138, 1.0003530979156494, 0.9934810996055603, 0.9784740209579468, 0.9725538492202759, 0.9597940444946289, 0.9535285830497742, 0.9423716068267822, 0.9491086602210999, 0.966484010219574, 0.9733442068099976, 0.9970974326133728, 1.0060924291610718, 1.0158592462539673, 1.0913983583450317, inf, inf, inf, inf, 2.0314512252807617, 2.0178802013397217, 1.9728460311889648, 1.961500883102417, 1.9714338779449463, 1.9641704559326172, 2.0064427852630615, 2.0385403633117676, 3.066349506378174, 3.039686918258667, 3.0638043880462646, 3.07513165473938, inf, inf, inf, inf, inf, inf, inf, inf, inf]
    

    o = Mapper()
    prob_map = Mapper.main(o,scan)

    d =AStar()
    d(prob_map , [36,36], [50,30])
    
    print('\n ' + '-'*30 +  "\n> Starting operation ...\n " + '-'*30 + '\n')
    
    start_time = time.time()
    final_path = d.find_path()

    print('\n ' + '-'*30 + "\n> Time taken: {:.4} seconds.\n ".format(time.time() - start_time) + '-'*30 + '\n')
    d.draw_final_graph(final_path)

    
def test2():
    inf = np.inf
    scan=[inf, inf, inf, inf, inf, inf, 2.122950792312622, 1.8218177556991577, 1.59413743019104, 1.423231601715088, 1.323502540588379, 1.3081393241882324, 1.3145588636398315, 1.3490028381347656, 1.335472822189331, 1.319705605506897, 1.3400593996047974, 1.3491653203964233, 1.3466880321502686, 1.3696467876434326, 1.3745601177215576, 1.3833107948303223, 1.3923722505569458, 1.4062138795852661, 1.3897963762283325, 1.4243078231811523, 1.4298373460769653, 1.4416676759719849, 1.450016736984253, 1.471937656402588, 1.5024218559265137, 1.4850928783416748, 1.5270593166351318, 1.5272008180618286, 1.5350757837295532, 1.5613079071044922, 1.58877432346344, 1.6090070009231567, 1.6587506532669067, 1.6668319702148438, 1.6823045015335083, 1.711564540863037, 1.7509064674377441, 1.7584381103515625, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 2.650038242340088, 2.6445717811584473, 2.631784677505493, 2.6164636611938477, 2.6125850677490234, 2.5924696922302246, 2.5889229774475098, 2.5727877616882324, 2.5825552940368652, 2.5913491249084473, 2.5679054260253906, 2.575549840927124, 2.5961365699768066, 2.578033447265625, 2.563906669616699, 2.576000690460205, 2.586289644241333, 2.5772287845611572, 2.5811655521392822, 2.5825459957122803, 2.588222026824951, 2.5943994522094727, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 2.9890737533569336, 2.9071550369262695, 2.8188626766204834, 2.7494678497314453, 2.67634916305542, 2.6266491413116455, 2.5653467178344727, 2.5333642959594727, 2.4661786556243896, 2.4012131690979004, 2.3687829971313477, 2.323002338409424, 2.2887566089630127, 2.2677664756774902, 2.296781539916992, 2.3500185012817383, 2.360821008682251, 2.453289031982422, 2.4872214794158936, 2.548398017883301, 2.6022679805755615, 2.6568949222564697, 2.7322375774383545, 2.7981326580047607, 2.8849222660064697, 2.9328646659851074, 3.0372416973114014, inf, inf, inf, inf, inf, 3.4685451984405518, 3.4392693042755127, 3.423564910888672, 3.389524221420288, 3.3799402713775635, 3.355445146560669, 3.335869073867798, 3.295499086380005, 3.285273551940918, 3.2675883769989014, 3.2415120601654053, 3.2439682483673096, 3.21799898147583, 3.207578659057617, 3.2076492309570312, 3.3214356899261475, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 1.7193019390106201, 1.679825782775879, 1.650679349899292, 1.6179615259170532, 1.5983997583389282, 1.5532128810882568, 1.5364797115325928, 1.5386948585510254, 1.5013322830200195, 1.4845850467681885, 1.4534012079238892, 1.444892168045044, 1.4262295961380005, 1.4062203168869019, 1.4057549238204956, 1.3824982643127441, 1.367220163345337, 1.3536320924758911, 1.3183528184890747, 1.3393183946609497, 1.312820553779602, 1.3034974336624146, 1.2918084859848022, 1.2986373901367188, 1.2754086256027222, 1.271276831626892, 1.2715413570404053, 1.2496140003204346, 1.220840334892273, 1.259627103805542, 1.2267930507659912, 1.2130810022354126, 1.2276153564453125, 1.2212096452713013, 1.281704306602478, 1.3779208660125732, 1.5410783290863037, 1.7324031591415405, 1.9674873352050781, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 2.966913938522339, 2.879478931427002, 2.812376022338867, 2.7323076725006104, 2.667478322982788, 2.613341808319092, 2.5557971000671387, 2.4918932914733887, 2.439162492752075, 2.3888156414031982, 2.3447256088256836, 2.304054021835327, 2.2600510120391846, 2.2221076488494873, 2.216076374053955, 2.2552261352539062, 2.31876802444458, 2.357189178466797, 2.396010398864746, 2.4466495513916016, 2.4985275268554688, 2.564828395843506, 2.634127140045166, 2.671659231185913, 2.7563955783843994, 2.829598903656006, 2.9014203548431396, 2.9869801998138428, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

    o = Mapper()
    prob_map = Mapper.main(o,scan)

    d =AStar()
    d(prob_map , [36,36], [10,50])
    
    print('\n ' + '-'*30 +  "\n> Starting operation ...\n " + '-'*30 + '\n')
    
    start_time = time.time()
    final_path = d.find_path()

    print('\n ' + '-'*30 + "\n> Time taken: {:.4} seconds.\n ".format(time.time() - start_time) + '-'*30 + '\n')
    d.draw_final_graph(final_path)

