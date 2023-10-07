import threading
import time
import random
import tkinter as tk
from queue import Queue

class Robot1:
    def __init__(self, robot_id, tasks_queue, gui):
        self.robot_id = robot_id
        self.tasks_queue = tasks_queue
        self.gui = gui

    def perform_task(self):
        while True:
            if not self.tasks_queue.empty():
                task = self.tasks_queue.get()
                self.gui.update_display(f"Robot {self.robot_id} is performing {task}.")
                time.sleep(random.uniform(1, 5))
                self.gui.update_display(f"Robot {self.robot_id} completed {task}.")
                self.analyze_task(task)

    def analyze_task(self, task):
        # Perform task analysis (simplified for demonstration)
        analysis = f"Task Analysis: {task} task completed successfully."
        self.gui.update_display(analysis)

class ManufacturingLine:
    def __init__(self, num_robots, gui):
        self.robots = [Robot1(i, gui) for i in range(1, num_robots + 1)]
        self.tasks = ['Welding', 'Painting', 'Assembly', 'Packaging']

    def start_manufacturing(self, tasks_queue):
        while True:
            time.sleep(2)  # Pause between cycles
            for robot in self.robots:
                task = random.choice(self.tasks)
                tasks_queue.put(task)

class ManufacturingGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Manufacturing Simulation")
        self.display = tk.Text(self.root, width=50, height=20)
        self.display.pack()
        self.clear_button = tk.Button(self.root, text="Clear Display", command=self.clear_display)
        self.clear_button.pack()

    def update_display(self, message):
        self.display.insert(tk.END, message + '\n')
        self.display.see(tk.END)  # Scroll to the end

    def clear_display(self):
        self.display.delete(1.0, tk.END)  # Clear the display

    def start_gui(self):
        self.root.mainloop()

if __name__ == "__main__":
    manufacturing_gui = ManufacturingGUI()
    tasks_queue = Queue()
    manufacturing_line = ManufacturingLine(num_robots=5, gui=manufacturing_gui)

    for robot in manufacturing_line.robots:
        threading.Thread(target=robot.perform_task).start()

    threading.Thread(target=manufacturing_line.start_manufacturing, args=(tasks_queue,)).start()
    manufacturing_gui.start_gui()
