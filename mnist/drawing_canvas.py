"""
drawing_canvas.py — 숫자를 그릴 수 있는 Tkinter 캔버스 위젯

기능:
    - 280x280 흰색 캔버스에 검정색 브러시로 그리기
    - 마우스 드래그로 자연스러운 획 그리기
    - PIL Image로 내보내기 (전처리용)
    - 지우기 기능
"""

import tkinter as tk
from PIL import Image, ImageDraw


class DrawingCanvas:
    """숫자를 그릴 수 있는 캔버스 위젯"""

    CANVAS_SIZE = 280
    BRUSH_RADIUS = 12
    BG_COLOR = 'white'
    BRUSH_COLOR = 'black'

    def __init__(self, parent, on_draw_complete=None):
        self.on_draw_complete = on_draw_complete
        self.strokes = []
        self.all_strokes = []

        self.frame = tk.Frame(parent, bg='white')

        self.canvas = tk.Canvas(
            self.frame,
            width=self.CANVAS_SIZE,
            height=self.CANVAS_SIZE,
            bg=self.BG_COLOR,
            cursor='crosshair',
            highlightthickness=1,
            highlightbackground='#CCCCCC'
        )
        self.canvas.pack()

        self.canvas.bind('<B1-Motion>', self._on_drag)
        self.canvas.bind('<ButtonPress-1>', self._on_press)
        self.canvas.bind('<ButtonRelease-1>', self._on_release)

        self.label = tk.Label(
            self.frame,
            text='여기에 숫자를 그려주세요',
            font=('Apple SD Gothic Neo', 10),
            fg='#AAAAAA', bg='white'
        )
        self.label.pack(pady=(4, 0))

    def _on_press(self, event):
        self.strokes = [(event.x, event.y)]
        self._draw_point(event.x, event.y)

    def _on_drag(self, event):
        x, y = event.x, event.y
        self.strokes.append((x, y))

        if len(self.strokes) >= 2:
            x0, y0 = self.strokes[-2]
            self.canvas.create_line(
                x0, y0, x, y,
                fill=self.BRUSH_COLOR,
                width=self.BRUSH_RADIUS * 2,
                capstyle=tk.ROUND,
                smooth=True
            )
        self._draw_point(x, y)

    def _on_release(self, event):
        if self.strokes:
            self.all_strokes.append(self.strokes.copy())
            self.strokes = []

        if self.on_draw_complete and self.all_strokes:
            self.on_draw_complete()

    def _draw_point(self, x, y):
        r = self.BRUSH_RADIUS
        self.canvas.create_oval(
            x - r, y - r, x + r, y + r,
            fill=self.BRUSH_COLOR,
            outline=self.BRUSH_COLOR
        )

    def get_image(self):
        """
        캔버스의 내용을 PIL Image로 반환합니다.

        흰 배경에 검정 글씨로 그리지만, MNIST 형식(검정 배경, 흰 글씨)으로
        반전하여 반환합니다.
        """
        # 흰 배경에 검정으로 그리기
        image = Image.new('L', (self.CANVAS_SIZE, self.CANVAS_SIZE), 255)
        draw = ImageDraw.Draw(image)

        for stroke in self.all_strokes:
            for i in range(len(stroke)):
                x, y = stroke[i]
                r = self.BRUSH_RADIUS
                draw.ellipse([x - r, y - r, x + r, y + r], fill=0)

                if i > 0:
                    x0, y0 = stroke[i - 1]
                    draw.line([x0, y0, x, y], fill=0, width=self.BRUSH_RADIUS * 2)

        # MNIST 형식으로 반전: 흰 배경/검정 글씨 → 검정 배경/흰 글씨
        from PIL import ImageOps
        image = ImageOps.invert(image)

        return image

    def clear(self):
        self.canvas.delete('all')
        self.strokes = []
        self.all_strokes = []

    def is_empty(self):
        return len(self.all_strokes) == 0
