#! /usr/bin/python
# -*- coding: UTF-8 -*-

# @author: Visgean Skeloru
# email: <visgean@gmail.com>
# jabber: <visgean@jabber.org>
# github: http://github.com/Visgean

from hashlib import sha512, md5
from Crypto.Cipher import AES

import sys
import getpass
import base64
import exceptions
import os
import tarfile

"Module for crypting files"


class WrongPassException(exceptions.BaseException):
    def __str__(self):
        return "You have used wrong pass. This incident will be reported ( http://xkcd.com/838/ )"


class FileContainer:
    def __init__(self, filepath, password):
        self.tar = True if os.path.isdir(filepath) else False
        if self.tar:
            tarpath = filepath[:-1] if filepath[-1] is "/" else filepath
            tarpath += ".tar"
            
            self.tarFolder(filepath, tarpath)
            self.filepath = tarpath
            self.newFile = self.filepath + ".taes" # filename for encryption
        else:
            self.filepath = filepath
            self.newFile = self.filepath + ".aes" # filename for encryption

        if self.filepath.endswith(".aes"):
            self.fileIsTar = False # encrypted file is just a file
        if self.filepath.endswith(".taes"):
            self.fileIsTar = True # encrypted file is a folder
        
        self.oldFile = self.filepath[:-4] # filename for decryption
        
        
        self.hashlist = self._pass2hashList(password)
        del password # there is no need to store it anymore cause we have hashes
    
    
    def _pass2hashList(self, rawPass):
        "Return list of hashes from password. "
        hashlist = []
        for i in range(1984):
            rawPass = sha512(md5(rawPass).hexdigest()).hexdigest()
            rawPass = md5(rawPass).hexdigest()
            hashlist.append(rawPass)
        
        return hashlist[-3:]
    
    def _encryptdata(self, data):
        "Encrypt data using AES algorithm, data is encrypted for every hash."
        for hash in self.hashlist:
            aes = AES.new(hash, AES.MODE_CFB)
            data = base64.b64encode(aes.encrypt(data))
        return data
        
    def _decryptdata(self, data):
        "decrypt data using AES algorithm"
        hashReverse = list(self.hashlist) # we need to create new list to be reversed
                                            # this list must not be same object as original list
        hashReverse.reverse() # finally we reverse list
        
        for hash in hashReverse:
            aes = AES.new(hash, AES.MODE_CFB)
            try:
                data = aes.decrypt(base64.b64decode(data))
            except TypeError:
                raise WrongPassException
        return data
    
    def encryptFile(self):
        with open(self.filepath, "rb") as fileObj:
            data = fileObj.read()
        
        crypted = self._encryptdata(data)
        
        with open(self.newFile, "wb") as fileObj:
            fileObj.write(crypted)
            
        if self.tar:
            os.remove(self.filepath)
        
    def decryptFile(self):
        with open(self.filepath, "rb") as fileObj:
            data = fileObj.read()
        
        decrypted = self._decryptdata(data)
        
        with open(self.oldFile, "wb") as fileObj:
            fileObj.write(decrypted)
            
        if self.fileIsTar:
            self.untar(self.oldFile)
            os.remove(self.oldFile)
            
    def tarFolder(self, folder, tarpath):
        "tar folder"
        tarball = tarfile.open(tarpath, "w")
        tarball.add(folder)
        tarball.close()
    
    def untar(self, filename):
        tarball = tarfile.open(filename)
        tarball.extractall()
        tarball.close()
