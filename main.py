from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QFont, QIcon
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve, QEvent, QPoint  # Added QPoint here
import sys
import os

# Global variables for rounded square label properties
ROUNDED_LABEL_WIDTH = 850
ROUNDED_LABEL_HEIGHT = 150
ROUNDED_LABEL_COLOR = "rgba(174, 208, 194, 0.24)"
ROUNDED_LABEL_POS_X = ((1665 - 850) // 2) + 10  # Center horizontally with offset
ROUNDED_LABEL_POS_Y = 45

# Global variables for cloud image size in KIKD window
CLOUD_IMAGE_WIDTH = 1350
CLOUD_IMAGE_HEIGHT = 1350

# Global variables for rounded square label properties
ROUNDED_LABEL_WIDTH = 850
ROUNDED_LABEL_HEIGHT = 150
ROUNDED_LABEL_COLOR = "rgba(174, 208, 194, 0.24)"
ROUNDED_LABEL_POS_X = ((1665 - 850) // 2) + 10  # Center horizontally with offset
ROUNDED_LABEL_POS_Y = 45

# Global variables for cloud image size in KIKD window
CLOUD_IMAGE_WIDTH = 1350
CLOUD_IMAGE_HEIGHT = 1350


class MaterialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Materi")
        self.resize(1665, 780)
        image_path = os.path.join(os.path.dirname(__file__), "assets", "mainBackground.png")
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Error: Failed to load image at {image_path}")
        else:
            self.pixmap = self.pixmap.scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Main title label with global properties and centered text
        self.title_label = QLabel("Materi", self)
        self.title_label.setFont(QFont("Cooper Black", 60))
        self.title_label.setStyleSheet(f"color: #333F50; background-color: {ROUNDED_LABEL_COLOR}; border: 3px solid black; border-radius: 10px;")
        self.title_label.setFixedWidth(ROUNDED_LABEL_WIDTH)
        self.title_label.setFixedHeight(ROUNDED_LABEL_HEIGHT)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.move(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT)  # Start off-screen top

        # Five buttons with icons from materiresource
        button_dir = os.path.join(os.path.dirname(__file__), "assets", "materiresource")
        button_paths = [
            os.path.join(button_dir, "ball.png"),
            os.path.join(button_dir, "block.png"),
            os.path.join(button_dir, "cone.png"),
            os.path.join(button_dir, "cube.png"),
            os.path.join(button_dir, "cylinder.png")
        ]
        buttonXOffset = 195
        buttonYOffset = 330
        buttonSpacing = 250
        buttonSize = 212
        labelYOffset = buttonYOffset + buttonSize + 10

        # Ball Button
        self.ballButton = QPushButton("", self)
        pixmap1 = QPixmap(button_paths[0])
        if pixmap1.isNull():
            print(f"Error: Failed to load image at {button_paths[0]}")
        else:
            pixmap1 = pixmap1.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ballButton.setIcon(QIcon(pixmap1))
            self.ballButton.setIconSize(QSize(buttonSize, buttonSize))
        self.ballButton.setFixedSize(buttonSize, buttonSize)
        self.ballButton.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.ballButton.move(buttonXOffset, -buttonSize)  # Start off-screen top
        self.ballButton.clicked.connect(self.on_ball_clicked)

        # Label for Ball Button
        self.ball_label = QLabel("Ball", self)
        self.ball_label.setFont(QFont("Cooper Black", 20))
        self.ball_label.setStyleSheet("color: #333F50; background: transparent;")
        self.ball_label.move(buttonXOffset + 20, -20)  # Start off-screen top
        self.ball_label.setFixedWidth(150)  # Ensure label stays with button

        # Block Button
        self.button2 = QPushButton("", self)
        pixmap2 = QPixmap(button_paths[1])
        if pixmap2.isNull():
            print(f"Error: Failed to load image at {button_paths[1]}")
        else:
            pixmap2 = pixmap2.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.button2.setIcon(QIcon(pixmap2))
            self.button2.setIconSize(QSize(buttonSize, buttonSize))
        self.button2.setFixedSize(buttonSize, buttonSize)
        self.button2.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.button2.move(buttonXOffset + buttonSpacing, -buttonSize)  # Start off-screen top
        self.button2.clicked.connect(self.on_button2_clicked)

        # Label for Block Button
        self.block_label = QLabel("Block", self)
        self.block_label.setFont(QFont("Cooper Black", 20))
        self.block_label.setStyleSheet("color: #333F50; background: transparent;")
        self.block_label.move(buttonXOffset + buttonSpacing + 20, -20)  # Start off-screen top
        self.block_label.setFixedWidth(150)  # Ensure label stays with button

        # Cone Button
        self.button3 = QPushButton("", self)
        pixmap3 = QPixmap(button_paths[2])
        if pixmap3.isNull():
            print(f"Error: Failed to load image at {button_paths[2]}")
        else:
            pixmap3 = pixmap3.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.button3.setIcon(QIcon(pixmap3))
            self.button3.setIconSize(QSize(buttonSize, buttonSize))
        self.button3.setFixedSize(buttonSize, buttonSize)
        self.button3.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.button3.move(buttonXOffset + 2 * buttonSpacing, -buttonSize)  # Start off-screen top
        self.button3.clicked.connect(self.on_button3_clicked)

        # Label for Cone Button
        self.cone_label = QLabel("Cone", self)
        self.cone_label.setFont(QFont("Cooper Black", 20))
        self.cone_label.setStyleSheet("color: #333F50; background: transparent;")
        self.cone_label.move(buttonXOffset + 2 * buttonSpacing + 20, -20)  # Start off-screen top
        self.cone_label.setFixedWidth(150)  # Ensure label stays with button

        # Cube Button
        self.button4 = QPushButton("", self)
        pixmap4 = QPixmap(button_paths[3])
        if pixmap4.isNull():
            print(f"Error: Failed to load image at {button_paths[3]}")
        else:
            pixmap4 = pixmap4.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.button4.setIcon(QIcon(pixmap4))
            self.button4.setIconSize(QSize(buttonSize, buttonSize))
        self.button4.setFixedSize(buttonSize, buttonSize)
        self.button4.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.button4.move(buttonXOffset + 3 * buttonSpacing, -buttonSize)  # Start off-screen top
        self.button4.clicked.connect(self.on_button4_clicked)

        # Label for Cube Button
        self.cube_label = QLabel("Cube", self)
        self.cube_label.setFont(QFont("Cooper Black", 20))
        self.cube_label.setStyleSheet("color: #333F50; background: transparent;")
        self.cube_label.move(buttonXOffset + 3 * buttonSpacing + 20, -20)  # Start off-screen top
        self.cube_label.setFixedWidth(150)  # Ensure label stays with button

        # Cylinder Button
        self.button5 = QPushButton("", self)
        pixmap5 = QPixmap(button_paths[4])
        if pixmap5.isNull():
            print(f"Error: Failed to load image at {button_paths[4]}")
        else:
            pixmap5 = pixmap5.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.button5.setIcon(QIcon(pixmap5))
            self.button5.setIconSize(QSize(buttonSize, buttonSize))
        self.button5.setFixedSize(buttonSize, buttonSize)
        self.button5.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.button5.move(buttonXOffset + 4 * buttonSpacing, -buttonSize)  # Start off-screen top
        self.button5.clicked.connect(self.on_button5_clicked)

        # Label for Cylinder Button
        self.cylinder_label = QLabel("Cylinder", self)
        self.cylinder_label.setFont(QFont("Cooper Black", 20))
        self.cylinder_label.setStyleSheet("color: #333F50; background: transparent;")
        self.cylinder_label.move(buttonXOffset + 4 * buttonSpacing + 20, -20)  # Start off-screen top
        self.cylinder_label.setFixedWidth(150)  # Ensure label stays with button

        # Animation setup for all elements
        self.title_anim = QPropertyAnimation(self.title_label, b"pos")
        self.title_anim.setDuration(500)
        self.title_anim.setStartValue(QPoint(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT))
        self.title_anim.setEndValue(QPoint(ROUNDED_LABEL_POS_X, ROUNDED_LABEL_POS_Y))
        self.title_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.ballButton_anim = QPropertyAnimation(self.ballButton, b"pos")
        self.ballButton_anim.setDuration(500)
        self.ballButton_anim.setStartValue(QPoint(buttonXOffset, -buttonSize))
        self.ballButton_anim.setEndValue(QPoint(buttonXOffset, buttonYOffset))
        self.ballButton_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.ballLabel_anim = QPropertyAnimation(self.ball_label, b"pos")
        self.ballLabel_anim.setDuration(500)
        self.ballLabel_anim.setStartValue(QPoint(buttonXOffset + 20, -20))
        self.ballLabel_anim.setEndValue(QPoint(buttonXOffset + 20, labelYOffset))
        self.ballLabel_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.blockButton_anim = QPropertyAnimation(self.button2, b"pos")
        self.blockButton_anim.setDuration(500)
        self.blockButton_anim.setStartValue(QPoint(buttonXOffset + buttonSpacing, -buttonSize))
        self.blockButton_anim.setEndValue(QPoint(buttonXOffset + buttonSpacing, buttonYOffset))
        self.blockButton_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.blockLabel_anim = QPropertyAnimation(self.block_label, b"pos")
        self.blockLabel_anim.setDuration(500)
        self.blockLabel_anim.setStartValue(QPoint(buttonXOffset + buttonSpacing + 20, -20))
        self.blockLabel_anim.setEndValue(QPoint(buttonXOffset + buttonSpacing + 20, labelYOffset))
        self.blockLabel_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.coneButton_anim = QPropertyAnimation(self.button3, b"pos")
        self.coneButton_anim.setDuration(500)
        self.coneButton_anim.setStartValue(QPoint(buttonXOffset + 2 * buttonSpacing, -buttonSize))
        self.coneButton_anim.setEndValue(QPoint(buttonXOffset + 2 * buttonSpacing, buttonYOffset))
        self.coneButton_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.coneLabel_anim = QPropertyAnimation(self.cone_label, b"pos")
        self.coneLabel_anim.setDuration(500)
        self.coneLabel_anim.setStartValue(QPoint(buttonXOffset + 2 * buttonSpacing + 20, -20))
        self.coneLabel_anim.setEndValue(QPoint(buttonXOffset + 2 * buttonSpacing + 20, labelYOffset))
        self.coneLabel_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.cubeButton_anim = QPropertyAnimation(self.button4, b"pos")
        self.cubeButton_anim.setDuration(500)
        self.cubeButton_anim.setStartValue(QPoint(buttonXOffset + 3 * buttonSpacing, -buttonSize))
        self.cubeButton_anim.setEndValue(QPoint(buttonXOffset + 3 * buttonSpacing, buttonYOffset))
        self.cubeButton_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.cubeLabel_anim = QPropertyAnimation(self.cube_label, b"pos")
        self.cubeLabel_anim.setDuration(500)
        self.cubeLabel_anim.setStartValue(QPoint(buttonXOffset + 3 * buttonSpacing + 20, -20))
        self.cubeLabel_anim.setEndValue(QPoint(buttonXOffset + 3 * buttonSpacing + 20, labelYOffset))
        self.cubeLabel_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.cylinderButton_anim = QPropertyAnimation(self.button5, b"pos")
        self.cylinderButton_anim.setDuration(500)
        self.cylinderButton_anim.setStartValue(QPoint(buttonXOffset + 4 * buttonSpacing, -buttonSize))
        self.cylinderButton_anim.setEndValue(QPoint(buttonXOffset + 4 * buttonSpacing, buttonYOffset))
        self.cylinderButton_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.cylinderLabel_anim = QPropertyAnimation(self.cylinder_label, b"pos")
        self.cylinderLabel_anim.setDuration(500)
        self.cylinderLabel_anim.setStartValue(QPoint(buttonXOffset + 4 * buttonSpacing + 20, -20))
        self.cylinderLabel_anim.setEndValue(QPoint(buttonXOffset + 4 * buttonSpacing + 20, labelYOffset))
        self.cylinderLabel_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def on_ball_clicked(self):
        print("Ball button clicked!")
        self.ball_window = BallWindow()
        self.ball_window.show()
        self.close()

    def on_button2_clicked(self):
        print("Block button clicked!")
        self.block_window = BlockWindow()
        self.block_window.show()
        self.close()

    def on_button3_clicked(self):
        print("Cone button clicked!")
        self.cone_window = ConeWindow()
        self.cone_window.show()
        self.close()

    def on_button4_clicked(self):
        print("Cube button clicked!")
        self.cube_window = CubeWindow()
        self.cube_window.show()
        self.close()

    def on_button5_clicked(self):
        print("Cylinder button clicked!")
        self.cylinder_window = CylinderWindow()
        self.cylinder_window.show()
        self.close()

    def showEvent(self, event):
        super().showEvent(event)
        self.title_anim.start()
        self.ballButton_anim.start()
        self.ballLabel_anim.start()
        self.blockButton_anim.start()
        self.blockLabel_anim.start()
        self.coneButton_anim.start()
        self.coneLabel_anim.start()
        self.cubeButton_anim.start()
        self.cubeLabel_anim.start()
        self.cylinderButton_anim.start()
        self.cylinderLabel_anim.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        x = (self.width() - self.pixmap.width()) // 2
        y = (self.height() - self.pixmap.height()) // 2
        painter.drawPixmap(x, y, self.pixmap)

class CylinderWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cylinder")
        self.resize(1665, 780)
        image_path = os.path.join(os.path.dirname(__file__), "assets", "mainBackground.png")
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Error: Failed to load image at {image_path}")
        else:
            self.pixmap = self.pixmap.scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Main title label with global properties and centered text
        self.title_label = QLabel("Cylinder", self)
        self.title_label.setFont(QFont("Cooper Black", 60))
        self.title_label.setStyleSheet(f"color: #333F50; background-color: {ROUNDED_LABEL_COLOR}; border: 3px solid black; border-radius: 10px;")
        self.title_label.setFixedWidth(ROUNDED_LABEL_WIDTH)
        self.title_label.setFixedHeight(ROUNDED_LABEL_HEIGHT)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.move(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT)  # Start off-screen top

        # Text label explaining the cylinder
        self.text_label = QLabel("Tabung adalah bangun ruang tiga dimensi yang dibentuk oleh dua buah lingkaran identik yang sejajar dan sebuah persegi panjang yang mengelilingi kedua lingkaran tersebut. Tabung memiliki 3 sisi dan 2 rusuk. Kedua lingkaran disebut sebagai alas dan tutup tabung serta persegi panjang yang menyelimutinya disebut sebagai selimut tabung.", self)
        self.text_label.setFont(QFont("Corbel", 11))
        self.text_label.setStyleSheet("color: #333F50; background: transparent; padding: 10px;")
        self.text_label.setWordWrap(True)
        self.text_label.setFixedWidth(500)
        self.text_label.move(-500, 325)  # Start off-screen left

        # "CONTOH" label above the images
        self.contoh_label = QLabel("CONTOH", self)
        self.contoh_label.setFont(QFont("Cooper Black", 20))
        self.contoh_label.setStyleSheet("color: #333F50; background: transparent;")
        self.contoh_label.move(750, -50)  # Start off-screen top

        # Three images from materiresource/cylinderslide
        self.image1_label = QLabel(self)
        self.image2_label = QLabel(self)
        self.image3_label = QLabel(self)
        ballslide_dir = os.path.join(os.path.dirname(__file__), "assets", "materiresource", "cylinderslide")
        image_paths = [
            os.path.join(ballslide_dir, "batteryCylinder.png"),
            os.path.join(ballslide_dir, "biscuitCylinder.png"),
            os.path.join(ballslide_dir, "sodaCanCylinder.png")
        ]
        image_size = 180

        # Image 1 (batteryCylinder.png)
        pixmap1 = QPixmap(image_paths[0])
        if pixmap1.isNull():
            print(f"Error: Failed to load image at {image_paths[0]}")
        else:
            pixmap1 = pixmap1.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image1_label.setPixmap(pixmap1)
        self.image1_label.setFixedSize(image_size, image_size)
        self.image1_label.move(-image_size, 305)  # Start off-screen left

        # Image 2 (biscuitCylinder.png)
        pixmap2 = QPixmap(image_paths[1])
        if pixmap2.isNull():
            print(f"Error: Failed to load image at {image_paths[1]}")
        else:
            pixmap2 = pixmap2.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image2_label.setPixmap(pixmap2)
        self.image2_label.setFixedSize(image_size, image_size)
        self.image2_label.move(977, -image_size)  # Start off-screen top

        # Image 3 (sodaCanCylinder.png)
        pixmap3 = QPixmap(image_paths[2])
        if pixmap3.isNull():
            print(f"Error: Failed to load image at {image_paths[2]}")
        else:
            pixmap3 = pixmap3.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image3_label.setPixmap(pixmap3)
        self.image3_label.setFixedSize(image_size, image_size)
        self.image3_label.move(1665 + image_size, 302)  # Start off-screen right

        # CloudBackground (nontransparentCloud.png)
        self.image4_label = QLabel(self)
        pixmap4 = QPixmap(os.path.join(os.path.dirname(__file__), "assets", "materiresource", "nontransparentCloud.png"))
        if pixmap4.isNull():
            print(f"Error: Failed to load image at {os.path.join(os.path.dirname(__file__), 'assets', 'materiresource', 'nontransparentCloud.png')}")
        else:
            pixmap4 = pixmap4.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image4_label.setPixmap(pixmap4)
        self.image4_label.setFixedSize(600, 600)
        self.image4_label.move(-600, 150)  # Start off-screen left
        self.image4_label.lower()

        # Animation setup for all elements
        self.title_anim = QPropertyAnimation(self.title_label, b"pos")
        self.title_anim.setDuration(500)
        self.title_anim.setStartValue(QPoint(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT))
        self.title_anim.setEndValue(QPoint(ROUNDED_LABEL_POS_X, ROUNDED_LABEL_POS_Y))
        self.title_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.text_anim = QPropertyAnimation(self.text_label, b"pos")
        self.text_anim.setDuration(500)
        self.text_anim.setStartValue(QPoint(-500, 325))
        self.text_anim.setEndValue(QPoint(150, 325))
        self.text_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.contoh_anim = QPropertyAnimation(self.contoh_label, b"pos")
        self.contoh_anim.setDuration(500)
        self.contoh_anim.setStartValue(QPoint(750, -50))
        self.contoh_anim.setEndValue(QPoint(750, 230))
        self.contoh_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image1_anim = QPropertyAnimation(self.image1_label, b"pos")
        self.image1_anim.setDuration(500)
        self.image1_anim.setStartValue(QPoint(-image_size, 305))
        self.image1_anim.setEndValue(QPoint(750, 305))
        self.image1_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image2_anim = QPropertyAnimation(self.image2_label, b"pos")
        self.image2_anim.setDuration(500)
        self.image2_anim.setStartValue(QPoint(977, -image_size))
        self.image2_anim.setEndValue(QPoint(977, 298))
        self.image2_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image3_anim = QPropertyAnimation(self.image3_label, b"pos")
        self.image3_anim.setDuration(500)
        self.image3_anim.setStartValue(QPoint(1665 + image_size, 302))
        self.image3_anim.setEndValue(QPoint(1190, 302))
        self.image3_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image4_anim = QPropertyAnimation(self.image4_label, b"pos")
        self.image4_anim.setDuration(500)
        self.image4_anim.setStartValue(QPoint(-600, 150))
        self.image4_anim.setEndValue(QPoint(90, 150))
        self.image4_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def showEvent(self, event):
        super().showEvent(event)
        self.title_anim.start()
        self.text_anim.start()
        self.contoh_anim.start()
        self.image1_anim.start()
        self.image2_anim.start()
        self.image3_anim.start()
        self.image4_anim.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        x = (self.width() - self.pixmap.width()) // 2
        y = (self.height() - self.pixmap.height()) // 2
        painter.drawPixmap(x, y, self.pixmap)

class ConeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cone")
        self.resize(1665, 780)
        image_path = os.path.join(os.path.dirname(__file__), "assets", "mainBackground.png")
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Error: Failed to load image at {image_path}")
        else:
            self.pixmap = self.pixmap.scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Main title label with global properties and centered text
        self.title_label = QLabel("Cone", self)
        self.title_label.setFont(QFont("Cooper Black", 60))
        self.title_label.setStyleSheet(f"color: #333F50; background-color: {ROUNDED_LABEL_COLOR}; border: 3px solid black; border-radius: 10px;")
        self.title_label.setFixedWidth(ROUNDED_LABEL_WIDTH)
        self.title_label.setFixedHeight(ROUNDED_LABEL_HEIGHT)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.move(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT)  # Start off-screen top

        # Text label explaining the cone
        self.text_label = QLabel("Kerucut adalah sebuah limas istimewa yang beralas lingkaran. Kerucut memiliki 2 sisi dan 1 rusuk. Sisi tegak kerucut tidak berupa segitiga tapi berupa bidang miring yang disebut selimut kerucut.", self)
        self.text_label.setFont(QFont("Corbel", 15))
        self.text_label.setStyleSheet("color: #333F50; background: transparent; padding: 10px;")
        self.text_label.setWordWrap(True)
        self.text_label.setFixedWidth(500)
        self.text_label.move(-500, 325)  # Start off-screen left

        # "CONTOH" label above the images
        self.contoh_label = QLabel("CONTOH", self)
        self.contoh_label.setFont(QFont("Cooper Black", 20))
        self.contoh_label.setStyleSheet("color: #333F50; background: transparent;")
        self.contoh_label.move(750, -50)  # Start off-screen top

        # Three images from materiresource/coneslide
        self.image1_label = QLabel(self)
        self.image2_label = QLabel(self)
        self.image3_label = QLabel(self)
        ballslide_dir = os.path.join(os.path.dirname(__file__), "assets", "materiresource", "coneslide")
        image_paths = [
            os.path.join(ballslide_dir, "carrotCone.png"),
            os.path.join(ballslide_dir, "partyHatCone.png"),
            os.path.join(ballslide_dir, "umbrellaCone.png")
        ]
        image_size = 180

        # Image 1 (carrotCone.png)
        pixmap1 = QPixmap(image_paths[0])
        if pixmap1.isNull():
            print(f"Error: Failed to load image at {image_paths[0]}")
        else:
            pixmap1 = pixmap1.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image1_label.setPixmap(pixmap1)
        self.image1_label.setFixedSize(image_size, image_size)
        self.image1_label.move(-image_size, 305)  # Start off-screen left

        # Image 2 (partyHatCone.png)
        pixmap2 = QPixmap(image_paths[1])
        if pixmap2.isNull():
            print(f"Error: Failed to load image at {image_paths[1]}")
        else:
            pixmap2 = pixmap2.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image2_label.setPixmap(pixmap2)
        self.image2_label.setFixedSize(image_size, image_size)
        self.image2_label.move(907, -image_size)  # Start off-screen top

        # Image 3 (umbrellaCone.png)
        pixmap3 = QPixmap(image_paths[2])
        if pixmap3.isNull():
            print(f"Error: Failed to load image at {image_paths[2]}")
        else:
            pixmap3 = pixmap3.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image3_label.setPixmap(pixmap3)
        self.image3_label.setFixedSize(image_size, image_size)
        self.image3_label.move(1665 + image_size, 302)  # Start off-screen right

        # CloudBackground (nontransparentCloud.png)
        self.image4_label = QLabel(self)
        pixmap4 = QPixmap(os.path.join(os.path.dirname(__file__), "assets", "materiresource", "nontransparentCloud.png"))
        if pixmap4.isNull():
            print(f"Error: Failed to load image at {os.path.join(os.path.dirname(__file__), 'assets', 'materiresource', 'nontransparentCloud.png')}")
        else:
            pixmap4 = pixmap4.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image4_label.setPixmap(pixmap4)
        self.image4_label.setFixedSize(600, 600)
        self.image4_label.move(-600, 150)  # Start off-screen left
        self.image4_label.lower()

        # Animation setup for all elements
        self.title_anim = QPropertyAnimation(self.title_label, b"pos")
        self.title_anim.setDuration(500)
        self.title_anim.setStartValue(QPoint(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT))
        self.title_anim.setEndValue(QPoint(ROUNDED_LABEL_POS_X, ROUNDED_LABEL_POS_Y))
        self.title_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.text_anim = QPropertyAnimation(self.text_label, b"pos")
        self.text_anim.setDuration(500)
        self.text_anim.setStartValue(QPoint(-500, 325))
        self.text_anim.setEndValue(QPoint(150, 325))
        self.text_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.contoh_anim = QPropertyAnimation(self.contoh_label, b"pos")
        self.contoh_anim.setDuration(500)
        self.contoh_anim.setStartValue(QPoint(750, -50))
        self.contoh_anim.setEndValue(QPoint(750, 230))
        self.contoh_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image1_anim = QPropertyAnimation(self.image1_label, b"pos")
        self.image1_anim.setDuration(500)
        self.image1_anim.setStartValue(QPoint(-image_size, 305))
        self.image1_anim.setEndValue(QPoint(750, 305))
        self.image1_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image2_anim = QPropertyAnimation(self.image2_label, b"pos")
        self.image2_anim.setDuration(500)
        self.image2_anim.setStartValue(QPoint(907, -image_size))
        self.image2_anim.setEndValue(QPoint(907, 298))
        self.image2_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image3_anim = QPropertyAnimation(self.image3_label, b"pos")
        self.image3_anim.setDuration(500)
        self.image3_anim.setStartValue(QPoint(1665 + image_size, 302))
        self.image3_anim.setEndValue(QPoint(1050, 302))
        self.image3_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image4_anim = QPropertyAnimation(self.image4_label, b"pos")
        self.image4_anim.setDuration(500)
        self.image4_anim.setStartValue(QPoint(-600, 150))
        self.image4_anim.setEndValue(QPoint(90, 150))
        self.image4_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def showEvent(self, event):
        super().showEvent(event)
        self.title_anim.start()
        self.text_anim.start()
        self.contoh_anim.start()
        self.image1_anim.start()
        self.image2_anim.start()
        self.image3_anim.start()
        self.image4_anim.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        x = (self.width() - self.pixmap.width()) // 2
        y = (self.height() - self.pixmap.height()) // 2
        painter.drawPixmap(x, y, self.pixmap)

class BallWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ball")
        self.resize(1665, 780)
        image_path = os.path.join(os.path.dirname(__file__), "assets", "mainBackground.png")
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Error: Failed to load image at {image_path}")
        else:
            self.pixmap = self.pixmap.scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Main title label with global properties and centered text
        self.title_label = QLabel("Ball", self)
        self.title_label.setFont(QFont("Cooper Black", 60))
        self.title_label.setStyleSheet(f"color: #333F50; background-color: {ROUNDED_LABEL_COLOR}; border: 3px solid black; border-radius: 10px;")
        self.title_label.setFixedWidth(ROUNDED_LABEL_WIDTH)
        self.title_label.setFixedHeight(ROUNDED_LABEL_HEIGHT)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.move(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT)  # Start off-screen top

        # Text label explaining the ball
        self.text_label = QLabel("Bola adalah bangun ruang tiga dimensi yang dibentuk oleh tak hingga lingkaran berjari-jari sama panjang dan berpusat pada titik yang sama. Bola hanya memiliki 1 sisi.", self)
        self.text_label.setFont(QFont("Corbel", 15))
        self.text_label.setStyleSheet("color: #333F50; background: transparent; padding: 10px;")
        self.text_label.setWordWrap(True)
        self.text_label.setFixedWidth(500)
        self.text_label.move(-500, 345)  # Start off-screen left

        # "CONTOH" label above the images
        self.contoh_label = QLabel("CONTOH", self)
        self.contoh_label.setFont(QFont("Cooper Black", 20))
        self.contoh_label.setStyleSheet("color: #333F50; background: transparent;")
        self.contoh_label.move(750, -50)  # Start off-screen top

        # Three images from materiresource/ballslide
        self.image1_label = QLabel(self)
        self.image2_label = QLabel(self)
        self.image3_label = QLabel(self)
        ballslide_dir = os.path.join(os.path.dirname(__file__), "assets", "materiresource", "ballslide")
        image_paths = [
            os.path.join(ballslide_dir, "appleBall.png"),
            os.path.join(ballslide_dir, "soccerBall.png"),
            os.path.join(ballslide_dir, "watermelonBall.png")
        ]
        image_size = 180

        # Image 1 (appleBall.png)
        pixmap1 = QPixmap(image_paths[0])
        if pixmap1.isNull():
            print(f"Error: Failed to load image at {image_paths[0]}")
        else:
            pixmap1 = pixmap1.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image1_label.setPixmap(pixmap1)
        self.image1_label.setFixedSize(image_size, image_size)
        self.image1_label.move(-image_size, 305)  # Start off-screen left

        # Image 2 (soccerBall.png)
        pixmap2 = QPixmap(image_paths[1])
        if pixmap2.isNull():
            print(f"Error: Failed to load image at {image_paths[1]}")
        else:
            pixmap2 = pixmap2.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image2_label.setPixmap(pixmap2)
        self.image2_label.setFixedSize(image_size, image_size)
        self.image2_label.move(910, -image_size)  # Start off-screen top

        # Image 3 (watermelonBall.png)
        pixmap3 = QPixmap(image_paths[2])
        if pixmap3.isNull():
            print(f"Error: Failed to load image at {image_paths[2]}")
        else:
            pixmap3 = pixmap3.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image3_label.setPixmap(pixmap3)
        self.image3_label.setFixedSize(image_size, image_size)
        self.image3_label.move(1665 + image_size, 321)  # Start off-screen right

        # CloudBackground (nontransparentCloud.png)
        self.image4_label = QLabel(self)
        pixmap4 = QPixmap(os.path.join(os.path.dirname(__file__), "assets", "materiresource", "nontransparentCloud.png"))
        if pixmap4.isNull():
            print(f"Error: Failed to load image at {os.path.join(os.path.dirname(__file__), 'assets', 'materiresource', 'nontransparentCloud.png')}")
        else:
            pixmap4 = pixmap4.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image4_label.setPixmap(pixmap4)
        self.image4_label.setFixedSize(600, 600)
        self.image4_label.move(-600, 150)  # Start off-screen left
        self.image4_label.lower()

        # Animation setup for all elements
        self.title_anim = QPropertyAnimation(self.title_label, b"pos")
        self.title_anim.setDuration(500)
        self.title_anim.setStartValue(QPoint(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT))
        self.title_anim.setEndValue(QPoint(ROUNDED_LABEL_POS_X, ROUNDED_LABEL_POS_Y))
        self.title_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.text_anim = QPropertyAnimation(self.text_label, b"pos")
        self.text_anim.setDuration(500)
        self.text_anim.setStartValue(QPoint(-500, 345))
        self.text_anim.setEndValue(QPoint(150, 345))
        self.text_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.contoh_anim = QPropertyAnimation(self.contoh_label, b"pos")
        self.contoh_anim.setDuration(500)
        self.contoh_anim.setStartValue(QPoint(750, -50))
        self.contoh_anim.setEndValue(QPoint(750, 230))
        self.contoh_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image1_anim = QPropertyAnimation(self.image1_label, b"pos")
        self.image1_anim.setDuration(500)
        self.image1_anim.setStartValue(QPoint(-image_size, 305))
        self.image1_anim.setEndValue(QPoint(750, 305))
        self.image1_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image2_anim = QPropertyAnimation(self.image2_label, b"pos")
        self.image2_anim.setDuration(500)
        self.image2_anim.setStartValue(QPoint(910, -image_size))
        self.image2_anim.setEndValue(QPoint(910, 321))
        self.image2_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image3_anim = QPropertyAnimation(self.image3_label, b"pos")
        self.image3_anim.setDuration(500)
        self.image3_anim.setStartValue(QPoint(1665 + image_size, 321))
        self.image3_anim.setEndValue(QPoint(1110, 321))
        self.image3_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image4_anim = QPropertyAnimation(self.image4_label, b"pos")
        self.image4_anim.setDuration(500)
        self.image4_anim.setStartValue(QPoint(-600, 150))
        self.image4_anim.setEndValue(QPoint(90, 150))
        self.image4_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def showEvent(self, event):
        super().showEvent(event)
        self.title_anim.start()
        self.text_anim.start()
        self.contoh_anim.start()
        self.image1_anim.start()
        self.image2_anim.start()
        self.image3_anim.start()
        self.image4_anim.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        x = (self.width() - self.pixmap.width()) // 2
        y = (self.height() - self.pixmap.height()) // 2
        painter.drawPixmap(x, y, self.pixmap)

class BlockWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Block")
        self.resize(1665, 780)
        image_path = os.path.join(os.path.dirname(__file__), "assets", "mainBackground.png")
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Error: Failed to load image at {image_path}")
        else:
            self.pixmap = self.pixmap.scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Main title label with global properties and centered text
        self.title_label = QLabel("Block", self)
        self.title_label.setFont(QFont("Cooper Black", 60))
        self.title_label.setStyleSheet(f"color: #333F50; background-color: {ROUNDED_LABEL_COLOR}; border: 3px solid black; border-radius: 10px;")
        self.title_label.setFixedWidth(ROUNDED_LABEL_WIDTH)
        self.title_label.setFixedHeight(ROUNDED_LABEL_HEIGHT)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.move(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT)  # Start off-screen top

        # Text label explaining the block
        self.text_label = QLabel("Balok adalah bangun ruang tiga dimensi yang dibentuk oleh tiga pasang persegi atau persegi panjang, dengan paling tidak satu pasang di antaranya berukuran berbeda. Balok memiliki 6 sisi, 12 rusuk dan 8 titik sudut.", self)
        self.text_label.setFont(QFont("Corbel", 15))
        self.text_label.setStyleSheet("color: #333F50; background: transparent; padding: 10px;")
        self.text_label.setWordWrap(True)
        self.text_label.setFixedWidth(500)
        self.text_label.move(-500, 315)  # Start off-screen left

        # "CONTOH" label above the images
        self.contoh_label = QLabel("CONTOH", self)
        self.contoh_label.setFont(QFont("Cooper Black", 20))
        self.contoh_label.setStyleSheet("color: #333F50; background: transparent;")
        self.contoh_label.move(750, -50)  # Start off-screen top

        # Three images from materiresource/blockslide
        self.image1_label = QLabel(self)
        self.image2_label = QLabel(self)
        self.image3_label = QLabel(self)
        ballslide_dir = os.path.join(os.path.dirname(__file__), "assets", "materiresource", "blockslide")
        image_paths = [
            os.path.join(ballslide_dir, "aquariumBlock.png"),
            os.path.join(ballslide_dir, "closetBlock.png"),
            os.path.join(ballslide_dir, "outletBlock.png")
        ]
        image_size = 180

        # Image 1 (aquariumBlock.png)
        pixmap1 = QPixmap(image_paths[0])
        if pixmap1.isNull():
            print(f"Error: Failed to load image at {image_paths[0]}")
        else:
            pixmap1 = pixmap1.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image1_label.setPixmap(pixmap1)
        self.image1_label.setFixedSize(image_size, image_size)
        self.image1_label.move(-image_size, 305)  # Start off-screen left

        # Image 2 (closetBlock.png)
        pixmap2 = QPixmap(image_paths[1])
        if pixmap2.isNull():
            print(f"Error: Failed to load image at {image_paths[1]}")
        else:
            pixmap2 = pixmap2.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image2_label.setPixmap(pixmap2)
        self.image2_label.setFixedSize(image_size, image_size)
        self.image2_label.move(910, -image_size)  # Start off-screen top

        # Image 3 (outletBlock.png)
        pixmap3 = QPixmap(image_paths[2])
        if pixmap3.isNull():
            print(f"Error: Failed to load image at {image_paths[2]}")
        else:
            pixmap3 = pixmap3.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image3_label.setPixmap(pixmap3)
        self.image3_label.setFixedSize(image_size, image_size)
        self.image3_label.move(1665 + image_size, 321)  # Start off-screen right

        # CloudBackground (nontransparentCloud.png)
        self.image4_label = QLabel(self)
        pixmap4 = QPixmap(os.path.join(os.path.dirname(__file__), "assets", "materiresource", "nontransparentCloud.png"))
        if pixmap4.isNull():
            print(f"Error: Failed to load image at {os.path.join(os.path.dirname(__file__), 'assets', 'materiresource', 'nontransparentCloud.png')}")
        else:
            pixmap4 = pixmap4.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image4_label.setPixmap(pixmap4)
        self.image4_label.setFixedSize(600, 600)
        self.image4_label.move(-600, 150)  # Start off-screen left
        self.image4_label.lower()

        # Animation setup for all elements
        self.title_anim = QPropertyAnimation(self.title_label, b"pos")
        self.title_anim.setDuration(500)
        self.title_anim.setStartValue(QPoint(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT))
        self.title_anim.setEndValue(QPoint(ROUNDED_LABEL_POS_X, ROUNDED_LABEL_POS_Y))
        self.title_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.text_anim = QPropertyAnimation(self.text_label, b"pos")
        self.text_anim.setDuration(500)
        self.text_anim.setStartValue(QPoint(-500, 315))
        self.text_anim.setEndValue(QPoint(160, 315))
        self.text_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.contoh_anim = QPropertyAnimation(self.contoh_label, b"pos")
        self.contoh_anim.setDuration(500)
        self.contoh_anim.setStartValue(QPoint(750, -50))
        self.contoh_anim.setEndValue(QPoint(750, 230))
        self.contoh_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image1_anim = QPropertyAnimation(self.image1_label, b"pos")
        self.image1_anim.setDuration(500)
        self.image1_anim.setStartValue(QPoint(-image_size, 305))
        self.image1_anim.setEndValue(QPoint(750, 305))
        self.image1_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image2_anim = QPropertyAnimation(self.image2_label, b"pos")
        self.image2_anim.setDuration(500)
        self.image2_anim.setStartValue(QPoint(910, -image_size))
        self.image2_anim.setEndValue(QPoint(910, 321))
        self.image2_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image3_anim = QPropertyAnimation(self.image3_label, b"pos")
        self.image3_anim.setDuration(500)
        self.image3_anim.setStartValue(QPoint(1665 + image_size, 321))
        self.image3_anim.setEndValue(QPoint(1110, 321))
        self.image3_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image4_anim = QPropertyAnimation(self.image4_label, b"pos")
        self.image4_anim.setDuration(500)
        self.image4_anim.setStartValue(QPoint(-600, 150))
        self.image4_anim.setEndValue(QPoint(90, 150))
        self.image4_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def showEvent(self, event):
        super().showEvent(event)
        self.title_anim.start()
        self.text_anim.start()
        self.contoh_anim.start()
        self.image1_anim.start()
        self.image2_anim.start()
        self.image3_anim.start()
        self.image4_anim.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        x = (self.width() - self.pixmap.width()) // 2
        y = (self.height() - self.pixmap.height()) // 2
        painter.drawPixmap(x, y, self.pixmap)

class CubeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cube")
        self.resize(1665, 780)
        image_path = os.path.join(os.path.dirname(__file__), "assets", "mainBackground.png")
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Error: Failed to load image at {image_path}")
        else:
            self.pixmap = self.pixmap.scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Main title label with global properties and centered text
        self.title_label = QLabel("Cube", self)
        self.title_label.setFont(QFont("Cooper Black", 60))
        self.title_label.setStyleSheet(f"color: #333F50; background-color: {ROUNDED_LABEL_COLOR}; border: 3px solid black; border-radius: 10px;")
        self.title_label.setFixedWidth(ROUNDED_LABEL_WIDTH)
        self.title_label.setFixedHeight(ROUNDED_LABEL_HEIGHT)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.move(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT)  # Start off-screen top

        # Text label explaining the cube
        self.text_label = QLabel("Kubus adalah bangun ruang tiga dimensi yang dibatasi oleh enam bidang sisi yang kongruen berbentuk bujur sangkar. Kubus memiliki 6 sisi, 12 rusuk dan 8 titik sudut. Kubus juga disebut bidang enam beraturan, selain itu juga merupakan bentuk khusus dalam prisma segiempat.", self)
        self.text_label.setFont(QFont("Corbel", 12))
        self.text_label.setStyleSheet("color: #333F50; background: transparent; padding: 10px;")
        self.text_label.setWordWrap(True)
        self.text_label.setFixedWidth(500)
        self.text_label.move(-500, 325)  # Start off-screen left

        # "CONTOH" label above the images
        self.contoh_label = QLabel("CONTOH", self)
        self.contoh_label.setFont(QFont("Cooper Black", 20))
        self.contoh_label.setStyleSheet("color: #333F50; background: transparent;")
        self.contoh_label.move(750, -50)  # Start off-screen top

        # Three images from materiresource/cubeslide
        self.image1_label = QLabel(self)
        self.image2_label = QLabel(self)
        self.image3_label = QLabel(self)
        ballslide_dir = os.path.join(os.path.dirname(__file__), "assets", "materiresource", "cubeslide")
        image_paths = [
            os.path.join(ballslide_dir, "diceCube.png"),
            os.path.join(ballslide_dir, "giftCube.png"),
            os.path.join(ballslide_dir, "vaultCube.png")
        ]
        image_size = 180

        # Image 1 (diceCube.png)
        pixmap1 = QPixmap(image_paths[0])
        if pixmap1.isNull():
            print(f"Error: Failed to load image at {image_paths[0]}")
        else:
            pixmap1 = pixmap1.scaled(image_size, image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image1_label.setPixmap(pixmap1)
        self.image1_label.setFixedSize(image_size, image_size)
        self.image1_label.move(-image_size, 305)  # Start off-screen left

        # Image 2 (giftCube.png)
        pixmap2 = QPixmap(image_paths[1])
        if pixmap2.isNull():
            print(f"Error: Failed to load image at {image_paths[1]}")
        else:
            pixmap2 = pixmap2.scaled(image_size * 2, image_size * 2, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image2_label.setPixmap(pixmap2)
        self.image2_label.setFixedSize(image_size * 2, image_size * 2)
        self.image2_label.move(860, -image_size * 2)  # Start off-screen top (adjusted for larger size)

        # Image 3 (vaultCube.png)
        pixmap3 = QPixmap(image_paths[2])
        if pixmap3.isNull():
            print(f"Error: Failed to load image at {image_paths[2]}")
        else:
            pixmap3 = pixmap3.scaled(round(image_size * 1.3), round(image_size * 1.3), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image3_label.setPixmap(pixmap3)
        self.image3_label.setFixedSize(round(image_size * 1.3), round(image_size * 1.3))
        self.image3_label.move(1665 + round(image_size * 1.3), 271)  # Start off-screen right (adjusted for size)

        # CloudBackground (nontransparentCloud.png)
        self.image4_label = QLabel(self)
        pixmap4 = QPixmap(os.path.join(os.path.dirname(__file__), "assets", "materiresource", "nontransparentCloud.png"))
        if pixmap4.isNull():
            print(f"Error: Failed to load image at {os.path.join(os.path.dirname(__file__), 'assets', 'materiresource', 'nontransparentCloud.png')}")
        else:
            pixmap4 = pixmap4.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image4_label.setPixmap(pixmap4)
        self.image4_label.setFixedSize(600, 600)
        self.image4_label.move(-600, 150)  # Start off-screen left
        self.image4_label.lower()

        # Animation setup for all elements
        self.title_anim = QPropertyAnimation(self.title_label, b"pos")
        self.title_anim.setDuration(500)
        self.title_anim.setStartValue(QPoint(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT))
        self.title_anim.setEndValue(QPoint(ROUNDED_LABEL_POS_X, ROUNDED_LABEL_POS_Y))
        self.title_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.text_anim = QPropertyAnimation(self.text_label, b"pos")
        self.text_anim.setDuration(500)
        self.text_anim.setStartValue(QPoint(-500, 325))
        self.text_anim.setEndValue(QPoint(150, 325))
        self.text_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.contoh_anim = QPropertyAnimation(self.contoh_label, b"pos")
        self.contoh_anim.setDuration(500)
        self.contoh_anim.setStartValue(QPoint(750, -50))
        self.contoh_anim.setEndValue(QPoint(750, 230))
        self.contoh_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image1_anim = QPropertyAnimation(self.image1_label, b"pos")
        self.image1_anim.setDuration(500)
        self.image1_anim.setStartValue(QPoint(-image_size, 305))
        self.image1_anim.setEndValue(QPoint(750, 305))
        self.image1_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image2_anim = QPropertyAnimation(self.image2_label, b"pos")
        self.image2_anim.setDuration(500)
        self.image2_anim.setStartValue(QPoint(860, -image_size * 2))
        self.image2_anim.setEndValue(QPoint(860, 198))
        self.image2_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image3_anim = QPropertyAnimation(self.image3_label, b"pos")
        self.image3_anim.setDuration(500)
        self.image3_anim.setStartValue(QPoint(1665 + round(image_size * 1.3), 271))
        self.image3_anim.setEndValue(QPoint(1130, 271))
        self.image3_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.image4_anim = QPropertyAnimation(self.image4_label, b"pos")
        self.image4_anim.setDuration(500)
        self.image4_anim.setStartValue(QPoint(-600, 150))
        self.image4_anim.setEndValue(QPoint(90, 150))
        self.image4_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def showEvent(self, event):
        super().showEvent(event)
        self.title_anim.start()
        self.text_anim.start()
        self.contoh_anim.start()
        self.image1_anim.start()
        self.image2_anim.start()
        self.image3_anim.start()
        self.image4_anim.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        x = (self.width() - self.pixmap.width()) // 2
        y = (self.height() - self.pixmap.height()) // 2
        painter.drawPixmap(x, y, self.pixmap)

class KIKDWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KI/KD")
        self.resize(1665, 780)
        image_path = os.path.join(os.path.dirname(__file__), "assets", "mainBackground.png")
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Error: Failed to load image at {image_path}")
        else:
            self.pixmap = self.pixmap.scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Main title label with global properties and centered text
        self.title_label = QLabel("KI/KD", self)
        self.title_label.setFont(QFont("Cooper Black", 60))
        self.title_label.setStyleSheet(f"color: #333F50; background-color: {ROUNDED_LABEL_COLOR}; border: 3px solid black; border-radius: 10px;")
        self.title_label.setFixedWidth(ROUNDED_LABEL_WIDTH)
        self.title_label.setFixedHeight(ROUNDED_LABEL_HEIGHT)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.move(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT)  # Start off-screen top

        # Kompetensi Inti label with transparent background
        self.kompetensi_label = QLabel(
            "<b style='font-size: 15pt;'><strong>Kompetensi Inti:</strong></b><br>"
            "<span style='font-size: 11pt;'> <ol>"
            "<li>Menerima dan menjalankan ajaran agama yang dianutnya.</li>"
            "<li>Memiliki perilaku jujur, disiplin, tanggung jawab, santun, peduli, dan percaya diri dalam berinteraksi dengan keluarga, teman, dan guru.</li>"
            "<li>Memahami pengetahuan faktual dengan cara mengamati [mendengar, melihat, membaca] dan menanya berdasarkan rasa ingin tahu tentang dirinya, makhluk ciptaan Tuhan dan kegiatannya, dan benda-benda yang dijumpainya di rumah dan di Sekolah.</li>"
            "<li>Menyajikan pengetahuan faktual dalam bahasa yang jelas dan logis, dalam karya yang estetis, dalam gerakan yang mencerminkan anak sehat, dan dalam tindakan yang mencerminkan perilaku anak beriman dan berakhlak mulia.</li>"
            "</ol> </span>", self
        )
        self.kompetensi_label.setFont(QFont("Corbel"))
        self.kompetensi_label.setStyleSheet("color: #333F50; background: transparent; padding: 10px;")
        self.kompetensi_label.setWordWrap(True)
        self.kompetensi_label.setFixedWidth(500)
        self.kompetensi_label.move(-500, 200)  # Start off-screen left

        # Kompetensi Dasar label with transparent background
        self.kompetensiDasarLabel = QLabel(
            "<span style='font-size: 15pt;'>"
            "<strong>Kompetensi Dasar:</strong><br>"
            "3.2 Mengenal bangun datar dan bangun ruang menggunakan benda-benda yang ada di sekitar rumah, sekolah, atau tempat bermain.<br>"
            "</span>", self
        )
        self.kompetensiDasarLabel.setFont(QFont("Corbel"))
        self.kompetensiDasarLabel.setStyleSheet("color: #333F50; background: transparent; padding: 10px;")
        self.kompetensiDasarLabel.setWordWrap(True)
        self.kompetensiDasarLabel.setFixedWidth(500)
        self.kompetensiDasarLabel.move(1665 + 500, 216)  # Start off-screen right

        # Cloud image with global size, centered and at bottommost layer
        cloud_path = os.path.join(os.path.dirname(__file__), "assets", "kikdresource", "cloud.png")
        cloud_pixmap = QPixmap(cloud_path)
        if cloud_pixmap.isNull():
            print(f"Error: Failed to load cloud image at {cloud_path}")
        else:
            cloud_pixmap = cloud_pixmap.scaled(CLOUD_IMAGE_WIDTH, CLOUD_IMAGE_HEIGHT, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.cloudImage = QLabel(self)
        self.cloudImage.setPixmap(cloud_pixmap)
        self.cloudImage.setFixedSize(CLOUD_IMAGE_WIDTH, CLOUD_IMAGE_HEIGHT)
        self.cloudImage.move(-CLOUD_IMAGE_WIDTH, ((780 - CLOUD_IMAGE_HEIGHT) // 2) + 100)  # Start off-screen left
        self.cloudImage.lower()

        # Animation setup for all elements
        self.title_anim = QPropertyAnimation(self.title_label, b"pos")
        self.title_anim.setDuration(500)
        self.title_anim.setStartValue(QPoint(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT))
        self.title_anim.setEndValue(QPoint(ROUNDED_LABEL_POS_X, ROUNDED_LABEL_POS_Y))
        self.title_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.kompetensi_anim = QPropertyAnimation(self.kompetensi_label, b"pos")
        self.kompetensi_anim.setDuration(500)
        self.kompetensi_anim.setStartValue(QPoint(-500, 200))
        self.kompetensi_anim.setEndValue(QPoint(332, 200))
        self.kompetensi_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.kompetensiDasar_anim = QPropertyAnimation(self.kompetensiDasarLabel, b"pos")
        self.kompetensiDasar_anim.setDuration(500)
        self.kompetensiDasar_anim.setStartValue(QPoint(1665 + 500, 216))
        self.kompetensiDasar_anim.setEndValue(QPoint(932, 216))
        self.kompetensiDasar_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.cloud_anim = QPropertyAnimation(self.cloudImage, b"pos")
        self.cloud_anim.setDuration(500)
        self.cloud_anim.setStartValue(QPoint(-CLOUD_IMAGE_WIDTH, ((780 - CLOUD_IMAGE_HEIGHT) // 2) + 100))
        self.cloud_anim.setEndValue(QPoint(((1665 - CLOUD_IMAGE_WIDTH) // 2) + 0, ((780 - CLOUD_IMAGE_HEIGHT) // 2) + 100))
        self.cloud_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def showEvent(self, event):
        super().showEvent(event)
        self.title_anim.start()
        self.kompetensi_anim.start()
        self.kompetensiDasar_anim.start()
        self.cloud_anim.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        x = (self.width() - self.pixmap.width()) // 2
        y = (self.height() - self.pixmap.height()) // 2
        painter.drawPixmap(x, y, self.pixmap)

class Slide2Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slide 2")
        self.resize(1665, 780)
        image_path = os.path.join(os.path.dirname(__file__), "assets", "mainBackground.png")
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Error: Failed to load image at {image_path}")
        else:
            self.pixmap = self.pixmap.scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Main title label with global properties and centered text
        self.label = QLabel("Menu Utama", self)
        self.label.setFont(QFont("Cooper Black", 60))
        self.label.setStyleSheet(f"color: #333F50; background-color: {ROUNDED_LABEL_COLOR}; border: 3px solid black; border-radius: 10px;")
        self.label.setFixedWidth(ROUNDED_LABEL_WIDTH)
        self.label.setFixedHeight(ROUNDED_LABEL_HEIGHT)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT)  # Start off-screen top

        # Three buttons as separate variables
        button_dir = os.path.join(os.path.dirname(__file__), "assets", "slide2resource", "buttons")
        books_path = os.path.join(button_dir, "books.png")
        kikd_path = os.path.join(button_dir, "kikd.png")
        checklist_path = os.path.join(button_dir, "checklist.png")
        buttonXOffset = 445
        buttonYOffset = 330
        buttonSpacing = 300
        buttonSize = 212
        labelYOffset = buttonYOffset + buttonSize + 10

        # Button for Book Slide (navigates to MaterialWindow)
        self.bookButton = QPushButton("", self)
        pixmap1 = QPixmap(books_path)
        if pixmap1.isNull():
            print(f"Error: Failed to load image at {books_path}")
        else:
            pixmap1 = pixmap1.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.bookButton.setIcon(QIcon(pixmap1))
            self.bookButton.setIconSize(QSize(buttonSize, buttonSize))
        self.bookButton.setFixedSize(buttonSize, buttonSize)
        self.bookButton.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.bookButton.move(buttonXOffset, -buttonSize)  # Start off-screen top
        self.bookButton.clicked.connect(self.on_book_clicked)

        # Label for Books button
        self.book_label = QLabel("Books", self)
        self.book_label.setFont(QFont("Cooper Black", 20))
        self.book_label.setStyleSheet("color: #333F50; background: transparent;")
        self.book_label.move(buttonXOffset + 20, -20)  # Start off-screen top
        self.book_label.setFixedWidth(150)  # Ensure label stays with button

        # Button for KIKD Slide
        self.KIKDbutton = QPushButton("", self)
        pixmap2 = QPixmap(kikd_path)
        if pixmap2.isNull():
            print(f"Error: Failed to load image at {kikd_path}")
        else:
            pixmap2 = pixmap2.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.KIKDbutton.setIcon(QIcon(pixmap2))
            self.KIKDbutton.setIconSize(QSize(buttonSize, buttonSize))
        self.KIKDbutton.setFixedSize(buttonSize, buttonSize)
        self.KIKDbutton.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.KIKDbutton.move(buttonXOffset + buttonSpacing, -buttonSize)  # Start off-screen top
        self.KIKDbutton.clicked.connect(self.on_kikd_clicked)

        # Label for KIKD button
        self.kikd_label = QLabel("KIKD", self)
        self.kikd_label.setFont(QFont("Cooper Black", 20))
        self.kikd_label.setStyleSheet("color: #333F50; background: transparent;")
        self.kikd_label.move(buttonXOffset + buttonSpacing + 30, -20)  # Start off-screen top
        self.kikd_label.setFixedWidth(150)  # Ensure label stays with button

        # Button for Evaluation Slide
        self.checklistButton = QPushButton("", self)
        pixmap3 = QPixmap(checklist_path)
        if pixmap3.isNull():
            print(f"Error: Failed to load image at {checklist_path}")
        else:
            pixmap3 = pixmap3.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.checklistButton.setIcon(QIcon(pixmap3))
            self.checklistButton.setIconSize(QSize(buttonSize, buttonSize))
        self.checklistButton.setFixedSize(buttonSize, buttonSize)
        self.checklistButton.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.checklistButton.move(buttonXOffset + 2 * buttonSpacing, -buttonSize)  # Start off-screen top
        self.checklistButton.clicked.connect(self.on_checklist_clicked)

        # Label for Checklist button
        self.checklist_label = QLabel("Checklist", self)
        self.checklist_label.setFont(QFont("Cooper Black", 20))
        self.checklist_label.setStyleSheet("color: #333F50; background: transparent;")
        self.checklist_label.move(buttonXOffset + 2 * buttonSpacing, -20)  # Start off-screen top
        self.checklist_label.setFixedWidth(150)  # Ensure label stays with button

        # Animation setup for all elements
        self.title_anim = QPropertyAnimation(self.label, b"pos")
        self.title_anim.setDuration(500)
        self.title_anim.setStartValue(QPoint(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT))
        self.title_anim.setEndValue(QPoint(ROUNDED_LABEL_POS_X, ROUNDED_LABEL_POS_Y))
        self.title_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.bookButton_anim = QPropertyAnimation(self.bookButton, b"pos")
        self.bookButton_anim.setDuration(500)
        self.bookButton_anim.setStartValue(QPoint(buttonXOffset, -buttonSize))
        self.bookButton_anim.setEndValue(QPoint(buttonXOffset, buttonYOffset))
        self.bookButton_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.bookLabel_anim = QPropertyAnimation(self.book_label, b"pos")
        self.bookLabel_anim.setDuration(500)
        self.bookLabel_anim.setStartValue(QPoint(buttonXOffset + 20, -20))
        self.bookLabel_anim.setEndValue(QPoint(buttonXOffset + 20, labelYOffset))
        self.bookLabel_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.KIKDbutton_anim = QPropertyAnimation(self.KIKDbutton, b"pos")
        self.KIKDbutton_anim.setDuration(500)
        self.KIKDbutton_anim.setStartValue(QPoint(buttonXOffset + buttonSpacing, -buttonSize))
        self.KIKDbutton_anim.setEndValue(QPoint(buttonXOffset + buttonSpacing, buttonYOffset))
        self.KIKDbutton_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.kikdLabel_anim = QPropertyAnimation(self.kikd_label, b"pos")
        self.kikdLabel_anim.setDuration(500)
        self.kikdLabel_anim.setStartValue(QPoint(buttonXOffset + buttonSpacing + 30, -20))
        self.kikdLabel_anim.setEndValue(QPoint(buttonXOffset + buttonSpacing + 30, labelYOffset))
        self.kikdLabel_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.checklistButton_anim = QPropertyAnimation(self.checklistButton, b"pos")
        self.checklistButton_anim.setDuration(500)
        self.checklistButton_anim.setStartValue(QPoint(buttonXOffset + 2 * buttonSpacing, -buttonSize))
        self.checklistButton_anim.setEndValue(QPoint(buttonXOffset + 2 * buttonSpacing, buttonYOffset))
        self.checklistButton_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.checklistLabel_anim = QPropertyAnimation(self.checklist_label, b"pos")
        self.checklistLabel_anim.setDuration(500)
        self.checklistLabel_anim.setStartValue(QPoint(buttonXOffset + 2 * buttonSpacing, -20))
        self.checklistLabel_anim.setEndValue(QPoint(buttonXOffset + 2 * buttonSpacing, labelYOffset))
        self.checklistLabel_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def on_book_clicked(self):
        print("Books button have been clicked!")
        self.material_window = MaterialWindow()
        self.material_window.show()
        self.close()

    def on_kikd_clicked(self):
        print("KIKD button have been clicked!")
        self.kikd_window = KIKDWindow()
        self.kikd_window.show()
        self.close()

    def on_checklist_clicked(self):
        print("Checklist button have been clicked!")
        self.evaluation_window = EvaluationWindow()
        self.evaluation_window.show()
        self.close()

    def showEvent(self, event):
        super().showEvent(event)
        self.title_anim.start()
        self.bookButton_anim.start()
        self.bookLabel_anim.start()
        self.KIKDbutton_anim.start()
        self.kikdLabel_anim.start()
        self.checklistButton_anim.start()
        self.checklistLabel_anim.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        x = (self.width() - self.pixmap.width()) // 2
        y = (self.height() - self.pixmap.height()) // 2
        painter.drawPixmap(x, y, self.pixmap)

class MainMenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bangun Ruang - Main Menu")
        self.resize(1665, 780)
        image_path = os.path.join(os.path.dirname(__file__), "assets", "slide1resource", "slide1.png")
        playbutton_path = os.path.join(os.path.dirname(__file__), "assets", "slide1resource", "playbutton.png")
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Error: Failed to load image at {image_path}")
        else:
            self.pixmap = self.pixmap.scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        xOffset = 20
        yOffset = 50

        # Label 1 ("Bangun Ruang")
        self.label1 = QLabel("Bangun Ruang", self)
        self.label1.setFont(QFont("Cooper Black", 45))
        self.label1.setStyleSheet("color: #333F50; background: transparent;")
        self.label1.move(670 + xOffset, -50)  # Start off-screen top

        # Label 2 (Subtitle)
        self.label2 = QLabel("Mengenal Bentuk Bangun Ruang\n                   Kelas 1 SD/MI", self)
        self.label2.setFont(QFont("Cooper Black", 24))
        self.label2.setStyleSheet("color: #8497B0; background: transparent;")
        self.label2.move(617 + xOffset, -50)  # Start off-screen top

        # Play Button
        self.playbutton_path = playbutton_path
        self.playbutton_pixmap = QPixmap(self.playbutton_path)
        if self.playbutton_pixmap.isNull():
            print(f"Error: Failed to load play button image at {playbutton_path}")
        else:
            self.playbutton_pixmap = self.playbutton_pixmap.scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.play_button = QPushButton("", self)
        self.play_button.setIcon(QIcon(self.playbutton_pixmap))
        self.play_button.setIconSize(QSize(120, 120))
        self.play_button.setFixedSize(120, 120)
        self.play_button.setMinimumSize(120, 120)
        self.play_button.setMaximumSize(120, 120)
        self.play_button.setFocusPolicy(Qt.NoFocus)
        self.play_button.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.play_button.move(938 + xOffset, -120)  # Start off-screen top
        self.play_button.clicked.connect(self.on_play_clicked)

        # Animation setup for all elements
        self.label1_anim = QPropertyAnimation(self.label1, b"pos")
        self.label1_anim.setDuration(500)
        self.label1_anim.setStartValue(QPoint(670 + xOffset, -50))
        self.label1_anim.setEndValue(QPoint(670 + xOffset, 100 + yOffset))
        self.label1_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.label2_anim = QPropertyAnimation(self.label2, b"pos")
        self.label2_anim.setDuration(500)
        self.label2_anim.setStartValue(QPoint(617 + xOffset, -50))
        self.label2_anim.setEndValue(QPoint(617 + xOffset, 205 + yOffset))
        self.label2_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.playButton_anim = QPropertyAnimation(self.play_button, b"pos")
        self.playButton_anim.setDuration(500)
        self.playButton_anim.setStartValue(QPoint(938 + xOffset, -120))
        self.playButton_anim.setEndValue(QPoint(938 + xOffset, 334 + yOffset))
        self.playButton_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def on_play_clicked(self):
        self.slide2 = Slide2Window()
        self.slide2.show()
        self.close()

    def showEvent(self, event):
        super().showEvent(event)
        self.label1_anim.start()
        self.label2_anim.start()
        self.playButton_anim.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        x = (self.width() - self.pixmap.width()) // 2
        y = (self.height() - self.pixmap.height()) // 2
        painter.drawPixmap(x, y, self.pixmap)

class EvaluationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Evaluation")
        self.resize(1665, 780)
        image_path = os.path.join(os.path.dirname(__file__), "assets", "mainBackground.png")
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Error: Failed to load image at {image_path}")
        else:
            self.pixmap = self.pixmap.scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Main title label
        self.title_label = QLabel("Evaluation", self)
        self.title_label.setFont(QFont("Cooper Black", 60))
        self.title_label.setStyleSheet(f"color: #333F50; background-color: {ROUNDED_LABEL_COLOR}; border: 3px solid black; border-radius: 10px;")
        self.title_label.setFixedWidth(ROUNDED_LABEL_WIDTH)
        self.title_label.setFixedHeight(ROUNDED_LABEL_HEIGHT)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.move(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT)

        # Four buttons with black_thingy.png asset
        button_path = os.path.join(os.path.dirname(__file__), "assets", "black thingy.png")
        buttonSize = 220
        buttonXOffset = 375
        buttonYOffset = 300
        buttonSpacing = 230

        # Button 1 (KUIS)
        self.button1 = QPushButton("", self)
        pixmap1 = QPixmap(button_path)
        if pixmap1.isNull():
            print(f"Error: Failed to load image at {button_path}")
        else:
            pixmap1 = pixmap1.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.button1.setIcon(QIcon(pixmap1))
            self.button1.setIconSize(QSize(buttonSize, buttonSize))
        self.button1.setFixedSize(buttonSize, buttonSize)
        self.button1.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.button1.move(buttonXOffset, -buttonSize)
        self.button1.clicked.connect(self.on_button1_clicked)
        self.button1.setEnabled(True)
        self.button1.show()

        # Label for Button 1 (KUIS)
        self.label1 = QLabel("KUIS", self)
        self.label1.setFont(QFont("Corbel", 20))
        self.label1.setStyleSheet("color: white; background: transparent;")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.move(buttonXOffset, -buttonSize)
        self.label1.setFixedSize(buttonSize, buttonSize)
        self.label1.setAttribute(Qt.WA_TransparentForMouseEvents)  # Make label non-interactive

        # Button 2 (ESSAY)
        self.button2 = QPushButton("", self)
        pixmap2 = QPixmap(button_path)
        if pixmap2.isNull():
            print(f"Error: Failed to load image at {button_path}")
        else:
            pixmap2 = pixmap2.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.button2.setIcon(QIcon(pixmap2))
            self.button2.setIconSize(QSize(buttonSize, buttonSize))
        self.button2.setFixedSize(buttonSize, buttonSize)
        self.button2.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.button2.move(buttonXOffset + buttonSpacing, -buttonSize)
        self.button2.clicked.connect(self.on_button2_clicked)
        self.button2.setEnabled(True)
        self.button2.show()

        # Label for Button 2 (ESSAY)
        self.label2 = QLabel("ESSAY", self)
        self.label2.setFont(QFont("Corbel", 20))
        self.label2.setStyleSheet("color: white; background: transparent;")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.move(buttonXOffset + buttonSpacing, -buttonSize)
        self.label2.setFixedSize(buttonSize, buttonSize)
        self.label2.setAttribute(Qt.WA_TransparentForMouseEvents)  # Make label non-interactive

        # Button 3 (ISIAN)
        self.button3 = QPushButton("", self)
        pixmap3 = QPixmap(button_path)
        if pixmap3.isNull():
            print(f"Error: Failed to load image at {button_path}")
        else:
            pixmap3 = pixmap3.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.button3.setIcon(QIcon(pixmap3))
            self.button3.setIconSize(QSize(buttonSize, buttonSize))
        self.button3.setFixedSize(buttonSize, buttonSize)
        self.button3.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.button3.move(buttonXOffset + 2 * buttonSpacing, -buttonSize)
        self.button3.clicked.connect(self.on_button3_clicked)
        self.button3.setEnabled(True)
        self.button3.show()

        # Label for Button 3 (ISIAN)
        self.label3 = QLabel("ISIAN", self)
        self.label3.setFont(QFont("Corbel", 20))
        self.label3.setStyleSheet("color: white; background: transparent;")
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.move(buttonXOffset + 2 * buttonSpacing, -buttonSize)
        self.label3.setFixedSize(buttonSize, buttonSize)
        self.label3.setAttribute(Qt.WA_TransparentForMouseEvents)  # Make label non-interactive

        # Button 4 (TUGAS PROYEK)
        self.button4 = QPushButton("", self)
        pixmap4 = QPixmap(button_path)
        if pixmap4.isNull():
            print(f"Error: Failed to load image at {button_path}")
        else:
            pixmap4 = pixmap4.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.button4.setIcon(QIcon(pixmap4))
            self.button4.setIconSize(QSize(buttonSize, buttonSize))
        self.button4.setFixedSize(buttonSize, buttonSize)
        self.button4.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.button4.move(buttonXOffset + 3 * buttonSpacing, -buttonSize)
        self.button4.clicked.connect(self.on_button4_clicked)
        self.button4.setEnabled(True)
        self.button4.show()

        # Label for Button 4 (TUGAS PROYEK)
        self.label4 = QLabel("TUGAS \n PROYEK", self)
        self.label4.setFont(QFont("Corbel", 20))
        self.label4.setStyleSheet("color: white; background: transparent;")
        self.label4.setAlignment(Qt.AlignCenter)
        self.label4.move(buttonXOffset + 3 * buttonSpacing, -buttonSize)
        self.label4.setFixedSize(buttonSize, buttonSize)
        self.label4.setAttribute(Qt.WA_TransparentForMouseEvents)  # Make label non-interactive

        # Animation setup
        self.title_anim = QPropertyAnimation(self.title_label, b"pos")
        self.title_anim.setDuration(500)
        self.title_anim.setStartValue(QPoint(ROUNDED_LABEL_POS_X, -ROUNDED_LABEL_HEIGHT))
        self.title_anim.setEndValue(QPoint(ROUNDED_LABEL_POS_X, ROUNDED_LABEL_POS_Y))
        self.title_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.button1_anim = QPropertyAnimation(self.button1, b"pos")
        self.button1_anim.setDuration(500)
        self.button1_anim.setStartValue(QPoint(buttonXOffset, -buttonSize))
        self.button1_anim.setEndValue(QPoint(buttonXOffset, buttonYOffset))
        self.button1_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.label1_anim = QPropertyAnimation(self.label1, b"pos")
        self.label1_anim.setDuration(500)
        self.label1_anim.setStartValue(QPoint(buttonXOffset, -buttonSize))
        self.label1_anim.setEndValue(QPoint(buttonXOffset, buttonYOffset))
        self.label1_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.button2_anim = QPropertyAnimation(self.button2, b"pos")
        self.button2_anim.setDuration(500)
        self.button2_anim.setStartValue(QPoint(buttonXOffset + buttonSpacing, -buttonSize))
        self.button2_anim.setEndValue(QPoint(buttonXOffset + buttonSpacing, buttonYOffset))
        self.button2_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.label2_anim = QPropertyAnimation(self.label2, b"pos")
        self.label2_anim.setDuration(500)
        self.label2_anim.setStartValue(QPoint(buttonXOffset + buttonSpacing, -buttonSize))
        self.label2_anim.setEndValue(QPoint(buttonXOffset + buttonSpacing, buttonYOffset))
        self.label2_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.button3_anim = QPropertyAnimation(self.button3, b"pos")
        self.button3_anim.setDuration(500)
        self.button3_anim.setStartValue(QPoint(buttonXOffset + 2 * buttonSpacing, -buttonSize))
        self.button3_anim.setEndValue(QPoint(buttonXOffset + 2 * buttonSpacing, buttonYOffset))
        self.button3_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.label3_anim = QPropertyAnimation(self.label3, b"pos")
        self.label3_anim.setDuration(500)
        self.label3_anim.setStartValue(QPoint(buttonXOffset + 2 * buttonSpacing, -buttonSize))
        self.label3_anim.setEndValue(QPoint(buttonXOffset + 2 * buttonSpacing, buttonYOffset))
        self.label3_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.button4_anim = QPropertyAnimation(self.button4, b"pos")
        self.button4_anim.setDuration(500)
        self.button4_anim.setStartValue(QPoint(buttonXOffset + 3 * buttonSpacing, -buttonSize))
        self.button4_anim.setEndValue(QPoint(buttonXOffset + 3 * buttonSpacing, buttonYOffset))
        self.button4_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.label4_anim = QPropertyAnimation(self.label4, b"pos")
        self.label4_anim.setDuration(500)
        self.label4_anim.setStartValue(QPoint(buttonXOffset + 3 * buttonSpacing, -buttonSize))
        self.label4_anim.setEndValue(QPoint(buttonXOffset + 3 * buttonSpacing, buttonYOffset))
        self.label4_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def on_button1_clicked(self):
        print("Button 1 (KUIS) clicked! Opening QuizWindow...")
        self.quiz_window = QuizWindow()
        self.quiz_window.show()
        self.close()

    def on_button2_clicked(self):
        print("Button 2 (ESSAY) clicked!")
        # Add your essay window logic here if needed
        self.essay_window = EssayWindow()
        self.essay_window.show()
        self.close()

    def on_button3_clicked(self):
        print("Button 3 (ISIAN) clicked!")
        # Add your isian window logic here if needed
        # self.isian_window = IsianWindow()
        # self.isian_window.show()

    def on_button4_clicked(self):
        print("Button 4 (TUGAS PROYEK) clicked!")
        # Add your tugas proyek window logic here if needed
        # self.tugas_window = TugasWindow()
        # self.tugas_window.show()

    def showEvent(self, event):
        super().showEvent(event)
        self.title_anim.start()
        self.button1_anim.start()
        self.label1_anim.start()
        self.button2_anim.start()
        self.label2_anim.start()
        self.button3_anim.start()
        self.label3_anim.start()
        self.button4_anim.start()
        self.label4_anim.start()
        self.button1.raise_()
        self.button2.raise_()
        self.button3.raise_()
        self.button4.raise_()
        self.label1.raise_()
        self.label2.raise_()
        self.label3.raise_()
        self.label4.raise_()
        print("EvaluationWindow shown, all buttons and labels raised and enabled")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        x = (self.width() - self.pixmap.width()) // 2
        y = (self.height() - self.pixmap.height()) // 2
        painter.drawPixmap(x, y, self.pixmap)

class QuizWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz")
        self.resize(1665, 780)
        image_path = os.path.join(os.path.dirname(__file__), "assets", "mainBackground.png")
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Error: Failed to load image at {image_path}")
        else:
            self.pixmap = self.pixmap.scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # List of kuis assets
        kuis_resource_dir = os.path.join(os.path.dirname(__file__), "assets", "kuisresource")
        self.kuis_assets = [
            os.path.join(kuis_resource_dir, "basketball.png"),
            os.path.join(kuis_resource_dir, "carrotCone.png"),
            os.path.join(kuis_resource_dir, "cocaCola.png"),
            os.path.join(kuis_resource_dir, "diceCube.png"),
            os.path.join(kuis_resource_dir, "farmerHat.png"),
            os.path.join(kuis_resource_dir, "giftCube.png"),
            os.path.join(kuis_resource_dir, "iceCream.png"),
            os.path.join(kuis_resource_dir, "partyHatCone.png"),
            os.path.join(kuis_resource_dir, "schoolBus.png"),
            os.path.join(kuis_resource_dir, "teddyBear.png"),
            os.path.join(kuis_resource_dir, "umbrellaCone.png"),
            os.path.join(kuis_resource_dir, "vaultCube.png"),
        ]

        # Tables for x_offset, y_offset, and size (6x2 grid)
        self.x_offset = [
            [150, 300, 420, 580, 750, 870],  # Row 0 (first row)
            [150, 300, 420, 830, 960, 0]   # Row 1 (second row)
        ]
        self.y_offset = [
            [200, 200, 200, 200, 200, 150],    # Row 0
            [420, 420, 275, 420, 420, 0]     # Row 1
        ]
        self.size = [
            [150, 150, 150, 150, 150, 230],    # Row 0
            [150, 150, 450, 150, 150, 0]     # Row 1
        ]

        # Create labels for each image
        self.image_labels = []
        for row in range(2):
            for col in range(6):
                idx = row * 6 + col
                if idx < len(self.kuis_assets):  # Ensure we don't exceed asset list
                    label = QLabel(self)
                    pixmap = QPixmap(self.kuis_assets[idx])
                    if pixmap.isNull():
                        print(f"Error: Failed to load image at {self.kuis_assets[idx]}")
                    else:
                        pixmap = pixmap.scaled(self.size[row][col], self.size[row][col], Qt.KeepAspectRatio, Qt.SmoothTransformation)
                        label.setPixmap(pixmap)
                    label.setFixedSize(self.size[row][col], self.size[row][col])
                    label.move(self.x_offset[row][col], -self.size[row][col])  # Start off-screen top
                    self.image_labels.append(label)

        # Description label for all images
        self.description_label = QLabel("Carilah benda dengan bentuk kerucut di bawah ini!", self)
        self.description_label.setFont(QFont("Cooper Black", 15))
        self.description_label.setStyleSheet("color: #333F50;")
        self.description_label.setWordWrap(True)
        self.description_label.setFixedWidth(1200)
        self.description_label.move(211, 3)  # Start off-screen above, centered

        # Decorative Quiz Button
        button_path = os.path.join(os.path.dirname(__file__), "assets", "black thingy.png")
        buttonSize = 220
        buttonXOffset = 1300  # Centered with description
        buttonYOffset = 60  # Above images
        self.quiz_button = QPushButton("", self)
        pixmap = QPixmap(button_path)
        if pixmap.isNull():
            print(f"Error: Failed to load image at {button_path}")
        else:
            pixmap = pixmap.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.quiz_button.setIcon(QIcon(pixmap))
            self.quiz_button.setIconSize(QSize(buttonSize, buttonSize))
        self.quiz_button.setFixedSize(buttonSize, buttonSize)
        self.quiz_button.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.quiz_button.move(buttonXOffset, -buttonSize)  # Start off-screen top

        # Label for Quiz Button
        self.quiz_label = QLabel("QUIZ", self)
        self.quiz_label.setFont(QFont("Corbel", 20))
        self.quiz_label.setStyleSheet("color: white; background: transparent;")
        self.quiz_label.setAlignment(Qt.AlignCenter)
        self.quiz_label.move(buttonXOffset, -buttonSize)  # Start off-screen top
        self.quiz_label.setFixedSize(buttonSize, buttonSize)
        self.quiz_label.setAttribute(Qt.WA_TransparentForMouseEvents)  # Prevent hitbox interference

        # Animation setup for all image labels and description
        self.image_anims = []
        for row in range(2):
            for col in range(6):
                idx = row * 6 + col
                if idx < len(self.image_labels):
                    anim = QPropertyAnimation(self.image_labels[idx], b"pos")
                    anim.setDuration(500)
                    anim.setStartValue(QPoint(self.x_offset[row][col], -self.size[row][col]))
                    anim.setEndValue(QPoint(self.x_offset[row][col], self.y_offset[row][col]))
                    anim.setEasingCurve(QEasingCurve.InOutQuad)
                    self.image_anims.append(anim)

        self.description_anim = QPropertyAnimation(self.description_label, b"pos")
        self.description_anim.setDuration(500)
        self.description_anim.setStartValue(QPoint(211, -100))  
        self.description_anim.setEndValue(QPoint(211, 153))
        self.description_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.quiz_button_anim = QPropertyAnimation(self.quiz_button, b"pos")
        self.quiz_button_anim.setDuration(500)
        self.quiz_button_anim.setStartValue(QPoint(buttonXOffset, -buttonSize))
        self.quiz_button_anim.setEndValue(QPoint(buttonXOffset, buttonYOffset))
        self.quiz_button_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.quiz_label_anim = QPropertyAnimation(self.quiz_label, b"pos")
        self.quiz_label_anim.setDuration(500)
        self.quiz_label_anim.setStartValue(QPoint(buttonXOffset, -buttonSize))
        self.quiz_label_anim.setEndValue(QPoint(buttonXOffset, buttonYOffset))
        self.quiz_label_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def showEvent(self, event):
        super().showEvent(event)
        for anim in self.image_anims:
            anim.start()
        self.description_anim.start()
        self.quiz_button_anim.start()
        self.quiz_label_anim.start()
        self.quiz_button.raise_()
        self.quiz_label.raise_()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        x = (self.width() - self.pixmap.width()) // 2
        y = (self.height() - self.pixmap.height()) // 2
        painter.drawPixmap(x, y, self.pixmap)

class EssayWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Essay")
        self.resize(1665, 780)
        bg_path = os.path.join(os.path.dirname(__file__), "assets", "mainBackground.png")
        self.bg_pixmap = QPixmap(bg_path)
        if self.bg_pixmap.isNull():
            print(f"Error: Failed to load background at {bg_path}")
        else:
            self.bg_pixmap = self.bg_pixmap.scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        cloud_path = os.path.join(os.path.dirname(__file__), "assets", "materiresource", "nontransparentCloud.png")
        self.cloud_pixmap = QPixmap(cloud_path)
        if self.cloud_pixmap.isNull():
            print(f"Error: Failed to load cloud texture at {cloud_path}")
        else:
            self.cloud_pixmap = self.cloud_pixmap.scaled(600, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Adjusted size for center

        # Essay Button (matching QuizWindow style)
        button_path = os.path.join(os.path.dirname(__file__), "assets", "black thingy.png")
        buttonSize = 220
        buttonXOffset = 1300  # Moved to 1300
        buttonYOffset = 60    # Moved to 60
        self.essay_button = QPushButton("", self)
        pixmap = QPixmap(button_path)
        if pixmap.isNull():
            print(f"Error: Failed to load image at {button_path}")
        else:
            pixmap = pixmap.scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.essay_button.setIcon(QIcon(pixmap))
            self.essay_button.setIconSize(QSize(buttonSize, buttonSize))
        self.essay_button.setFixedSize(buttonSize, buttonSize)
        self.essay_button.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.essay_button.move(buttonXOffset, -buttonSize)  # Start off-screen top

        # Label for Essay Button
        self.essay_label = QLabel("ESSAY", self)
        self.essay_label.setFont(QFont("Corbel", 20))
        self.essay_label.setStyleSheet("color: white; background: transparent;")
        self.essay_label.setAlignment(Qt.AlignCenter)
        self.essay_label.move(buttonXOffset, -buttonSize)  # Start off-screen top
        self.essay_label.setFixedSize(buttonSize, buttonSize)
        self.essay_label.setAttribute(Qt.WA_TransparentForMouseEvents)  # Prevent hitbox interference

        # Corbel Label
        self.corbel_label = QLabel("Essay Section", self)
        self.corbel_label.setFont(QFont("Corbel", 40))
        self.corbel_label.setStyleSheet("color: #333F50; background: transparent;")
        self.corbel_label.setAlignment(Qt.AlignCenter)
        self.corbel_label.setFixedWidth(600)
        self.corbel_label.move(532, 100)  # Centered above button

        # Animation setup for essay button and label
        self.essay_button_anim = QPropertyAnimation(self.essay_button, b"pos")
        self.essay_button_anim.setDuration(500)
        self.essay_button_anim.setStartValue(QPoint(buttonXOffset, -buttonSize))
        self.essay_button_anim.setEndValue(QPoint(buttonXOffset, buttonYOffset))
        self.essay_button_anim.setEasingCurve(QEasingCurve.InOutQuad)

        self.essay_label_anim = QPropertyAnimation(self.essay_label, b"pos")
        self.essay_label_anim.setDuration(500)
        self.essay_label_anim.setStartValue(QPoint(buttonXOffset, -buttonSize))
        self.essay_label_anim.setEndValue(QPoint(buttonXOffset, buttonYOffset))
        self.essay_label_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def showEvent(self, event):
        super().showEvent(event)
        self.essay_button_anim.start()
        self.essay_label_anim.start()
        self.essay_button.raise_()
        self.essay_label.raise_()
        self.corbel_label.raise_()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.bg_pixmap)  # Draw mainBackground.png as background
        center_x = (self.width() - self.cloud_pixmap.width()) // 2
        center_y = (self.height() - self.cloud_pixmap.height()) // 2
        painter.drawPixmap(center_x, center_y, self.cloud_pixmap)  # Draw cloud texture centered

app = QApplication(sys.argv)
window = MainMenuWindow()
window.show()
sys.exit(app.exec_())