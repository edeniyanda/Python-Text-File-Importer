import sqlite3 


#connect to the database
con = sqlite3.connect("classdata.sqlite")
cur = con.cursor()


#drop the table if the Data already exists
cur.execute('''
            DROP TABLE IF EXISTS Data
            ''')


#create the table Data
cur.execute('''
            CREATE TABLE Data (Firstname TEXT, Middlename TEXT, Lastname TEXT, Nickname TEXT, Rolemodel TEXT)
            ''')


#open the file to read the data
filehandle = open("info.txt", 'r')


#iterate through the file and read each line
for line in filehandle:
    word = line.split( )
    
    #extract the data
    fname = word[word.index('Name')+3]
    mname = word[word.index('Name')+4]
    lname = word[word.index('Name')+2]
    ambition = word[word.index('Ambition')+2 : word.index('Role')]
    rm = word[word.index('Model')+2 : len(word)]
    nn = word[word.index('Nickname')+2:word.index('Ambition')]
    
    
    #join the data in the list into a single string
    ambition = " ".join(ambition)
    rm = " ".join(rm)
    nn = " ".join(nn)
    
    
    #print the data to preview
    print ("Extracting data...")
    print (fname, mname, lname)
    print (ambition)
    print (rm)
    print (nn)
    print("\n")
    
    
    #insert the data into the database
    try:
        cur.execute('''
            INSERT INTO Data (Firstname, Middlename, Lastname, Nickname, Rolemodel) VALUES (?,?,?,?,?)
            ''', (fname,mname,lname,nn,rm,)) 
    
    except sqlite3.Error as Error:
        print ("Error")
        
        
    #commit the transaction
    con.commit()
    

#close the file   
filehandle.close() 

# Close the connection to the database
cur.close()
    
    
    
