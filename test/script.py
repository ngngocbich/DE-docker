from pathlib import Path 
#pathlib trong Python (được giới thiệu từ bản 3.4) là một thư viện tiêu chuẩn cung cấp các lớp hướng đối tượng để xử lý đường dẫn hệ thống tệp (file system paths) một cách dễ đọc, nhất quán và đa nền tảng (Windows, Linux, macOS). Nó thay thế các cách tiếp cận cũ, phức tạp như os.path và glob bằng các thao tác trực quan, an toàn hơn. 
current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"Files in {current_dir}:")

for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue

    print(f"  - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f"    Content: {content}")