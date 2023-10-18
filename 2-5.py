if __name__ == "__main__":
    # 读取输入字符串
    input_str = input()

    # 使用集合进行去重
    unique_chars = set(input_str)

    # 将去重后的字符转换为列表，并按字母顺序排序
    sorted_chars = sorted(unique_chars)

    # 将排序后的字符列表连接成一个字符串
    result_str = ''.join(sorted_chars)

    # 输出结果字符串
    print(result_str)