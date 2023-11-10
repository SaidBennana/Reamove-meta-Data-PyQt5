import sys
from PIL import Image
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import glob
import os,fnmatch

AllImages=[]

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("UI_App.ui",self)
        self.handle_Button()
        self.lineEdit_2.hide()
        self.SelectFolderBtn.hide()
        self.SelectFolder.hide()
    
    def handle_Button(self):
        self.GetFolderImages.clicked.connect(self._GetFolderImages)
        self.SelectFolderBtn.clicked.connect(self._Select_Browse_Save)
        self.SelectFolder.toggled.connect(self.SelectFolder_ChackBox)
        self.StartButton.clicked.connect(self.RemoveMetaDataFromImages)
        self.actionExit.triggered.connect(Exit)



    def _GetFolderImages(self):
        loctition=QFileDialog.getExistingDirectory()
        self.lineEdit.setText(loctition)
        Get_Images(loctition,["*.jpg","*.png",'*.JPEG'])
        self.AllImages.setText(f"All Images  : {len(AllImages)}")
        self.label_2.setText(f"Image Done  : 0/{len(AllImages)}")


    def SelectFolder_ChackBox(self,valueBool):
        if valueBool:
            self.lineEdit_2.show()
            self.SelectFolderBtn.show()
        else:
            self.lineEdit_2.hide()
            self.SelectFolderBtn.hide()


    def _Select_Browse_Save(self):
        loctition=QFileDialog.getExistingDirectory()
        self.lineEdit_2.setText(loctition)

    def RemoveMetaDataFromImages(self):
        images_Value_Done = 0
        for img in AllImages:
            image=Image.open(img)

            imageFormat=image.format
            imageName=img
            # print(imageName.split(self.lineEdit.text())[1])

            data=list(image.getdata())
            with_Out_data=Image.new(image.mode,image.size)
            with_Out_data.putdata(data)

            if self.SelectFolder.isChecked():
                ImageName=imageName.split(self.lineEdit.text())[1]
                try:
                    with_Out_data.save(self.lineEdit_2.text() + ImageName)
                    print(self.lineEdit_2.text() + ImageName)
                except Exception:
                    print("Error")
                    self._Select_Browse_Save()
            else :
                with_Out_data.save(img)

            images_Value_Done += 1
            self.label_2.setText(f"Image Done  : {images_Value_Done}/{len(AllImages)}")
            QApplication.processEvents()
            with_Out_data.close()

        QMessageBox.about(self,"Remove Complite", " Remove Meta Data is Complite")
        self.label_2.setText("0")
        self.AllImages.setText("0")
        self.lineEdit.setText("")







def Get_Images(Path,pattrein):
    for root,dirs,files in os.walk(Path):
        for name in files:
            if fnmatch.fnmatch(name,pattrein[0]):
                AllImages.append(os.path.join(root, name))
            if fnmatch.fnmatch(name,pattrein[1]):
                AllImages.append(os.path.join(root, name))
            if fnmatch.fnmatch(name,pattrein[2]):
                AllImages.append(os.path.join(root, name))


def Exit():
    exit()

def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_()
if __name__ == "__main__":
    main()


