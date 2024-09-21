import tkinter as tk
from tkinter import ttk
import psutil

class MemoryCleaner:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Memory Cleaner')

        # Create a frame for the CPU usage gauge
        self.cpu_frame = tk.Frame(self.root)
        self.cpu_frame.pack()

        # Label to display CPU usage
        self.cpu_label = tk.Label(self.cpu_frame, text='CPU Usage: 0%', font=('Helvetica', '16'))
        self.cpu_label.pack(side=tk.LEFT)

        # Create a gauge for the CPU usage (using ttk.Progressbar)
        self.cpu_gauge = ttk.Progressbar(self.cpu_frame, orient='horizontal', length=200, mode='determinate')
        self.cpu_gauge.pack(side=tk.LEFT)

        # Create a frame for the RAM usage gauge
        self.ram_frame = tk.Frame(self.root)
        self.ram_frame.pack()

        # Label to display RAM usage
        self.ram_label = tk.Label(self.ram_frame, text='RAM Usage: 0%', font=('Helvetica', '16'))
        self.ram_label.pack(side=tk.LEFT)

        # Create a gauge for the RAM usage (using ttk.Progressbar)
        self.ram_gauge = ttk.Progressbar(self.ram_frame, orient='horizontal', length=200, mode='determinate')
        self.ram_gauge.pack(side=tk.LEFT)

        # Button to clear cache
        self.clean_cache_button = tk.Button(self.root, text='Clean Cache', command=self.clear_cache)
        self.clean_cache_button.pack()

        # Update the gauges with initial values
        self.update_gauges()

    def update_gauges(self):
        # Get CPU usage
        cpu_usage = (psutil.cpu_percent() / psutil.cpu_count()) * 100
        self.cpu_label.config(text=f'CPU Usage: {cpu_usage:.2f}%')
        self.cpu_gauge['value'] = int(cpu_usage)

        # Get RAM usage
        mem_usage = psutil.virtual_memory().percent
        self.ram_label.config(text=f'RAM Usage: {mem_usage}%')
        self.ram_gauge['value'] = int(mem_usage)

        # Update the gauges after a short delay to get updated values
        self.root.after(1000, self.update_gauges)

    def clear_cache(self):
        try:
            print("Closing unnecessary applications...")
            app_names = ['chrome.exe', 'edge.exe', 'explorer.exe']
            for app in app_names:
                print(f"Closing {app} process")
        except Exception as e:
            print(f'Error closing application: {e}')

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    memory_cleaner = MemoryCleaner()
    memory_cleaner.run()