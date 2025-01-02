
import requests
from bs4 import BeautifulSoup

# Step 1: 登录报表系统
def login_to_system(base_url, login_endpoint, username, password):
    session = requests.Session()
    login_url = f"{base_url}/{login_endpoint}"
    
    # 模拟登录表单数据
    login_data = {
        'username': username,
        'password': password,
        # 根据实际表单参数调整
    }
    
    response = session.post(login_url, data=login_data)
    if response.status_code == 200 and "成功" in response.text:  # 根据实际成功标志调整
        print("登录成功！")
    else:
        print("登录失败！")
        exit()
    return session

# Step 2: 爬取报表数据
def scrape_report(session, report_url):
    response = session.get(report_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 根据页面结构提取数据
        # 例如，提取表格数据：
        table = soup.find('table', {'id': 'reportTable'})
        if table:
            rows = table.find_all('tr')
            for row in rows:
                cols = [col.text.strip() for col in row.find_all(['td', 'th'])]
                print(cols)
        else:
            print("未找到报表表格！")
    else:
        print(f"无法访问报表页面，状态码：{response.status_code}")

# 主函数
def main():
    # 根据实际情况调整 URL 和登录信息
    base_url = "https://example.com"
    login_endpoint = "login"
    report_endpoint = "reports/monthly"

    username = "your_username"
    password = "your_password"

    # 登录并爬取数据
    session = login_to_system(base_url, login_endpoint, username, password)
    report_url = f"{base_url}/{report_endpoint}"
    scrape_report(session, report_url)

if __name__ == "__main__":
    main()
