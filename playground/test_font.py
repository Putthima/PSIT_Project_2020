from tkinter import *
import tkinter.font as font

gui1 = Tk(className='1')
gui2 = Tk(className='2')
gui3 = Tk(className='3')
gui4 = Tk(className='4')
gui5 = Tk(className='5')

showfont1 = [
    'System',
    'Terminal',
    'Fixedsys',
    'Modern',
    'Roman',
    'Script',
    'Courier',
    'MS Serif',
    'MS Sans Serif',
    'Small Fonts',
    'Marlett',
    'Arial',
    'Arabic Transparent',
    'Arial Baltic',
    'Arial CE',
    'Arial CYR',
    'Arial Greek',
    'Arial TUR',
    'Arial Black',
    'Bahnschrift Light',
    'Bahnschrift SemiLight',
    'Bahnschrift',
    'Bahnschrift SemiBold',
    'Bahnschrift Light SemiCondensed',
    'Bahnschrift SemiLight SemiConde',
    'Bahnschrift SemiCondensed',
    'Bahnschrift SemiBold SemiConden',
    'Bahnschrift Light Condensed',
    'Bahnschrift SemiLight Condensed',
    'Bahnschrift Condensed',
    'Bahnschrift SemiBold Condensed',
    'Calibri',
    'Calibri Light',
    'Cambria',
    'Cambria Math',
    'Candara',
    'Candara Light',
    'Comic Sans MS',
    'Consolas',
    'Constantia',
    'Corbel',
    'Corbel Light',
]

showfont2 = [
    'Courier New',
    'Courier New Baltic',
    'Courier New CE',
    'Courier New CYR',
    'Courier New Greek',
    'Courier New TUR',
    'Ebrima',
    'Franklin Gothic Medium',
    'Gabriola',
    'Gadugi',
    'Georgia',
    'Impact',
    'Ink Free',
    'Javanese Text',
    'Leelawadee UI',
    'Leelawadee UI Semilight',
    'Lucida Console',
    'Lucida Sans Unicode',
    'Malgun Gothic',
    '@Malgun Gothic',
    'Malgun Gothic Semilight',
    '@Malgun Gothic Semilight',
    'Microsoft Himalaya',
    'Microsoft JhengHei',
    '@Microsoft JhengHei',
    'Microsoft JhengHei UI',
    '@Microsoft JhengHei UI',
    'Microsoft JhengHei Light',
    '@Microsoft JhengHei Light',
    'Microsoft JhengHei UI Light',
    '@Microsoft JhengHei UI Light',
    'Microsoft New Tai Lue',
    'Microsoft PhagsPa',
    'Microsoft Sans Serif',
    'Microsoft Tai Le',
    'Microsoft YaHei',
    '@Microsoft YaHei',
    'Microsoft YaHei UI',
    '@Microsoft YaHei UI',
    'Microsoft YaHei Light',
    '@Microsoft YaHei Light',
    'Microsoft YaHei UI Light',
]

showfont3 = [
    '@Microsoft YaHei UI Light',
    'Microsoft Yi Baiti',
    'MingLiU-ExtB',
    '@MingLiU-ExtB',
    'PMingLiU-ExtB',
    '@PMingLiU-ExtB',
    'MingLiU_HKSCS-ExtB',
    '@MingLiU_HKSCS-ExtB',
    'Mongolian Baiti',
    'MS Gothic',
    '@MS Gothic',
    'MS UI Gothic',
    '@MS UI Gothic',
    'MS PGothic',
    '@MS PGothic',
    'MV Boli',
    'Myanmar Text',
    'Nirmala UI',
    'Nirmala UI Semilight',
    'Palatino Linotype',
    'Segoe MDL2 Assets',
    'Segoe Print',
    'Segoe Script',
    'Segoe UI',
    'Segoe UI Black',
    'Segoe UI Emoji',
    'Segoe UI Historic',
    'Segoe UI Light',
    'Segoe UI Semibold',
    'Segoe UI Semilight',
    'Segoe UI Symbol',
    'SimSun',
    '@SimSun',
    'NSimSun',
    '@NSimSun',
    'SimSun-ExtB',
    '@SimSun-ExtB',
    'Sitka Small',
    'Sitka Text',
    'Sitka Subheading',
    'Sitka Heading',
    'Sitka Display',
]

