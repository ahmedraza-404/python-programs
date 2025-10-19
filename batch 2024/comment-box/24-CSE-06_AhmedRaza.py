# Simple Comment Box Program


comments = []

print("=== Comment Box ===")
print("Type your comment and press Enter.")
print("Type 'exit' to stop and view all comments.\n")


while True:
    comment = input("Enter your comment: ")

    if comment.lower() == "exit":
        break  # stop taking input

  
    comments.append(comment)
    print("✅ Comment added!\n")


print("\n--- All Comments ---")
if len(comments) == 0:
    print("No comments submitted.")
else:
    for i, c in enumerate(comments, start=1):
        print(f"{i}. {c}")
