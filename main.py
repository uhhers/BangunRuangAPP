from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QFont, QIcon
from PyQt5.QtCore import Qt, QSize
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

class MaterialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Materi")
        self.resize(1665, 780)
        image_path = os.path.join(os.path.dirname(__file__), "assets", "mainBackground.png")
        self.pixmap = QPixmap(image_path).scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Main title label with global properties and centered text
        title_label = QLabel("Materi", self)
        title_label.setFont(QFont("Cooper Black", 60))
        title_label.setStyleSheet(f"color: #333F50; background-color: {ROUNDED_LABEL_COLOR}; border: 3px solid black; border-radius: 10px;")
        title_label.setFixedWidth(ROUNDED_LABEL_WIDTH)
        title_label.setFixedHeight(ROUNDED_LABEL_HEIGHT)
        title_label.setAlignment(Qt.AlignCenter)  # Center text
        title_label.move(ROUNDED_LABEL_POS_X, ROUNDED_LABEL_POS_Y)

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
        labelYOffset = buttonYOffset + buttonSize + 10  # Place labels 10px below buttons

        # Ball Button
        self.button1 = QPushButton("", self)
        pixmap1 = QPixmap(button_paths[0]).scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
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
        self.button1.move(buttonXOffset, buttonYOffset)
        self.button1.clicked.connect(self.on_button1_clicked)

        # Label for Button 1
        button1_label = QLabel("Button 1", self)
        button1_label.setFont(QFont("Cooper Black", 20))
        button1_label.setStyleSheet("color: #333F50; background: transparent;")
        button1_label.move(buttonXOffset + 20, labelYOffset)

        # Button 2
        self.button2 = QPushButton("", self)
        pixmap2 = QPixmap(button_paths[1]).scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
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
        self.button2.move(buttonXOffset + buttonSpacing, buttonYOffset)
        self.button2.clicked.connect(self.on_button2_clicked)

        # Label for Button 2
        button2_label = QLabel("Button 2", self)
        button2_label.setFont(QFont("Cooper Black", 20))
        button2_label.setStyleSheet("color: #333F50; background: transparent;")
        button2_label.move(buttonXOffset + buttonSpacing + 20, labelYOffset)

        # Button 3
        self.button3 = QPushButton("", self)
        pixmap3 = QPixmap(button_paths[2]).scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
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
        self.button3.move(buttonXOffset + 2 * buttonSpacing, buttonYOffset)
        self.button3.clicked.connect(self.on_button3_clicked)

        # Label for Button 3
        button3_label = QLabel("Button 3", self)
        button3_label.setFont(QFont("Cooper Black", 20))
        button3_label.setStyleSheet("color: #333F50; background: transparent;")
        button3_label.move(buttonXOffset + 2 * buttonSpacing + 20, labelYOffset)

        # Button 4
        self.button4 = QPushButton("", self)
        pixmap4 = QPixmap(button_paths[3]).scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
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
        self.button4.move(buttonXOffset + 3 * buttonSpacing, buttonYOffset)
        self.button4.clicked.connect(self.on_button4_clicked)

        # Label for Button 4
        button4_label = QLabel("Button 4", self)
        button4_label.setFont(QFont("Cooper Black", 20))
        button4_label.setStyleSheet("color: #333F50; background: transparent;")
        button4_label.move(buttonXOffset + 3 * buttonSpacing + 20, labelYOffset)

        # Button 5
        self.button5 = QPushButton("", self)
        pixmap5 = QPixmap(button_paths[4]).scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
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
        self.button5.move(buttonXOffset + 4 * buttonSpacing, buttonYOffset)
        self.button5.clicked.connect(self.on_button5_clicked)

        # Label for Button 5
        button5_label = QLabel("Button 5", self)
        button5_label.setFont(QFont("Cooper Black", 20))
        button5_label.setStyleSheet("color: #333F50; background: transparent;")
        button5_label.move(buttonXOffset + 4 * buttonSpacing + 20, labelYOffset)

    def on_button1_clicked(self):
        print("Button 1 clicked!")

    def on_button2_clicked(self):
        print("Button 2 clicked!")

    def on_button3_clicked(self):
        print("Button 3 clicked!")

    def on_button4_clicked(self):
        print("Button 4 clicked!")

    def on_button5_clicked(self):
        print("Button 5 clicked!")

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
        self.pixmap = QPixmap(image_path).scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Main title label with global properties and centered text
        title_label = QLabel("KI/KD", self)
        title_label.setFont(QFont("Cooper Black", 60))
        title_label.setStyleSheet(f"color: #333F50; background-color: {ROUNDED_LABEL_COLOR}; border: 3px solid black; border-radius: 10px;")
        title_label.setFixedWidth(ROUNDED_LABEL_WIDTH)
        title_label.setFixedHeight(ROUNDED_LABEL_HEIGHT)
        title_label.setAlignment(Qt.AlignCenter)  # Center text
        title_label.move(ROUNDED_LABEL_POS_X, ROUNDED_LABEL_POS_Y)

        # Kompetensi Inti label with transparent background
        kompetensi_label = QLabel(
            "<b style='font-size: 15pt;'><strong>Kompetensi Inti:</strong></b><br>"
            "<span style='font-size: 11pt;'> <ol>"
            "<li>Menerima dan menjalankan ajaran agama yang dianutnya.</li>"
            "<li>Memiliki perilaku jujur, disiplin, tanggung jawab, santun, peduli, dan percaya diri dalam berinteraksi dengan keluarga, teman, dan guru.</li>"
            "<li>Memahami pengetahuan faktual dengan cara mengamati [mendengar, melihat, membaca] dan menanya berdasarkan rasa ingin tahu tentang dirinya, makhluk ciptaan Tuhan dan kegiatannya, dan benda-benda yang dijumpainya di rumah dan di Sekolah.</li>"
            "<li>Menyajikan pengetahuan faktual dalam bahasa yang jelas dan logis, dalam karya yang estetis, dalam gerakan yang mencerminkan anak sehat, dan dalam tindakan yang mencerminkan perilaku anak beriman dan berakhlak mulia.</li>"
            "</ol> </span>", self
        )
        kompetensi_label.setFont(QFont("Corbel"))
        kompetensi_label.setStyleSheet("color: #333F50; background: transparent; padding: 10px;")
        kompetensi_label.setWordWrap(True)
        kompetensi_label.setFixedWidth(500)  # Wide enough for text
        kompetensi_label.move(332, 200)  # Positioned below title, centered horizontally

        # Kompetensi Dasar label with transparent background
        kompetensiDasarLabel = QLabel(
            "<span style='font-size: 15pt;'>"
            "<strong>Kompetensi Dasar:</strong><br>"
            "3.2 Mengenal bangun datar dan bangun ruang menggunakan benda-benda yang ada di sekitar rumah, sekolah, atau tempat bermain.<br>"
            "</span>", self
        )
        kompetensiDasarLabel.setFont(QFont("Corbel"))
        kompetensiDasarLabel.setStyleSheet("color: #333F50; background: transparent; padding: 10px;")
        kompetensiDasarLabel.setWordWrap(True)
        kompetensiDasarLabel.setFixedWidth(500)  # Wide enough for text
        kompetensiDasarLabel.move(932, 216)

        # Cloud image with global size, centered and at bottommost layer
        cloud_path = os.path.join(os.path.dirname(__file__), "assets", "kikdresource", "cloud.png")
        cloud_pixmap = QPixmap(cloud_path).scaled(CLOUD_IMAGE_WIDTH, CLOUD_IMAGE_HEIGHT, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        cloudImage = QLabel(self)
        cloudImage.setPixmap(cloud_pixmap)
        cloudImage.setFixedSize(CLOUD_IMAGE_WIDTH, CLOUD_IMAGE_HEIGHT)
        cloudImage.move(((1665 - CLOUD_IMAGE_WIDTH) // 2) + 0, ((780 - CLOUD_IMAGE_HEIGHT) // 2) + 100)  # Center in window with offset
        cloudImage.lower()  # Move to bottommost layer (behind other widgets)

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
        self.pixmap = QPixmap(image_path).scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Main title label with global properties and centered text
        label = QLabel("Menu Utama", self)
        label.setFont(QFont("Cooper Black", 60))
        label.setStyleSheet(f"color: #333F50; background-color: {ROUNDED_LABEL_COLOR}; border: 3px solid black; border-radius: 10px;")
        label.setFixedWidth(ROUNDED_LABEL_WIDTH)
        label.setFixedHeight(ROUNDED_LABEL_HEIGHT)
        label.setAlignment(Qt.AlignCenter)  # Center text
        label.move(ROUNDED_LABEL_POS_X, ROUNDED_LABEL_POS_Y)

        # Three buttons as separate variables
        button_dir = os.path.join(os.path.dirname(__file__), "assets", "slide2resource", "buttons")
        books_path = os.path.join(button_dir, "books.png")
        kikd_path = os.path.join(button_dir, "kikd.png")
        checklist_path = os.path.join(button_dir, "checklist.png")
        buttonXOffset = 445
        buttonYOffset = 330
        buttonSpacing = 300
        buttonSize = 212
        labelYOffset = buttonYOffset + buttonSize + 10  # Place labels 10px below buttons

        # Button for Book Slide (navigates to MaterialWindow)
        self.bookButton = QPushButton("", self)
        pixmap1 = QPixmap(books_path).scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
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
        self.bookButton.move(buttonXOffset, buttonYOffset)
        self.bookButton.clicked.connect(self.on_book_clicked)

        # Label for Books button
        book_label = QLabel("Books", self)
        book_label.setFont(QFont("Cooper Black", 20))
        book_label.setStyleSheet("color: #333F50; background: transparent;")
        book_label.move(buttonXOffset + 20, labelYOffset)  # Adjusted for centering

        # Button for KIKD Slide
        self.KIKDbutton = QPushButton("", self)
        pixmap2 = QPixmap(kikd_path).scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
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
        self.KIKDbutton.move(buttonXOffset + buttonSpacing, buttonYOffset)
        self.KIKDbutton.clicked.connect(self.on_kikd_clicked)

        # Label for KIKD button
        kikd_label = QLabel("KIKD", self)
        kikd_label.setFont(QFont("Cooper Black", 20))
        kikd_label.setStyleSheet("color: #333F50; background: transparent;")
        kikd_label.move(buttonXOffset + buttonSpacing + 30, labelYOffset)  # Adjusted for centering

        # Button for Evaluation Slide
        self.checklistButton = QPushButton("", self)
        pixmap3 = QPixmap(checklist_path).scaled(buttonSize, buttonSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
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
        self.checklistButton.move(buttonXOffset + 2 * buttonSpacing, buttonYOffset)
        self.checklistButton.clicked.connect(self.on_checklist_clicked)

        # Label for Checklist button
        checklist_label = QLabel("Checklist", self)
        checklist_label.setFont(QFont("Cooper Black", 20))
        checklist_label.setStyleSheet("color: #333F50; background: transparent;")
        checklist_label.move(buttonXOffset + 2 * buttonSpacing, labelYOffset)  # Adjusted for centering

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
        self.pixmap = QPixmap(image_path).scaled(1665, 780, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        xOffset = 20
        yOffset = 50
        label1 = QLabel("Bangun Ruang", self)
        label1.setFont(QFont("Cooper Black", 45))
        label1.setStyleSheet("color: #333F50; background: transparent;")
        label1.move(670 + xOffset, 100 + yOffset)

        label2 = QLabel("Mengenal Bentuk Bangun Ruang\n                   Kelas 1 SD/MI", self)
        label2.setFont(QFont("Cooper Black", 24))
        label2.setStyleSheet("color: #8497B0; background: transparent;")
        label2.move(617 + xOffset, 205 + yOffset)

        # Play Button (no animation)
        self.playbutton_path = playbutton_path
        self.playbutton_pixmap = QPixmap(self.playbutton_path).scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation)
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
        self.play_button.move(938 + xOffset, 334 + yOffset)
        self.play_button.clicked.connect(self.on_play_clicked)

    def on_play_clicked(self):
        self.slide2 = Slide2Window()
        self.slide2.show()
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        x = (self.width() - self.pixmap.width()) // 2
        y = (self.height() - self.pixmap.height()) // 2
        painter.drawPixmap(x, y, self.pixmap)

app = QApplication(sys.argv)
window = MainMenuWindow()
window.show()
sys.exit(app.exec_())