showfont4 = [
    'Sitka Banner',
    'Sylfaen',
    'Symbol',
    'Tahoma',
    'Times New Roman',
    'Times New Roman Baltic',
    'Times New Roman CE',
    'Times New Roman CYR',
    'Times New Roman Greek',
    'Times New Roman TUR',
    'Trebuchet MS',
    'Verdana',
    'Webdings',
    'Wingdings',
    'Yu Gothic',
    '@Yu Gothic',
    'Yu Gothic UI',
    '@Yu Gothic UI',
    'Yu Gothic UI Semibold',
    '@Yu Gothic UI Semibold',
    'Yu Gothic Light',
    '@Yu Gothic Light',
    'Yu Gothic UI Light',
    '@Yu Gothic UI Light',
    'Yu Gothic Medium',
    '@Yu Gothic Medium',
    'Yu Gothic UI Semilight',
    '@Yu Gothic UI Semilight',
    'HoloLens MDL2 Assets',
    'BIZ UDGothic',
    '@BIZ UDGothic',
    'BIZ UDPGothic',
    '@BIZ UDPGothic',
    'BIZ UDMincho Medium',
    '@BIZ UDMincho Medium',
    'BIZ UDPMincho Medium',
    '@BIZ UDPMincho Medium',
    'Meiryo',
    '@Meiryo',
    'Meiryo UI',
    '@Meiryo UI',
    'MS Mincho',
]

showfont5 = [
    '@MS Mincho',
    'MS PMincho',
    '@MS PMincho',
    'UD Digi Kyokasho N-B',
    '@UD Digi Kyokasho N-B',
    'UD Digi Kyokasho NP-B',
    '@UD Digi Kyokasho NP-B',
    'UD Digi Kyokasho NK-B',
    '@UD Digi Kyokasho NK-B',
    'UD Digi Kyokasho N-R',
    '@UD Digi Kyokasho N-R',
    'UD Digi Kyokasho NP-R',
    '@UD Digi Kyokasho NP-R',
    'UD Digi Kyokasho NK-R',
    '@UD Digi Kyokasho NK-R',
    'Yu Mincho',
    '@Yu Mincho',
    'Yu Mincho Demibold',
    '@Yu Mincho Demibold',
    'Yu Mincho Light',
    '@Yu Mincho Light',
    'DengXian',
    '@DengXian',
    'DengXian Light',
    '@DengXian Light',
    'FangSong',
    '@FangSong',
    'KaiTi',
    '@KaiTi',
    'SimHei',
    '@SimHei',
    'Ubuntu',
    'Raleway',
    'Ubuntu Condensed',
    'Ubuntu Light'
]

usefont1 = []
usefont2 = []
usefont3 = []
usefont4 = []
usefont5 = []

for i in showfont1:
    myFont = font.Font(family=i, size=10)
    usefont1.append(myFont)

for i in showfont2:
    myFont = font.Font(family=i, size=10)
    usefont2.append(myFont)

for i in showfont3:
    myFont = font.Font(family=i, size=10)
    usefont3.append(myFont)

for i in showfont4:
    myFont = font.Font(family=i, size=10)
    usefont4.append(myFont)

for i in showfont5:
    myFont = font.Font(family=i, size=10)
    usefont5.append(myFont)

for j in range(len(usefont1)):
    label = Label(gui1, text=str(j) + " : " +
                  showfont1[j], fg='black', font=usefont1[j])
    label.grid(sticky="w")

for j in range(len(usefont2)):
    label = Label(gui2, text=str(j) + " : " +
                    showfont2[j], fg='black', font=usefont2[j])
    label.grid(sticky="w")

for j in range(len(usefont3)):
    label = Label(gui3, text=str(j) + " : " +
                    showfont3[j], fg='black', font=usefont3[j])
    label.grid(sticky="w")

for j in range(len(usefont4)):
    label = Label(gui4, text=str(j) + " : " +
                    showfont4[j], fg='black', font=usefont4[j])
    label.grid(sticky="w")

for j in range(len(usefont5)):
    label = Label(gui5, text=str(j) + " : " +
                    showfont5[j], fg='black', font=usefont5[j])
    label.grid(sticky="w")


gui1.mainloop()
gui2.mainloop()
gui3.mainloop()
gui4.mainloop()
gui5.mainloop()
