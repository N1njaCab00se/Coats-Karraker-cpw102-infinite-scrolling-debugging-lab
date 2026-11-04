posts = [
    "New campus coffee shop opens",
    "Python workshop this Friday",
    "Robotics club builds a drone",
    "Students launch a weather app",
    "Hackathon registration is open",
    "New library study spaces",
    "Campus Wi-Fi gets upgraded",
    "CS students build a game",
]

PAGE_SIZE = 3


def fetch_page(page):
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    return posts[start:end]


page = 0
feed = []

while True:
    new_posts = fetch_page(page)

    for post in new_posts:
        feed.append(post)

    print("\nYour Feed:")
    for post in feed:
        print("-", post)

    print(f"\nLoaded {len(feed)} posts")

    action = input("\nScroll? (y/n): ")

    if action == "n":
        break

    page = 0

print("Session ended.")
