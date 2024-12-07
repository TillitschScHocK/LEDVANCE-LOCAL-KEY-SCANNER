import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter import filedialog
from tkinter import PhotoImage
import socket
import os
import json
from typing import Tuple
from pyscript_modules.tuya.api import TuyaAPI
from pyscript_modules.tuya.exceptions import InvalidAuthentication

CONFIG_FILE = "config.json"

def save_config(username: str, password: str):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"username": username, "password": password}, f)

def load_config() -> Tuple[str, str]:
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
        return config.get("username", ""), config.get("password", "")
    return "", ""

def get_device_ip() -> str:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def write_device_info_to_file(devices_info: str, filename: str):
    with open(filename, "a") as file:
        file.write(devices_info)

def fetch_devices(username: str, password: str):
    api = TuyaAPI(username, password)
    try:
        api.login()
    except InvalidAuthentication:
        raise ValueError("Invalid authentication.")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {e}")

    devices = []
    for group in api.groups():
        for dev in api.devices(group["groupId"]):
            devices.append({
                "name": dev.name,
                "id": dev.id,
                "localKey": dev.localKey,
                "ip": get_device_ip()
            })
    return devices

class DeviceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ledvance Device Data")

        self.root.iconbitmap("tuya.ico")

        # Add header
        self.title_label = ttk.Label(root, text="Ledvance Device Data Manager", font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Save", command=self.save_user_data)
        self.file_menu.add_command(label="Quit", command=root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.status_var = tk.StringVar()
        self.status_var.set("Status: Connecting...")
        self.status_label = ttk.Label(root, textvariable=self.status_var, anchor="w")
        self.status_label.grid(row=6, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

        self.username_label = ttk.Label(root, text="E-Mail:")
        self.username_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.username_entry = ttk.Entry(root, width=30)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.username_entry.insert(0, load_config()[0])

        self.password_label = ttk.Label(root, text="Password:")
        self.password_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = ttk.Entry(root, width=30, show="*")
        self.password_entry.grid(row=2, column=1, padx=(5,0), pady=5, sticky="w")
        self.password_entry.insert(0, load_config()[1])

        self.show_pass_button = ttk.Button(root, text="👁", command=self.toggle_password_visibility, width=2)
        self.show_pass_button.grid(row=2, column=1, padx=(0,5), pady=5, sticky="e")

        self.treeview = ttk.Treeview(root, columns=("Name", "Device ID", "Local Key", "IP Address"), show="headings")
        self.treeview.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
        self.treeview.heading("Name", text="Device Name")
        self.treeview.heading("Device ID", text="Device ID")
        self.treeview.heading("Local Key", text="Local Key")
        self.treeview.heading("IP Address", text="IP Address")
        self.treeview.bind("<Double-1>", self.show_device_details)
        self.treeview.bind("<ButtonRelease-1>", self.copy_cell_content)

        self.fetch_button = ttk.Button(root, text="Fetch Device Data", command=self.fetch_device_data)
        self.fetch_button.grid(row=4, column=0, padx=5, pady=5)

        self.save_button = ttk.Button(root, text="Save User Data", command=self.save_user_data)
        self.save_button.grid(row=4, column=1, padx=5, pady=5)

        self.help_button = ttk.Button(root, text="Help", command=self.show_help)
        self.help_button.grid(row=4, column=2, padx=5, pady=5)

    def fetch_device_data(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty.")
            return

        self.status_var.set("Status: Connecting to the API...")

        try:
            devices = fetch_devices(username, password)
            self.treeview.delete(*self.treeview.get_children())
            for dev in devices:
                self.treeview.insert("", "end", values=(dev["name"], dev["id"], dev["localKey"], dev["ip"]))
            self.status_var.set("Status: Device data successfully fetched.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set(f"Status: Error: {e}")

    def save_user_data(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty.")
            return

        save_config(username, password)
        messagebox.showinfo("Success", "User data saved.")

    def toggle_password_visibility(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def show_device_details(self, event):
        item = self.treeview.selection()[0]
        device = self.treeview.item(item)["values"]
        details = f"Device Name: {device[0]}\nDevice ID: {device[1]}\nLocal Key: {device[2]}\nIP Address: {device[3]}"
        messagebox.showinfo("Device Details", details)

    def copy_cell_content(self, event):
        region = self.treeview.identify("region", event.x, event.y)
        if region == "cell":
            column = self.treeview.identify_column(event.x)
            item = self.treeview.identify_row(event.y)
            
            if item and column:
                column_index = int(column[1:]) - 1  # Convert column string to index
                cell_value = self.treeview.item(item, "values")[column_index]
                
                self.root.clipboard_clear()
                self.root.clipboard_append(str(cell_value))
                self.status_var.set(f"Cell content copied: {cell_value}")

    def show_help(self):
        help_text = """
        Welcome to the Tuya/Ledvance Device Data Manager!

        Instructions:
        1. Enter your email and password.
        2. Click "Fetch Device Data" to display your devices.
        3. Click on any cell in the table to copy its content.
        4. Double-click a row to see detailed device information.
        5. Use "Save User Data" to save your credentials for future sessions.

        Tip: The eye button next to the password field toggles password visibility.
        """
        messagebox.showinfo("Help", help_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = DeviceGUI(root)
    root.mainloop()
