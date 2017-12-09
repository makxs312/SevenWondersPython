from DAL.SevenWondersContext import SevenWondersContext
from flask import session
import itertools
import hashlib
import base64


class AccountService(object):
    def login(self, dictform):
        context = SevenWondersContext()
        email = dictform.get("Email")
        password = dictform.get("Password")
        current_user = context.exec_param_sproc(context.GET_USER, [("email", str(email)),
                                                                   ("hashedPassword", str(self.hashPassword(password)))])
        
        if (current_user == []):
            return False;
        role = current_user[0]["RoleId"]
        id = current_user[0]["Id"]

        #admin
        if (role == 2):
            session["id"] = id
            session["role"] = role
            return True
        #customer
        elif (role == 1):
            customer = context.exec_param_sproc(context.GET_CUSTOMER_BY_EMAIL, [("email", str(email))])
            if (customer[0]["IsDeleted"] == 0):
                session["id"] = id
                session["role"] = role
                return True
            else:
                return False
        #manager
        elif (role == 3):
            manager = context.exec_param_sproc(context.GET_MANAGER_BY_EMAIL, [("email", str(email))])
            if (manager[0]["IsDeleted"] == 0):
                session["id"] = id
                session["role"] = role
                return True
            else:
                return False

    def logout(self):
        session.clear()


    def hashPassword(self, pwd):
        pswd = pwd + "blabla"
        password = hashlib.md5()
        password.update(pswd)
        res = password.digest()[:16]
        b = bytearray()
        b.extend(res)
        resarr = (map(hex,b))
        resstr = []
        result = [int(x,0) for x in resarr]
        endres = str()
        for r in result:
            endres += chr(r)
        endres64 = base64.b64encode(endres)
        return endres64[:len(endres64) - 2]