def solution(id_pw, db):
    result = 'fail'
    for id, pw in db :
        if id == id_pw[0] :
            if pw == id_pw[1] :
                result = 'login' 
                break
            else :
                result = 'wrong pw'
                break
    return result