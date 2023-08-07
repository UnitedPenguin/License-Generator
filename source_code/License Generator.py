from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QLabel, QLineEdit, QMessageBox, QTextEdit, QFrame
import sys
import datetime

licenses = {
    "MIT": """
    MIT License
    
    Copyright (c) {year} {name}

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """,
    "Apache 2.0": """
    Apache License 2.0
    
    Copyright (c) {year} {name}
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
        
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
    """,
    "GNU GPL v3.0": """
    GNU General Public License v3.0
    
    Copyright (c) {year} {name}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    """
}

class LicenseGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("License Generator")
        self.setStyleSheet("""
            QWidget {
                background-color: #4a4a4a;
            }
            QLabel, QComboBox, QLineEdit {
                color: #ffffff;
            }
            QPushButton {
                background-color: #27ae60;
                color: #ffffff;
                font-weight: bold;
            }
            QTextEdit {
                background-color: #ffffff;
            }
        """)
        self.resize(800, 600)

        layout = QVBoxLayout()

        self.license_type_label = QLabel("License Type:")
        self.license_type_combo = QComboBox()
        self.license_type_combo.addItems(["MIT", "Apache 2.0", "GNU GPL v3.0"])

        self.name_label = QLabel("Name:")
        self.name_entry = QLineEdit()

        self.year_label = QLabel("Year:")
        self.year_entry = QLineEdit(str(datetime.datetime.now().year))

        self.preview_label = QLabel("Preview:")
        self.preview_text = QTextEdit()
        self.preview_text.setReadOnly(True)

        self.generate_button = QPushButton("Generate License")
        self.generate_button.clicked.connect(self.generate_license)

        layout.addWidget(self.license_type_label)
        layout.addWidget(self.license_type_combo)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(self.year_label)
        layout.addWidget(self.year_entry)
        layout.addWidget(self.preview_label)
        layout.addWidget(self.preview_text)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def generate_license(self):
        license_key = self.license_type_combo.currentText()
        name = self.name_entry.text()
        year = self.year_entry.text()

        license_text = licenses.get(license_key)
        if license_text:
            license_text = license_text.format(year=year, name=name)
            self.preview_text.setPlainText(license_text)
            with open('LICENSE', 'w') as f:
                f.write(license_text)
            QMessageBox.information(self, "Success", "LICENSE file has been created.")
        else:
            QMessageBox.critical(self, "Error", "Invalid license key.")

def main():
    app = QApplication(sys.argv)

    generator = LicenseGenerator()
    generator.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
