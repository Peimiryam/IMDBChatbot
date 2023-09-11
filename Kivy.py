from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import random
from imdb import IMDb
#import main
ia = IMDb()

# List of genres for recommendations
#https://www.imdb.com/feature/genre/
genres = ["action", "comedy", "drama", "sci-fi", "horror", "adventure", "romance", 'animation', 'biography', 'comedy', 'crime', 'documentary', 'drama', 
            'family', 'fantasy', 'film-noir', 'history', 'music', 'musical', 'mystery', 'short', 'sport',
             'thriller', 'war', 'western' ]

genre_tv = ["action", "comedy", "drama", "sci-fi", "horror", "adventure", "romance", 'animation', 'biography', 'comedy', 'crime', 'documentary', 'drama', 
            'family', 'fantasy', 'film-noir', 'history', 'music', 'musical', 'mystery', 'short', 'sport',
             'thriller', 'war', 'western', 'reality-tv', 'game-show', 'talk-show', 'news']

user_inputs = ['recommendations', 'info', 'search', 'reviews',  'q']

reviews = {}


class Menu(App):
    def __init__(self):
        super(Menu, self).__init__()

    def build(self):
        self.title = 'Movie & Series Chatbot App'
        self.layout = BoxLayout(orientation='vertical')
        self.title_label = Label(text='Welcome to the Recommendator of movies and TV series Chatbot!\n"You can ask for recommendations or info about a movie or Tv serie.\n')
        self.layout.add_widget(self.title_label)

        self.menu_label = Label(text='Select one of the following feature :"recommendations", "info", "search" "reviews" or press "q" to quit: ')
        self.recommendations_button = Button(text='Recommendations')
        self.info_button = Button(text='Info')
        self.review_button = Button(text='Reviews')
        self.exit_button = Button(text='Exit')
        self.layout.add_widget(self.menu_label)
        self.layout.add_widget(self.recommendations_button)
        #self.recommendations_button.bind(on_release=self.get_recommendation)
        self.layout.add_widget(self.info_button)
        self.layout.add_widget(self.review_button)
        self.layout.add_widget(self.exit_button)

        return self.layout

if __name__ == '__main__':
    Menu().run()