#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日关怀 - 给妈妈的暖心应用
一个温馨的手机应用，包含天气提醒、健康小贴士和暖心话语
"""

import random
import requests
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.text import LabelBase


class MainApp(App):
    def __init__(self):
        super().__init__()
        self.title = "每日关怀 💝"
        
    def build(self):
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # 标题
        title_label = Label(
            text='每日关怀 💝\n给最爱的妈妈',
            font_size='24sp',
            size_hint_y=None,
            height=dp(80),
            halign='center',
            valign='middle',
            color=(0.8, 0.3, 0.5, 1)
        )
        title_label.bind(size=title_label.setter('text_size'))
        main_layout.add_widget(title_label)
        
        # 当前时间显示
        self.time_label = Label(
            text=self.get_current_time(),
            font_size='16sp',
            size_hint_y=None,
            height=dp(40),
            color=(0.4, 0.4, 0.4, 1)
        )
        main_layout.add_widget(self.time_label)
        
        # 每秒更新时间
        Clock.schedule_interval(self.update_time, 1)
        
        # 功能按钮区域
        button_layout = BoxLayout(orientation='vertical', spacing=dp(10))
        
        # 天气查询按钮
        weather_btn = Button(
            text='🌤️ 查看今日天气',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.3, 0.7, 0.9, 1)
        )
        weather_btn.bind(on_press=self.show_weather)
        button_layout.add_widget(weather_btn)
        
        # 健康小贴士按钮
        health_btn = Button(
            text='🏃‍♀️ 健康小贴士',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.5, 0.8, 0.5, 1)
        )
        health_btn.bind(on_press=self.show_health_tips)
        button_layout.add_widget(health_btn)
        
        # 暖心话语按钮
        love_btn = Button(
            text='💕 暖心话语',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.9, 0.6, 0.7, 1)
        )
        love_btn.bind(on_press=self.show_love_words)
        button_layout.add_widget(love_btn)
        
        # 记录心情按钮
        mood_btn = Button(
            text='😊 记录今日心情',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.8, 0.7, 0.3, 1)
        )
        mood_btn.bind(on_press=self.record_mood)
        button_layout.add_widget(mood_btn)
        
        main_layout.add_widget(button_layout)
        
        # 底部说明
        footer_label = Label(
            text='这是你儿子/女儿用Python为你开发的应用 ❤️\n希望能给你的每一天带来温暖',
            font_size='14sp',
            size_hint_y=None,
            height=dp(60),
            halign='center',
            valign='middle',
            color=(0.6, 0.6, 0.6, 1)
        )
        footer_label.bind(size=footer_label.setter('text_size'))
        main_layout.add_widget(footer_label)
        
        return main_layout
    
    def get_current_time(self):
        """获取当前时间"""
        now = datetime.now()
        return now.strftime("%Y年%m月%d日 %H:%M:%S")
    
    def update_time(self, dt):
        """更新时间显示"""
        self.time_label.text = self.get_current_time()
    
    def show_weather(self, instance):
        """显示天气信息"""
        # 模拟天气数据（实际项目中可以接入天气API）
        weather_data = [
            "今日天气：晴朗 ☀️\n温度：22-28°C\n提醒：适合出门散步，记得带帽子防晒哦！",
            "今日天气：多云 ⛅\n温度：18-25°C\n提醒：天气舒适，是个好日子！",
            "今日天气：小雨 🌧️\n温度：15-20°C\n提醒：记得带伞，注意保暖！",
            "今日天气：阴天 ☁️\n温度：20-26°C\n提醒：虽然没有太阳，但心情要像阳光一样明媚！"
        ]
        
        weather_info = random.choice(weather_data)
        self.show_popup("今日天气预报", weather_info)
    
    def show_health_tips(self, instance):
        """显示健康小贴士"""
        health_tips = [
            "💧 每天至少喝8杯水\n保持身体水分充足，皮肤也会更好哦！",
            "🚶‍♀️ 每天走路30分钟\n适量运动有助于身心健康，还能延缓衰老！",
            "🥗 多吃蔬菜水果\n丰富的维生素让你活力满满！",
            "😴 保证充足睡眠\n每晚7-8小时睡眠，是最好的美容养颜方法！",
            "🧘‍♀️ 保持心情愉悦\n笑一笑十年少，快乐是最好的良药！",
            "📱 减少看手机时间\n适当休息眼睛，保护视力健康！",
            "🍵 喝些绿茶或花茶\n抗氧化又养生，还能静心宁神！"
        ]
        
        tip = random.choice(health_tips)
        self.show_popup("健康小贴士", tip)
    
    def show_love_words(self, instance):
        """显示暖心话语"""
        love_words = [
            "💕 妈妈，你是我心中永远的女神！\n感谢你给了我生命和无条件的爱！",
            "🌹 时光不老，我们不散\n愿你永远健康快乐，笑容满面！",
            "✨ 你的笑容是我最大的动力\n希望每天都能看到你开心的样子！",
            "🎈 妈妈辛苦了！\n你为家庭付出的一切，我都记在心里！",
            "🌈 你是我见过最坚强最美丽的女人\n我为有你这样的妈妈而自豪！",
            "🎯 学习编程让我更懂得\n科技的力量和知识的重要性，感谢你的支持！",
            "💖 无论我走到哪里\n你都是我心中最温暖的港湾！"
        ]
        
        word = random.choice(love_words)
        self.show_popup("暖心话语", word)
    
    def record_mood(self, instance):
        """记录心情"""
        # 创建心情记录弹窗
        content = BoxLayout(orientation='vertical', spacing=dp(10))
        
        mood_label = Label(
            text='今天心情怎么样？\n分享一下吧 😊',
            size_hint_y=None,
            height=dp(60)
        )
        content.add_widget(mood_label)
        
        mood_input = TextInput(
            hint_text='写下今天的心情...',
            multiline=True,
            size_hint_y=None,
            height=dp(100)
        )
        content.add_widget(mood_input)
        
        button_layout = BoxLayout(size_hint_y=None, height=dp(40), spacing=dp(10))
        
        def save_mood(instance):
            if mood_input.text.strip():
                popup.dismiss()
                self.show_popup("心情已保存 💝", f"今日心情：{mood_input.text}\n\n愿你每天都有好心情！")
            else:
                self.show_popup("提示", "请先写下你的心情哦 😊")
        
        save_btn = Button(text='保存心情')
        save_btn.bind(on_press=save_mood)
        button_layout.add_widget(save_btn)
        
        cancel_btn = Button(text='取消')
        cancel_btn.bind(on_press=lambda x: popup.dismiss())
        button_layout.add_widget(cancel_btn)
        
        content.add_widget(button_layout)
        
        popup = Popup(
            title='记录心情',
            content=content,
            size_hint=(0.8, 0.6)
        )
        popup.open()
    
    def show_popup(self, title, message):
        """显示弹窗"""
        content = BoxLayout(orientation='vertical')
        
        # 创建可滚动的标签
        scroll = ScrollView()
        label = Label(
            text=message,
            text_size=(None, None),
            halign='center',
            valign='top'
        )
        label.bind(texture_size=label.setter('size'))
        scroll.add_widget(label)
        content.add_widget(scroll)
        
        # 关闭按钮
        close_btn = Button(
            text='知道了 ❤️',
            size_hint_y=None,
            height=dp(40)
        )
        content.add_widget(close_btn)
        
        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.8, 0.6)
        )
        
        close_btn.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == '__main__':
    MainApp().run()
