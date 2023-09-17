from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QFileDialog
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from GradesQtGui import Ui_GradeCalculator


class Ui_MainWindow:
    def __init__(self):
        self.Widget = QWidget()
        self.ui = Ui_GradeCalculator()
        self.ui.setupUi(self.Widget)

        self.setupUi()

        self.Widget.show()

    def setupUi(self):
        # Initialize the weight and grade arrays
        self.weightArr = [0]
        self.gradeArr = [0]

        self.wList = [self.ui.w1, self.ui.w2, self.ui.w3,
                      self.ui.w4, self.ui.w5, self.ui.w6,
                      self.ui.w7, self.ui.w8, self.ui.w9, self.ui.w10]
        self.gList = [self.ui.g1, self.ui.g2, self.ui.g3,
                      self.ui.g4, self.ui.g5, self.ui.g6,
                      self.ui.g7, self.ui.g8, self.ui.g9, self.ui.g10]
        self.sList = [self.ui.s1, self.ui.s2, self.ui.s3,
                      self.ui.s4, self.ui.s5, self.ui.s6,
                      self.ui.s7, self.ui.s8, self.ui.s9, self.ui.s10]

        # Connect the buttons to their functions
        self.ui.w1.textChanged.connect(self.updateGrade)
        self.ui.w2.textChanged.connect(self.updateGrade)
        self.ui.w3.textChanged.connect(self.updateGrade)
        self.ui.w4.textChanged.connect(self.updateGrade)
        self.ui.w5.textChanged.connect(self.updateGrade)
        self.ui.w6.textChanged.connect(self.updateGrade)
        self.ui.w7.textChanged.connect(self.updateGrade)
        self.ui.w8.textChanged.connect(self.updateGrade)
        self.ui.w9.textChanged.connect(self.updateGrade)
        self.ui.w10.textChanged.connect(self.updateGrade)

        self.ui.g1.textChanged.connect(self.updateGrade)
        self.ui.g2.textChanged.connect(self.updateGrade)
        self.ui.g3.textChanged.connect(self.updateGrade)
        self.ui.g4.textChanged.connect(self.updateGrade)
        self.ui.g5.textChanged.connect(self.updateGrade)
        self.ui.g6.textChanged.connect(self.updateGrade)
        self.ui.g7.textChanged.connect(self.updateGrade)
        self.ui.g8.textChanged.connect(self.updateGrade)
        self.ui.g9.textChanged.connect(self.updateGrade)
        self.ui.g10.textChanged.connect(self.updateGrade)

        # Connect the save & clear buttons to their functions
        self.ui.saveButton.clicked.connect(self.saveToFile)
        self.ui.clearButton.clicked.connect(self.clearAll)
        self.ui.detailsButton.clicked.connect(self.openDetails)

        # Set the alignment of the final percentage & letter grade to center right
        self.ui.finalPerc.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.ui.finalLetter.setAlignment(Qt.AlignmentFlag.AlignRight)

    def gradeComputing(self, weightLst, gradeLst):
        sList = []
        for i in range(len(weightLst)):
            weight = float(weightLst[i] / 100)
            grade = float(gradeLst[i] / 100)
            score = round(weight * grade, 4)
            sList.append(score)
        sumScore = sum(sList)
        return sumScore * 100

    def updateGrade(self):
        """
        Update the weight and grade arrays, only if the user has entered a value
        """
        wList = self.wList.copy()
        gList = self.gList.copy()

        for lst in [wList, gList]:
            for i in reversed(range(len(lst))):
                currText = lst[i].text()
                if currText == '' or currText == '0':
                    lst[i] = 0
                else:
                    try:
                        lst[i] = float(currText)
                    except ValueError:
                        # Set the ui text so there isn't a non-numeric character
                        lst[i] = lst[i].setText(currText[:-1])
                        return

        self.ui.sumWeight.setText(f"{str(sum(wList))}%")

        # Update the final percentage & letter grade
        if sum(wList) == 100:
            # Color the sumWeight green if it is 100
            self.ui.sumWeight.setStyleSheet("color: rgb(150, 255, 150);")

            fGrade = self.gradeComputing(wList, gList)
            fGrade = round(fGrade, 2)
            self.ui.finalPerc.setText(f"{str(fGrade)}%")
            self.updateLetter()
        else:
            # Color the sumWeight red if it is not 100
            self.ui.sumWeight.setStyleSheet("color: rgb(255, 150, 150);")

    def updateLetter(self):
        """
        Update the letter grade based on the final percentage & UFV grading scale
        """
        fGrade = float(self.ui.finalPerc.text()[:-1])
        if fGrade > 100:
            self.ui.finalLetter.setText("LMAO")
        elif fGrade >= 90:
            self.ui.finalLetter.setText("A+")
        elif fGrade >= 85:
            self.ui.finalLetter.setText("A")
        elif fGrade >= 80:
            self.ui.finalLetter.setText("A-")
        elif fGrade >= 77:
            self.ui.finalLetter.setText("B+")
        elif fGrade >= 73:
            self.ui.finalLetter.setText("B")
        elif fGrade >= 70:
            self.ui.finalLetter.setText("B-")
        elif fGrade >= 67:
            self.ui.finalLetter.setText("C+")
        elif fGrade >= 63:
            self.ui.finalLetter.setText("C")
        elif fGrade >= 60:
            self.ui.finalLetter.setText("C-")
        elif fGrade >= 50:
            self.ui.finalLetter.setText("D")
        elif 0 <= fGrade < 50:
            self.ui.finalLetter.setText("F")
        else:
            self.ui.finalLetter.setText("")

    def saveToFile(self):
        """
        Save the current window as an image
        """
        map = QPixmap(QSize(1000, 700))
        self.Widget.render(map)
        # Open save directory
        fileName = QFileDialog.getSaveFileName(self.Widget, "Save Image", "",
                                               "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*)")

        map.save(fileName[0])

    def clearAll(self):
        if self.wList is None and self.gList is None:
            return
        for lst in [self.wList, self.gList]:
            for i in range(len(lst)):
                lst[i].setText('')
        self.ui.finalPerc.setText("%")
        self.ui.finalLetter.setText("")

        self.sList = [self.ui.s1, self.ui.s2, self.ui.s3,
                      self.ui.s4, self.ui.s5, self.ui.s6,
                      self.ui.s7, self.ui.s8, self.ui.s9, self.ui.s10]
        for section in self.sList:
            section.setText("")

    def openDetails(self):
        """
        Open the details window
        """
        wList = self.wList.copy()
        gList = self.gList.copy()
        sList = self.sList.copy()

        secStrings = []

        for i in reversed(range(len(wList))):
            currText = wList[i].text()
            if currText == '' or currText == '0':
                continue
            currString = f"Section Name: {sList[i].text()}      \n" \
                         f"Weight: {wList[i].text()}%\n" \
                         f"Grade: {gList[i].text()}%\n" \
                         f"Contribution to Grade: " \
                         f"{round(float(wList[i].text()) * float(gList[i].text()) / 100, 2)}%\n\n"

            # Insert at the beginning of the list because loop was reversed
            secStrings.insert(0, currString)

        detailsString = ''.join(secStrings)

        self.details = QMessageBox()
        message = (f'\n{self.ui.courseName.text()}\n------------------------------------------   \n\n'
                   f'{detailsString}' \
                   f'------------------------------------------   \nFinal Percentage:\n{self.ui.finalPerc.text()}\n')

        if 'html' in self.ui.finalPerc.text():
            message = ('\nOnce you have entered all information, your final percentage along with the details of '
                       'each section of the course will appear here.')

        # Show the message in the window
        self.details.setWindowTitle("Details")
        # Change font to Montserrat Medium
        font = self.details.font()
        font.setFamily("Montserrat Medium")

        font.setPointSize(11)
        self.details.setFont(font)

        self.details.setText(message)
        self.details.show()
