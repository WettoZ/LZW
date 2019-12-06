import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./bookbase-1864c-firebase-adminsdk-6z2el-e9e582fa57.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://bookbase-1864c.firebaseio.com/'})
post = db.reference('books')

def first_el(strl):
    i = 0    
    while i < len(strl):
        t = 0
        g = 0
        while g < len(table):
            if strl[i] != table[g]:
                t = t + 1
            g = g +1
        if t == len(table):
            table.append(strl[i])
        i = i + 1
    print(table)

str = input()
#strl = 'Всё повторяется и много было их, Тех, кто как я, искал на всё ответ. На свой мотив слова рифмуя в стих, Оставив в нём, души нетленной свет. Всё повторяется — похожие вопросы, Во все века ум будут волновать. Тем кто не может жить легко и просто, Плыть по течению и ветра в спину ждать. Всё повторяется, спустя столетья, Распад империи подарит кровь войной. И трудно тем, кто жил тогда на свете, Кому в то время, жизнь дана судьбой. Всё повторяется и телом канув в Лету, Мотивы душ... '

#input()
table = [strl[0]]
first_el(strl)

i = 0
info = []
kod = 0

while i < len(strl):  
    
    t_str = strl[i]
    g = 0
    while g < len(table):        
        r = 0
        if t_str == table[g]:
           while t_str == table[g]:
               if i+1 < len(strl):
                 i = i + 1
                 t_str =  t_str + strl[i]
               else:
                   break
           print(t_str)         
           
        g = g +1 
    if t_str != strl[i]:
        table.append(t_str)
        info.append({
                    'Строка': t_str,
                    'Код': kod,
                    'Биты': bin(kod),
                    'Словарь': len(info)
                    })
        kod = kod + 1    
    print(i)
    i = i + 1

post.set(info)
print(info)
