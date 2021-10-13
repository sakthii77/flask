from flask import Flask,render_template,url_for,request
import sqlite3

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html");

@app.route("/add")
def add():   
    return render_template("add.html")

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            First_Name = request.form["firstname"]
            Last_Name = request.form["lastname"]
            Mobile_Number = request.form["mnumber"]
            Office_Number = request.form["onumber"]
            E_mail = request.form["mail"]
            Address = request.form["address"]
            with sqlite3.connect(r"C:\Users\s\Desktop\flask_project\contact_project\address1.db") as connection:
                cursor = connection.cursor()   
                cursor.execute("""insert into addressbook (FirstName,LastName,MobileNumber,OfficeNumber,mailid,address)
                values(?,?,?,?,?,?);""",(First_Name,Last_Name,Mobile_Number,Office_Number,E_mail,Address))
                connection.commit()
                msg = "Contact successfully Added"   
        except:
            connection.rollback()
            msg = "Can't Add Details Into Contact List Check The Input Data's"
        finally:
            return render_template("sucess.html",message = msg)
            connection.close()

@app.route("/view")
def view():
	
    with sqlite3.connect(r"C:\Users\s\Desktop\flask_project\contact_project\address1.db") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor() 
        cursor.execute("select * from addressbook")   
        data = cursor.fetchall()
        return render_template("view.html",rows = data)

@app.route("/edit")
def edit():
    return render_template("edit.html")        
@app.route("/updating",methods = ["GET","POST"])   
def updating():
    id = request.form["sno"]
    print("@@@@@@@@@@@@@@###################$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%",id)
    with sqlite3.connect(r"C:\Users\s\Desktop\flask_project\contact_project\address1.db") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor() 
        cursor.execute("select * from addressbook where Sno= ?",id)   
        data = cursor.fetchall()
        return render_template("update_show.html",rows = data)

@app.route("/updated",methods = ["POST","GET"])
def updated():
    msg = ""
    
    if request.method == "POST":
        try:
           
            First_Name = request.form["firstname"]
            Last_Name = request.form["lastname"]
            Mobile_Number = request.form["mnumber"]
            Office_Number = request.form["onumber"]
            E_mail = request.form["mail"]
            Address = request.form["address"]
            with sqlite3.connect(r"C:\Users\s\Desktop\flask_project\contact_project\address1.db") as connection:
                cursor = connection.cursor()   
                cursor.execute("UPDATE addressbook SET FirstName=?,LastName=?,MobileNumber=?,OfficeNumber=?,mailid=?,address=? where sno=? ",(First_Name,Last_Name,Mobile_Number,Office_Number,E_mail,Address,Sno))
                connection.commit()
                msg = "Updated successfully Added"   
        except:
            connection.rollback()
            msg = "Can't Update Into Contact List Check The Input Data's"
        finally:
            return render_template("updated.html",message = msg)
            connection.close()

    
@app.route("/delete")
def delete():
    return render_template("delete.html")
@app.route("/deleterecord" ,methods = ['POST'])   
def deleterecord():
        id=request.form['sno']
        
        with sqlite3.connect(r"C:\Users\s\Desktop\flask_project\contact_project\address1.db") as con:
            try:
                cur = con.cursor()
                cur.execute("delete from addressbook where Sno= ?;",id)
                msg = "Contact successfully Deleted"   
            except:
                msg = "Can't Be Deleted"
            finally:
                return render_template("delete_record.html",msg = msg)


if __name__ == "__main__":
    app.run(debug = True)  
