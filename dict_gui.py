from tkinter import *
import json
from difflib import get_close_matches
from tkinter import ttk


class Dictionary:

    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Grandpa Dictionary (First Edition)")
        self.parent.configure(background="cyan")
        # self.parent.geometry("1600x900")
        self.parent.resizable(height=False, width=False)

        NORMAL_FONT = ("Times New Roman", 12)
        LARGE_FONT = ("Times New Roman", 25, "bold")
        MEDIUM_FONT = ("Times New Roman", 15,)

        data = json.load(open('076 data.json'))  # dictionary words

        def meaning(word):

            # check for non-existing words
            if word in data:
                return data[word]

            # check for Proper Nouns
            elif word.title() in data:
                return data[word.title()]

            # check for acronyms(with all letters in upper case) eg: USA, NATO etc.
            elif word.upper() in data:
                return data[word.upper()]

            # check for lower case input
            elif word.lower() in data:
                return data[word.lower()]

        def search(event):
            display_result.delete(0, END)
            result = meaning(word_entry.get())
            user_input = word_entry.get()

            # display_words.delete(0, END)
            # for items in get_close_matches(user_input, data.keys(), n=50,):
            #   display_words.insert(END, items)

            if len(word_entry.get()) <= 0:
                display_words.delete(0, END)
                for words in data.keys():
                    display_words.insert(END, words)

            elif type(result) == list:
                for definitions in result:
                    display_result.insert(END, definitions)

            # check for similar words
            elif len(get_close_matches(word_entry.get(), data.keys())) > 0:
                result = meaning(get_close_matches(word_entry.get(), data.keys())[0])
                word_entry.delete(0, END)
                word_entry.insert(END, get_close_matches(user_input, data.keys())[0])
                if type(result) == list:
                    for definitions in result:
                        display_result.insert(END, definitions)

            else:
                display_result.insert(END, result)

        def search_btn_command():
            display_result.delete(0, END)
            result = meaning(word_entry.get())
            user_input = word_entry.get()

            # display_words.delete(0, END)
            # for items in get_close_matches(user_input, data.keys(), n=50,):
            #   display_words.insert(END, items)

            if len(word_entry.get()) <= 0:
                display_words.delete(0, END)
                for words in data.keys():
                    display_words.insert(END, words)

            elif type(result) == list:
                for definitions in result:
                    display_result.insert(END, definitions)

            # check for similar words
            elif len(get_close_matches(word_entry.get(), data.keys())) > 0:
                result = meaning(get_close_matches(word_entry.get(), data.keys())[0])
                word_entry.delete(0, END)
                word_entry.insert(END, get_close_matches(user_input, data.keys())[0])
                if type(result) == list:
                    for definitions in result:
                        display_result.insert(END, definitions)

            else:
                display_result.insert(END, result)

        # =================== Frames ===================================
        label_frame = Frame(self.parent, bd=2, pady=5, padx=5, relief=SUNKEN, )
        label_frame.grid(row=0, pady=5, padx=5)

        entries_frame = Frame(self.parent, bd=1, pady=5, padx=5, relief=SUNKEN, )
        entries_frame.grid(row=1, pady=5, padx=5)

        result_frame = Frame(self.parent, bd=1, pady=5, padx=5, relief=SUNKEN, )
        result_frame.grid(row=2, pady=5, padx=5)

        # ================== Label ==============================
        dic_label = Label(label_frame, text="GRANDPA DICTIONARY", font=LARGE_FONT, padx=10, pady=5, )
        dic_label.grid(row=0, columnspan=3, pady=5, padx=5)

        # =================== Entries ==========================
        word_label = Label(entries_frame, text="Enter word here: ", font=NORMAL_FONT)
        word_label.grid(row=0, column=0, sticky=W, padx=10)

        word_entry_var = StringVar()
        word_entry = Entry(entries_frame, width=40, font=MEDIUM_FONT, textvariable=word_entry_var)
        word_entry.grid(row=0, column=1, sticky=W, padx=10)
        word_entry.bind("<Return>", search)

        search_button = Button(entries_frame, text="Search", font=NORMAL_FONT, padx=10, width=15, relief=RIDGE,
                               command=search_btn_command)
        search_button.grid(row=0, column=2, padx=10)

        # ==================== Result box ===============================
        display_words = Listbox(result_frame, font=NORMAL_FONT, height=30, width=25)
        display_words.grid(row=0, rowspan=10, columnspan=1, padx=5, pady=5)

        for definitions in data.keys():
            display_words.insert(END, definitions)

        def get_selected_data(event):
            try:
                index = display_words.curselection()[0]
                selected_data = display_words.get(index)
                word_entry.delete(0, END)
                word_entry.insert(END, selected_data)

                display_result.delete(0, END)
                result = meaning(selected_data)

                if type(result) == list:
                    for definitions in result:
                        display_result.insert(END, definitions)
                else:
                    display_result.insert(END, result)
            except IndexError:
                pass

        display_words.bind("<<ListboxSelect>>", get_selected_data)

        display_scroll_bar = ttk.Scrollbar(result_frame)
        display_scroll_bar.grid(row=0, column=2, rowspan=10, sticky='ns')

        display_words.configure(yscrollcommand=display_scroll_bar.set)
        display_scroll_bar.configure(command=display_words.yview)

        display_result = Listbox(result_frame, font=NORMAL_FONT, height=30, width=160)
        display_result.grid(row=0, rowspan=10, column=3, columnspan=5, padx=5, pady=5)

        # result_scroll_bar = Scrollbar(result_frame)
        # result_scroll_bar.grid(row=1, column=3, columnspan=5)

        # display_result.configure(xscrollcommand=result_scroll_bar.set)
        # result_scroll_bar.configure(command=display_result.xview)


if __name__ == "__main__":
    root = Tk()
    app = Dictionary(root)
    root.mainloop()
