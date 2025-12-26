import sqlite3
import os
import csv
#we need to get a title variable from the user input-and the year and director
#find a way to commit new entries using a scanner function, making options between 3 tables
#being movies, music, and books
con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "media.db"))
cur = con.cursor()
#create the tables for the first time- if it dosent exist- 
cur.execute("CREATE TABLE IF NOT EXISTS movies(mtitle TEXT, myear INTEGER, dir TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS music(ctitle TEXT, cyear INTEGER, band TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS books(btitle TEXT, byear INTEGER, author TEXT)")

#variable to answer if the user wants to view at the end
x=0
target_table = ""
#options for the user
print("hello User what would you like to do today?\n")
while True:
    print("\n--- Media Database Menu ---")
    print("1. Add a Movie")
    print("2. Add a CD (Music)")
    print("3. Add a Book")
    print("4. View All Entries")
    print("5. Exit")
    try:
        op = int(input("Option: "))
    except ValueError:
        print("Please enter a valid number.")
 

#options for adding to each table 1:movies 2:music 3:books-might add 4 for viewing entries later
#Note: maybe add the new database table to view at the end? if t/f booleans exists to check just do that
    if op==1:
        tit=input("Enter the movie title: ")
        yr=int(input("Enter the movie year: "))
        dr=input("Enter the movie director: ")
        cur.execute("INSERT INTO movies (mtitle, myear, dir) VALUES (?, ?, ?)", (tit, yr, dr))
        target_table = "movies"
    
    elif op==2:
        album=input("Enter the Album name:")
        ayear=int(input("Enter the Year the Album was relased:"))
        bname=input("Enter the Band name:")
        cur.execute("INSERT INTO music(ctitle,cyear,band) VALUES(?,?,?)",(album,ayear,bname))
        target_table = "music"
    elif op==3:
        bookn=input("Enter the Book name:")
        byear=int(input("Enter the year of relase"))
        authorn=input("Enter the Author name")
        cur.execute("INSERT INTO books(btitle,byear,author) VALUES(?,?,?)",(bookn,byear,authorn))
        target_table = "books"
    elif op == 4:
        print("\nWhich table would you like to view?")
        view_choice = input("Enter 'movies', 'music', or 'books': ").lower()
        if view_choice in ['movies', 'music', 'books']:
            cur.execute(f"SELECT * FROM {view_choice}")
            data = cur.fetchall()
            print(f"\n--- {view_choice.upper()} ENTRIES ---")
            for row in data:
                print(row)
        else:
            print("Invalid table name.")

    elif op == 5:
        print("Closing database. Goodbye!")
        break
    
    else:
        print("Please select a valid option (1-5).")


    
#for rn use csv file

#close everything up :3
# could change the table inputs to be in a while loop to keep the program running and working for the
# entire time- though ik for a fact that i would like to make this visually made thourgh ui/website- so for right now
# this is just the basis for a terminal based sql database   
con.commit()
con.close()