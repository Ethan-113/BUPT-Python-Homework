if __name__ == "__main__":
    # 打开文件以读取和写入（'r+' 模式）
    with open('example.txt', 'r+') as file:
        # 读取文件的内容
        file_contents = file.read()
        print("原始内容：")
        print(file_contents)

        # 在文件末尾追加新内容
        new_content = input()
        file.write(new_content)
        print("已写入新内容。")

    with open('example.txt', 'r') as file:
        file_content = file.read()

    print(file_content, end='')
