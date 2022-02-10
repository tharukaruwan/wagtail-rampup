import requests
import os

def registerUser(email,password):
    apikey=os.environ.get('FIREBASEAPIKEY')
    details={
        'email':email,
        'password':password,
        'returnSecureToken': True
    }
    r=requests.post('https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={}'.format(apikey),data=details)
    if 'error' in r.json().keys():
        return {'status':'error','message':r.json()['error']['message']}
    if 'idToken' in r.json().keys() :
        return {'status':'success','idToken':r.json()['idToken'],'refreshToken':r.json()['refreshToken'],'id':r.json()['localId']}

def loginUser(email,password):
    apikey=os.environ.get('FIREBASEAPIKEY')
    details={
        'email':email,
        'password':password,
        'returnSecureToken': True
    }
    r=requests.post('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={}'.format(apikey),data=details)
    if 'error' in r.json().keys():
        return {'status':'error','message':r.json()['error']['message']}
    if 'idToken' in r.json().keys() :
        return {'status':'success','idToken':r.json()['idToken'],'refreshToken':r.json()['refreshToken'],'id':r.json()['localId']}