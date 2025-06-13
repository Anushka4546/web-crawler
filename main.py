from crawler.manager import Manager

def main():
    start_url = 'https://github.com/Anushka4546'
    max_workers = 3
    max_pages = 20
    max_depth = 2
    driver_path = 'chromedriver'  # Update with your actual path!
    timeout = 20

    manager = Manager(
        start_url=start_url,
        max_workers=max_workers,
        max_pages=max_pages,
        max_depth=max_depth,
        driver_path=driver_path,
        timeout=timeout
    )
    manager.start()
    manager.storage.save_to_csv('crawled_results.csv')
    print(f"Crawling complete. Results saved to crawled_results.csv.")

if __name__ == '__main__':
    main()
