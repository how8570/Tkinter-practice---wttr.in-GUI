import requests
import tkinter
from PIL import Image,ImageTk
from functools import partial
import itertools
def main():
    def getWeatherImg(location:str):
    #     print(location)
        global img
        with open('weather.png', 'wb') as file:  # 抓取圖片
            file.write(requests.get('http://wttr.in/' + location + '.png?lang=zh-tw').content)
            file.flush()
        file.close()
        img = ImageTk.PhotoImage(Image.open('weather.png'))
        lImg = tkinter.Label(root,image=img).grid(row = 0, column=4, rowspan=20, sticky='snwe', padx=5, pady=5)
    # getWeatherImg('花蓮') # test

    def on_return_search(etyLocation):
        getWeatherImg(etyLocation.widget.get())

    def on_click_search():
        getWeatherImg(etyLocation.get())


    root = tkinter.Tk()
    height, width = 1100, 540
    root.maxsize(height, width)  
    root.minsize(height, width)
    for i in range(3):
        root.columnconfigure(i, weight=1)

    root.columnconfigure(3, weight=10)
    for i in range(20):
        root.rowconfigure(i, weight=1)


    getWeatherImg('')
    area_list = ['台北市','新北市','基隆市','桃園市',
                '新竹市','新竹縣','苗栗縣','臺中市',
                '南投縣','彰化縣','雲林縣','嘉義市',
                '嘉義縣','臺南市','高雄市','屏東縣',
                '宜蘭縣','花蓮縣','臺東縣','澎湖縣',
                '金門縣','連江縣']

    c, r = 0, 0
    for (r, c), loc in zip(list(itertools.product(range(10), range(3)))[:len(area_list)], area_list):
    #     print(c,r,loc)
        tkinter.Button(root, text=loc, 
                    command=partial(getWeatherImg, loc)).grid(column=c, row=r, sticky='news')
        
    tkinter.Label(root, text="其他區域：").grid(column=0, row=10, sticky='ew')
    etyLocation = tkinter.Entry(root)
    etyLocation.grid(column=1, row=10, columnspan=2, sticky='ew')
    etyLocation.bind("<Return>", on_return_search)
    tkinter.Button(root, text="Enter 搜尋",
                command = on_click_search).grid(column=0, row=11, columnspan=3, sticky='nesw')


    root.mainloop()


if __name__ == '__main__':
    main()