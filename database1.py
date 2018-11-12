import sqlite3

db = sqlite3.connect('database.db')
c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS UserInfo (username string, password string, email string, role string)')

def insert_user(name, passW, email, role):
    c.execute('INSERT INTO UserInfo (username, password, email, role) VALUES(?, ?, ?, ?)', (name, passW, email, role))
    db.commit()

def check_user_password(inputUser, inputPassword):
    find_user_password = ('SELECT * FROM UserInfo WHERE username = ? AND password = ?')
    c.execute(find_user_password,[(inputUser), (inputPassword)])
    results = c.fetchall()
    return results

def check_user(inputUser):
    find_user = ('SELECT * FROM UserInfo WHERE username = ?')
    c.execute(find_user,[(inputUser)])
    results = c.fetchall()
    return results

def check_email(inputEmail):
    find_email = ('SELECT * FROM UserInfo WHERE email = ?')
    c.execute(find_email,[(inputEmail)])
    results = c.fetchall()
    return results

def check_role(inputUser):
    find_user = ('SELECT * FROM UserInfo WHERE username = ?')
    c.execute(find_user,[(inputUser)])
    results = c.fetchall()
    for i in results:
        print("")
    return i[3]

c.execute('CREATE TABLE IF NOT EXISTS UserPortfolio (username string, num_credits integer, total_value double)')
def insert_UP(name):
    c.execute('INSERT INTO UserPortfolio (username, num_credits, total_value) VALUES(?, ?, ?)', (name, "5000", "5000"))
    db.commit()

def find_credits(inputUser):
    find_credit = ('SELECT * FROM UserPortfolio WHERE username = ?')
    c.execute(find_credit,[(inputUser)])
    results = c.fetchall()
    for i in results:
        print("")
    return i[1]

def update_credit(inputName, inputCredit):
    c.execute('UPDATE UserPortfolio SET num_credits = (?) WHERE username = (?)', (inputCredit, inputName))
    db.commit()

def update_total_value(inputName, inputTotalValue):
    c.execute('UPDATE UserPortfolio SET total_value = (?) WHERE username = (?)', (inputTotalValue, inputName))
    db.commit()

c.execute('CREATE TABLE IF NOT EXISTS UserStockAmount (username string, stockname string, amount integer)')
def insert_stock(name, stockName, amount):
    c.execute('INSERT INTO UserStockAmount (username, stockname, amount) VALUES(?, ?, ?)', (name, stockName, amount))
    db.commit()
    
def find_stock_of_user(inputUser):
    find_stock = ('SELECT * FROM UserStockAmount WHERE username = ?')
    c.execute(find_stock,[(inputUser)])
    results = c.fetchall()
    return results

c.execute('CREATE TABLE IF NOT EXISTS UserQuickAccess (username string, stockname string)')
def insert_user_quick_access(name, stockName):
    c.execute('INSERT INTO UserQuickAccess (username, stockname) VALUES(?, ?)', (name, stockName))
    db.commit()

def find_user_quick_access(inputUser):
    find_stock = ('SELECT * FROM UserQuickAccess WHERE username = ?')
    c.execute(find_stock,[(inputUser)])
    results = c.fetchall()
    return results

#c.close
#db.close()
