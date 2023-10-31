from selenium import webdriver
import time
import datetime
import os
from zip_sendemail import send_zip
from make_dir_to_zip import zip_files


def create_folder(folder_path):  # 创建文件夹
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    else:
        print(f"Folder '{folder_path}' already exists.")


path = "G:/screen_shoot"
driver = webdriver.Edge()
# 获取当前时间
now = datetime.datetime.now()

# 计算第二天凌晨3点的时间
target_time = now + datetime.timedelta(days=1)
target_time = target_time.replace(hour=3, minute=0, second=0, microsecond=0)


def main():
    url = input("请输入网址:")
    # 打开网页
    driver.get(url)
    # 最大化窗口
    driver.maximize_window()

    i = 0
    flag = 1  # 用于指示是第几个文件夹

    dir_path = path + '/1'
    create_folder(dir_path)

    while True:
        # 获取当前时间
        now_time = datetime.datetime.now()

        # 注意，当时间结束后，需要把正在装入图像的包压缩后发送
        if now_time >= target_time:
            # 先压缩文件夹变为.zip文件
            zip_path = dir_path + ".zip"
            zip_files(dir_path, zip_path)
            # 发送文件夹
            send_zip(zip_path)
            break

        # 设立图片名称为截图时间
        formatted_time = now_time.strftime("%Y-%m-%d-%H-%M-%S")
        driver.save_screenshot(f'{dir_path}/{formatted_time}.png')

        i = i + 1
        if i == 39:
            # 先压缩文件夹变为.zip文件
            zip_path = dir_path + ".zip"
            zip_files(dir_path, zip_path)

            flag = flag + 1
            dir_path = path + '/' + str(flag)
            create_folder(dir_path)  # 创建文件夹

            # 发送文件夹
            send_zip(zip_path)
            i = 0  # 重新开始计数

        time.sleep(25)

    driver.quit()
    print("程序结束")


if __name__ == '__main__':
    main()
