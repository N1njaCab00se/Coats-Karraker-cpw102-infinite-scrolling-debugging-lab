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

new_posts = fetch_page(page)

for post in new_posts:
    feed.append(post)

print("\nYour Feed:")
for post in feed:
    print("-", post)

print(f"\nLoaded {len(feed)} posts")

while True:


    action = input("\nScroll? (y/n): ").strip().lower()

    if action == "n":
        print("DEBUG: no entered")
        break
    elif action == "y":
        page += 1
        new_posts = fetch_page(page)
        print(f"DEBUG: new_posts = {new_posts}")

        for post in new_posts:
            feed.append(post)

        print("\nYour Feed:")
        for post in feed:
            print("-", post)

        print(f"\nLoaded {len(feed)} posts")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

print("Session ended.")
