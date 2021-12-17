from os import access
import dropbox

class transfer_Data:
    def __init__(self,acessToken):
        self.acessToken=acessToken
    def upload_file(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.acessToken)
        f = open(fileFrom,"rb")
        dbx.files_upload(f.read(),fileTo)

def mainFunction():
    accessToken = "sl.A-XISM9J-3jZDVA9T-1x6yfAr5s57UksiAotBSWKc51CAne_R5suT5JMaLCgCD1_6U30Y8F51Vd3EPJwAPB8YXexfHM7PsH2izWhgejBa59PD7TU97rCh0BmVDaQIOCmcXmhzjs"
    TransferData = transfer_Data(accessToken)
    fileFrom = input("Enter File To Transfer : ")
    fileTo = input("Enter Destination of The File : ")
    TransferData.upload_file(fileFrom,fileTo)
    print("File Has Been Moved Sucessfully")
    
mainFunction()
