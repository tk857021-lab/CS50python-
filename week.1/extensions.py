
def main():
    filename = input("File name: ")
    print(media_type(filename))


def media_type(filename):
    filename = filename.lower()

    if filename.endswith(".jpg") or filename.endswith("jpeg"):
        return "image/jpeg"
    elif filename.endswith(".gif"):
        return "image/gif"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".pdf".strip()):
        return "application/pdf"
    elif filename.endswith(".txt"):
        return "text/plain"
    elif filename.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


main()


