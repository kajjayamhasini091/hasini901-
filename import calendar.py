import calendar
import tkinter as tk
from tkinter import ttk, messagebox


class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Calendar")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Title
        title_label = tk.Label(
            root,
            text="📅 GUI Calendar",
            font=("Arial", 16, "bold"),
            pady=10,
        )
        title_label.pack()

        # Frame for inputs
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        # Year input
        tk.Label(input_frame, text="Year:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        self.year_entry = tk.Entry(input_frame, width=8, font=("Arial", 12))
        self.year_entry.grid(row=0, column=1, padx=5)

        # Month dropdown
        tk.Label(input_frame, text="Month:", font=("Arial", 12)).grid(row=0, column=2, padx=5)
        self.month_combo = ttk.Combobox(
            input_frame,
            values=list(calendar.month_name)[1:],  # Skip empty first element
            font=("Arial", 12),
            width=10,
            state="readonly"
        )
        self.month_combo.grid(row=0, column=3, padx=5)

        # Show Button
        show_button = tk.Button(
            input_frame,
            text="Show Calendar",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.show_calendar
        )
        show_button.grid(row=0, column=4, padx=10)

        # Text area for calendar
        self.text_area = tk.Text(root, wrap="word", font=("Courier New", 12), width=60, height=15)
        self.text_area.pack(pady=10)

    def show_calendar(self):
        year = self.year_entry.get()
        month = self.month_combo.get()

        if not year.isdigit() or int(year) < 1:
            messagebox.showerror("Invalid Input", "Please enter a valid year!")
            return

        if not month:
            messagebox.showerror("Invalid Input", "Please select a month!")
            return

        year = int(year)
        month_num = list(calendar.month_name).index(month)

        # Generate calendar
        cal_text = calendar.month(year, month_num)

        # Display calendar
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, cal_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
