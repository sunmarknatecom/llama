import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox, QFileDialog, QLineEdit
import ollama

class MyJarvis(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('라마 질문기')

        # 레이아웃 설정
        layout = QVBoxLayout()

        # 클리어 버튼
        self.clear_button = QPushButton('클리어')
        self.clear_button.clicked.connect(self.clear_text)
        layout.addWidget(self.clear_button)

        # 입력 텍스트 레이블 및 텍스트 입력창
        self.input_label = QLabel('텍스트를 입력하세요:')
        layout.addWidget(self.input_label)

        self.text_input = QTextEdit()
        layout.addWidget(self.text_input)

        # 실행 버튼
        self.process_button = QPushButton('실행')
        self.process_button.clicked.connect(self.process_text)
        layout.addWidget(self.process_button)

        # 출력 텍스트 레이블 및 텍스트 출력창
        self.output_label = QLabel('결과:')
        layout.addWidget(self.output_label)

        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)
        layout.addWidget(self.text_output)

        # 저장 버튼
        self.save_button = QPushButton('저장')
        self.save_button.clicked.connect(self.save_text)
        layout.addWidget(self.save_button)

        # 저장 경로 설정 버튼
        self.set_path_button = QPushButton('저장 경로 설정')
        self.set_path_button.clicked.connect(self.set_save_path)
        layout.addWidget(self.set_path_button)

        # 파일 경로 레이블
        self.file_path_label = QLabel('저장 경로:')
        layout.addWidget(self.file_path_label)

        # 저장 경로 표시 텍스트 위젯 (한 줄로 줄이기 위해 QLineEdit 사용)
        self.save_path_display = QLineEdit()
        self.save_path_display.setReadOnly(True)
        layout.addWidget(self.save_path_display)

        # 메인 레이아웃 설정
        self.setLayout(layout)

    def process_text(self):
        try:
            # 입력된 텍스트 가져오기
            input_text = self.text_input.toPlainText().strip()
            
            # ollama 모듈을 사용한 텍스트 처리
            response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': input_text}])
            processed_text = response['message']['content']
            
            # 처리된 텍스트를 출력창에 표시
            self.text_output.setPlainText(processed_text)
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    def clear_text(self):
        self.text_input.clear()
        self.text_output.clear()
        self.file_path_label.clear()
        self.save_path_display.clear()

    def save_text(self):
        try:
            input_text = self.text_input.toPlainText().strip()
            output_text = self.text_output.toPlainText().strip()

            file_path = self.save_path_display.text().strip()

            if file_path:
                with open(file_path, 'a') as f:
                    f.write(f'Input: {input_text}\nOutput: {output_text}\n\n')
                
                self.file_path_label.setText(f'Saved to: {file_path}')
            else:
                QMessageBox.warning(self, 'Warning', '저장 경로를 설정하세요.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    def set_save_path(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt)')
        if file_path:
            self.save_path_display.setText(file_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyJarvis()
    ex.show()
    sys.exit(app.exec_())
