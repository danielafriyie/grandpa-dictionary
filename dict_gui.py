"""

INTERACTIVE DICTIONARY MADE BY DANIEL AFRIYIE

"""

__app_name__ = "Grandpa Dictionary"
__version__ = "1.0"
__author__ = "Afriyie Daniel"
__email__ = "afriyiedaniel1@outlook.com"
__status__ = "Development"
__description__ = "Grandpa Dictionary Project"

from tkinter import *
import json
from difflib import get_close_matches
from tkinter import ttk
import tkinter.messagebox as mbx


class Dictionary:

    def __init__(self, parent):
        self.parent = parent
        self.parent.title(__app_name__ + ' First Edition ' + __version__)
        self.parent.configure(background="green")
        self.parent.state('zoomed')
        # self.parent.geometry("1600x900")
        # self.parent.resizable(height=False, width=False)

        NORMAL_FONT = ("Times New Roman", 12)
        LARGE_FONT = ("Algerian", 40)
        MEDIUM_FONT = ("Times New Roman", 15,)

        self.data = json.load(open('data.json'))  # dictionary words

        # =================== Frames ===================================
        self.label_frame = Frame(self.parent, pady=5, padx=5, bg='green')
        self.label_frame.pack(padx=10, pady=10)

        self.entries_frame = Frame(self.parent, pady=5, padx=5, bg='green')
        self.entries_frame.pack(padx=10, pady=10)

        self.result_frame = Frame(self.parent, pady=5, padx=5, bg='light green')
        self.result_frame.pack(expand=True, fill=BOTH, padx=10, pady=5)

        # ================== Label ==============================
        self.dic_label = Label(self.label_frame, text="GRANDPA DICTIONARY", font=LARGE_FONT, padx=10, pady=5,
                               bg='green', fg='white')
        self.dic_label.grid(row=0, columnspan=3, pady=5, padx=5)

        # =================== Entries ==========================
        # self.word_label = Label(self.entries_frame, text="Enter word here: ", font=NORMAL_FONT)
        # self.word_label.grid(row=0, column=0, sticky=W, padx=10)

        self.word_entry_var = StringVar()
        self.word_entry = ttk.Entry(self.entries_frame, width=50, font=MEDIUM_FONT, textvariable=self.word_entry_var)
        self.word_entry.grid(row=0, column=1, sticky=W, padx=10)
        self.word_entry.bind("<Return>", self.search)

        self.search_button = ttk.Button(self.entries_frame, text="Search", width=15,
                                        command=self.search_btn_command)
        self.search_button.grid(row=0, column=2, padx=10, ipady=1)

        # ==================== Result box ===============================
        self.display_words = Listbox(self.result_frame, font=NORMAL_FONT, width=25)
        self.display_words.pack(fill=Y, side=LEFT)

        self.display_words.bind("<<ListboxSelect>>", self.get_selected_data)

        self.display_scroll_bar = ttk.Scrollbar(self.result_frame)
        self.display_scroll_bar.pack(fill=Y, side=LEFT)

        self.display_words.configure(yscrollcommand=self.display_scroll_bar.set)
        self.display_scroll_bar.configure(command=self.display_words.yview)

        self.display_result = Text(self.result_frame, font=NORMAL_FONT, )
        self.display_result.pack(side=LEFT, fill=BOTH, expand=True)

        for definitions in sorted(self.data.keys()):
            self.display_words.insert(END, definitions)

    def meaning(self, word):

        # check for non-existing words
        if word in self.data:
            return self.data[word]

        # check for Proper Nouns
        elif word.title() in self.data:
            return self.data[word.title()]

        # check for acronyms(with all letters in upper case) eg: USA, NATO etc.
        elif word.upper() in self.data:
            return self.data[word.upper()]

        # check for lower case input
        elif word.lower() in self.data:
            return self.data[word.lower()]

    def search(self, event):
        self.display_result.delete(1.0, END)
        result = self.meaning(self.word_entry.get())
        user_input = self.word_entry.get()

        # self.display_words.delete(0, END)
        # for items in get_close_matches(user_input, self.data.keys(), n=50,):
        #   self.display_words.insert(END, items)

        if self.word_entry.get() == "":
            mbx.showinfo("", "You have not entered anything")

        elif len(self.word_entry.get()) <= 0:
            self.display_words.delete(0, END)
            for words in self.data.keys():
                self.display_words.insert(END, words)

        elif type(result) == list:
            for definitions in result:
                self.display_result.insert(END, definitions)

        # check for similar words
        elif len(get_close_matches(self.word_entry.get(), self.data.keys())) > 0:
            result = self.meaning(get_close_matches(self.word_entry.get(), self.data.keys())[0])
            self.word_entry.delete(0, END)
            self.word_entry.insert(END, get_close_matches(user_input, self.data.keys())[0])
            if type(result) == list:
                for definitions in result:
                    self.display_result.insert(END, definitions)

        else:
            self.display_result.insert(END, result)

    def search_btn_command(self):
        self.display_result.delete(1.0, END)
        result = self.meaning(self.word_entry.get())
        user_input = self.word_entry.get()

        # self.display_words.delete(0, END)
        # for items in get_close_matches(user_input, self.data.keys(), n=50,):
        #   self.display_words.insert(END, items)

        if self.word_entry.get() == "":
            mbx.showinfo("", "You have not entered anything")

        elif len(self.word_entry.get()) <= 0:
            self.display_words.delete(0, END)
            for words in self.data.keys():
                self.display_words.insert(END, words)

        elif type(result) == list:
            for definitions in result:
                self.display_result.insert(END, definitions)

        # check for similar words
        elif len(get_close_matches(self.word_entry.get(), self.data.keys())) > 0:
            result = self.meaning(get_close_matches(self.word_entry.get(), self.data.keys())[0])
            self.word_entry.delete(0, END)
            self.word_entry.insert(END, get_close_matches(user_input, self.data.keys())[0])
            if type(result) == list:
                for definitions in result:
                    self.display_result.insert(END, definitions)
            else:
                self.display_result.insert(END, result)

    def get_selected_data(self, event):
        try:
            index = self.display_words.curselection()[0]
            selected_data = self.display_words.get(index)
            self.word_entry.delete(0, END)
            self.word_entry.insert(END, selected_data)

            self.display_result.delete(1.0, END)
            result = self.meaning(selected_data)

            if type(result) == list:
                for definitions in result:
                    self.display_result.insert(END, definitions)
            else:
                self.display_result.insert(END, result)
        except IndexError:
            raise


if __name__ == "__main__":
    root = Tk()
    app = Dictionary(root)
    root.mainloop()
