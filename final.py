from tkinter import *
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Website Blocker")

Label(root, text='WEBSITE BLOCKER', font='arial 20 bold').pack()
Label(root, text='WEBSITE BLOCKER', font='arial 20 bold').pack(side=BOTTOM)

host_path = 'C:/Windows/System32/drivers/etc/hosts'  # Use forward slashes in the path

ip_address = '127.0.0.1'

Label(root, text='Enter Website:', font='arial 13 bold').place(x=5, y=60)
Websites = Text(root, font='arial 10', height='2', width='40', wrap=WORD, padx=5, pady=5)
Websites.place(x=140, y=60)

result_label = Label(root, text="", font='arial 12 bold')
result_label.place(x=230, y=200)  # Label to display results

def Blocker():
    result_label.config(text="")  # Reset the result_label text
    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.split(","))
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                result_label.config(text='Already Blocked')  # Update label text
            else:
                host_file.write(ip_address + " " + website + '\n')
                result_label.config(text="Blocked")  # Update label text

def Unblock():
    result_label.config(text="")  # Reset the result_label text
    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.strip().split(","))  # Remove leading/trailing spaces
    with open(host_path, 'r+') as host_file:
        file_content = host_file.readlines()
        host_file.seek(0)
        for line in file_content:
            blocked = any(web in line for web in Website)
            if not blocked:
                host_file.write(line)
        host_file.truncate()
    result_label.config(text="UnBlocked")  # Update label text

block_btn = Button(root, text='Block', font='arial 12 bold', command=Blocker, width=6, bg='royal blue1',
                   activebackground='sky blue')
block_btn.place(x=200, y=150)

unblock_btn = Button(root, text='Unblock', font='arial 12 bold', command=Unblock, width=6, bg='royal blue1',
                     activebackground='sky blue')
unblock_btn.place(x=300, y=150)

root.mainloop()
