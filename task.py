
import sqlite3

db = sqlite3.connect("baza.db")

sql= db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS bankomat ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR (50) NOT NULL, 
    surname VARCHAR(50) NOT NULL,
    password VARCHAR(4) NOT NULL,
    cash INT NOT NULL DEFAULT 0)""")



secim= input("""
(1) Balansi yoxla
(2) Kartdan Pul Cixar
(3) Karta Medaxil et
(4) Pini deyish
(5) Cixish et

Secim edin: 

""")


if secim== 1:
    
    name = input("Name Daxil edin : ")
    surname = input("Surname Daxil edin : ")
    password = input("Password Daxil edin : ")
    cash = int(input("Mebleg : "))
    
    sql.execute(f"""
                
                INSERT INTO casino 
                (
                    
                    name,
                    surname,
                    password,
                    cash
                    
                    )
                    
                VALUES (
                    
                    '{name}','{surname}''{password}',{cash}
                    
                    )
                    
                
                """)
    db.commit()
    




if secim== 2:
    
    name = input("Name Daxil edin : ")
    surname = input("Surname Daxil edin : ")
    password = input("Password Daxil edin : ")
    cash = int(input("Kartdan cixarilacaq mebleg : "))
    
    sql.execute(f"""
                    
                    UPDATE casino SET cash = cash - {cash} 
                    WHERE name == '{name}'
                    
                    
                    """)
    db.commit()
    
    print(f"Sizin hesabinizdan {cash} Azn cixildi")


if secim == 3:

 name = input("Name Daxil edin : ")
 surname = input("Surname Daxil edin : ")
 password = input("Password Daxil edin : ")
 cash = int(input("Karta elave olunacaq mebleg : "))

 sql.execute(f"""
                    
                    UPDATE casino SET cash = cash + {cash} 
                    WHERE name == '{name}'
                    
                    
                    """)
db.commit()
print(f"Sizin hesabiniza {cash}Azn elave olundu")
    

