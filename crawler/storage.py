import csv
import threading

class Storage:
    def __init___(self):
        self.data = []
        self.lock = threading.Lock()

    def add_result(self, url, title):
        with self.lock:
            self.data.append({
                'url': url,
                'title': title
            })

    def save_to_csv(self, filename='results.csv'):
        with self.lock:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['url', 'title']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.data)